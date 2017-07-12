#include <ros/ros.h>
#include <std_msgs/Int32.h>

#include <iostream>
#include <ros/ros.h>
#include <std_msgs/Char.h>

#include <iostream>

using namespace std;

class Field {
  bool** data;
  int x;
  int y;
  int size_x;
  int size_y;

  bool position_is_possible(int x, int y) const {
    return data[x][y];
  }

public:
  Field(int size_x = 10, int size_y = 10, int pos_x = 5, int pos_y = 5) {
    x = pos_x; y = pos_y;
    this->size_x = size_x; this->size_y = size_y;
    data = new bool*[size_x];
    for (int x = 0; x < size_x; x++) {
      data[x] = new bool[size_y];
      for (int y = 0; y < size_y; y++) {
        data[x][y] = true;
      }
    }
  }

  friend ostream& operator << (ostream& ostr, const Field& f) {
    system("clear");
    ostr << "┌"; for (int i = 0; i < f.size_x; i++) { ostr << "―"; } ostr << "┐" << endl;
    for (int y = 0; y < f.size_y; y++) {
      ostr << "|";
      for (int x = 0; x < f.size_x; x++) {
        if (x == f.x && y == f.y)
          ostr << "x";
        else if (f.data[x][y] == true)
          ostr << " ";
        else if (f.data[x][y] == false)
          ostr << "■";
        else
          ostr << "?";
      }
      ostr << "|" << endl;
    }
    ostr << "└"; for (int i = 0; i < f.size_x; i++) { ostr << "―"; } ostr << "┘" << endl;
    return ostr;
  }

  void move_up ()    { if (y > 0        && position_is_possible(x, y-1)) y--; }
  void move_down ()  { if (y < size_y-1 && position_is_possible(x, y+1)) y++; }
  void move_left ()  { if (x > 0        && position_is_possible(x-1, y)) x--; }
  void move_right () { if (x < size_x-1 && position_is_possible(x+1, y)) x++; }
} field;

void handle_function(const std_msgs::Char& msg) {
  switch (msg.data) {
  case 'w': field.move_up();    break;
  case 's': field.move_down();  break;
  case 'a': field.move_left();  break;
  case 'd': field.move_right(); break;
  default :                     break;
  }
  cout << field << endl;
}

int main(int argc, char **argv) {
  ros::init(argc,argv,"command_subscriber");
  ros::NodeHandle n;
  ros::Subscriber subscriber = n.subscribe("command_topic", 1000, handle_function);
  ros::spin();
  return 0;
}

