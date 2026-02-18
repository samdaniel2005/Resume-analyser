2A - Python Problem Statement: 
An organization receives internship applications from multiple colleges every day. Each 
application includes personal details, skills, preferred roles, and availability. Currently, 
applications are stored but not analysed, leading to delays in shortlisting and communication. 
The organization wants a system that can organize applications, identify incomplete or 
duplicate entries, and provide a basic shortlist to help the hiring team move faster. 


# Resume-analyser
AI Resume Analyser using OCR

project overview
This project is an AI-powered Resume Analyzer that automatically extracts text from resumes using Optical Character Recognition (OCR) and evaluates candidates based on skills, experience, and relevant keywords.
It helps automate the internship hiring shortlisting process.

Features
Resume text extraction using OCR (OpenCV + Tesseract)
Automatic skill detection (Python, ML, AI, SQL, etc.)
Experience keyword detection
Score calculation for candidates
Automatic shortlisting:
Selected
Hold
Rejected
Supports multiple resumes through CSV dataset.


Technologies Used
Python
OpenCV
Pytesseract OCR
Pandas
Regular Expressions (Regex)


How to Run
1.Install dependencies:
pip install opencv-python pytesseract pandas pillow
2.Run the project:
python main.py
3.Output will be saved in:
output/final_results.csv
