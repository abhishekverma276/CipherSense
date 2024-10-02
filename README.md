## Overview

**CipherSense** is an intelligent cipher type detection tool currently under development. It aims to identify and classify different types of ciphers (DIGRAFID and FOURSQUARE) using machine learning techniques. This project will assist researchers and security professionals in understanding and analyzing encrypted data.

## Project Structure

```plaintext
cipher_sense/
│
├── data/
│   ├── plaintexts.txt        # Input plaintext data (for generating ciphertext)
│   ├── digrafid_ciphertexts.csv  # Ciphertexts generated using DIGRAFID
│   └── foursquare_ciphertexts.csv # Ciphertexts generated using FOURSQUARE
│
├── src/
│   ├── algorithms/
│   │   ├── digrafid.py        # DIGRAFID cipher implementation
│   │   └── foursquare.py      # FOURSQUARE cipher implementation
│   │
│   ├── ml_models/
│   │   ├── naive_bayes.py     # Naive Bayes model training
│   │   ├── transformer_model.py # Transformer-based model training
│   │   ├── neural_network.py    # Neural Network model training
│   │   └── lstm_model.py        # LSTM model training
│   │
│   ├── gui/
│   │   └── cipher_gui.py        # Simple GUI for input and prediction
│   │
│   └── data_preprocessing.py     # Code for dataset preparation and preprocessing
│
├── results/
│   ├── model_performance.csv     # Results and performance metrics of each model
│   └── comparative_analysis.png    # Visual comparative analysis of model performance
│
├── README.md                     # Project overview and instructions
├── requirements.txt              # List of Python dependencies
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip

### Clone the Repository

```bash
git clone https://github.com/yourusername/CipherSense.git
cd CipherSense
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

To run the GUI:

```bash
python src/gui/cipher_gui.py
```

## Contributing

CipherSense is under active development, and contributions are welcome! To get started:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your branch.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions, suggestions, or feedback, please reach out:

- **Email**: abhishek27.sv@gmail.com
---
