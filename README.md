# Handwritten Digit Recognition

## About the Project

Handwritten Digit Recognition is a Python-based machine learning project that identifies handwritten digits from 0 to 9 using the MNIST dataset.

The project uses a Convolutional Neural Network (CNN) built with TensorFlow and Keras to learn patterns in handwritten digit images and classify them into the correct numerical categories.

## Features

- Uses the MNIST handwritten digit dataset.
- Preprocesses image data by normalizing pixel values.
- Builds a CNN model for digit classification.
- Trains the model using training data.
- Evaluates the model on a separate test dataset.
- Reports the test dataset accuracy.

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- MNIST dataset
- Convolutional Neural Network (CNN)

## Model Architecture

The model contains the following layers:

1. Input layer for 28 × 28 grayscale images.
2. Convolutional layer with 32 filters and ReLU activation.
3. Max pooling layer.
4. Convolutional layer with 64 filters and ReLU activation.
5. Max pooling layer.
6. Flatten layer.
7. Dense layer with 64 neurons and ReLU activation.
8. Output layer with 10 neurons and Softmax activation.

## How It Works

1. Load the MNIST dataset.
2. Normalize the image pixel values.
3. Prepare the image dimensions for the CNN.
4. Build and compile the neural network.
5. Train the model using the training dataset.
6. Evaluate the trained model on the test dataset.
7. Display the test accuracy.

## Prerequisites

- Python 3
- TensorFlow
- NumPy

## Installation

Install the required libraries using pip:

```bash
pip install tensorflow numpy
```

## How to Run

Run the Python script from your terminal:

```bash
python "Handwritten digit recognition.py"
```

The program prints the model summary, training progress, and test dataset accuracy.

## Future Improvements

- Add a confusion matrix to evaluate classification performance.
- Display sample handwritten digits with their predicted labels.
- Allow users to upload their own handwritten digit images.
- Build a simple graphical user interface for predictions.

## Contribution

Contributions that improve the documentation, code quality, testing, or functionality of the project are welcome.

## License

No license has been specified yet. Please check with the repository owner before choosing or adding one.