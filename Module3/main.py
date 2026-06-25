with open("Module3/data.txt", "r") as file:
    content = file.read()
    
# read whole file
with open("Module3/data.txt", "r") as file:
    for line in file:
        print(line.strip())
        
# Read the file with \n
with open("Module3/data.txt", "r") as file:
    lines = file.readlines()

print(lines)    

# Write Something in the file
with open("Module3/data.txt", "w") as file:
    file.write("Hello Python BY Vivek")

# Append something in the file
with open("Module3/data.txt", "a") as file:
    file.write("\nNew Line")

# error handling
try:
    with open("Module3/missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
    
# Path Handling
# path = "C:\\Users\\Vivek\\Documents\\file.txt"

# PrintFilePath
from pathlib import Path
file_path = Path("Module3/data.txt")
print(file_path)

# Check the existence of the file
from pathlib import Path
path = Path("Module3/data.txt")
print(path.exists())

# Getcurrent working directory
from pathlib import Path

print(Path.cwd())

# Create directory if file not exists
from pathlib import Path
Path("logs").mkdir(exist_ok=True)

# Append Path to the file
from pathlib import Path
log_file = Path("logs") / "app.log"
print(log_file)

# Lesson2: JSON

import json

user = {
    "id": 1,
    "name": "Vivek"
}

json_string = json.dumps(user)

print(json_string)

# JSON TO DICTONARY
import json

json_string = '{"id":1,"name":"Vivek1"}'
user = json.loads(json_string)
print(user)

# Access JSON Data
user = json.loads(
    '{"id":1,"name":"Vivek"}'
)

print(user["name"])


# Read Nested JSON
response = {
    "success": True,
    "data": {
        "id": 1,
        "name": "Vivek",
        "skills": [
            "Python",
            "FastAPI"
        ]
    }
}

print(response["data"]["name"])

print(
    response["data"]["skills"][0]
)

# Write JSON to a file - IT WILL Create a new file if not exists
import json

user = {
    "id": 1,
    "name": "Vivek"
}

with open("user.json", "w") as file:
    json.dump(user, file)
    
# Read newly created file
import json

print("Reading JSON file:")
with open("user.json", "r") as file:
    user = json.load(file)

print(user["name"])

# | Method  | Purpose                       |
# | ------- | ----------------------------- |
# | dump()  | Write JSON to file            |
# | dumps() | Convert object to JSON string |
# | load()  | Read JSON from file           |
# | loads() | Convert JSON string to object |

# | Function | Input | Output |
# | -------- | ----- | ------ |
# | dumps()  | dict  | str    |
# | loads()  | str   | dict   |
# | dump()   | dict  | file   |
# | load()   | file  | dict   |

# learning CSV
import csv

with open("Module3/employee.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
        
print("Reading CSV file without header:")
# How to skip with the header row in CSV file:
import csv

with open("Module3/employee.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print(row)
        
print("Reading CSV file without header dictonary reading:")
# Dictonary reader in CSV file:
import csv

with open("Module3/employee.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
        
print("Reading CSV file without header dictonary reading:")
# Access column
import csv

with open("Module3/employee.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])
        
# Write CSV file
import csv

rows = [
    ["id", "name"],
    [1, "Vivek"],
    [2, "John"]
]

with open("Module3/users.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerows(rows)
    
# write CSV from dictonary
print("Write CSV from dictonary")
import csv

users = [
    {"id": 1, "name": "Vivek"},
    {"id": 2, "name": "John"},
    {"id": 3, "name": "Alice"}
]

with open("users.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["id", "name"]
    )

    writer.writeheader()
    writer.writerows(users)
    
# Reading Same CSV File
import csv

with open("users.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
        
# PDF FILES
# | Library          | Purpose                         |
# | ---------------- | ------------------------------- |
# | `pypdf`          | Read, merge, split PDFs         |
# | `pdfplumber`     | Extract text and tables         |
# | `PyMuPDF (fitz)` | High-performance PDF processing |
# | `reportlab`      | Create PDFs from scratch        |

# reading first page
# pip install pypdf
from pathlib import Path

from pypdf import PdfReader
from pypdf.errors import PdfStreamError

pdf_path = Path(__file__).with_name("Sample PDF.pdf")

try:
    if pdf_path.read_bytes()[:5] != b"%PDF-":
        raise ValueError(
            f"{pdf_path} is not a valid PDF file. "
            "Replace it with a real PDF, not a plain text file renamed to .pdf."
        )

    reader = PdfReader(pdf_path) 
    page = reader.pages[0]
    text = page.extract_text()

    print(text)
except FileNotFoundError:
    print(f"PDF file not found: {pdf_path}")
except (PdfStreamError, ValueError, IndexError) as error:
    print(f"Could not read PDF: {error}")

# reading all pages
from pypdf import PdfReader
print('------NEW------')
reader = PdfReader("Module3/Sample PDF.pdf")

for page in reader.pages:
    print(page.extract_text())
    
# Get Pdf file pages
from pypdf import PdfReader

reader = PdfReader("Module3/Sample PDF.pdf")

print(f"Total Pages: {len(reader.pages)}")

# create own pdf
from reportlab.pdfgen import canvas

pdf = canvas.Canvas("hello.pdf")

pdf.drawString(100, 750, "Hello Vivek")

pdf.save()