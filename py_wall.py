#py_file
import json
import urllib
import os

os.system('export GIO_EXTRA_MODULES=/usr/lib/x86_64-linux-gnu/gio/modules/')	#to remove backend error
url = urllib.urlopen('https://api.nasa.gov/planetary/apod?api_key=LBzdGVRkhVayk4DL6sxLtUuBv0gc1cy0goHcvLNz')
urlj = json.load(url)

if urlj['media_type'] == 'image':	#to check if the element is picture only
	urllib.urlretrieve(urlj['hdurl'],'/home/raghuttam/apod_img.jpg')
else:
	print("The image is unavailable today as the server has uploaded a "+urlj['media_type'])

os.system('export GIO_EXTRA_MODULES=/usr/lib/x86_64-linux-gnu/gio/modules/')
os.system('gsettings set org.gnome.desktop.background picture-uri file:///home/raghuttam/apod_img.jpg')

