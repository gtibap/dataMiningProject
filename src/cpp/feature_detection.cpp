#include "cv.h"
#include "highgui.h"
#include <stdio.h>
#include <iostream>
#include "opencv2/core/core.hpp"
#include "opencv2/features2d/features2d.hpp"
#include "opencv2/nonfree/features2d.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/nonfree/nonfree.hpp"

using namespace cv;

void readme();

/** @function main */
int main( int argc, char** argv )
{
  IplImage gray;

  if( argc != 4 )
  { readme(); return -1; }

  Mat img_1 = imread( argv[1], CV_LOAD_IMAGE_GRAYSCALE );
  Mat img_2 = imread( argv[1], CV_LOAD_IMAGE_GRAYSCALE );

  if( !img_1.data || !img_2.data )
  { std::cout<< " --(!) Error reading the image " << std::endl; return -1; }

  //-- Step 1: Detect the keypoints using SURF Detector
  //int minHessian = 600;
  int minHessian1 = atoi(argv[2]);
  int minHessian2 = atoi(argv[3]);


  SurfFeatureDetector detector1( minHessian1 );
//  SurfFeatureDetector detector2( minHessian2 );
  SiftFeatureDetector detector2(;

  std::vector<KeyPoint> keypoints_1, keypoints_2;

  detector1.detect( img_1, keypoints_1 );
  detector2.detect( img_2, keypoints_2 );

  //-- Draw keypoints
  Mat img_keypoints_1; Mat img_keypoints_2;

  drawKeypoints( img_1, keypoints_1, img_keypoints_1, Scalar::all(-1), DrawMatchesFlags::DEFAULT );
  drawKeypoints( img_2, keypoints_2, img_keypoints_2, Scalar::all(-1), DrawMatchesFlags::DEFAULT );

  //-- Show detected (drawn) keypoints
  imshow("Keypoints 1", img_keypoints_1 );
  imshow("Keypoints 2", img_keypoints_2 );

  waitKey(0);

  return 0;
  }

  /** @function readme */
  void readme()
  { std::cout << " Usage: ./feat <img1> <hessian1> <hessian2>" << std::endl; }
