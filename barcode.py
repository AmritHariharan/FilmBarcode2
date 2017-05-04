import imageio
import numpy as np

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

wallpaper = np.zeros((height, width))
sq_img = np.zeros((length, length))

for i, im in enumerate(reader):
	#print('Mean of frame %i is %1.1f' % (i, im.mean()))
	mean = im.mean()
	for c in range(length):
		sq_img[c][i] = mean


# Writing final image
writer = imageio.get_writer('test.png')
writer.append_data(sq_img)
