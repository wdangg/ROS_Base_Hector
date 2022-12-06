#!/usr/bin/env python3


import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseActionResult
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

from PyQt5.QtGui import QIcon
from std_msgs.msg import String
import sys
import time

px = [0.5, 0.5, -1.0, -0.5, -2, -2]
py = [-0.5, 1.5, 1.7, 0.2, -0.5, 0.5]
pz = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
oz = [0.7, 0.7, -1.0, -0.6, -5.0, 0.7]
ow = [0.7, 0.7, 0.3, 0.7, 1.0, 0.7]


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        rospy.init_node('oops_ui_add', anonymous=True)
        self.pub = rospy.Publisher("pygui_topic", String, queue_size=10)
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.time = time
        MainWindow.setWindowFlags(Qt.WindowStaysOnTopHint)
        MainWindow.setWindowIcon(QIcon('fpt.png'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 391)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 461, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.g1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.g1.setObjectName("g1")
        self.gridLayout.addWidget(self.g1, 0, 0, 1, 1)
        self.g3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.g3.setObjectName("g3")
        self.gridLayout.addWidget(self.g3, 2, 0, 1, 1)
        self.g4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.g4.setObjectName("g4")
        self.gridLayout.addWidget(self.g4, 0, 1, 1, 1)
        self.g2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.g2.setObjectName("g2")
        self.gridLayout.addWidget(self.g2, 1, 0, 1, 1)
        self.g6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.g6.setObjectName("g6")
        self.gridLayout.addWidget(self.g6, 2, 1, 1, 1)
        self.g5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.g5.setObjectName("g5")
        self.gridLayout.addWidget(self.g5, 1, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 230, 461, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.schedule_bt = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.schedule_bt.setObjectName("schedule_bt")
        self.horizontalLayout.addWidget(self.schedule_bt)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.quit_bt = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.quit_bt.setObjectName("quit_bt")
        self.horizontalLayout.addWidget(self.quit_bt)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 484, 22))
        self.menubar.setObjectName("menubar")
        self.menuMove = QtWidgets.QMenu(self.menubar)
        self.menuMove.setObjectName("menuMove")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMove.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        
        self.g1.clicked.connect(self.send_1st)
        self.g2.clicked.connect(self.send_2nd)
        self.g3.clicked.connect(self.send_3rd)
        self.g4.clicked.connect(self.send_4th)
        # self.g5.clicked.connect(self.send_5th)
        # self.g6.clicked.connect(self.send_6th)
        
        self.quit_bt.clicked.connect(self.force_quit)
        self.schedule_bt.clicked.connect(self.schedule_func)
    
    def schedule_func(self):
        
        self.send_1st()
        rospy.loginfo('hey')
        rospy.loginfo(self.client.get_state)
        
        # while not self.client.get_state:
        #     rospy.loginfo(self.client.get_state)
        # self.send_2nd()
    
           
    def send_goal(self, number):
        self.number = number
        self.client.wait_for_server()
        self.x_goal = MoveBaseGoal()
        self.x_goal.target_pose.header.frame_id = "map"
        self.x_goal.target_pose.header.stamp = rospy.Time.now()
        self.x_goal.target_pose.pose.position.x    = px[self.number]
        self.x_goal.target_pose.pose.position.y    = py[self.number]
        self.x_goal.target_pose.pose.position.z    = pz[self.number]
        self.x_goal.target_pose.pose.orientation.z = oz[self.number] 
        self.x_goal.target_pose.pose.orientation.w = ow[self.number]
        self.client.send_goal(self.x_goal)
        self.wait = self.client.wait_for_result()
        # rospy.shutdown()
        if not self.wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
        # Result of executing the action
            return self.client.get_result()         

    def force_quit(self):
        app.quit()
        
    def send_1st(self):
        # L208
        # rospy.init_node('send_1st_goal')
        self.pub = rospy.Publisher("pygui_topic", String, queue_size=10)
        self.move_g1 = MoveBaseGoal()
        self.move_g1.target_pose.header.frame_id = "map"
        self.move_g1.target_pose.header.stamp = rospy.Time.now()
        self.move_g1.target_pose.pose.position.x = 8.4 #0.2 #0.5;
        self.move_g1.target_pose.pose.position.y = -0.5 #-0.5;
        self.move_g1.target_pose.pose.position.z = 0.0 #0.0;
        self.move_g1.target_pose.pose.orientation.z = 0.0 #0.7;
        self.move_g1.target_pose.pose.orientation.w = 1 #0.7
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.wait = self.client.wait_for_server()
        self.client.send_goal(self.move_g1)
        if not self.wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            rospy.loginfo('processing 1st')
            
            return self.client.get_result() 
        
    def send_2nd(self):
        # L207
        # rospy.init_node('send_2nd_goal')
        self.pub = rospy.Publisher("pygui_topic", String, queue_size=10)
        self.move_g2 = MoveBaseGoal()
        self.move_g2.target_pose.header.frame_id = "map"
        self.move_g2.target_pose.header.stamp = rospy.Time.now()
        self.move_g2.target_pose.pose.position.x =   11.4 #0.5
        self.move_g2.target_pose.pose.position.y =   -0.5#1.5
        self.move_g2.target_pose.pose.position.z =   0.0 #0.0
        self.move_g2.target_pose.pose.orientation.z = 0.0 #0.7
        self.move_g2.target_pose.pose.orientation.w = 1 #0.7
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.wait = self.client.wait_for_server()
        self.client.send_goal(self.move_g2)
        if not self.wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            # rospy.signal_shutdown("2nd goal")
            rospy.loginfo('processing 2nd')
            return self.client.get_result() 
        
    def send_3rd(self):
        # L206
        # rospy.init_node('send_3rd_goal')
        self.pub = rospy.Publisher("pygui_topic", String, queue_size=10)
        self.move_g3 = MoveBaseGoal()
        self.move_g3.target_pose.header.frame_id = "map"
        self.move_g3.target_pose.header.stamp = rospy.Time.now()
        self.move_g3.target_pose.pose.position.x = 24.6
        self.move_g3.target_pose.pose.position.y = -0.5 #1.7;
        self.move_g3.target_pose.pose.position.z = 0.0 #0.0;
        self.move_g3.target_pose.pose.orientation.z = 0 #-1.0;
        self.move_g3.target_pose.pose.orientation.w = 1.0 #0.3;
        
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.wait = self.client.wait_for_server()
        self.client.send_goal(self.move_g3)
        if not self.wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            # rospy.signal_shutdown('3rd goal')
            rospy.loginfo('processing 3rd')
            
            return self.client.get_result()
    
    def send_4th(self):
        # rospy.init_node('send_4th_goal')
        # L205
        self.pub = rospy.Publisher("pygui_topic", String, queue_size=10)
        self.move_g4 = MoveBaseGoal()
        self.move_g4.target_pose.header.frame_id = "map"
        self.move_g4.target_pose.header.stamp = rospy.Time.now()
        self.move_g4.target_pose.pose.position.x = 31.2
        self.move_g4.target_pose.pose.position.y = -0.75 #0.2;
        self.move_g4.target_pose.pose.position.z = 0.0 #0.0;
        self.move_g4.target_pose.pose.orientation.z = 0 #-0.6;
        self.move_g4.target_pose.pose.orientation.w = 1 #0.7;
        
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.wait = self.client.wait_for_server()
        self.client.send_goal(self.move_g4)
        if not self.wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            rospy.loginfo('processing 4th')
            
            return self.client.get_result()
        
    def send_5th(self):
        # rospy.init_node('send_5th_goal')
        self.pub = rospy.Publisher("pygui_topic", String, queue_size=10)
        self.move_g5 = MoveBaseGoal()
        self.move_g5.target_pose.header.frame_id = "map"
        self.move_g5.target_pose.header.stamp = rospy.Time.now()
        self.move_g5.target_pose.pose.position.x = 0.45#-2;
        self.move_g5.target_pose.pose.position.y = -2.38#-0.5;
        self.move_g5.target_pose.pose.position.z = 0.0
        self.move_g5.target_pose.pose.orientation.z = 0.8 #-5;
        self.move_g5.target_pose.pose.orientation.w = 0.5 #1;
        
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.wait = self.client.wait_for_server()
        self.client.send_goal(self.move_g5)
        if not self.wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            rospy.loginfo('processing 5th')
            
            return self.client.get_result()


    
    def send_6th(self):
        # rospy.init_node('send_6th_goal')
        self.pub = rospy.Publisher("pygui_topic", String, queue_size=10)
        self.move_g6 = MoveBaseGoal()
        self.move_g6.target_pose.header.frame_id = "map"
        self.move_g6.target_pose.header.stamp = rospy.Time.now()
        self.move_g6.target_pose.pose.position.x = -2
        self.move_g6.target_pose.pose.position.y = 0.5
        self.move_g6.target_pose.pose.position.z = 0.0
        self.move_g6.target_pose.pose.orientation.z = 0.7
        self.move_g6.target_pose.pose.orientation.w = 0.7
        
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.wait = self.client.wait_for_server()
        self.client.send_goal(self.move_g6)
        if not self.wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            rospy.loginfo('processing 6th')
            
            return self.client.get_result()
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FPL Navigating"))
        self.g1.setText(_translate("MainWindow", "L208"))
        self.g3.setText(_translate("MainWindow", "L206"))
        self.g4.setText(_translate("MainWindow", "L205"))
        self.g2.setText(_translate("MainWindow", "L207"))
        self.g6.setText(_translate("MainWindow", "goal 6"))
        self.g5.setText(_translate("MainWindow", "goal 5"))
        self.schedule_bt.setText(_translate("MainWindow", "Schedule"))
        self.quit_bt.setText(_translate("MainWindow", "Force Quit"))
        self.menuMove.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

