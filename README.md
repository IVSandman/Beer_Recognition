# Beer_Recognition


https://github.com/IVSandman/Beer_Recognition/assets/79752360/76661563-8a01-40ca-89fe-83c33c1c81c3




https://github.com/IVSandman/Beer_Recognition/assets/79752360/dfe96c50-69b0-420a-ab35-ea94a1f23b70





This project is part of the Digital Image Processing and Machine Vision subject and continuously developed in the Industrial Based Design Project subject of King Mongkut's University of Technology North Bangkok's third year.

Real-time Beer Recognition using digital image processing for classified and label type of beers using HSV color model.

                                                        Background
We're developing a beer recognition system that identifies beer types based on label colors with high 
precision and minimal errors. Our objective is to explore techniques to pinpoint the most effective model for 
this discrimination.

                                                        Scope
1. Utitlize exclusively commercial beers in Thailand supermarket. 
2. Observe the hindrance of classification using HSV color model. 
3. Employ solely Image processing procedures. 
4. The programe nacessitates execute on instantaneous camera with actual beers. 
5. Implement at most five sample type of beers.

                                                        Objective

1.Create a system that can identify different types of beers based on their label colors. 
2.Aim for high precision in recognizing beer types, while minimizing mistakes. 
3.Explore different color techniques to find the best way to recognize beer labels


                                                        Methodology
1.  Capture the image
2.  Read the frame
3.  Convert frame to HSV
4.  Color Thresholding
5.  Find contour in the mask
6.  Draw the box and label
7.  Display result

                                                        Conclusion
From our hypothesis, we expected our program to have high precision in the recognition system, minimized number of contours, and errors. The final result, it’s capable of 3 types of beer such as larger, amber ale, and dunkel.

                                                        Reference
Identifying the range of color in HSV using OpenCV
https://stackoverflow.com/questions/36817133/identifying-the-range-of-a-color-in-hsv-using-opencv

Problem with HSV and RGB color model
https://dsp.stackexchange.com/questions/14408/problem-with-hsv-and-rgb-color-model

Choosing the correct upper and lower HSV boundaries for color detection with`cv::inRange` (OpenCV)
https://stackoverflow.com/questions/10948589/choosing-the-correct-upper-and-lower-hsv-boundaries-for-color-detection-withcv

Beer color scale
https://homebrewing.org/pages/srm-beer-color-scale
https://blackcreekbrewery.wordpress.com/2015/04/09/degl-srm-and-ebc-a-brief-look-at-beer-colour-scales/
