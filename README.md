# DNA Automation - Streamlit Application

## Description
This application automates web scraping and data processing tasks using Selenium and provides a user-friendly Streamlit interface.

## Features
- **Authentication System**: Login with hardcoded credentials
- **File Upload**: Upload TSV files for processing
- **Web Automation**: Automated data extraction using Selenium
- **Excel Generation**: Creates master Excel files with processed data

## Credentials
- **Username**: Yash
- **Password**: Yash@2003

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure you have the Edge WebDriver installed and the path configured correctly in the code.

## Running the Application

To start the Streamlit application, run:
```bash
streamlit run Project.py
```

The application will open in your default web browser at `http://localhost:8501`

## Usage

1. **Login**: Enter your username and password (Yash/Yash@2003)
2. **Upload TSV File**: Click on the file uploader and select your TSV file
3. **Run Automation**: Click the "Run Automation" button to start processing
4. **Wait**: The automation process will take several minutes to complete
5. **Success**: Once complete, a master Excel file will be created and opened automatically

## Requirements
- Python 3.7+
- Microsoft Edge Browser
- Edge WebDriver (msedgedriver.exe)
- Internet connection for web automation

## Notes
- The application uses headless browser mode for automation
- Downloaded files are saved to the configured download directory
- Temporary files are automatically cleaned up after processing
