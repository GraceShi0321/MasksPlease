# MasksPlease
This repository contains code for PIC16B project of face mask detection in real time.

```
X..
.O.
.OX
```

Here will be the place for our Proposal!

# Abstract
#### The problem: 
During the period of pandemic, face masks and social distance are necessary for everyone’s safety concerns; however, as shown on the school’s website, there are still new COVID cases being discovered almost every day in UCLA while we can still see many students walking around the campus without the mask on.  
If we can build a real-time face mask detection program, we could provide friendly reminders to those who didn’t put their masks on so to create a safer environment on campus to solve the problem that it is difficult to check and make sure everyone has followed the guidance.
#### The overall approach:
The goal of this face mask detection project is to create an image recognition system by executing image classification accurately.        
In order to achieve detecting masks in images first and then later try to detect masks in real-time video streams, we will need to build and train our face mask detector on a training set then test the detector on a test set, also making any further modifications if necessary.

# Planned Deliverables
We are aiming to create a real-time face mask detection system that can accurately classify people who have worn the masks and those who haven't so to provide a friendly reminder to those haven't in order to create a safer campus environment.  
We will be making a face mask detection system and the core will be building a successful face mask detector.
#### “Full success.” 
We will be making a real-time face masks detection system that can accurately detect whether a person has worn a mask or not even, and this capability should work under variables such as gender, race, patterns on the masks, size of the masks, the fit of the masks and also whether the masks are worn properly.    
The interface in this case would be a Jupyter notebook containing the necessary code.
#### “Partial success.”
Even if our real-time face masks detection system is not perfect, we would still expect a successful deliver of a face mask detection system working accurately on images.
The interface in this case would be a Jupyter notebook containing the necessary code.

# Resources Required
Data sets are the essential resources required for this project.   
We would need data that can be seperated into three groups: 1) images of people wearing the masks correctly, 2) images of people wearing the masks incorrectly, and 3) images of people not wearing masks     
Link to data set:     
- 67,049 images of the Correctly Masked Face Dataset: https://esigelec-my.sharepoint.com/personal/cabani_esigelec_fr/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fcabani%5Fesigelec%5Ffr%2FDocuments%2FMaskedFaceNetDataset%2FCMFD&originalPath=aHR0cHM6Ly9lc2lnZWxlYy1teS5zaGFyZXBvaW50LmNvbS86ZjovZy9wZXJzb25hbC9jYWJhbmlfZXNpZ2VsZWNfZnIvRXYzR2RuUVN5enhQanl6VTVFbEhxYWdCbGtSQ2FLbm5DSTg1aVgtZDFMNE9IQT9ydGltZT10RVF5WUFPTzJVZw      
- 66,734 images of the Incorrectly Masked Face Dataset: https://esigelec-my.sharepoint.com/personal/cabani_esigelec_fr/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fcabani%5Fesigelec%5Ffr%2FDocuments%2FMaskedFaceNetDataset%2FIMFD&originalPath=aHR0cHM6Ly9lc2lnZWxlYy1teS5zaGFyZXBvaW50LmNvbS86ZjovZy9wZXJzb25hbC9jYWJhbmlfZXNpZ2VsZWNfZnIvRWlyalM4ZXc3LTVMbk84STU2VWs2M3dCS2Vid1NsdWtGQkZCYU84TjI1d24zZz9ydGltZT1SMTQ1a0FPTzJVZw
- 20k+ images of the Not Masked Face Dataset: https://susanqq.github.io/UTKFace/

# Tools and Skills Required
The tools and skills that are required for this project would be TensorFlow, OpenCV and an understanding of the rationale behind machine learning or deep learning.
- TensorFlow: will be needed to build our model. (From the schedule, we will learned about TensorFlow in PIC16B during week 6)
- OpenCV: images inside the library will be needed to train the face detection system
- Will need to understand the core pricinples of machine learning or deep learning to decide on the best algorithm to train

# What We Will Learn
First, we will learn all the tools and skills required in this project, as mentioned in the previous section. These include TensorFlow, OpenCV, and an overall understanding of the rationale behind machine learning / deep learning. In addition, we will need to be familiar with collaborating over GitHub. Finally, we will learn how to collaborate!

# Risks
First, due to our limited knowledge in machine learning / deep learning, we may not be able to select the best type of algorithm/neural network for our task. Second, even if our face mask detection algorithm works great on our datasets, its applicability to real-life situations is uncertain and is contingent on several external factors, such as how representative our training/testing datasets are, and quality of images captured by the camera and delivered to the algorithm (suppose our face mask detection algorithm will eventually be implemented in hardwares). 


