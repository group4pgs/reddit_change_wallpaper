#!/usr/bin/env python
import ctypes
import os

class apply_background():
	"""docstring for apply_background"""
	image_name = ""
	def __init__(self, todays_date):
		self.image_name = todays_date
		self.apply()

	def apply(self):
		drive = "C:\\"
		folder = "Users\Azazel\Desktop\IOTD"
		image = self.image_name
		image_path = os.path.join(drive, folder, image)
		SPI_SETDESKWALLPAPER = 20 
		ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)
		print "Done :)"

