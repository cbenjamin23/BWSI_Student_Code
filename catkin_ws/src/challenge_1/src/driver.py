#!/usr/bin/env python
from ctypes import MSG
import queue
from sre_parse import State
import rospy
import pygame
from djitellopy import Tello
from std_msgs.msg import Empty
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from challenge_1.msg import flip, state

class Driver:
    def __init__(self) -> None:
        self.v = [0,0,0,0]
        rospy.loginfo('Tello buddy says wasaaaaaah')
        rospy.init_node('driver', anonymous=True)
        #self.state_pub = rospy.Publisher('state', state, queue_size=10)
        #self.img_pub = rospy.Publisher('vid', Image, queue_size=10)
        self.flip_lis = rospy.Subscriber('flip', flip, self.flip())
        self.vel_lis = rospy.Subscriber('velocity', Twist, self.cmd_vel)
        self.take_off_lis = rospy.Subscriber('takeoff', Empty, self.takeoff())
        self.land_lis = rospy.Subscribe('land', Empty, self.land())
        self.tello = Tello()
        self.tello.connect()
        
    def takeoff(self):
        if not self.tello.is_flying():
            rospy.loginfo('Ready for takeoffffffff-')
        else:
            rospy.loginfo('My tello is flyyyyyyyyyying!')
        
    def land(self, data):
        if self.tello.is_flying():
            rospy.loginfo('About to land!')
            self.tello.land()
        else:
            rospy.loginfo('On the ground already bub...')

    def flip(self, data):
        self.tello.flip(data.direction)

    def cmd_vel(self, data):
        self.v = [data.linear.x, data.linear.y, data.linear.z, data.angular.x]
    
if __name__ == '__main__':
    try:
        driver = Driver()
        
    except:
        print('RIP the code is failing (sent from Driver)')
        pass
        
    