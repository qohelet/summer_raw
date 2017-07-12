#include <termios.h>
#include <unistd.h>

#include <ros/ros.h>
#include <std_msgs/Char.h>

#include <iostream>

using namespace std;

int getch()
{
  static struct termios oldt, newt;
  tcgetattr( STDIN_FILENO, &oldt);           // save old settings
  newt = oldt;
  newt.c_lflag &= ~(ICANON);                 // disable buffering
  tcsetattr( STDIN_FILENO, TCSANOW, &newt);  // apply new settings

  int c = getchar();  // read character (non-blocking)

  tcsetattr( STDIN_FILENO, TCSANOW, &oldt);  // restore old settings
  return c;
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "command_publisher");

  ros::NodeHandle n;
  ros::Publisher publisher = n.advertise<std_msgs::Char>("command_topic", 1000);
  ros::Rate loop_rate(10);

  while (ros::ok())
  {
    int c = getch();   // call your non-blocking input function

    std_msgs::Char msg;
    cout << "\tIt is pressed key " << char(c) << " (its int value = " << int(c) << ")" << endl;
    msg.data = char(c);
    publisher.publish(msg);
    ros::spinOnce();
    loop_rate.sleep();
  }
  ros::spinOnce();
  return 0;
}
