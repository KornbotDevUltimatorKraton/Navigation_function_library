import os
import cv2
import serial
import json
import math
import threading
import subprocess
import time
from itertools import count
from navigation_lib import rssi_distance_report, Lidar_info_report,data_projection_post,Camera_image_sensor
data_sensor = {}
cap_Camera_1 = cv2.VideoCapture(0)

def device_Camera_1():
		while True:
			Camera_image_sensor('kornbot380@hotmail.com','Smart_bots',cap_Camera_1,0,'Camera_1')
def device_WiFi_1():
	while True:
		data_WiFi_1 = rssi_distance_report('kornbot380@hotmail.com', 'WiFi_1')
		data_sensor['WiFi_1'] = data_WiFi_1
def post_data_core():
	while True:
		data_projection = data_projection_post('kornbot380@hotmail.com',data_sensor)
		print(data_projection)
t_Camera_1 = threading.Thread(target=device_Camera_1)
t_Camera_1.start()
t_WiFi_1 = threading.Thread(target=device_WiFi_1)
t_WiFi_1.start()
t_post_projection = threading.Thread(target=post_data_core)
t_post_projection.start()
