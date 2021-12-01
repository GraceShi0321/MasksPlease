
# First we need to read in the required packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# List of file names
masks_list1 = ["data/with_mask/000 copy 36.jpg", "data/with_mask/001 copy 2.jpg", "data/with_mask/004 copy 2.jpg", "data/with_mask/004 copy 9.jpg"]
# Loop through all images, display them
for x in masks_list1:
    # Read in the image
    image = mpimg.imread(x)
    # Show it
    plt.imshow(image)
    plt.show()
    
# List of file names
masks_list2 = ["data/with_mask/1-with-mask.jpg", "data/with_mask/2-with-mask.jpg", "data/with_mask/3-with-mask.jpg", "data/with_mask/5-with-mask.jpg"]
# Loop through all images, display them
for x in masks_list2:
    image = mpimg.imread(x)
    plt.imshow(image)
    plt.show()