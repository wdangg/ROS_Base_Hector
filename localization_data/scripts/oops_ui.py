#!/usr/bin/env python3


import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from PyQt5 import QtCore, QtGui, QtWidgets
from std_msgs.msg import String



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 311)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 541, 261))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 541, 22))
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
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.g1.clicked.connect(self.send_1st)
    
    def send_1st(self):
        rospy.init_node('send_1st_goal')
        self.pub = rospy.Publisher("pygui_topic", String, queue_size=10)
        self.move_g1 = MoveBaseGoal()
        self.move_g1.target_pose.header.frame_id = "map"
        self.move_g1.target_pose.header.stamp = rospy.Time.now()
        self.move_g1.target_pose.pose.position.x = 0.5;
        self.move_g1.target_pose.pose.position.y = -0.5;
        self.move_g1.target_pose.pose.position.z = 0.0;
        self.move_g1.target_pose.pose.orientation.z = 0.7;
        self.move_g1.target_pose.pose.orientation.w = 0.7;
        
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.wait = self.client.wait_for_server()
        self.client.send_goal(self.move_g1)
        if not self.wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            return self.client.get_result() 
        
    def send_2nd(self):
        rospy.init_node('send_2nd_goal')
        self.pub = rospy.Publisher("pygui_topic", String, queue_size=10)
        self.move_g2 = MoveBaseGoal()
        self.move_g2.target_pose.header.frame_id = "map"
        self.move_g2.target_pose.header.stamp = rospy.Time.now()
        self.move_g2.target_pose.pose.position.x = 0.5;
        self.move_g2.target_pose.pose.position.y = -0.5;
        self.move_g2.target_pose.pose.position.z = 0.0;
        self.move_g2.target_pose.pose.orientation.z = 0.7;
        self.move_g2.target_pose.pose.orientation.w = 0.7;
        
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.wait = self.client.wait_for_server()
        self.client.send_goal(self.move_g1)
        if not self.wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            return self.client.get_result() 
        
    def send_3rd(self):
        rospy.init_node('send_3rd_goal')
        self.pub = rospy.Publisher("pygui_topic", String, queue_size=10)
        self.move_g3 = MoveBaseGoal()
        self.move_g3.target_pose.header.frame_id = "map"
        self.move_g3.target_pose.header.stamp = rospy.Time.now()
        self.move_g3.target_pose.pose.position.x = 0.5;
        self.move_g3.target_pose.pose.position.y = -0.5;
        self.move_g3.target_pose.pose.position.z = 0.0;
        self.move_g3.target_pose.pose.orientation.z = 0.7;
        self.move_g3.target_pose.pose.orientation.w = 0.7;
        
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.wait = self.client.wait_for_server()
        self.client.send_goal(self.move_g1)
        if not self.wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            return self.client.get_result()
    
    def send_4th(self):
        rospy.init_node('send_4th_goal')
        self.pub = rospy.Publisher("pygui_topic", String, queue_size=10)
        self.move_g4 = MoveBaseGoal()
        self.move_g4.target_pose.header.frame_id = "map"
        self.move_g4.target_pose.header.stamp = rospy.Time.now()
        self.move_g4.target_pose.pose.position.x = 0.5;
        self.move_g4.target_pose.pose.position.y = -0.5;
        self.move_g4.target_pose.pose.position.z = 0.0;
        self.move_g4.target_pose.pose.orientation.z = 0.7;
        self.move_g4.target_pose.pose.orientation.w = 0.7;
        
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.wait = self.client.wait_for_server()
        self.client.send_goal(self.move_g1)
        if not self.wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            return self.client.get_result()
        
    def send_5th(self):
        rospy.init_node('send_5th_goal')
        self.pub = rospy.Publisher("pygui_topic", String, queue_size=10)
        self.move_g5 = MoveBaseGoal()
        self.move_g5.target_pose.header.frame_id = "map"
        self.move_g5.target_pose.header.stamp = rospy.Time.now()
        self.move_g5.target_pose.pose.position.x = 0.5;
        self.move_g5.target_pose.pose.position.y = -0.5;
        self.move_g5.target_pose.pose.position.z = 0.0;
        self.move_g5.target_pose.pose.orientation.z = 0.7;
        self.move_g5.target_pose.pose.orientation.w = 0.7;
        
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.wait = self.client.wait_for_server()
        self.client.send_goal(self.move_g1)
        if not self.wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            return self.client.get_result()
    
    def send_6th(self):
        rospy.init_node('send_6th_goal')
        self.pub = rospy.Publisher("pygui_topic", String, queue_size=10)
        self.move_g4 = MoveBaseGoal()
        self.move_g4.target_pose.header.frame_id = "map"
        self.move_g4.target_pose.header.stamp = rospy.Time.now()
        self.move_g4.target_pose.pose.position.x = 0.5;
        self.move_g4.target_pose.pose.position.y = -0.5;
        self.move_g4.target_pose.pose.position.z = 0.0;
        self.move_g4.target_pose.pose.orientation.z = 0.7;
        self.move_g4.target_pose.pose.orientation.w = 0.7;
        
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.wait = self.client.wait_for_server()
        self.client.send_goal(self.move_g1)
        if not self.wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            return self.client.get_result()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FPL Navigating"))
        self.g1.setText(_translate("MainWindow", "goal 1"))
        self.g3.setText(_translate("MainWindow", "goal 3"))
        self.g4.setText(_translate("MainWindow", "goal 4"))
        self.g2.setText(_translate("MainWindow", "goal 2"))
        self.g6.setText(_translate("MainWindow", "goal 6"))
        self.g5.setText(_translate("MainWindow", "goal 5"))
        self.menuMove.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))


if __name__ == "__main__":
    import sys
    
    
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

