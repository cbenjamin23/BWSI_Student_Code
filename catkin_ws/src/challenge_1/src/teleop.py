from ctypes import MSG
import queue
from sre_parse import State
import rospy
import pygame
import time
from djitellopy import Tello
from std_msgs.msg import Empty
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from challenge_1.msg import flip, state
       
class Teleop:
    def __init__(self) -> None:
        rospy.loginfo('Hello from the master')
        rospy.init_node('teleop', anonymous=True)
        self.flip_pub = rospy.Publisher('flip', flip, queue_size=10)
        self.takeoff_pub = rospy.Publisher('takeoff', Empty, queue_size=10)
        self.land_pub = rospy.Publisher('land', Empty, queue_size=10)
        self.vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        pygame.init()
        self.SPEED = 50
        self.FPS = 20
        self.velocity = Twist()
        self.velocity.linear.x = self.velocity.linear.y = self.velocity.linear.z = self.velocity.angular.x = 0

    def run(self):
        running = True
        while(running):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    rospy.loginfo(f'the master pressed the {str(event.key)}~~')
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_t:
                        self.takeoff_pub.publish(Empty())
                    elif event.key == pygame.K_l:
                        self.land_pub.publish(Empty())
                    elif event.key == pygame.K_d:
                        self.velocity.linear.x += self.SPEED
                    elif event.key == pygame.K_a:
                        self.velocity.linear.x -= self.SPEED
                    elif event.key == pygame.K_UP:
                        self.velocity.linear.z += self.SPEED
                    elif event.key == pygame.K_DOWN:
                        self.velocity.linear.z -= self.SPEED
                    elif event.key == pygame.K_w:
                        self.velocity.linear.y += self.SPEED
                    elif event.key == pygame.K_s:
                        self.velocity.linear.y -= self.SPEED 
                    elif event.key == pygame.K_q:
                        self.velocity.angular.x += self.SPEED
                    elif event.key == pygame.K_e:
                        self.velocity.angular.x -= self.SPEED
                    else:
                        rospy.loginfo('pressed da wrong key ya dumb')
                elif event.type == pygame.QUIT:
                    running = False
            self.vel_pub(self.velocity)
            self.sleep(1/self.FPS)
        self.land_pub(Empty())

if __name__ == '__main__':
    try:
        to = Teleop()
        to.run()   
    except:
        print('The code is failing (sent from Teleop)')
        pass