import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import sys

def extract_package_data(url):
    """
    Fetches the package webpage and extracts data into structured format.
    
    Args:
        url (str): The package webpage URL
        
    Returns:
        list: List of dictionaries containing RPM Spec Name, Package Path, and CL
    """
    try:
        print(f"Fetching data from: {url}")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all text content from the page
        # Looking for lines that contain package information
        page_text = soup.get_text()
        lines = page_text.strip().split('\n')
        
        package_data = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Pattern to match the package information
            # Looking for: text. //path. number
            # Example: rpm-spec-name. //path/to/package. 12345678
            
            # Check if line contains both a path starting with // and ends with a number
            if '//' in line:
                try:
                    # Extract RPM Spec Name (from start to first .)
                    rpm_spec_match = re.match(r'^([^.]+)\.', line)
                    rpm_spec_name = rpm_spec_match.group(1).strip() if rpm_spec_match else ""
                    
                    # Extract Package Path (from // to the next .)
                    package_path_match = re.search(r'(//[^.]+\.)', line)
                    package_path = package_path_match.group(1).strip() if package_path_match else ""
                    
                    # Extract CL number (last number in the line)
                    cl_match = re.findall(r'\b(\d+)\b', line)
                    cl_number = cl_match[-1] if cl_match else ""
                    
                    # Only add if we found all three components
                    if rpm_spec_name and package_path and cl_number:
                        package_data.append({
                            'RPM Spec Name': rpm_spec_name,
                            'Package Path': package_path,
                            'CL': cl_number
                        })
                except Exception as e:
                    # Skip lines that don't match the expected format
                    continue
        
        return package_data
        
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []
    except Exception as e:
        print(f"Error parsing data: {e}")
        return []


def generate_excel(package_data, output_filename='package_data.xlsx'):
    """
    Generate an Excel file from the extracted package data.
    
    Args:
        package_data (list): List of dictionaries with package information
        output_filename (str): Name of the output Excel file
    """
    if not package_data:
        print("No data to export!")
        return False
    
    try:
        # Create DataFrame
        df = pd.DataFrame(package_data)
        
        # Export to Excel
        df.to_excel(output_filename, index=False, engine='openpyxl')
        print(f"\n✅ Excel file generated successfully: {output_filename}")
        print(f"Total records: {len(package_data)}")
        
        # Display preview
        print("\n📋 Preview of data (first 5 rows):")
        print(df.head().to_string(index=False))
        
        return True
        
    except Exception as e:
        print(f"Error generating Excel: {e}")
        return False


def main():
    """
    Main function to run the package data extraction and Excel generation.
    """
    print("=" * 80)
    print("Package Data Extractor")
    print("=" * 80)
    
    # Get URL from user input or command line argument
    if len(sys.argv) > 1:
        package_url = sys.argv[1]
    else:
        package_url = input("Enter the package webpage URL: ").strip()
    
    if not package_url:
        print("❌ Error: URL is required!")
        sys.exit(1)
    
    # Validate URL format
    if not package_url.startswith(('http://', 'https://')):
        print("❌ Error: Invalid URL format. URL must start with http:// or https://")
        sys.exit(1)
    
    # Extract package data
    print("\n🔄 Processing...")
    package_data = extract_package_data(package_url)
    
    if not package_data:
        print("❌ No package data found or error occurred!")
        sys.exit(1)
    
    # Generate Excel file
    output_file = input("\nEnter output filename (default: package_data.xlsx): ").strip()
    if not output_file:
        output_file = "package_data.xlsx"
    elif not output_file.endswith('.xlsx'):
        output_file += '.xlsx'
    
    success = generate_excel(package_data, output_file)
    
    if success:
        print("\n✨ Process completed successfully!")
    else:
        print("\n❌ Failed to generate Excel file!")
        sys.exit(1)


if __name__ == "__main__":
    main()
