import rospy
import sdh_interface
from sdh_interface_sim import SDHInterfaceSim

if __name__ == "__main__":
    rospy.init_node("example")

    sdhi = SDHInterfaceSim()
    rospy.sleep(10)
    sdhi.cmdOpen()
    rospy.sleep(10)
    sdhi.cmdGoToStartPos()