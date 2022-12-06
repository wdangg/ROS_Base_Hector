#include <tf/transform_listener.h>
#include <geometry_msgs/PoseWithCovarianceStamped.h>

typedef struct Home
{
    double x;
    double y;
    double theta;
} PoseTypes;

// PoseTypes home_pose = {-2.0, -0.5, 0.0};
PoseTypes home_pose = {0.4, -0.3, 0.0};

ros::Publisher pub_ ;

void onPoseSet(double x, double y, double theta)
{   
    ros::NodeHandle nh_;
    ros::Publisher pub_ = nh_.advertise<geometry_msgs::PoseWithCovarianceStamped> ("/initialpose", 10);
    // ros::Rate loop_rate(10); // 10HZ = 0.1s
    // ros::spinOnce();

    std::string fixed_frame = "map";
    geometry_msgs::PoseWithCovarianceStamped pose;
    pose.header.frame_id = fixed_frame;
    // pose.header.stamp = ros::Time::now();

    // set x,y coord
    pose.pose.pose.position.x = x;
    pose.pose.pose.position.y = y;
    pose.pose.pose.position.z = 0.0;

    // set theta
    tf::Quaternion quat;
    quat.setRPY(0.0, 0.0, theta);
    tf::quaternionTFToMsg(quat, pose.pose.pose.orientation);
    pose.pose.covariance[6*0+0] = 0.5 * 0.5;
    pose.pose.covariance[6*1+1] = 0.5 * 0.5;
    pose.pose.covariance[6*5+5] = M_PI/12.0 * M_PI/12.0;

    // publish
    ROS_INFO("x: %f, y: %f, z: 0.0, theta: %f",x,y,theta);
    pub_.publish(pose);
}

int main(int argc, char** argv)
{
    // setting
    ros::init(argc, argv, "set_pose_node");
    ros::NodeHandle nh_;
    pub_ = nh_.advertise<geometry_msgs::PoseWithCovarianceStamped> ("/initialpose", 1);

    // onPoseSet(0.968507917975, -4.61491396765, 1); 

    ros::Rate loop_rate(10);
    int i = 0;
    while (ros::ok() && i < 5)
    {
        onPoseSet(home_pose.x , home_pose.y , home_pose.theta); 
        loop_rate.sleep(); 
        i++;
    }    
    ros::shutdown();
   return 0;
}