#!/usr/bin/env python3
from curses.ascii import EM
import rospy
import pygame
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
from challenge_1.msg import Flip, State
       
class Teleop:
    def __init__(self) -> None:
        rospy.loginfo('Hello from the master')
        rospy.init_node('teleop', anonymous=True)
        self.flip_pub = rospy.Publisher('flip', Flip, queue_size=10)
        self.takeoff_pub = rospy.Publisher('takeoff', Empty, queue_size=10)
        self.stop_pub = rospy.Publisher('stop', Empty, queue_size=10)
        self.land_pub = rospy.Publisher('land', Empty, queue_size=10)
        self.vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.cam_pub = rospy.Publisher('switch_cam', Empty, queue_size=10)
        #pygame stuff:
        pygame.init()
        pygame.display.set_caption("Tello video stream")
        self.screen = pygame.display.set_mode((960, 720))
        #end pygame stuff
        self.SPEED = 50 #max is 100
        self.FPS = 2

    def run(self):
        running = True
        r = rospy.Rate(self.FPS) #called with r.sleep() later to limit speed of while loop
        while(running):
            velocity = Twist()
            velocity.linear.x = velocity.linear.y = velocity.linear.z = velocity.angular.x = 0
            self.screen.fill([0,0,0])
            message = Flip()
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
                        velocity.linear.x = self.SPEED
                    elif event.key == pygame.K_a:
                        velocity.linear.x = -self.SPEED
                    elif event.key == pygame.K_UP:
                        velocity.linear.z = self.SPEED
                    elif event.key == pygame.K_DOWN:
                        velocity.linear.z = -self.SPEED
                    elif event.key == pygame.K_w:
                        velocity.linear.y = self.SPEED
                    elif event.key == pygame.K_s:
                        velocity.linear.y = -self.SPEED 
                    elif event.key == pygame.K_q:
                        velocity.angular.x = self.SPEED
                    elif event.key == pygame.K_e:
                        velocity.angular.x = -self.SPEED
                    elif event.key == pygame.K_u:
                        message.direction = 'f'
                        self.flip_pub.publish(message)
                    elif event.key == pygame.K_j:
                        message.direction = 'b'
                        self.flip_pub.publish(message)
                    elif event.key == pygame.K_h:
                        message.direction = 'l'
                        self.flip_pub.publish(message)
                    elif event.key == pygame.K_k:
                        message.direction = 'r'
                        self.flip_pub.publish(message)
                    elif event.key == pygame.K_SPACE:
                        self.cam_pub.publish(Empty())
                    else:
                        rospy.loginfo('You pressed the wrong key')
                elif event.type == pygame.QUIT:
                    running = False
            self.vel_pub.publish(velocity)
            # rospy.loginfo(f'Tello set to move at {[self.velocity.linear.x, self.velocity.linear.y, self.velocity.linear.z, self.velocity.angular.x]}')
            r.sleep()
        self.land_pub.publish(Empty())
        self.stop_pub.publish(Empty())
        pygame.quit()
            
if __name__ == '__main__':
    to = Teleop()
    to.run()
    

    # try:
    #     to = Teleop()
    #     to.run()
    #     #add rospy.spin()?
    # except:
    #     print('The code is failing (sent from Teleop)')
    #     pass
    