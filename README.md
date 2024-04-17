# Download MetaData For Research Papers

This project allows you to download metadata for research papers using their DOI (Digital Object Identifier). The DOI information is sourced from a CSV file named `DOI.csv`.

## Getting Started

To set up and run this project, follow these steps:

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your/repository.git
cd repository
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies. If you don't have virtualenv installed, you can install it using pip:
```
pip install virtualenv
```
```
virtualenv venv
```
Activate the virtual environment:
```
source venv/bin/activate

```

### 3. Install Required Packages

Install the required Python packages specified in requirements.txt
```
pip install -r requirements.txt
```

### 4. Run the Script
Now you're ready to run the Python script that downloads metadata for the research papers based on the DOI information provided in DOI.csv
```
python download_metadata.py
```

This script will process the DOI.csv file and download the metadata for each paper referenced by the DOIs.


 
You can adjust the commands, file names, and paths based on your specific project structure and requirements. This README.md provides a clear guide for users to set up and run your research paper metadata downloader project.
