# Package Data Extractor (test1.py)

## Overview
`test1.py` is a Python script that extracts package information from a webpage and generates a structured Excel file.

## What It Does
1. **Takes a Package Link (URL)** as input
2. **Scrapes the webpage** where package data is present in rows
3. **Extracts 3 key pieces of information** from each line:
   - **RPM Spec Name**: Text from the beginning of the line to ".armv" (inclusive)
   - **Package Path**: Path that starts with "//" and ends before "(- number)"
   - **CL**: A number present at the end of the line
4. **Generates an Excel file** with these 3 columns

## Data Format Example
Based on the webpage content, each line follows this pattern:
```
rpm-spec-name.armv //path/to/package (- 123456) 12345678
```

### Extracted Columns:
| RPM Spec Name | Package Path | CL |
|---------------|--------------|-----|
| rpm-spec-name.armv | //path/to/package | 12345678 |

## Installation

### Prerequisites
Install required dependencies:
```bash
pip install requests beautifulsoup4 pandas openpyxl
```

Or install all dependencies from requirements.txt:
```bash
pip install -r requirements.txt
```

## Usage

### Method 1: Interactive Mode
Run the script and enter the URL when prompted:
```bash
python test1.py
```

Then enter:
1. The package webpage URL
2. Output filename (optional, default: `package_data.xlsx`)

### Method 2: Command Line Argument
Pass the URL directly as an argument:
```bash
python test1.py https://example.com/package-page
```

## Example

```bash
$ python test1.py

================================================================================
Package Data Extractor
================================================================================
Enter the package webpage URL: https://example.com/package-page

🔄 Processing...
Fetching data from: https://example.com/package-page

Enter output filename (default: package_data.xlsx): my_packages.xlsx

✅ Excel file generated successfully: my_packages.xlsx
Total records: 150

📋 Preview of data (first 5 rows):
     RPM Spec Name              Package Path        CL
   example-package    //path/to/package1.  12345678
  another-package    //path/to/package2.  87654321
...

✨ Process completed successfully!
```

## Output
The script generates an Excel file (`.xlsx`) with three columns:
1. **RPM Spec Name** - Package specification name
2. **Package Path** - Full path to the package
3. **CL** - Change list number

## Features
- ✅ Automatic webpage content extraction
- ✅ Pattern-based data parsing
- ✅ Excel file generation with proper formatting
- ✅ Data preview before saving
- ✅ Error handling and validation
- ✅ Command line and interactive modes

## Error Handling
The script handles:
- Invalid URLs
- Network errors
- Parsing errors
- Empty data scenarios
- Invalid line formats

## Notes
- The script automatically skips lines that don't match the expected format
- Only lines containing "//" and ending with a number are processed
- The Excel file is saved in the current working directory
- Duplicate entries are not filtered (all matching lines are included)

## Troubleshooting

### No data found
- Verify the URL is correct and accessible
- Check that the webpage contains the expected data format
- Ensure the webpage is not behind authentication

### Excel generation fails
- Verify `openpyxl` is installed
- Check write permissions in the output directory
- Ensure the filename is valid

## Requirements
- Python 3.6+
- requests
- beautifulsoup4
- pandas
- openpyxl
