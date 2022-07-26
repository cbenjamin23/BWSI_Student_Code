#!/usr/bin/env python3
import traceback
import rospy
import cv2
import math
import numpy as np
from cv_bridge import CvBridge
from djitellopy import Tello
from std_msgs.msg import Empty
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from challenge_1.msg import Flip, State #a message file easily defines the type of data to expect

class Driver:
    def __init__(self) -> None:
        self.v = [0,0,0,0] #velocity in x,y,z,angular directions (this is initializing 'v')
        rospy.loginfo('Tello buddy says wasaaaaaah')
        rospy.init_node('driver', anonymous=True)
        self.state_pub = rospy.Publisher('state', State, queue_size=10)
        self.img_pub = rospy.Publisher('vid', Image, queue_size=10)
        self.flip_lis = rospy.Subscriber('flip', Flip, self.flip)
        self.vel_lis = rospy.Subscriber('cmd_vel', Twist, self.cmd_vel)
        self.take_off_lis = rospy.Subscriber('takeoff', Empty, self.takeoff)
        self.land_lis = rospy.Subscriber('land', Empty, self.land)
        self.stop_lis = rospy.Subscriber('stop', Empty, self.stop)
        self.cam_lis = rospy.Subscriber('switch_cam', Empty, self.switch_cam)
        self.down_cam = False
        self.FPS = 30
        self.running = True
        self.MAX_SPEED = 80
        self.tello = Tello()
        self.tello.connect()
        self.tello.streamoff()
        self.tello.streamon()
        self.frame_read = self.tello.get_frame_read() #gets camera view
        self.br = CvBridge() #getting ready for later image conversion
        
        
    def takeoff(self, data): #data because a command is being called somewhere (the keyboard key is the 'input')
        if not self.tello.is_flying:
            rospy.loginfo('Ready for takeoffffffff-')
            self.tello.takeoff()
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
        self.v = [data.linear.x, data.linear.y, data.linear.z, -data.angular.x]
        for i in range(len(self.v)):
            self.v[i] = min(self.v[i], self.MAX_SPEED)
            
    def switch_cam(self, data):
        self.down_cam = not self.down_cam
        if self.down_cam:
            rospy.loginfo('Switching to downward camera')
            self.tello.set_video_direction(self.tello.CAMERA_DOWNWARD)
        else:
            rospy.loginfo('Switching to front camera')
            self.tello.set_video_direction(self.tello.CAMERA_FORWARD)
            
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
        
    def stop(self, data):
        self.running = False
        
    def run(self):
        r = rospy.Rate(self.FPS)
        self.running = True
        while self.running:
            self.state_pub.publish(self.update_info())
            # rospy.loginfo(f'the tello is {info.state}')
            frame = self.frame_read.frame
            self.img_pub.publish(self.br.cv2_to_imgmsg(frame, 'bgr8')) #converting cv2 image to ross image form
            
            arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_1000)
            corners, ids, rejects = cv2.aruco.detectMarkers(frame, arucoDict)
            print("Corners are: " + str(corners))
            print("ID is: " + str(ids))
            obj = marker(ids, corners)
            if corners:
                print("centroid is: " + str(obj.get_centroid()))
                print("average side length is: " + str(obj.avg_side_len()))
                obj.getAttributes()
                
            
            if self.tello.is_flying:
                self.tello.send_rc_control(int(self.v[0]), int(self.v[1]), int(self.v[2]), int(self.v[3]))
            r.sleep()
        self.land()
        
        
class marker:
    
    def __init__(self, ID, corners) -> None:
        self.corners = corners
        self.ID = ID
        
    def get_centroid(self):
        return np.mean(self.corners[0][0], axis=0)
        
    def avg_side_len(self):
        side_lengths = [math.dist(self.corners[0][0][0], self.corners[0][0][1]), math.dist(self.corners[0][0][1], self.corners[0][0][2]),
                            math.dist(self.corners[0][0][2], self.corners[0][0][3]), math.dist(self.corners[0][0][3], self.corners[0][0][0])]
        return np.mean(side_lengths)
    
    def _rotationMatrix2EulerAngles(self, R):
        sy = math.sqrt(R[0,0]*R[0,0] + R[0,1]*R[0,1])
        singular = sy<1e-6
        if not singular:
            x = math.atan2(R[2,1], R[2,2])
            y = math.atan2(-R[2,0], sy)
            z = math.atan2(R[1,0], R[0,0])
        else:
            x = math.atan2(-R[1,2], R[1,1])
            y = math.atan2(-R[2,0], sy)
            z = 0
        return np.rad2deg(np.array([x,y,z]))
    
    def getAttributes(self):
        self.cameraMatrix = np.array([[921.170702, 0.000000, 459.904354], [0.000000, 919.018377, 351.238301], [0.000000, 0.000000, 1.000000]])
        self.distCoeffs = np.array([-0.033458, 0.105152, 0.001256, -0.006647, 0.000000])
        self.rvecs, self.tvecs, _objPoints = cv2.aruco.estimatePoseSingleMarkers(self.corners, 0.127, self.cameraMatrix, self.distCoeffs)
        
        R_flip  = np.zeros((3,3), dtype=np.float32)
        R_flip[0,0] = 1.0
        R_flip[1,1] =-1.0
        R_flip[2,2] =-1.0
        
        R_tc = np.matrix(cv2.Rodrigues(self.rvecs)[0]).T
        self.pitch, self.yaw, self.roll = self._rotationMatrix2EulerAngles(R_flip*R_tc)
        self.pos_camera = -R_tc*np.matrix(self.tvecs).T
        #these printouts are from the perspective of the marker
        print("X translation vector is: " + str(self.pos_camera[0]))
        print("Y translation vector is: " + str(self.pos_camera[1]))
        print("Z translation vector is: " + str(self.pos_camera[2])) #distance to tag/tello
        print("roll is: " + str(self.roll))
        print("pitch is: " + str(-self.pitch))
        print("yaw is: " + str(self.yaw))
        
        
if __name__ == '__main__':
    try:
        driver = Driver()  
        driver.run()
    except Exception as e:
        print(traceback.print_exc())
        print(str(e))
        print('RIP the code is failing (sent from Driver)')
        pass
        
