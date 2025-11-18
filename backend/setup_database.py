"""
Database Setup Script for DNA Automation Portal
Creates MySQL database and populates it with model names
"""
import mysql.connector
from mysql.connector import Error

# Database credentials
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "dna_automation"

# InfoLink Server Names - For both Current and Reference use
INFOLINK_SERVERS = [
    "T-INFOLINK2024-1000",
    "T-INFOLINK2023-1008",
    "T-INFOLINK2023-1007",
    "T-INFOLINK2023-1006",
    "T-INFOLINK2023-1005",
    "T-INFOLINK2023-1004",
    "T-INFOLINK2023-1003",
    "T-INFOLINK2023-1002",
    "T-INFOLINK2023-1001",
    "T-INFOLINK2023-1000",
    "T-INFOLINK2022-1012",
    "T-INFOLINK2022-1011",
    "T-INFOLINK2022-1010",
    "T-INFOLINK2022-1009",
    "T-INFOLINK2022-1008",
    "T-INFOLINK2022-1007",
    "T-INFOLINK2022-1006",
    "T-INFOLINK2022-1005",
    "T-INFOLINK2022-1004",
    "T-INFOLINK2022-1003",
    "T-INFOLINK2022-1002",
    "T-INFOLINK2022-1001",
    "T-INFOLINK2022-1000",
    "T-INFOLINK2021-1014",
    "T-INFOLINK2021-1013",
    "T-INFOLINK2021-1012",
    "T-INFOLINK2021-1011",
    "T-INFOLINK2021-1010",
    "T-INFOLINK2021-1009",
    "T-INFOLINK2021-1008",
    "T-INFOLINK2021-1007",
    "T-INFOLINK2021-1006",
    "T-INFOLINK2021-1005",
    "T-INFOLINK2021-1004",
    "T-INFOLINK2021-1003",
    "T-INFOLINK2021-1002",
    "T-INFOLINK2021-1001",
    "T-INFOLINK2021-1000",
    "T-INFOLINK2020-1012",
    "T-INFOLINK2020-1011",
    "T-INFOLINK2020-1010",
    "T-INFOLINK2020-1009",
    "T-INFOLINK2020-1008",
    "T-INFOLINK2020-1007",
    "T-INFOLINK2020-1006",
    "T-INFOLINK2020-1005",
    "T-INFOLINK2020-1004",
    "T-INFOLINK2020-1003",
    "T-INFOLINK2020-1002",
    "T-INFOLINK2020-1001",
    "T-INFOLINK2020-1000",
    "T-INFOLINK2019-1013",
    "T-INFOLINK2019-1012",
    "T-INFOLINK2019-1011",
    "T-INFOLINK2019-1010",
    "T-INFOLINK2019-1009",
    "T-INFOLINK2019-1008",
    "T-INFOLINK2019-1007",
    "T-INFOLINK2019-1006",
    "T-INFOLINK2019-1005_B",
    "T-INFOLINK2019-1005_A",
    "T-INFOLINK2019-1005",
    "T-INFOLINK2019-1004",
    "T-INFOLINK2019-1003",
    "T-INFOLINK2019-1002",
    "T-INFOLINK2019-1001",
    "T-INFOLINK2019-1000",
    "T-INFOLINK2018-1016",
    "T-INFOLINK2018-1015",
    "T-INFOLINK2018-1014",
    "T-INFOLINK2018-1013",
    "T-INFOLINK2018-1012",
    "T-INFOLINK2018-1011",
    "T-INFOLINK2018-1010",
    "T-INFOLINK2018-1009",
    "T-INFOLINK2018-1008",
    "T-INFOLINK2018-1007",
    "T-INFOLINK2018-1006",
    "T-INFOLINK2018-1005",
    "T-INFOLINK2018-1004",
    "T-INFOLINK2018-1003",
    "T-INFOLINK2018-1002",
    "T-INFOLINK2018-1001",
    "T-INFOLINK2018-1000",
    "T-INFOLINK2017-1009",
    "T-INFOLINK2017-1008",
    "T-INFOLINK2017-1007",
    "T-INFOLINK2017-1006",
    "T-INFOLINK2017-1005",
    "T-INFOLINK2017-1004",
    "T-INFOLINK2017-1003",
    "T-INFOLINK2017-1002",
    "T-INFOLINK2017-1001",
    "T-INFOLINK2017-1000",
    "T-INFOLINK2016-1020",
    "T-INFOLINK2016-1019",
    "T-INFOLINK2016-1018",
    "T-INFOLINK2016-1017",
    "T-INFOLINK2016-1016",
    "T-INFOLINK2016-1015",
    "T-INFOLINK2016-1014",
    "T-INFOLINK2016-1013",
    "T-INFOLINK2016-1012",
    "T-INFOLINK2016-1011",
    "T-INFOLINK2016-1010",
    "T-INFOLINK2016-1009",
    "T-INFOLINK2016-1008",
    "T-INFOLINK2016-1007",
    "T-INFOLINK2016-1006",
    "T-INFOLINK2016-1005",
    "T-INFOLINK2016-1004",
    "T-INFOLINK2016-1003",
    "T-INFOLINK2016-1002",
    "T-INFOLINK2016-1001",
    "T-INFOLINK2016-1000",
    "T-INFOLINK2015-1021",
    "T-INFOLINK2015-1020",
    "T-INFOLINK2015-1019",
    "T-INFOLINK2015-1018",
    "T-INFOLINK2015-1017",
    "T-INFOLINK2015-1016",
    "T-INFOLINK2015-1015",
    "T-INFOLINK2015-1014",
    "T-INFOLINK2015-1013",
    "T-INFOLINK2015-1012",
    "T-INFOLINK2015-1011",
    "T-INFOLINK2015-1010",
    "T-INFOLINK2015-1009",
    "T-INFOLINK2015-1008",
    "T-INFOLINK2015-1007",
    "T-INFOLINK2015-1006",
    "T-INFOLINK2015-1005",
    "T-INFOLINK2015-1004",
    "T-INFOLINK2015-1003",
    "T-INFOLINK2015-1002",
    "T-INFOLINK2015-1001",
    "T-INFOLINK2015-1000",
    "T-INFOLINK2014-1044",
    "T-INFOLINK2014-1043",
    "T-INFOLINK2014-1042",
    "T-INFOLINK2014-1041",
    "T-INFOLINK2014-1040",
    "T-INFOLINK2014-1039",
    "T-INFOLINK2014-1038",
    "T-INFOLINK2014-1037",
    "T-INFOLINK2014-1036",
    "T-INFOLINK2014-1035",
    "T-INFOLINK2014-1034",
    "T-INFOLINK2014-1033",
    "T-INFOLINK2014-1032",
    "T-INFOLINK2014-1031",
    "T-INFOLINK2014-1030",
    "T-INFOLINK2014-1029",
    "T-INFOLINK2014-1028",
    "T-INFOLINK2014-1027",
    "T-INFOLINK2014-1026",
    "T-INFOLINK2014-1025",
    "T-INFOLINK2014-1024",
    "T-INFOLINK2014-1023",
    "T-INFOLINK2014-1022",
    "T-INFOLINK2014-1021",
    "T-INFOLINK2014-1020",
    "T-INFOLINK2014-1019",
    "T-INFOLINK2014-1018",
    "T-INFOLINK2014-1017",
    "T-INFOLINK2014-1016",
    "T-INFOLINK2014-1015",
    "T-INFOLINK2014-1014",
    "T-INFOLINK2014-1013",
    "T-INFOLINK2014-1012",
    "T-INFOLINK2014-1011",
    "T-INFOLINK2014-1010",
    "T-INFOLINK2014-1009",
    "T-INFOLINK2014-1008",
    "T-INFOLINK2014-1007",
    "T-INFOLINK2014-1006",
    "T-INFOLINK2014-1005",
    "T-INFOLINK2014-1004",
    "T-INFOLINK2014-1003",
    "T-INFOLINK2014-1002",
    "T-INFOLINK2014-1001",
    "T-INFOLINK2014-1000",
    "T-INFOLINK2013-1031",
    "T-INFOLINK2013-1030",
    "T-INFOLINK2013-1029",
    "T-INFOLINK2013-1028",
    "T-INFOLINK2013-1027",
    "T-INFOLINK2013-1026",
    "T-INFOLINK2013-1025",
    "T-INFOLINK2013-1024",
    "T-INFOLINK2013-1023",
    "T-INFOLINK2013-1022",
    "T-INFOLINK2013-1021",
    "T-INFOLINK2013-1020",
    "T-INFOLINK2013-1019",
    "T-INFOLINK2013-1018",
    "T-INFOLINK2013-1017",
    "T-INFOLINK2013-1016",
    "T-INFOLINK2013-1015",
    "T-INFOLINK2013-1014",
    "T-INFOLINK2013-1013",
    "T-INFOLINK2013-1012",
    "T-INFOLINK2013-1011",
    "T-INFOLINK2013-1010",
    "T-INFOLINK2013-1009",
    "T-INFOLINK2013-1008",
    "T-INFOLINK2013-1007",
    "T-INFOLINK2013-1006",
    "T-INFOLINK2013-1005",
    "T-INFOLINK2013-1004",
    "T-INFOLINK2013-1003",
    "T-INFOLINK2013-1002",
    "T-INFOLINK2013-1001",
    "T-INFOLINK2013-1000",
    "T-INFOLINK2012-1027",
    "T-INFOLINK2012-1026",
    "T-INFOLINK2012-1025",
    "T-INFOLINK2012-1024",
    "T-INFOLINK2012-1023",
    "T-INFOLINK2012-1022",
    "T-INFOLINK2012-1021",
    "T-INFOLINK2012-1020",
    "T-INFOLINK2012-1019",
    "T-INFOLINK2012-1018",
    "T-INFOLINK2012-1017",
    "T-INFOLINK2012-1016",
    "T-INFOLINK2012-1015",
    "T-INFOLINK2012-1014",
    "T-INFOLINK2012-1013",
    "T-INFOLINK2012-1012",
    "T-INFOLINK2012-1011",
    "T-INFOLINK2012-1010",
    "T-INFOLINK2012-1009",
    "T-INFOLINK2012-1008",
    "T-INFOLINK2012-1007",
    "T-INFOLINK2012-1006",
    "T-INFOLINK2012-1005",
    "T-INFOLINK2012-1004",
    "T-INFOLINK2012-1003",
    "T-INFOLINK2012-1002",
    "T-INFOLINK2012-1001",
    "T-INFOLINK2012-1000",
    "TC-INFOLINK2011-1000",
    "T-INFOLINK2011-1016",
    "T-INFOLINK2011-1015",
    "T-INFOLINK2011-1014",
    "T-INFOLINK2011-1013",
    "T-INFOLINK2011-1012",
    "T-INFOLINK2011-1011",
    "T-INFOLINK2011-1010",
    "T-INFOLINK2011-1009",
    "T-INFOLINK2011-1008",
    "T-INFOLINK2011-1007",
    "T-INFOLINK2011-1006",
    "T-INFOLINK2011-1005",
    "T-INFOLINK2011-1004",
    "T-INFOLINK2011-1003",
    "T-INFOLINK2011-1002",
    "T-INFOLINK2011-1001",
    "T-INFOLINK2011-1000",
    "T-INFOLINK2010-1400",
    "T-INFOLINK2010-1300",
    "T-INFOLINK2010-1200",
    "T-INFOLINK2010-1100",
    "T-INFOLINK2010-1014",
    "T-INFOLINK2010-1013",
    "T-INFOLINK2010-1012",
    "T-INFOLINK2010-1011",
    "T-INFOLINK2010-1010",
    "T-INFOLINK2010-1009",
    "T-INFOLINK2010-1008",
    "T-INFOLINK2010-1007",
    "T-INFOLINK2010-1006",
    "T-INFOLINK2010-1005",
    "T-INFOLINK2010-1004",
    "T-INFOLINK2010-1003",
    "T-INFOLINK2010-1002",
    "T-INFOLINK2010-1001",
    "T-INFOLINK2010-1000",
    "E-INFOLINK2010-1000",
    "B-INFOLINK2010-1001",
    "B-INFOLINK2010-1000",
    "T-VALENCIA-1000",
    "T-INFOLINK2025-1008",
    "T-INFOLINK2024-1010",
    "T-INFOLINK2022-1025"
]

# Country Names - For both Current and Reference use
COUNTRIES = [
    "Afghanistan",
    "Aland Islands",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Anguilla",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Bermuda",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei Darussalam",
    "Bulgaria",
    "Burkina Faso",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Cape Verde",
    "Cayman Islands",
    "China",
    "Colombia",
    "Congo",
    "Cook Islands",
    "Costa Rica",
    "Croatia",
    "Cuba",
    "Denmark",
    "Dominica",
    "Dominican Republic",
    "Ecuador",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Ethiopia",
    "Faroe Islands",
    "Finland",
    "France",
    "Gabon",
    "Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Greenland",
    "Grenada",
    "Guam",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran, Islamic Republic of",
    "Iraq",
    "Ireland",
    "Isle of Man",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Korea, Republic",
    "Kuwait",
    "Lao People's Democratic Republic",
    "Latvia",
    "Lebanon",
    "Liberia",
    "Libyan Arab Jamahiriya",
    "Lithuania",
    "Macao",
    "Macedonia",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Mauritania",
    "Mauritius",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Montserrat",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Nigeria",
    "Norway",
    "Oman",
    "Pakistan",
    "Palestinian Territory",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russian Federation",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent and the Grenadines",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Somalia",
    "South Africa",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Swaziland",
    "Switzerland",
    "Syrian Arab Republic",
    "Taiwan",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Turks and Caicos Islands",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom of Great Britain and Northern Ireland",
    "United States of America",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Venezuela",
    "Vietnam",
    "Virgin Islands, British",
    "Virgin Islands, U.S.",
    "Western Sahara",
    "Zambia",
    "Zimbabwe"
]

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
        
        # Create infolink_servers table for both current and reference servers
        create_infolink_query = """
        CREATE TABLE IF NOT EXISTS infolink_servers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            server_name VARCHAR(100) UNIQUE NOT NULL,
            server_type ENUM('current', 'reference', 'both') DEFAULT 'both',
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """
        cursor.execute(create_infolink_query)
        print("✓ Table 'infolink_servers' created/verified")
        
        # Create countries table for both current and reference countries
        create_countries_query = """
        CREATE TABLE IF NOT EXISTS countries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            country_name VARCHAR(100) UNIQUE NOT NULL,
            country_type ENUM('current', 'reference', 'both') DEFAULT 'both',
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """
        cursor.execute(create_countries_query)
        print("✓ Table 'countries' created/verified")
        
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

def populate_infolink_servers(connection):
    """Insert InfoLink server names into database."""
    try:
        cursor = connection.cursor()
        cursor.execute(f"USE {DB_NAME}")
        
        # Clear existing data
        cursor.execute("DELETE FROM infolink_servers")
        
        # Insert InfoLink servers (available for both current and reference)
        insert_query = "INSERT INTO infolink_servers (server_name, server_type, is_active) VALUES (%s, %s, %s)"
        for server_name in INFOLINK_SERVERS:
            cursor.execute(insert_query, (server_name, 'both', True))
        
        connection.commit()
        print(f"✓ Inserted {len(INFOLINK_SERVERS)} InfoLink servers")
        
        cursor.close()
    except Error as e:
        print(f"✗ Error populating InfoLink servers: {e}")

def populate_countries(connection):
    """Insert country names into database."""
    try:
        cursor = connection.cursor()
        cursor.execute(f"USE {DB_NAME}")
        
        # Clear existing data
        cursor.execute("DELETE FROM countries")
        
        # Insert countries (available for both current and reference)
        insert_query = "INSERT INTO countries (country_name, country_type, is_active) VALUES (%s, %s, %s)"
        for country_name in COUNTRIES:
            cursor.execute(insert_query, (country_name, 'both', True))
        
        connection.commit()
        print(f"✓ Inserted {len(COUNTRIES)} countries")
        
        cursor.close()
    except Error as e:
        print(f"✗ Error populating countries: {e}")

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
        populate_infolink_servers(connection)
        populate_countries(connection)
        
        # Display results
        display_model_names(connection)
        
        # Display InfoLink servers and countries count
        cursor = connection.cursor()
        cursor.execute(f"USE {DB_NAME}")
        cursor.execute("SELECT COUNT(*) FROM infolink_servers")
        server_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM countries")
        country_count = cursor.fetchone()[0]
        print(f"\n✓ Total InfoLink Servers: {server_count}")
        print(f"✓ Total Countries: {country_count}")
        cursor.close()
        
        print("\n" + "=" * 70)
        print("✓ DATABASE SETUP COMPLETED SUCCESSFULLY!")
        print("=" * 70)
        print("\nNOTE: Users will select Model Names from dropdown,")
        print("      and the system will use corresponding Model IDs for automation.")
        print(f"      InfoLink servers ({server_count} total) and Countries ({country_count} total) are available for selection.")
        
    finally:
        if connection.is_connected():
            connection.close()
            print("\n✓ MySQL connection closed")

if __name__ == "__main__":
    main()
