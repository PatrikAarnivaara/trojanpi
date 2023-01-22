from moviepy.editor import *
import numpy as np

clip1 = VideoFileClip("laokoon.mp4").subclip(0, 03.00)
clip2 = VideoFileClip("laokoon.mp4").subclip(03.00, 05.00)
clip3 = VideoFileClip("laokoon.mp4").subclip(05.00, 08.00)
clip4 = VideoFileClip("laokoon.mp4").subclip(08.00, 11.00)
clip5 = VideoFileClip("laokoon.mp4").subclip(14.00, 17.00)
clip6 = VideoFileClip("laokoon.mp4").subclip(17.00, 20.00)
clip7 = VideoFileClip("laokoon.mp4").subclip(20.00, 23.00)
clip8 = VideoFileClip("laokoon.mp4").subclip(23.00, 27.00)
clip9 = VideoFileClip("laokoon.mp4").subclip(27.00, 29.33)

clips = np.array([clip1, clip2, clip3, clip4, clip5, clip6, clip7, clip8, clip9])
np.random.shuffle(clips)

final_clip = concatenate_videoclips(clips)

final_clip.write_videofile("laokoon_edit.mp4", fps=25)

""" 29.33 """
