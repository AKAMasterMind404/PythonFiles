# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "E:/" #to_do

# link of the video to be downloaded
link="https://www.youtube.com/watch?v=xWOoBJUqlbI"

# try:
# 	# object creation using YouTube
# 	# which was imported in the beginning
# 	yt = YouTube(link)
# except:
# 	yt=None
# 	print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension
yt=YouTube(link)
print(yt)

mp4files = yt.filter()

#to set the name of the file
yt.set_filename('GeeksforGeeks Video')

# get the video with the extension and
# resolution passed in the get() function
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
try:
	# downloading the video
	d_video.download(SAVE_PATH)
except:
	print("Some Error!")
print('Task Completed!')
