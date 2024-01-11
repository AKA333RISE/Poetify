import random
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import LSTM, Dense, Actvation
from keras.optimizers import RMSprop

filepath = tf.keras.utils.get_file('Shakesphere_reference.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
poem_text = open(filepath,'rb').read().decode(encoding='utf-8').lower()
