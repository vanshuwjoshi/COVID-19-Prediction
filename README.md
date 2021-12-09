# Data-Challenge-2
In-Class kaggle competition 

In this data challenge we were given a supervised dataset of chest X-ray images, and were asked to train a model to detect the COVID-19 cases using neural network that gets the images from the input and predicts the labels of the images in the output. The dataset consisted 15264 (512x512) chest X-ray images for the train set and 400 images for the test set. The dataset contains positive and negative classes to indicate the positive and negative COVID-19 cases.

In the file update_train.py I seperated the images into different folders for the two different classes in my local enviornment. 

Then I rescaled the images to the size of 32x32 and then created a Neural net with 3 convolutional blocks using tf.keras.layers.Conv2D and max pooling layer with each one of them.

Another model was trained using SVM, in which the fully-connected layer with 128 units is created with activation by a linear activation function. In the end the model was compiled with hinge loss function. This model score 0.85 on kaggle private leaderboard. 
