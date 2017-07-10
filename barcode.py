import imageio
import numpy as np
import math
from queue import *

# -------------------- HELPER FUNCTIONS -------------------- #

def get_average(q):
	total = 0
	count = 0
	while not q.empty():
		total = total + q.get()
		count = count + 1
	if total < 1:
		print("ITS 0 LMAO GG")
		print(total)
	return int(total / count)

def pop_all(q):
	while not q.empty():
		temp = q.get()
	return q


# -------------------------- MAIN -------------------------- #

# Get filename from user
#print "What file do you want to convert?"
#filename = 'stay.mp4' 
# TODO: Change this so people can actually use it...

# Creating reader
reader = imageio.get_reader('stay.mp4')

# Getting static values
length = reader.get_length()
width = 2560
height = 1600
q_length = length / width # NOTE: THIS CANNOT BE 0
q = Queue(q_length) # queue for rolling average with max size q_length
px_count = 0

wallpaper = np.zeros((height, width))

# Iterating through rows
for i, im in enumerate(reader):
	# Adding to the rolling average
	q.put(im.mean())
	# Once the rolling average has reached its limit, add the
	# average to the image and reset
	if q.full():
		# Iterating through one column
		pixel = get_average(q)
		for c in range(height):
			wallpaper[c][px_count] = pixel
		print(px_count)
		px_count = px_count + 1
		# Emptying the queue
		q = pop_all(q) # there must be a better way to do this...
		#print(q.qsize())

# Writing final image
writer = imageio.get_writer('test.png')
writer.append_data(wallpaper)
