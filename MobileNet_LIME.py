# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 11:47:06 2022

@author: simpletree
"""

import numpy as np
#import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import preprocess_input
from tensorflow.keras.applications import MobileNetV3Large
from tensorflow.keras.applications import imagenet_utils

from skimage.io import imread
import matplotlib.pyplot as plt

import os,sys
import lime   # LOL first try : pip install lime
from lime import lime_image


# Instantiates the MobileNet architecture.

model = MobileNetV3Large(
    input_shape= (224,224,3),
    #alpha=1.0,
    minimalistic=False,
    #include_top=True,
    weights="imagenet",
    #input_tensor=None,
    classes=1000,
    #pooling=None,
    dropout_rate=0.2,
    classifier_activation="softmax",
    include_preprocessing=True,
)  
#model.save('MobileNet.h5')

## Load a test image and predict it with pre-trained MobileNetV3Large
img_path = '1.JPG'  
img = image.load_img(img_path, target_size=(224,224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

## See the prediction
predictions = model.predict(x)
results = imagenet_utils.decode_predictions(predictions)

# initialize LIME explainer
explainer = lime_image.LimeImageExplainer()

## time
# Hide color is the color for a superpixel turned OFF. Alternatively, if it is NONE, the superpixel will be replaced by the average of its pixels
img_explained = image.img_to_array(img)

explanation = explainer.explain_instance(
    img_explained.astype('double'), 
    model.predict, 
    top_labels=5, 
    hide_color=0, 
    num_samples=1000)


## Show the explaination

from skimage.segmentation import mark_boundaries

temp, mask = explanation.get_image_and_mask(explanation.top_labels[0], positive_only=True, num_features=5, hide_rest=False)

#temp = temp.astype('int')
#zz = mark_boundaries(temp, mask)

plt.imshow(mark_boundaries(img, mask,))


'''
# For image overlay, but not necessary
import cv2 as cv

c = cv.addWeighted(temp, 0.5, mask, 0.5, 0)

cv.imshow("addWeighted", c)

cv.waitKey(0)


'''









