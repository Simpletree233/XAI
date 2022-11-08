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
)  # Instantiates the MobileNet architecture.


img_path = '1.JPG'
img = image.load_img(img_path, target_size=(224,224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

predictions = model.predict(x)
results = imagenet_utils.decode_predictions(predictions)
results