import random
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import LSTM, Dense, Actvation
from keras.optimizers import RMSprop

filepath = tf.keras.utils.get_file('Shakesphere_reference.txt', 'https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqazZYcGpPaXVDVzBBM3V5WE82ZGplcFdoVllDUXxBQ3Jtc0tuZUNuVk9iZ0t1b2NlZFJ2b183RlhvSVAxblIxN3lMWTFMQklmaV9PMVc2M1VkcThESWYwdGVJTmpLbkdIWTV1VUdLZUVkRzhVUjk2TjF0UzZvSGZYMnYycUhNVnJjSXZ6Y2pfM1RuTEQ5aUZzaTNlYw&q=https%3A%2F%2Fstorage.googleapis.com%2Fdownload.tensorflow.org%2Fdata%2Fshakespeare.txt&v=QM5XDc4NQJo')
poem_text = open(filepath,'rb').read().decode(encoding='utf-8').lower()
