import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import RMSprop

# We are going to use Shakesphere poems to train the model!
filepath = tf.keras.utils.get_file('Shakesphere_reference.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt') #To get the file from the website

#*************************************Preparing the Data**********************************************
poem_text = open(filepath,'rb').read().decode(encoding='utf-8').lower()
poem_text = poem_text[100000:1000000]

characters = sorted(set(poem_text))

get_index = dict((c, i) for i, c in enumerate(characters)) #We create a dictionary with all possible characters and numbers corresponding to them 
get_char = dict((i, c) for i, c in enumerate(characters)) #For finding characters from numbers

SEQ_LENGTH = 40 #We use 40 characters to predict the next character
STEP_SIZE = 3   #To find next sequence

sentences = [] #Array where sentence is stored
next_char = [] #Array where next character is stored

for i in range(0, len(poem_text) - SEQ_LENGTH, STEP_SIZE): #Loop to get sentences and next characters
    sentences.append(poem_text[i: i + SEQ_LENGTH])
    next_char.append(poem_text[i + SEQ_LENGTH])


x = np.zeros((len(sentences), SEQ_LENGTH,
              len(characters)), dtype=np.bool_) #For training data 
y = np.zeros((len(sentences),
              len(characters)), dtype=np.bool_) #For test data

for i, st in enumerate(sentences): #For loop to set 1 in numpy array if character occurs in that position
    for t, char in enumerate(st):
        x[i, t, get_index[char]] = 1
    y[i, get_index[next_char[i]]] = 1

#***********************************Building the Recurrent Neural Network**********************************

model = Sequential()
model.add(LSTM(128,
               input_shape=(SEQ_LENGTH,
                            len(characters))))
model.add(Dense(len(characters), activation='softmax'))


model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(lr=0.01))

model.fit(x, y, batch_size=256, epochs=50)

def sample(preds, temperature=1.0): #Helper function to generate some reasonable text.
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

#***********************************Generating the text*****************************************************

def generate_text(length, temperature):
    start_index = random.randint(0, len(poem_text) - SEQ_LENGTH - 1)
    generated = ''
    sentence = poem_text[start_index: start_index + SEQ_LENGTH]
    generated += sentence
    for i in range(length):
        x_predictions = np.zeros((1, SEQ_LENGTH, len(characters)))
        for t, char in enumerate(sentence):
            x_predictions[0, t, get_index[char]] = 1

        predictions = model.predict(x_predictions, verbose=0)[0]
        next_index = sample(predictions, temperature)
        next_character = get_char[next_index]

        generated += next_character
        sentence = sentence[1:] + next_character
    return generated

#***********************************Output the result*******************************************************

print('---------0.2---------')
print(generate_text(300, 0.2))
print('---------0.4---------')
print(generate_text(300, 0.4))
print('---------0.5---------')
print(generate_text(300, 0.5))
print('---------0.6---------')
print(generate_text(300, 0.6))
print('---------0.7---------')
print(generate_text(300, 0.7))
print('---------0.8---------')
print(generate_text(300, 0.8))