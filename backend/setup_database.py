"""
Database Setup Script for DNA Automation Portal
Creates MySQL database and populates it with model names
"""
import mysql.connector
from mysql.connector import Error

# Database credentials
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Yash@8855"
DB_NAME = "dna_automation"

# Model mapping (model_id to model_names)
# Format: "model_name": "model_id" where model_name is what users select, model_id is used in automation
model_mapping = {
    # T09 Models - 2023 Series
    "23_OSCP_GMT9_T09": "G97NC_T09",
    "23_OSCS_GMT9_T09": "G95SC/SD_T09",
    "23_OSCS_SMT9_T09": "S90PC_T09",
    "23_PTML_SMT7_T09": "M70C_T09",
    "23_PTML_SMT8_T09": "M80C_T09",
    "23_NKL_SMT5_T09": "M50C_T09",
    
    # T10 Models - 2023 Series
    "23_OSCP_GM9_T10": "G97NC_T10",
    "23_OSCS_GM9_T10": "G95SC/SD_T10",
    "23_OSCS_SM9_T10": "S90PC_T10",
    "23_PTML_SM7_T10": "M70C_T10",
    "23_PTML_SM8_T10": "M80C_T10",
    "23_NKL_SM5_T10": "M50C_T10",
    
    # T09 Models - 2025 Series
    "25_PTM_MSC": "LSM7F_T09",
    "25_PTM_SMT8": "M80F_T09",
    "25_RSL_SMT7": "M70F_T09",
    "25_RSM_SMT9": "M90SF_T09",
    "25_RSP_SM9": "M90SF_P_T09",
    "25_RSSF_SMT5": "M50F_T09",
    
    # T10 Models - 2025 Series
    "25_PTM_MSC_T10": "LSM7F_T10",
    "25_PTM_SM8_T10": "M80F_T10",
    "25_RSL_SM7_T10": "M70F_T10",
    "25_RSM_SM9_T10": "M90SF_T10",
    "25_RSP_SM9_T10": "M90SF_P_T10",
    "25_RSSF_SM5_T10": "M50F_T10",
    
    # T09 Models - 2024 Series
    "24_NKL_SM5_T09": "M50D_T09",
    "24_NKL_SMT7_T09": "M70D_T09,M70DO_T09,M1ED_T09,M1EDO_T09",
    "24_NKL_SMT7_AT_T09": "M70D_AT_T09",
    "24_PTML_GMT7_T09": "G70D_T09",
    "24_PTML_GMT7_AT_T09": "G70D_AT_T09",
    "24_PTML_GMT8_T09": "G85SD_T09",
    "24_PTML_GMT8_AT_T09": "G85SD_AT_T09",
    "24_PTML_SMT8_T09": "M80D_T09",
    "24_PTML_SMT8_AT_T09": "M80D_AT_T09",
    
    # T10 Models - 2024 Series
    "24_NKL_SM5_T10": "M50D_T10",
    "24_NKL_SM7_T10": "M70D_T10,M70DO_T10,M1ED_T10,M1EDO_T10",
    "24_NKL_SM7_T10_AT": "M70D_AT_T10",
    "24_PTML_GM7_T10": "G70D_T10",
    "24_PTML_GM7_T10_AT": "G70D_AT_T10",
    "24_PTML_GM8_T10": "G85SD_T10",
    "24_PTML_GM8_T10_AT": "G85SD_AT_T10",
    "24_PTML_SM8_T10": "M80D_T10",
    "24_PTML_SM8_T10_AT": "M80D_AT_T10",
}

def extract_model_name_to_id_mapping():
    """Extract model name to model ID mapping for database storage.
    
    Users will select by display name (e.g., 'G97NC_T09'), 
    and the system will use the model_id (e.g., '23_OSCP_GMT9_T09') for automation.
    """
    model_data = []
    for model_id, display_names_str in model_mapping.items():
        # model_id is the key (e.g., '23_OSCP_GMT9_T09')
        # display_names_str is the value (e.g., 'G97NC_T09')
        # Split by comma and strip whitespace to handle multiple names
        display_names = [name.strip() for name in display_names_str.split(',')]
        for display_name in display_names:
            model_data.append({
                'model_name': display_name,  # What users select (e.g., 'G97NC_T09')
                'model_id': model_id  # What system uses (e.g., '23_OSCP_GMT9_T09')
            })
    return sorted(model_data, key=lambda x: x['model_name'])

def create_database_connection():
    """Create connection to MySQL server."""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        if connection.is_connected():
            print("✓ Connected to MySQL server")
            return connection
    except Error as e:
        print(f"✗ Error connecting to MySQL: {e}")
        return None

def create_database(connection):
    """Create the database if it doesn't exist."""
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"✓ Database '{DB_NAME}' created/verified")
        cursor.close()
    except Error as e:
        print(f"✗ Error creating database: {e}")

def create_tables(connection):
    """Create the model_names table."""
    try:
        cursor = connection.cursor()
        
        # Switch to the database
        cursor.execute(f"USE {DB_NAME}")
        
        # Create model_names table with both name and ID
        create_table_query = """
        CREATE TABLE IF NOT EXISTS model_names (
            id INT AUTO_INCREMENT PRIMARY KEY,
            model_name VARCHAR(100) NOT NULL,
            model_id VARCHAR(100) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE KEY unique_model_name (model_name)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """
        cursor.execute(create_table_query)
        print("✓ Table 'model_names' created/verified")
        
        # Create model_mapping table for reference
        create_mapping_query = """
        CREATE TABLE IF NOT EXISTS model_mapping (
            id INT AUTO_INCREMENT PRIMARY KEY,
            model_id VARCHAR(100) UNIQUE NOT NULL,
            model_names TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """
        cursor.execute(create_mapping_query)
        print("✓ Table 'model_mapping' created/verified")
        
        cursor.close()
    except Error as e:
        print(f"✗ Error creating tables: {e}")

def populate_model_names(connection, model_data):
    """Insert model names with their corresponding model IDs into the database."""
    try:
        cursor = connection.cursor()
        cursor.execute(f"USE {DB_NAME}")
        
        # Clear existing data
        cursor.execute("DELETE FROM model_names")
        
        # Insert model names with IDs
        insert_query = "INSERT INTO model_names (model_name, model_id) VALUES (%s, %s)"
        for item in model_data:
            try:
                cursor.execute(insert_query, (item['model_name'], item['model_id']))
            except Error as e:
                print(f"Warning: Could not insert {item['model_name']}: {e}")
        
        connection.commit()
        print(f"✓ Inserted {len(model_data)} model name-to-ID mappings")
        
        cursor.close()
    except Error as e:
        print(f"✗ Error populating model names: {e}")

def populate_model_mapping(connection):
    """Insert model ID to model names mapping."""
    try:
        cursor = connection.cursor()
        cursor.execute(f"USE {DB_NAME}")
        
        # Clear existing data
        cursor.execute("DELETE FROM model_mapping")
        
        # Insert mappings
        insert_query = "INSERT INTO model_mapping (model_id, model_names) VALUES (%s, %s)"
        for model_id, model_names in model_mapping.items():
            cursor.execute(insert_query, (model_id, model_names))
        
        connection.commit()
        print(f"✓ Inserted {len(model_mapping)} model mappings")
        
        cursor.close()
    except Error as e:
        print(f"✗ Error populating model mapping: {e}")

def display_model_names(connection):
    """Display all model names with their IDs from the database."""
    try:
        cursor = connection.cursor()
        cursor.execute(f"USE {DB_NAME}")
        cursor.execute("SELECT model_name, model_id FROM model_names ORDER BY model_name")
        
        results = cursor.fetchall()
        print(f"\n\u2713 Total Model Name-ID Mappings: {len(results)}")
        print("-" * 80)
        print(f"{'#':<4} {'Model Name (User Selects)':<30} {'Model ID (System Uses)':<40}")
        print("-" * 80)
        for idx, (model_name, model_id) in enumerate(results, 1):
            print(f"{idx:<4} {model_name:<30} {model_id:<40}")
        print("-" * 80)
        
        cursor.close()
    except Error as e:
        print(f"✗ Error displaying model names: {e}")

def main():
    """Main setup function."""
    print("=" * 70)
    print("DNA AUTOMATION - DATABASE SETUP")
    print("=" * 70)
    print()
    
    # Extract model name to ID mappings
    model_data = extract_model_name_to_id_mapping()
    print(f"✓ Extracted {len(model_data)} model name-to-ID mappings")
    
    # Connect to MySQL
    connection = create_database_connection()
    if not connection:
        print("\n✗ Failed to connect to MySQL. Please check credentials.")
        return
    
    try:
        # Create database
        create_database(connection)
        
        # Close and reconnect to the specific database
        connection.database = DB_NAME
        
        # Create tables
        create_tables(connection)
        
        # Populate tables
        populate_model_names(connection, model_data)
        populate_model_mapping(connection)
        
        # Display results
        display_model_names(connection)
        
        print("\n" + "=" * 70)
        print("✓ DATABASE SETUP COMPLETED SUCCESSFULLY!")
        print("=" * 70)
        print("\nNOTE: Users will select Model Names from dropdown,")
        print("      and the system will use corresponding Model IDs for automation.")
        
    finally:
        if connection.is_connected():
            connection.close()
            print("\n✓ MySQL connection closed")

if __name__ == "__main__":
    main()
