# -*- coding: utf-8 -*-
"""
* @File Name:           pdbtest.py
* @Author:              XXXXX
* @Created Date:        2018-01-15 20:05:27
* @Last Modified Data:  2018-01-16 09:24:13
* @Desc:
* @function :           HSV color space computation for original captured image
"""

from skimage import io,data,color,exposure
import os

#################################################################
# address of the original captured image
data_path_root = '/media/chenzp/DA7C896D7C8944EB/DATA_Collect/next/'
#data_path = '/media/liuqianfei/DATADRIVE0/项目资料/X4R/'
#data_path_root = os.path.join(data_path,'03 数据标注','03原始数据')

Valid_num = 30

for root, dirs, files in os.walk(data_path_root):
   if len(files)!=0 and root.split('_cam/0')!='' and len(root.split('_cam/0')) == 2:
      temp_folder = '%s%s' %(root.split('_cam/0')[0],'_cam')
      save_folder = os.path.join(temp_folder,'2')

      #create a new folder which is named '2' to save the output files
      if os.path.exists(save_folder) == False:
         os.mkdir(save_folder)
      with open(os.path.join(save_folder,'log.txt'),'w') as log:
         files = ",".join(files)
         files = files.split(',')
         for file in range(0,len(files)):
             if (int(files[file].split('.')[0]))%2 == 1:  #only computation for odd frames
                src = os.path.join(root,files[file])
                try:
                    img = io.imread(src)
                except IOError:
                    continue
                hsv = color.convert_colorspace(img,'RGB','HSV')
                hist1 = exposure.histogram(hsv[185:480,:,2]*255, nbins=256)

                # value computation of 'v_range'
                v_range = 0
                for i in range (len(hist1[0])):
                    m = (hist1[0][i]/hist1[0].max())*800
                    if m >= Valid_num :
                       v_range = v_range + 1

                #original image size is 480*640; for interested of image region, the num of row is range from 185 to 480
                if v_range >= 16 and (hsv[185:480,:,2].mean()*255)>=31:
                   io.imsave(os.path.join(save_folder,files[file]),img)# 'V' value computed only,left alone the 'H'and 'S' value
                   print('{} : V_ave={:.1f}  V_range={:.1f}\n'.format(files[file],hsv[185:480,:,2].mean()*255, v_range))
                   log.write('{} : V_ave={:.1f}  V_range={:.1f}\n'.format(files[file],hsv[185:480,:,2].mean()*255, v_range))

#################################################################
''' 将原始图像名编号补齐成为4位数，eg '12.jpg'-->'0012.jpg'
for root, dirs, files in os.walk(data_path_root):
   if len(files)!=0:
      files = ",".join(files)
      files = files.split(',')
      for file in range(0,len(files)):
          src = os.path.join(root,files[file])
          img = io.imread(src)
          name_1 = files[file].split('.')[0]
          if len(name_1) <4 :
             for num in range(0,4-len(name_1)):
                 name_1 = '%s%s' %('0',name_1)
          files2 = '%s%s' %(name_1,'.jpg')
          dst = os.path.join(root,files2)
          os.rename(src,dst)
          print(dst)
'''
#################################################################

''' 利用matplotlib读取并显示图像
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image = mpimg.imread("chelsea-the-cat.png")
plt.imshow(image)
plt.show()
'''

'''利用skimage.viewer显示图像
from skimage.viewer import ImageViewer
image = data.coins()
viewer = ImageViewer(image)
viewer.show()
'''
#################################################################
