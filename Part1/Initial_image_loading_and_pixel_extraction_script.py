#importing necessary libraries
import cv2
import csv
import numpy as np
import matplotlib.pyplot as plt

#importing the numpy array file of images
data = np.load('images.npy')

#Vissualizing the pixel data of image
#choosing one of the images from data
import matplotlib.pyplot as plt
image = data[0]
# Display the data as an image
plt.imshow(image)
plt.show()

#just an example to get intensity at row 100, col 100
pixel_intensity = image[100, 100] 
print(pixel_intensity)

#Writing whole data fo pixel values to a csv file
# Open the CSV file for writing
with open('pixel_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(['R', 'G', 'B'])
    
    # Iterate through every pixel
    for row in image:
        for pixel in row:
            # Each pixel in OpenCV is in BGR format, so we need to reorder to RGB
            writer.writerow([pixel[2], pixel[1], pixel[0]])  # Convert BGR to RGB
