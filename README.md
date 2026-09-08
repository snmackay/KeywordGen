# KeywordGen

A keyword generator for academic papers. It creates text files containing both the provided keywords and the most frequently used words within the paper.

These steps are guaranteed to work on Linux with a 64-bit install of Python 3.7.4.

## Step 1: Install prerequisites

Ensure you have Python 3 installed, as well as the `pip` package manager.

## Step 2: Run the Python interpreter

From your terminal, type:

```bash
python
```

## Step 3: Download NLTK data

Inside the Python interpreter, type:

```python
import nltk
nltk.download()
```

When a window pops up, select **all** from the options, then click **download**.

## Step 4: Install dependencies

Run the following commands, in order:

```bash
pip install PyPDF2

sudo apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig

sudo apt-get install -y python python-dev python-pip build-essential swig git libpulse-dev

sudo apt-get install libasound2-dev

pip install pocketsphinx

pip install textract

pip install six --upgrade

pip install pdfminer.six

python3 pdfSanity.py 'directory you have the pdfs in'
```

## Step 5: Enjoy!
