import pandas as pd
import cv2
import pytesseract
import re
# SET TESSERACT PATH
pytesseract.pytesseract.tesseract_cmd = \
r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# OCR TEXT EXTRACTION FUNCTION
def extract_text(path):
    img = cv2.imread(path)

    if img is None:
        print(f"Image not found: {path}")
        return ""

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)

    return text.lower()

# Scoring function
def calculate_score(resume_path):
    text = extract_text(resume_path)
    score = 0
# Skill detection
    if "python" in text:
        score += 10

    if "machine learning" in text or "ml" in text:
        score += 15

    if "sql" in text:
        score += 5

    if "artificial intelligence" in text:
        score += 10
# Internship / experience indicator
    if "intern" in text:
        score += 10
# Certification / course
    if "certification" in text or "course" in text:
        score += 5
# Experience years detection
    exp = re.findall(r'\d+\s+year|\d+\s+month', text)
    if exp:
        score += 10

    return score
# Shortlisting function
def shortlist(score):
    if score >= 40:
        return "Selected"
    elif score >= 20:
        return "Hold"
    else:
        return "Rejected"
# Main execution

data = pd.read_csv("data/applications.csv")

data["score"] = data["resume_path"].apply(calculate_score)
data["status"] = data["score"].apply(shortlist)

data.to_csv("output/final_results.csv", index=False)

print("\nFinal Results:\n")
print(data)
