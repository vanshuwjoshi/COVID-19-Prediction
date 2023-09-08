# COVID-19 Detection from Chest X-ray Images

## Overview

This repository contains the code and documentation for an in-class Kaggle competition focused on the detection of COVID-19 cases from chest X-ray images. In this challenge, participants were tasked with training machine learning models to accurately classify chest X-ray images as either positive or negative for COVID-19 using a supervised dataset. The goal was to develop an effective neural network model for image classification.

## Dataset

- **Training Data**: The training dataset consisted of 15,264 chest X-ray images (512x512) containing both positive and negative COVID-19 cases.
- **Test Data**: The test dataset included 400 chest X-ray images for model evaluation.
- **Labels**: The dataset provided labels for each image, indicating whether it was a positive or negative COVID-19 case.

## Code Overview

### Data Preprocessing and Organization

- `update_train.py`: This Python script was used to preprocess the training data. It organized the images into separate folders for positive and negative classes in the local environment.

### Model Development

- `covid_detection_model.py`: This Python script contains the code for building a neural network model using TensorFlow and Keras. The model architecture includes 3 convolutional blocks with max-pooling layers, followed by a fully connected layer with 128 units and a linear activation function. The model was compiled using the hinge loss function.

- `svm_model.py`: In addition to the neural network model, an SVM model was also developed for comparison. This model achieved a Kaggle private leaderboard score of 0.85.

## Evaluation

The evaluation of model performance was based on the Kaggle private leaderboard score, which reflects the model's ability to accurately classify COVID-19 cases in the test dataset.
