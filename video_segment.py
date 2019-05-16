import cv2
import os
def video_seg(video_path, save_path, sample_margin=5, start_frame=0):
    videos = []
    for v in os.listdir(video_path):
        if v.endswith("MTS"):
            videos.append(v)
    videos = sorted(videos, key=lambda a: int(a.split(".")[0]))
    count = start_frame
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    for v in videos:
        vidcap = cv2.VideoCapture(os.path.join(video_path, v))

        success,image = vidcap.read()
        # count = 0
        success = True
        while success:
          if count % sample_margin - start_frame == 0:
            cv2.imwrite(os.path.join(save_path, "frame%d.jpg" % count), image)     # save frame as JPEG file
          success,image = vidcap.read()
          count += 1
video_seg("F:/Dataset/DukeMTMC/re-id/01", "F:/Dataset/DukeMTMC/re-id/01/frames")