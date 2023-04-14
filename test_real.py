import rospy
import sdh_interface
from sdh_interface import SDHInterface

import numpy as np

if __name__ == "__main__":
	rospy.init_node("example")
	
	sdhi = SDHInterface()
	rospy.sleep(10)
	for i in range(10):
		# sdhi.cmdZeroJointVel()
		# k=1.3
		# j=1
		# joint_pos = [np.pi/6, -k*np.pi/4, j*np.pi/6, -k*np.pi/4, j*np.pi/6, -k*np.pi/4,  j*np.pi/6]
		# sdhi.cmdJointState(joint_pos, time=3.0)
		sdhi.cmdOpen()
		rospy.sleep(1)
		sdhi.cmdGoToStartPos()		
		rospy.sleep(1)