from tensorflow.keras.applications import Xception
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_dir = "data/train/"
val_dir = "data/val/"

img_size = (299, 299)
batch_size = 32

datagen = ImageDataGenerator(rescale=1./255, horizontal_flip=True, rotation_range=10)
train_gen = datagen.flow_from_directory(train_dir, target_size=img_size, batch_size=batch_size, class_mode="binary")
val_gen = datagen.flow_from_directory(val_dir, target_size=img_size, batch_size=batch_size, class_mode="binary")

base_model = Xception(weights='imagenet', include_top=False, input_shape=(299, 299, 3))
x = GlobalAveragePooling2D()(base_model.output)
predictions = Dense(1, activation='sigmoid')(x)
model = Model(inputs=base_model.input, outputs=predictions)

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(train_gen, validation_data=val_gen, epochs=20)
model.save("xception_deepfake.h5")
