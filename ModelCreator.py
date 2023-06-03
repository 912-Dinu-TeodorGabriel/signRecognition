import numpy
import DataParser
import tensorflow as tf
from functools import partial
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import BatchNormalization
from keras.layers import Activation
from keras.layers import LeakyReLU

# fix random seed for reproducibility
def modelCreate():
    seed = 7
    numpy.random.seed(seed)

    # load data
    (X_train,y_train) = DataParser.data_set

    # normalize inputs from 0-255 to 0.0-1.0
    X_train = X_train * 1./255

    # one hot encode outputs
    y_train = np_utils.to_categorical(y_train)

    class_num = y_train.shape[1]

    # Create the model
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape=(25,25,3), padding='same'))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))


    model.add(Conv2D(64, (3,3), activation='relu', padding='same'))
    model.add(MaxPooling2D((2,2)))
    model.add(Dropout(0.2))


    model.add(Conv2D(128, (3,3),activation='relu', padding='same'))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dropout(0.2))

    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.3))

    model.add(Dense(class_num, activation='softmax'))

    # Compile model

    opt = tf.keras.optimizers.Adam(learning_rate=0.003)

    model.compile(loss='categorical_crossentropy',
                optimizer=opt,
                metrics=['accuracy'])

    print(model.summary())


    model.fit(X_train, y_train, shuffle = True, epochs=15, batch_size=32)

    model.save('model')
