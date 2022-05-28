import os
import sys
import numpy as np
import tensorflow as tf
assert tf.__version__.startswith('2')

from tflite_model_maker import model_spec
from tflite_model_maker import image_classifier
from tflite_model_maker.config import ExportFormat
from tflite_model_maker.config import QuantizationConfig
from tflite_model_maker.image_classifier import DataLoader

import matplotlib.pyplot as plt

#Try to download and extract dataset
try:
    print("Downloading and extracting dataset...")
    image_path = tf.keras.utils.get_file(
        'master.tar.gz',
        'https://github.com/dmquilez/tohacks2022-dataset/archive/master.tar.gz',
        extract=True)
    image_path = os.path.join(os.path.dirname(image_path), 'tohacks2022-dataset-main/dataset')
except Exception as e:
    print("Error trying to download and extract dataset: "+e)
    sys.exit()

#Load data and split into trianing and validation/testing data
try:
    print("Loading data and split into trianing and validation/testing data...")
    data = DataLoader.from_folder(image_path)
    train_data, test_data = data.split(0.8)
except Exception as e:
    print("Error trying to split data into training and validation: "+e)
    sys.exit()


#TensorFlow model training
try:
    print("Training TensorFlow model...")
    model = image_classifier.create(train_data, epochs=50)
except Exception as e:
    print("Error trying to train the TensorFlow model: "+e)
    sys.exit()

#Evaluate model
try:
    print("Evaluating TensorFlow model...")
    loss, accuracy = model.evaluate(test_data)
except Exception as e:
    print("Error trying to evaluate the TensorFlow model: "+e)
    sys.exit()

#Export model
try:
    print("Exporting TensorFlow model...")
    config = QuantizationConfig.for_float16()
    export_dir = os.path.abspath('/export')
    model.export(export_dir, with_metadata=False, quantization_config=config)
except Exception as e:
    print("Error trying to export the TensorFlow model: "+e)
    sys.exit()