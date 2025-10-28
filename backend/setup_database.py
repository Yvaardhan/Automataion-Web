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
model_mapping = {
    "23_OSCS_GMT9_T09": "G95SC,G95SD,S90PC",
    "23_OSCS_SMT9_T09": "S90PC",
    "23_PTML_SMT7_T09": "M70C",
    "23_PTML_SMT8_T09": "M80C",
    "23_OSCP_GMT9_T09": "G97NC",
    "23_NKL_SMT5_T09": "M50C",
    "23_KSUE_UB_BIZ_T09": "BEC-H",
    "23_PTM_LTR_T09": "LST7C, LST9C",
    "24_RSP_GMT8_T09": "G80SD",
    "24_RSP_GMT8_AT_T09": "G80SD_AT",
    "24_PTML_GMT8_T09": "G85SD",
    "24_PTML_GMT7_T09": "G70D",
    "24_PTML_GMT8_AT_T09": "G85SD_AT",
    "24_PTML_GMT7_AT_T09": "G70D_AT",
    "24_PTML_SMT8_T09": "M80D",
    "24_NKL_SMT7_T09": "M70D,M70DO,M1ED,M1EDO",
    "24_PTML_SMT8_AT_T09": "M80D_AT",
    "24_NKL_SMT7_AT_T09": "M70D_AT",
    "24_NKL_SM5_T09": "M50D",
    "25_RSP_SM9": "M90SF_P",
    "25_PTM_SMT8": "M80F",
    "25_RSL_SMT7": "M70F",
    "25_RSM_SMT9": "M90SF",
}

def extract_model_name_to_id_mapping():
    """Extract model name to model ID mapping."""
    model_data = []
    for model_id, names_str in model_mapping.items():
        # Split by comma and strip whitespace
        names = [name.strip() for name in names_str.split(',')]
        for model_name in names:
            model_data.append({
                'model_name': model_name,
                'model_id': model_id
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
        print(f"\n✓ Total Model Name-ID Mappings: {len(results)}")
        print("-" * 70)
        print(f"{'#':<4} {'Model Name':<20} {'Model ID':<30}")
        print("-" * 70)
        for idx, (model_name, model_id) in enumerate(results, 1):
            print(f"{idx:<4} {model_name:<20} {model_id:<30}")
        print("-" * 70)
        
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
