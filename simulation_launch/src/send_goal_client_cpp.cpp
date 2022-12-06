#include <ros/ros.h>
#include <move_base_msgs/MoveBaseAction.h>
#include <actionlib/client/simple_action_client.h>
#include <iostream>

using namespace std;

// Action specification for move_base
typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> MoveBaseClient;



// Create a new goal to send to move_base
move_base_msgs::MoveBaseGoal goal;



int main(int argc, char **argv)
{
	ros::init(argc, argv, "send_goal_client_cpp");

	MoveBaseClient ac("move_base", true);

	// Send a goal to the robot
	goal.target_pose.header.frame_id = "map";
	goal.target_pose.header.stamp = ros::Time::now();

	goal.target_pose.pose.position.x = 0.5;
	goal.target_pose.pose.position.y = 0.5;
	goal.target_pose.pose.orientation.z = 0.0;
	goal.target_pose.pose.orientation.w = 0.0;

	while (!ac.waitForServer(ros::Duration(5.0)))
	{
		ROS_INFO("Waiting for the move_base action server to come up");
	}


	while(1)
	{
		ROS_INFO("Sending goal");
		ac.sendGoal(goal);
		ros::spinOnce();

		if (ac.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
		{
			ros::shutdown();
		}
	}




} /* MAIN */
