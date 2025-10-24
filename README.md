# Scaffolding Assignment 3 - Gutenberg text cleaner

Course: Introduction to AI - Fall 2025
Student: raghulch
University at Buffalo

## Overview


This assignment will produce a Flask web app that will be able to download, clean, analyze, and summarize text from Project Gutenberg .txt books.
It was created and tested using GitHub Codespaces, from the scaffolding repository you have been given (scaffolding3_startup).

Here is the full app:

Processes a Project Gutenberg URL.
Cleanses and normalizes the text.
Calculates significant statistics (characters, words, sentences, etc.).
Generates a brief (3 sentence) summary.
Displays first 500 characters of processed text.
Provides a simple web interface.

## Tasks
### Part 1: Files ran in GitHub Codespaces 

Fork 
Opened this repo in GitHub Codespaces.

Verified Flask and dependencies.

Confirmed starter_preprocess.py structure and imports are as expected.

![Test Setup](docs/screenshots/setup_ok.png)
![Test Setup](docs/screenshots/setup_ok1.png)

### Part 2: Implementation of Text Preprocessing

All functions yet to be implemented in the file starter_preprocess.py have now been completed:

fetch_from_url() → Downloads plain text from Project Gutenberg.

clean_gutenberg_text() → Eliminates headers, licenses, and other meta information.

normalize_text() → Normalizes to lowercase, standardizes punctuation, while preserving the terminating sentence.

get_text_statistics() → Produces total chars, words, sentences, average, as well as most frequently used words.

create_summary() → Uses NLTK to tokenize sentences, and creates a 3-sentence paragraph that is a brief summary.

I pre-processed some of the books (Pride and Prejudice, Frankenstein) with Python REPL.

### Part 3: Flask API and integration.

I finished the app.py Flask backend with the following routes:

/ - serves index.html UI.

 /api/clean - accepts URL and does complete cleaning + analyis + summary.

 /api/analyze - accepts raw text and returns only statistics.

 /health - Simple test endpoint that returns {ok: True}

/health - Simple test endpoint that returns {ok: True}

Integrated the TextPreprocessor from the file starter_preprocess.py as the API

Included some reasonable checking and handling to check for missing and malformed URLs.
Enhanced the regular expression clean tables and simultaneously trimmed the extra Chapter lines. 
The API was tested locally in Codespaces (http://127.0.0.0.1:5000).


### Part 4: Web UI


Constructed /templates/index.html as the browser-facing webpage.

New Functionalities: 

- Searchable and visually appealing input form for the Gutenberg urls 
- AJAX POST to /api/clean as invoked by the "Clean & Analyze" button 
- Spinner added to body of page while cleaning is in process 
- Results area displays statistics, summary and first 500 characters cleaned 
- Validation and handling of url and network errors on invalid url 
- Responsive and light styling through bootstrap5 
- The above mentioned ui features and functionalities have been tested and confirmed on one of the urls noted below: 
[Pride and Prejudice] 
[Frankenstein] 
[Alice in Wonderland] 
[Moby Dick]

![Working application 1](docs/screenshots/working_application_1.png)
![Working Application 1](docs/screenshots/working_application_2.png)
![Working Application 1](docs/screenshots/working_application_3.png)
![Working Application 1](docs/screenshots/working_application_4.png)

I validated that cleaning took place starting from the first line of the actual story and did NOT include the title/license.

## Set up and run 
Clone and open in Codespaces 
git clone https://github.com/raghuldav/scaffolding3_startup.git
cd scaffolding3_startup 

Install dependencies 
python --version 
pip install -r requirements.txt 

Run the app 
python app.py 
make the URL public or go to ports and click the link
Open in your browser 
Go to → http://127.0.0.1:5000 

## URLs to test 

Pride and Prejudice, 
Frankenstein, 
Alice in Wonderland, 
Moby Dick

## Key Learnings 

Web scraping & cleaning natural language data 
Content normalization through regex 
Flask API design & routing 
Using asynchronous JS fetch and handling JSON 
Building simple AI preprocessing pipelines 
The deployment and testing workflow in GitHub Codespaces 

## Project Structure 

```text
scaffolding3_startup/
├── app.py                    # Backend Flask app 
├── starter_preprocess.py     # Preprocessing, cleaning and analysis 
├── templates/                
│   └── index.html            # Frontend UI                         
├── docs/                     
│   ├── screenshots/          # Screenshots of app 
├── README.md                 # Documentation on the project 
└── requirements.txt          # Requirements (Flask, requests, bs4, nltk) 
