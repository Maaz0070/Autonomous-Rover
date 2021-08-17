#include <ros/ros.h>
#include "husky_highlevel_controller/HuskyHighlevelController.hpp"
#include <husky_highlevel_controller/TwoInts.h>
#include <cstdlib>

bool add(husky_highlevel_controller::TwoInts::Request &request, husky_highlevel_controller::TwoInts::Response &response)
{
  response.sum = request.a + request.b;
  ROS_INFO("request: x=%ld, y=%ld", (long int)request.a, (long int)request.b);
  ROS_INFO("  sending back response: [%ld]", (long int)request.sum);
  return true;
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "add_two_ints_server");
  //ros::NodeHandle nodeHandle("~");
  ros::NodeHandle nh;
  ros::ServiceServer service = nh.advertiseService("add_two_ints", add);

  //husky_highlevel_controller::HuskyHighlevelController huskyHighlevelController(nodeHandle);

  ros::spin();
  return 0;
}
