""" ROS Bag file topic definitions
"""

SINGLE_CAMERA_TOPIC = "/image_raw"
CAMERA_TOPICS = [SINGLE_CAMERA_TOPIC]

CAP_REAR_GPS_TOPICS = ["/gps/fix"]
CAP_REAR_RTK_TOPICS = ["/gps/rtkfix"]
CAP_FRONT_GPS_TOPICS = ["/gps/fix"]
CAP_FRONT_RTK_TOPICS = ["/gps/rtkfix"]

OBJECTS_TOPIC_ROOT = "/"

TF_TOPIC = "/tf"
