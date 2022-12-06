#!/usr/bin/env python3


import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

g1 = MoveBaseGoal()
g2 = MoveBaseGoal()
g3 = MoveBaseGoal()
g4 = MoveBaseGoal()
g5 = MoveBaseGoal()


def movebase_client(g):

   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    # goal.target_pose.header.frame_id = "map"
    # goal.target_pose.header.stamp = rospy.Time.now()

    
    # goal.target_pose.pose.position.x = 0.5
    # goal.target_pose.pose.position.y = -0.5
    # goal.target_pose.pose.position.z = 0.0
    # goal.target_pose.pose.orientation.z = 0.7
    # goal.target_pose.pose.orientation.w = 0.7

    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    
    goal.target_pose.pose.position.x = g.target_pose.pose.position.x;
    goal.target_pose.pose.position.y = g.target_pose.pose.position.y
    goal.target_pose.pose.position.z = g.target_pose.pose.position.z
    goal.target_pose.pose.orientation.z = g.target_pose.pose.orientation.z
    goal.target_pose.pose.orientation.w = g.target_pose.pose.orientation.w
    
    
   # Sends the goal to the action server.
    client.send_goal(g1)
   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()
   # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
    # Result of executing the action
        return client.get_result()   

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
        
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('set_goal_node_py')
        g1.target_pose.header.frame_id = "map"
        g1.target_pose.header.stamp = rospy.Time.now()
        g1.target_pose.pose.position.x = 0.5;
        g1.target_pose.pose.position.y = -0.5;
        g1.target_pose.pose.position.z = 0.0;
        g1.target_pose.pose.orientation.z = 0.7;
        g1.target_pose.pose.orientation.w = 0.7;
        result = movebase_client(g1)
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")