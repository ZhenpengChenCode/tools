import os
import os.path as osp

import cv2

folder_path = '/beiming/data/person_detection/mscoco_instance/val2017'

txt_list = []
for root, _, files in os.walk(folder_path):
    for f in files:
        if f.endswith('txt'):
            txt_list.append(osp.join(root, f))

for txt_path in txt_list:
    img_path = txt_path.replace('txt', 'png')
    cvimg = cv2.imread(img_path)
    height, width, channels = cvimg.shape
    with open(txt_path, 'r') as f:
        line = f.readlines()[0].strip().split(' ')
        line = [float(it) for it in line]
        ctx, cty, bw, bh = line[1:]
        ctx, cty, bw, bh = int(ctx*width), int(cty*height), int(bw*width), int(bh*height)
        
        # represents the top left corner of rectangle
        start_point = (ctx-bw//2, cty-bh//2)
        end_point = (ctx+bw//2, cty+bh//2)
        # Blue color in BGR
        color = (255, 0, 0)
        
        # Line thickness of 2 px
        thickness = 2
        
        # Using cv2.rectangle() method
        # Draw a rectangle with blue line borders of thickness of 2 px
        cvimg = cv2.rectangle(cvimg, start_point, end_point, color, thickness)
    imgname = osp.basename(img_path)
    cv2.imwrite(imgname, cvimg)
        
        
