#!/usr/bin/env python3
import traceback
import rospy
from cv_bridge import CvBridge
from djitellopy import Tello
from std_msgs.msg import Empty
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from challenge_1.msg import Flip, State

class Driver:
    def __init__(self) -> None:
        self.v = [0,0,0,0]
        rospy.loginfo('Tello buddy says wasaaaaaah')
        rospy.init_node('driver', anonymous=True)
        self.state_pub = rospy.Publisher('state', State, queue_size=10)
        self.img_pub = rospy.Publisher('vid', Image, queue_size=10)
        self.flip_lis = rospy.Subscriber('flip', Flip, self.flip)
        self.vel_lis = rospy.Subscriber('velocity', Twist, self.cmd_vel)
        self.take_off_lis = rospy.Subscriber('takeoff', Empty, self.takeoff)
        self.land_lis = rospy.Subscriber('land', Empty, self.land)
        self.stop_list = rospy.Subscriber('stop', Empty, self.stop)
        self.FPS = 30
        self.running = True
        self.max_speed = 80
        self.tello = Tello()
        self.tello.connect()
        self.tello.streamoff()
        self.tello.streamon()
        self.frame_read = self.tello.get_frame_read()
        self.br = CvBridge()
        
        
    def takeoff(self, data):
        if not self.tello.is_flying:
            rospy.loginfo('Ready for takeoffffffff-')
        else:
            rospy.loginfo('My tello is flyyyyyyyyyying!')
        
    def land(self, data):
        if self.tello.is_flying:
            rospy.loginfo('About to land!')
            self.tello.land()
        else:
            rospy.loginfo('On the ground already bub...')

    def flip(self, data):
        self.tello.flip(data.direction)

    def cmd_vel(self, data):
        self.v = [data.linear.x, data.linear.y, data.linear.z, data.angular.x]
        for i in range(len(self.v)):
            self.v[i] = min(self.v[i], self.MAX_SPEED)
            
    def switch_cam(self, data):
        self.down_cam = not self.down_cam
        if self.down_cam:
            rospy.loginfo('Switching to downward camera')
            self.tello.set_video_direction(self.tello.CAMERA_DOWNWARD)
        else:
            rospy.loginfo('Switching to front camera')
            
    def update_info(self):
        info = State()
        info.battery = int(self.tello.get_battery())
        info.height = float(self.tello.get_height())
        info.pressure = float(self.tello.get_barometer())
        # info.tof = float(self.tello.get_distance_tof())
        # info.temp = float(self.tello.get_highest_temperature())
        # info.vx, info.vy, info.vz = float(self.tello.get_speed_x()), float(self.tello.get_speed_y()), float(self.tello.get_speed_z())
        # info.ax, info.ay, info.az = float(self.tello.get_acceleration_x()), float(self.tello.get_acceleration_y()), float(self.tello.get_acceleration_z())
        # info.is_flying = self.tello.is_flying
        # info.cam_forward = not self.down_cam
        return info
        
    def stop(self, _):
        self.running = False
        
    def run(self):
        r = rospy.Rate(self.FPS)
        self.running = True
        while self.running:
            self.state_pub.publish(self.update_info())
            # rospy.loginfo(f'the tello is {info.state}')
            frame = self.frame_read.frame
            self.img_pub.publish(self.br.cv2_to_imgmsg(frame))
            if self.tello.is_flying:
                self.tello.send_rc_control(self.v[0], self.v[1], self.v[2], self.v[3])
            r.sleep()
        self.land()
    
if __name__ == '__main__':
    try:
        driver = Driver()  
        driver.run()
    except Exception as e:
        print(traceback.print_exc())
        print(str(e))
        print('RIP the code is failing (sent from Driver)')
        pass
        
    