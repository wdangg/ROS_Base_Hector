#!/usr/bin/env python3

import os, sys
from std_msgs.msg import String
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

g1 = MoveBaseGoal()
g2 = MoveBaseGoal()
g3 = MoveBaseGoal()
g4 = MoveBaseGoal()
g5 = MoveBaseGoal()

class pyGui(QWidget):
    def __init__(self):
        super(pyGui, self).__init__()
        uic.loadUi('pygui.ui', self)
        self.pub = rospy.Publisher("pygui_topic", String, queue_size=10)
        rospy.init_node('py_gui')
        self.is_pub = False
        self.current_value = self.horizontalSlider.value()
        print (self.current_value)
        self.label.setText("num: " + str(self.current_value))
        
        self.pushButton.pressed.connect(self.publish_topic)
        self.pushButton_2.pressed.connect(self.gui_close)
        self.horizontalSlider.valueChanged.connect(self.change_value)

    def publish_topic(self):
        self.pub.publish(str(self.current_value))
        self.pushButton.setEnabled(False)
        self.is_pub = True

    def change_value(self, value):
        self.current_value = value
        if True == self.is_pub:
            self.label.setText("num: " + str(value))
            self.pub.publish(str(self.current_value))

    def gui_close(self):
        self.close()


def main():
    app= QApplication(sys.argv)
    pyShow = pyGui()
    pyShow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()