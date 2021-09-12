import os
import os.path as osp
import shutil
import cv2
from tqdm import tqdm

video_folder = "/home/chenzp/datasets/adas/20210207" # 原始视频目录
output_path = "" # 原始视频目录路径

max_grab_frame_num_of_each_video = None   # 指定每个视频抽帧的最大帧数, 默认为None（不限制). 设为1000张，则每个视频最多只截取1000张图片
skip_frame_num_of_each_video = 30  # 抽帧间隔
skip_frame_time_length = 30   # 抽帧时间间隔 s


video_list = []
for root, _, files in os.walk(video_folder):
    for f in files:
        video_list.append(os.path.join(root, f))


for video_path in tqdm(video_list):
    #output_folder = os.path.join(output_path, osp.basename(video_path))
    output_folder = output_path.replace('synchronized', 'synchronized_out')
    #if (os.path.exists(output_folder)):
    #    shutil.rmtree(output_folder)
    os.makedirs(output_folder, exist_ok=True)
    vc = cv2.VideoCapture(video_path)
    framerate = int(vc.get(5))
    framenum = int(vc.get(7))
    skip_frame_num_of_each_video = skip_frame_time_length * framerate

    index = list(range(0, framenum, skip_frame_num_of_each_video))
    if max_grab_frame_num_of_each_video is None:
        pass
    elif isinstance(max_grab_frame_num_of_each_video, int):
        if len(index) > max_grab_frame_num_of_each_video:
            index = []
            index = list(range(0, framenum, int(framenum/max_grab_frame_num_of_each_video)))[:max_grab_frame_num_of_each_video]

    for i in index:
        #vc = cv2.VideoCapture(video)
        vc.set(cv2.CAP_PROP_POS_FRAMES, i)
        if vc.isOpened():
            rval, frame = vc.read()
            if frame is None:
                continue
            cv2.imwrite(os.path.join(output_folder , str(i) + '.jpg'), frame)
            #break
        else:
            print('openerror!')
            rval = False
    cv2.waitKey(1)
    vc.release()

    '''
    vc.set(cv2.CAP_PROP_POS_FRAMES, framenum-1)
    a, b2 = vc.read()


    c = 1
    if vc.isOpened():
        rval, frame = vc.read()
    else:
        print('openerror!')
        rval = False

    timeF = 1  #视频帧计数间隔次数
    while rval:
        rval, frame = vc.read()
        if c % timeF == 0 and rval:
            cv2.imwrite(os.path.join(output_folder , str(int(c / timeF)) + '.jpg'), frame)
        c += 1
    cv2.waitKey(1)
    vc.release()
    '''
