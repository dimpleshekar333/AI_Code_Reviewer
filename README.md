
# AI Code Reviewer

A **Streamlit-based AI Code Reviewer** that analyzes Python code files for style issues, formatting, and complexity.  
It integrates popular Python tools like **Flake8**, **Black**, and **Radon** to provide automated code review suggestions.

---

## 🚀 Features

- **Flake8 Style Check**: Detect PEP8 violations and other style issues.  
- **Black Auto-Format Suggestions**: Generate formatting differences for cleaner code.  
- **Radon Code Complexity Analysis**: Measure cyclomatic complexity and provide a readability score.  
- **Upload Python Files**: Drag and drop `.py` files for analysis.  
- **Interactive Streamlit Dashboard**: Simple and intuitive UI for quick code review.

---

## 🛠️ Tools & Libraries

- [Streamlit](https://streamlit.io/) – Web application framework for Python  
- [Flake8](https://flake8.pycqa.org/) – Python style guide enforcement  
- [Black](https://black.readthedocs.io/) – Code autoformatter  
- [Radon](https://radon.readthedocs.io/) – Code complexity analysis

---

## ⚡ Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd AI-Code-Reviewer
Create and activate a virtual environment (optional but recommended):
Copy code
Bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies:
Copy code
Bash
pip install streamlit flake8 black radon
▶️ How to Run
Run the Streamlit app:
Copy code
Bash
python -m streamlit run app.py
Open the browser window that appears.
Upload your .py file or drag & drop it into the UI.
See Flake8 issues, Black diff, and Radon complexity instantly.
📝 Usage Example
Upload a Python file test_sample.py and the dashboard will show:
Flake8 Style Issues
Copy code

E231 missing whitespace after ','
E703 statement ends with a semicolon
Black Auto-Format Suggestions
Copy code
Diff
- def add(a,b):
+ def add(a, b):
Radon Code Complexity
Copy code

A (1.0)
🔧 Folder Structure
Copy code

AI-Code-Reviewer/
│
├─ app.py                # Main Streamlit app
├─ analyzer/
│  ├─ style_checker.py   # Flake8 & Black functions
│  └─ complexity_checker.py # Radon functions
├─ requirements.txt      # Dependencies
└─ README.md             # Project documentation
✅ Notes
Ensure all dependencies (flake8, black, radon) are installed.
Use python -m <module> to avoid Windows PATH issues.
Works on Windows, macOS, and Linux.
📌 Future Improvements
Add GitHub integration to analyze repositories.
Include AI suggestions for code improvement.
Generate downloadable reports for code reviews.
📚 References
PEP8 Python Style Guide
Streamlit Documentation
Radon Python Complexity
