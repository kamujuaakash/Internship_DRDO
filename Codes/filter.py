# # Importing Image and ImageFilter module from PIL package  
# from PIL import Image, ImageFilter 
     
# # creating a image object 
# im1 = Image.open(r"sar-1.jpg") 
# im1.show()

# Importing Image and ImageFilter module from PIL package  
from PIL import Image, ImageFilter 
     
# creating a image object 
im1 = Image.open(r"sar-1.jpg") 
     
# applying the median filter 
im2 = im1.filter(ImageFilter.MedianFilter(size = 3)) 

# applying the mode filter 
im3 = im1.filter(ImageFilter.ModeFilter(size = 3)) 

im4 = im1.filter(ImageFilter.Filter(size = 3)) 

     
im1.show() 
im2.show()
im3.show()
import scipy

from scipy.ndimage.filters import uniform_filter
from scipy.ndimage.measurements import variance

def lee_filter(img, size):
    img_mean = uniform_filter(img, (size, size))
    img_sqr_mean = uniform_filter(img**2, (size, size))
    img_variance = img_sqr_mean - img_mean**2

    overall_variance = variance(img)

    img_weights = img_variance / (img_variance + overall_variance)
    img_output = img_mean + img_weights * (img - img_mean)
    return img_output