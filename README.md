# PDF Combiner Script

## Overview
This repository hosts a Python script for merging multiple PDF files within a specified folder into a single comprehensive PDF document. Designed for simplicity and efficiency, the script streamlines the process of combining PDF files into one.

## Features
- **Simple PDF Merging**: Automatically combines all PDF files in a designated folder into one large PDF file.
- **User-Friendly**: Designed to be straightforward for anyone with basic Python and file handling knowledge.


## Installation Guide
```markdown
### Prerequisites

Before you begin, make sure you have:
- Python (version 3.x or later)
- pip (Python package installer)

Python can be downloaded from [python.org](https://www.python.org/downloads/), and pip is included by default in Python 3.4 and later.
```
### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/zEleceed/Simple-Pdf-Combiner
```

Navigate to the script directory:

```bash
cd [path-to-script-directory]
```

### Step 2: Install Required Packages

The script requires `PyPDF2`. Install it using pip:

```bash
pip install PyPDF2
```

### Step 3: Run the Script

Execute the script with:

```bash
python pdf_merger.py
```

Replace `pdf_merger.py` with your script's actual name if different.

### Usage Instructions

1. Enter the directory path containing your PDF files when prompted.
2. The script displays a list of PDFs in the directory. Select files by entering their numbers, type 'all' to merge all, or '0' to finish.
3. Enter a name for your merged PDF file when prompted.

### Troubleshooting

- Ensure all PDFs are in the same directory with '.pdf' extensions.
- Verify Python and pip are correctly installed.
- Run the script with administrator rights or check file permissions if you encounter permission issues.
