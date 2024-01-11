# Poetify



## Overview
Poetify is an AI-powered tool that generates poetry in the style of Shakespeare. It utilizes a Recurrent Neural Network (RNN) with Long Short-Term Memory (LSTM) to model and generate text. The AI has been trained on a large dataset of Shakespeare's poems, allowing it to capture the essence and style of his writing.

## Features
- **Shakespearean Style Text Generation:** Generates text that mimics the style of Shakespeare's poetry.
- **Customizable Output:** Users can specify the length of the generated poems and the creativity (temperature) of the text generation.
- **Deep Learning Model:** Utilizes LSTM, a type of RNN, suitable for modeling sequences and text.

## Requirements
To run Poetify, you need the following:
- Python (developed and tested on version 3.10.13)
- TensorFlow (version 2.15.0)
- NumPy (version 1.26.2)

## Installation
1. Clone this repository to your local machine.
2. Ensure you have the required versions of Python, TensorFlow, and NumPy installed.
3. Navigate to the directory containing the Poetify code.

## Usage
To generate poems:
1. Run `main.py` in your Python environment.
2. The script will automatically download the training data (Shakespeare's poems) and train the model.
3. After training, the model will generate poems with varying levels of creativity, as shown by the different temperature settings in the output.

## How It Works
- **Data Preparation:** The script preprocesses Shakespeare's poems to create training data for the neural network.
- **Model Architecture:** The model is built using the Sequential model in Keras, incorporating LSTM layers for sequence modeling and Dense layers for output generation.
- **Training:** The model is trained on the prepared dataset to learn patterns in Shakespeare's writing style.
- **Text Generation:** Generates new text based on the learned patterns, with a helper function to introduce randomness (temperature) in the text generation process.

## Customizing Text Generation
- You can customize the length of the generated text and the temperature parameter in the `generate_text` function.
- The temperature parameter controls the randomness of text generation. A lower temperature results in more predictable text, while a higher temperature makes it more random and creative.

## Contributing
Contributions to Poetify are welcome! If you have suggestions or improvements, feel free to fork this repository and submit a pull request.

## License
This project is open-sourced under the MIT License.

## Acknowledgments
- Thanks to the TensorFlow team for providing an excellent platform for deep learning.
- Inspired by the works of William Shakespeare.
