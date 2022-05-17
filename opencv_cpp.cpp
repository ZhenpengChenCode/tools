#include <iostream>
#include <opencv2/opencv.hpp>

/**
 * 使用图片替换src图片的roi区域
*/
int main() {
    cv::Mat src_image = cv::imread("/home/beiming/workspace/posetrack_czp/data/0001.png");
    cv::Mat roi_image = cv::imread("/home/beiming/workspace/posetrack_czp/data/old_show.jpg");
    cv::Rect roi = cv::Rect(50, 50, 50+384, 50+384);
    cv::resize(roi_image, roi_image, cv::Size(roi.width, roi.height), cv::INTER_NEAREST);
    roi_image.copyTo(src_image(roi));
    cv::imwrite("./show_img.jpg", src_image);
  
    return 0;
}
