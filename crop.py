
import os, sys
sys.path.append('../SoSeq-segment')
from utils.io import *

video_lenghts = get_video_lengths('../data')

#color_pipe = None
depth_pipe = None
for k,l in video_lenghts.items():
    if k == sys.argv[1]:
        for frame in range(0,l,100):
#             cc = read_color_frames('../data/'+k, range(frame,np.min([frame+100,l])), frame_size=(1280,720))
#             color_pipe = write_color_frames('data_cropped/'+k,
#                                             cc[:,100:580,300:840,:],
#                                             pipe=color_pipe, 
#                                             close_pipe=False, fps=30,
#                                             pixel_format='rgb24', 
#                                             codec='h264')
            dd = read_depth_frames('../data/'+k.replace('color.mp4','depth.avi'), range(frame,np.min([frame+100,l])), frame_size=(1280,720))
            depth_pipe = write_depth_frames('data_cropped/'+k.replace('color.mp4','depth.avi'),
                                            dd[:,100:580,300:840], 
                                            pipe=depth_pipe, 
                                            close_pipe=False, fps=30)

            print(k,frame)

#color_pipe.stdin.close()
depth_pipe.stdin.close()

