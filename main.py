import io
import os
import fitz  # PyMuPDF for handling PDF files
from PIL import Image
import pytesseract  # OCR tool for extracting text from images
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold 

# Set the path to the Tesseract executable
# This is required for pytesseract to interface with the installed Tesseract OCR software
pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_CMD', r'Path\To\tesseract.exe')

# Configure the Google Generative AI API with your API key
# The API key should be set in the environment variable "GEMINI_API_KEY"
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
generation_config = {
  "temperature": 1,  # Controls randomness. Higher values mean more random outputs.
  "top_p": 0.95,  # Nucleus sampling. Higher values allow more diversity.
  "top_k": 64,  # Controls diversity. Lower values mean less randomness.
  "max_output_tokens": 8192,  # Maximum length of the generated content.
  "response_mime_type": "text/plain",  # The format of the generated content.
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",  # The model to use for content generation.
  generation_config=generation_config,
  safety_settings={
    # Configure the model to not block any content related to these categories.
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
  }
)

def preprocessImageForOCR(img):
    # Placeholder for image preprocessing steps before OCR
    # You can implement contrast adjustment, resizing, etc., here.
    return img

def extractTextFromPDF(pdfPath):
    """Extracts text from a PDF file using OCR."""
    text = ""
    doc = fitz.open(pdfPath)  # Open the PDF file
    for page in range(doc.page_count):  # Iterate through each page
        pageDoc = doc.load_page(page)  # Load the current page
        pix = pageDoc.get_pixmap()  # Render page to an image
        imgBytes = pix.tobytes("png")  # Convert the image to PNG bytes
        img = Image.open(io.BytesIO(imgBytes))  # Open the image with PIL

        imgPreprocessed = preprocessImageForOCR(img)  # Preprocess the image for better OCR results
        pageText = pytesseract.image_to_string(imgPreprocessed, lang="en")  # Extract text using OCR // chage lang="por" for portuguese
        text += pageText  # Append the extracted text to the total text
    return text

def generateContentWithAI(text):
    """Generates content using the Google Generative AI API based on the provided text."""
    prompt = "\nIsolate only the debtor's name and CPF, separated by a semicolon from the following text - DO NOT WRITE ANYTHING BEYOND THE MODEL: \"NAME ; CPF\".\n"
    response = model.generate_content([
      f"input: {prompt + text}",  # Input text with the prompt
      "output: ",  # Placeholder for the output
    ])
    return response.text

# Usage example
pdfPath = 'Path\to\doc.pdf'  # Path to the PDF file
extractedText = extractTextFromPDF(pdfPath)  # Extract text from the PDF
result = generateContentWithAI(extractedText)  # Generate content based on the extracted text
print(result)  # Print the generated content