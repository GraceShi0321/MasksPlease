# First we need to read in the required packages
import cv2,os
import numpy as np
from keras.utils import np_utils

# Create an empty dictionary to store data
data_path='data'
categories=os.listdir(data_path)
# labels: without_mask, with_mask
labels=[i for i in range(0, len(categories))]

# Create an empty dictionary with keys = labels
label_dict=dict(zip(categories,labels))

print(label_dict)
print(categories)
print(labels)

# Loop through the datasets, preprocess each image, 
# and append the preprocessed image to the empty dictionary created above
img_size=100
data=[]
target=[]


for category in categories:
    # Construct path to each folder ('without_mask', 'with_mask')
    folder_path=os.path.join(data_path,category)
    img_names=os.listdir(folder_path)
    
    # Loop through images in each folder
    for img_name in img_names:
        img_path=os.path.join(folder_path,img_name)
        img=cv2.imread(img_path)

        try:
            # Coverting the image into gray scale
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)           
            # Resizing the gray scale into 50x50, since we need a fixed common size for all the images in the dataset
            resized=cv2.resize(gray,(img_size,img_size))
            #appending the image and the label(categorized) into the list (dataset)
            data.append(resized)
            target.append(label_dict[category])
            
        except Exception as e:
            print('Exception:',e)
            #if any exception rasied, the exception will be printed here.
            
"""
In this part we transform the numeric value to between 0 and 1
to speed up the training process, and reshape the image
to a smaller size
"""
# Convert RGB values to 0-1 scale
data=np.array(data)/255.0
# Reshape data to a smaller size
data=np.reshape(data,(data.shape[0],img_size,img_size,1))
target=np.array(target)

# Covert integer vector to binary class matrix
new_target=np_utils.to_categorical(target)

# save data so can access later 
np.save('data',data)
np.save('target',new_target)