# Fake News Detection using Machine Learning

This repository contains code for a machine learning project focused on the detection of fake news articles. The project utilizes a dataset consisting of fake and genuine news articles to train a machine learning model that can classify news articles as either fake or genuine.

## Dataset

The dataset used in this project includes two CSV files: "Fake.csv" and "True.csv". The "Fake.csv" file contains fabricated news articles, while the "True.csv" file contains genuine news articles. These files serve as the input data for training and evaluating the machine learning model.

## Code Structure

The code in this repository is organized as follows:

- `main.py`: This script serves as the main entry point for the project. It orchestrates the workflow, including data loading, preprocessing, model training, and evaluation.
- `preprocess.py`: This module contains functions for preprocessing the text data. It includes operations such as converting text to lowercase, removing URLs and special characters, and performing other text cleaning tasks.
- `model.py`: This module defines and trains the machine learning model. It utilizes the scikit-learn library and implements the PassiveAggressiveClassifier algorithm.
- `evaluation.py`: This module evaluates the performance of the trained model using metrics such as accuracy and confusion matrix.
- `utils.py`: This module provides utility functions used throughout the project, such as loading the dataset and visualizing the results.
- `README.md`: This file provides an overview of the project, its structure, and instructions for running the code.

## Usage

To run the project, follow these steps:

1. Make sure you have the required dependencies installed. You can install them by running `pip install -r requirements.txt`.
2. Place the dataset files ("Fake.csv" and "True.csv") in the same directory as the code files.
3. Run the `main.py` script: `python main.py`

The script will load the dataset, preprocess the text data, train the model, and evaluate its performance. The accuracy score and confusion matrix will be displayed as output.

## Results

The machine learning model achieves a high accuracy score, indicating its ability to differentiate between genuine and fake news articles. The confusion matrix provides detailed insights into the model's predictions, enabling further analysis of false positives and false negatives.

## Future Enhancements

There are several potential areas for future enhancements:

- Exploring more advanced natural language processing (NLP) techniques, such as word embeddings or transformer models, to improve the model's understanding of the text.
- Incorporating additional features, such as article metadata or social media data, to enhance the model's predictive power.
- Developing a user interface or web application to provide an interactive way to classify news articles in real-time.
- Continuously monitoring and retraining the model to adapt to evolving fake news patterns and improve its generalization capabilities.

Contributions to this project are welcome. If you have any ideas, improvements, or bug fixes, please feel free to submit a pull request.

