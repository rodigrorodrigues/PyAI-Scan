# PDF Text Extractor and Content Generator

This repository contains a Python application designed to extract text from PDF files using Optical Character Recognition (OCR) and then generate content based on the extracted text using Google's Generative AI API.

## Features

- **Text Extraction from PDF**: Utilizes PyMuPDF and pytesseract to extract text from any given PDF file.
- **Image Preprocessing**: Implements image preprocessing techniques to improve OCR results.
- **Content Generation**: Leverages Google's Generative AI API to generate content based on the extracted text.
- **Customizable AI Settings**: Allows configuration of AI generation settings such as temperature, top_p, top_k, and more.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your system.
- Tesseract OCR installed and accessible in your system's PATH or specified directly in the script.
- A valid API key for Google's Generative AI API.

## Installation

To install the necessary Python packages, run the following command:

```bash
pip install -r requirements.txt

```


## Configuration
Tesseract OCR: Set the path to the Tesseract executable in the environment variable TESSERACT_CMD or directly in the script.
Google Generative AI API Key: Set your API key in the environment variable GEMINI_API_KEY.
Usage
To use the application, follow these steps:

Update the pdfPath variable in main.py to point to your target PDF file.
Run the script:

```bash
python main.py
```

The script will extract text from the PDF, preprocess the images for better OCR results, and then generate content based on the extracted text using the configured AI model.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

