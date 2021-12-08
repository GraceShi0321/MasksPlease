# MasksPlease Final Project

## Part 1: Running Our Project
1. Our project and the source codes in it should be ran in the Jupyter Notebook or google colab. If you cannot establish the connection, you can feel free to download our dataset and establish a new path for the notebook to find the data.
2. All required packages are listed on top of the project itself. Make sure to run the package chunk before others. If you do not have some of those, download them in Anaconda Navigator or manually install them in console. Be aware to designate the path to PIC16B.
3. If you are using google colab, store the dataset in your google drive then establish a path to retrieve it.

## Part 2: Project Structure
Our project is roughly devided into 5 parts: the visualization part to have you get an idea of what our dataset looks like, the preprocessing part where we read the image into analyzable matrices and transform it, the augmentation part to further expand on our dataset, the model validation part where we build our pipelines, and the verification part where we test our model on different test sets to draw conclusions about its performance.

## Part 3: In-Depth Demonstration of Each Part
### Data Visualization
In this part, we have roughly 1600 images with masks and 900 images without masks. All of them are in real life settings, with different lighting conditions, color schemes, facial sizes, and people belonging to different races. In general, proprtion of Asians is higher than that of Whites than that of Blacks.

### Data Processing
In this part we transformed our image size from approximately 400*400 to 100*100. We kept our original color scheme, taken into account the fact that otherwise it would confound skin colors. Also, it is necessary to remove unecessary data types like DS.store

### Data Augmentation
Given the fact that images that exhibit certain traits might be limited, we decided to experiment on the augmentation layers. We adopt both randomflip and rotation. 

### Model Building
Besides the two aforementioned augmentation layers, we also included the preprocessing layer defined in the corresponding section, four convolutional layers, three max pooling layers, a flatten layer, a dropout layer, and two Dense layers, which the latter onr has an output dimension that matches the number of classes, which is 2.

### Model Compilation and Analysis
1. In general, our model performed quite well on both the training and test set. It does not show signs of overfitting in the training-validation split, and in the test set, it reached an accuracy of around 95 percent, which is very decent.
2. When we choose different test sets, however, it showed varied accuracy. It performed better on whites than on Blacks or Asians. Difference might result from difference in proportion of images that constitude each group, or that in the heterogeneity within.

## Part 4: Transfer Learning
With the assistance of MobileNet V2, we are able to achieve an even higher accuracy.

## Part 5: Limitations and Future Expectations
### Limitations
1. Our project is based more on classification instead of identification.
2. It only recognizes static images but not in real time.
3. Limited image size leaves out some details that might or might not assist us in classification.
### Future Applications
1. Real-time facial detection
2. Flexibility to more age groups
3. Facial recognition that is able to recognize faces even with masks on.