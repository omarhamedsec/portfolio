import sys
try:
    import pypdf
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf", "--quiet"])
    import pypdf

reader = pypdf.PdfReader(r"k:\om170\Documents\jarvis\portfolio\cv and resume\OMAR HAMED CV.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

with open(r"k:\om170\Documents\jarvis\portfolio\cv_text.txt", "w", encoding="utf-8") as f:
    f.write(text)
print("Done extracting PDF text")
