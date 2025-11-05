# DNA Automation Portal - Windows Setup Guide

## 🪟 Complete Database Setup for Windows Machine

This guide covers setting up the DNA Automation Portal database on a **new Windows machine** from scratch.

---

## 📋 Prerequisites for Windows

### 1. **Install Python 3.8 or Higher**

#### Download & Install:
1. Visit: https://www.python.org/downloads/windows/
2. Download **Python 3.8+** (recommended: Python 3.11 or 3.12)
3. **IMPORTANT:** During installation, check ✅ **"Add Python to PATH"**
4. Choose **"Install Now"**

#### Verify Installation:
```cmd
python --version
pip --version
```

Expected output: `Python 3.x.x` and `pip 23.x.x`

---

### 2. **Install MySQL Server for Windows**

#### Option A: MySQL Installer (Recommended)

1. **Download MySQL Installer:**
   - Visit: https://dev.mysql.com/downloads/installer/
   - Download **MySQL Installer (Web Community)**
   - File: `mysql-installer-web-community-x.x.xx.msi`

2. **Run the Installer:**
   - Double-click the downloaded `.msi` file
   - Choose **"Custom"** installation type
   - Select the following components:
     - ✅ **MySQL Server** (Latest version, e.g., 8.0.x)
     - ✅ **MySQL Workbench** (Optional, but recommended for GUI management)
     - ✅ **Connector/Python** (Optional, we'll install via pip anyway)

3. **MySQL Server Configuration:**
   - **Config Type:** Development Computer
   - **Connectivity:** 
     - Port: `3306` (default)
     - ✅ Open Windows Firewall ports
   - **Authentication Method:** 
     - Choose **"Use Strong Password Encryption"**
   
4. **Set Root Password:**
   - **IMPORTANT:** Remember this password!
   - Example: `MySecurePassword123!`
   - You'll need this for the application
   
5. **Windows Service:**
   - ✅ Configure MySQL Server as Windows Service
   - Service Name: `MySQL80` (or similar)
   - ✅ Start MySQL Server at System Startup
   
6. **Complete Installation**
   - Click "Execute" and wait for installation
   - Click "Finish"

#### Option B: Manual ZIP Archive Installation

1. Download MySQL ZIP archive from: https://dev.mysql.com/downloads/mysql/
2. Extract to: `C:\Program Files\MySQL\MySQL Server 8.0\`
3. Initialize MySQL:
   ```cmd
   cd "C:\Program Files\MySQL\MySQL Server 8.0\bin"
   mysqld --initialize --console
   ```
4. Note the temporary root password shown in console
5. Install as Windows service:
   ```cmd
   mysqld --install
   net start mysql
   ```

#### Verify MySQL Installation:
```cmd
mysql --version
```

Expected output: `mysql  Ver 8.0.xx for Win64 on x86_64`

---

### 3. **Install Microsoft Edge WebDriver**

The application uses Selenium with Microsoft Edge browser.

#### Download Edge WebDriver:
1. Check your Edge version:
   - Open Edge browser
   - Go to: `edge://settings/help`
   - Note the version (e.g., `120.0.2210.144`)

2. Download matching WebDriver:
   - Visit: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
   - Download the version matching your Edge browser
   - Download for **Windows x64**

3. Extract the driver:
   - Extract `msedgedriver.exe` from the ZIP file
   - **Recommended location:** `C:\WebDriver\msedgedriver.exe`
   - Or any location you prefer (you'll configure this later)

4. **Note the full path** - you'll need it later
   - Example: `C:\WebDriver\msedgedriver.exe`

---

### 4. **Install Node.js (for Frontend)**

1. Visit: https://nodejs.org/
2. Download **LTS version** (e.g., 20.x.x)
3. Run the installer
4. Accept defaults and complete installation

#### Verify:
```cmd
node --version
npm --version
```

---

## 🗄️ Database Setup Steps

### Step 1: Start MySQL Service

MySQL should auto-start if you enabled it during installation. To manually control it:

```cmd
# Start MySQL Service
net start MySQL80

# Check MySQL Service Status
sc query MySQL80

# Stop MySQL Service (if needed)
net stop MySQL80
```

Or use **Services** app:
- Press `Win + R`, type `services.msc`
- Find "MySQL80" (or similar)
- Right-click → Start/Stop

---

### Step 2: Configure MySQL Root Access

#### Login to MySQL:
```cmd
mysql -u root -p
```

Enter the root password you set during installation.

#### Create Database User (Optional but Recommended):

If you want to use a different user instead of root:

```sql
-- Create new user
CREATE USER 'dna_user'@'localhost' IDENTIFIED BY 'YourStrongPassword123!';

-- Grant all privileges
GRANT ALL PRIVILEGES ON *.* TO 'dna_user'@'localhost' WITH GRANT OPTION;

-- Flush privileges
FLUSH PRIVILEGES;

-- Exit MySQL
EXIT;
```

For this guide, we'll use **root** user as configured in the application.

---

### Step 3: Copy Project to Windows Machine

1. **Copy the entire `Project_DNA` folder** to your Windows machine
   - Recommended location: `C:\Users\YourUsername\Documents\Project_DNA`
   - Or Desktop: `C:\Users\YourUsername\Desktop\Project_DNA`

2. **Open Command Prompt or PowerShell** in the project folder:
   - Navigate to folder in File Explorer
   - Hold `Shift` + Right-click → "Open PowerShell window here"
   - Or use `cd` command:
     ```cmd
     cd C:\Users\YourUsername\Documents\Project_DNA
     ```

---

### Step 4: Configure Database Credentials

You need to update database credentials in **TWO files**:

#### File 1: `backend/app.py`

Open `backend/app.py` in a text editor (Notepad++, VS Code, etc.)

Find lines **45-48** and update:

```python
# Database credentials
DB_HOST = "localhost"
DB_USER = "root"                    # Your MySQL username
DB_PASSWORD = "YourMySQLPassword"   # ⚠️ CHANGE THIS!
DB_NAME = "dna_automation"
```

#### File 2: `backend/setup_database.py`

Open `backend/setup_database.py` in a text editor

Find lines **9-12** and update:

```python
# Database credentials
DB_HOST = "localhost"
DB_USER = "root"                    # Your MySQL username
DB_PASSWORD = "YourMySQLPassword"   # ⚠️ CHANGE THIS!
DB_NAME = "dna_automation"
```

**⚠️ IMPORTANT:** Use the **same password** you set during MySQL installation!

---

### Step 5: Configure Windows-Specific Paths

#### Update Edge WebDriver Path in `backend/app.py`

Open `backend/app.py` and find line **36**:

**CHANGE THIS:**
```python
driver_path = r"C:\Users\yash.v1\Documents\Web Scapping Project\edgedriver_win64\msedgedriver.exe"
```

**TO YOUR PATH:**
```python
driver_path = r"C:\WebDriver\msedgedriver.exe"  # Use YOUR actual path
```

**Important:** 
- Use `r"..."` for raw strings (handles backslashes correctly)
- OR use forward slashes: `"C:/WebDriver/msedgedriver.exe"`

#### Update Download Directory in `backend/app.py`

Find line **37** and update to your desired download location:

```python
download_dir = r"C:\Users\YourUsername\Downloads\DNA_Automation"
```

Or use your default Downloads folder:
```python
download_dir = r"C:\Users\YourUsername\Downloads"
```

**Replace `YourUsername`** with your actual Windows username!

To find your username:
```cmd
echo %USERNAME%
```

---

### Step 6: Install Python Dependencies

Open **Command Prompt** or **PowerShell** in the project folder:

```cmd
# Navigate to backend folder
cd Project_DNA\backend

# Install required packages
pip install -r requirements.txt
```

**Packages being installed:**
- `flask==3.0.0` - Web framework
- `flask-cors==4.0.0` - Cross-origin support
- `pandas==2.1.3` - Data processing
- `selenium==4.15.2` - Web automation
- `mysql-connector-python==8.2.0` - MySQL database connector
- `openpyxl==3.1.2` - Excel file handling

#### Verify installation:
```cmd
pip list
```

Look for the packages listed above in the output.

---

### Step 7: Initialize the Database

Now we'll create the database and populate it with initial data.

```cmd
# Make sure you're in the backend folder
cd C:\Users\YourUsername\Documents\Project_DNA\backend

# Run the database setup script
python setup_database.py
```

#### Expected Output:

```
======================================================================
DNA AUTOMATION - DATABASE SETUP
======================================================================

✓ Extracted 48 model name-to-ID mappings
✓ Connected to MySQL server
✓ Database 'dna_automation' created/verified
✓ Table 'model_names' created/verified
✓ Table 'model_mapping' created/verified
✓ Table 'infolink_servers' created/verified
✓ Table 'countries' created/verified
✓ Inserted 48 model name-to-ID mappings
✓ Inserted 42 model mappings
✓ Inserted 301 InfoLink servers
✓ Inserted 169 countries

✓ Total Model Name-ID Mappings: 48
--------------------------------------------------------------------------------
#    Model Name (User Selects)     Model ID (System Uses)
--------------------------------------------------------------------------------
1    G70D_AT_T09                   24_PTML_GMT7_AT_T09
2    G70D_AT_T10                   24_PTML_GM7_T10_AT
...
[Full list of 48 model mappings]
--------------------------------------------------------------------------------

✓ Total InfoLink Servers: 301
✓ Total Countries: 169

======================================================================
✓ DATABASE SETUP COMPLETED SUCCESSFULLY!
======================================================================
```

#### If you see errors:

**Error: "Access denied for user 'root'@'localhost'"**
- Solution: Double-check your password in `setup_database.py` and `app.py`

**Error: "Can't connect to MySQL server"**
- Solution: Ensure MySQL service is running (see Step 1)

**Error: "No module named 'mysql'"**
- Solution: Run `pip install mysql-connector-python`

---

### Step 8: Verify Database Setup

#### Check Database in MySQL:

```cmd
mysql -u root -p
```

Enter your password, then run:

```sql
-- Show all databases
SHOW DATABASES;

-- You should see 'dna_automation' in the list

-- Use the database
USE dna_automation;

-- Show all tables
SHOW TABLES;

-- You should see:
-- - model_names
-- - model_mapping
-- - infolink_servers
-- - countries

-- Check data count
SELECT COUNT(*) FROM model_names;     -- Should return 48
SELECT COUNT(*) FROM infolink_servers; -- Should return 301
SELECT COUNT(*) FROM countries;        -- Should return 169

-- View sample data
SELECT * FROM model_names LIMIT 10;

-- Exit
EXIT;
```

---

## 🚀 Running the Application

### Start the Backend Server

```cmd
# Navigate to backend folder
cd C:\Users\YourUsername\Documents\Project_DNA\backend

# Start Flask server
python app.py
```

**Expected output:**
```
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
```

**Backend API is now running at:** http://localhost:5001

### Test Backend Health Check

Open a new Command Prompt and run:

```cmd
curl http://localhost:5001/api/health
```

Or open in browser: http://localhost:5001/api/health

**Expected response:**
```json
{"status": "healthy", "message": "Backend is running"}
```

---

### Start the Frontend (React)

Open a **new Command Prompt or PowerShell window**:

```cmd
# Navigate to frontend folder
cd C:\Users\YourUsername\Documents\Project_DNA\frontend

# Install Node dependencies (first time only)
npm install

# Start React development server
npm start
```

**Expected output:**
```
Compiled successfully!

You can now view frontend in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://192.168.x.x:3000
```

**Frontend will automatically open in your default browser at:** http://localhost:3000

---

## ✅ Verification Checklist

After setup, verify everything is working:

- [ ] **MySQL Service is running**
  - Check: `net start MySQL80` or Services app

- [ ] **Database exists and is populated**
  ```cmd
  mysql -u root -p -e "USE dna_automation; SELECT COUNT(*) FROM model_names;"
  ```
  - Should return: 48

- [ ] **Backend server starts without errors**
  ```cmd
  cd backend
  python app.py
  ```
  - Should show: Running on http://127.0.0.1:5001

- [ ] **Backend health check responds**
  - Visit: http://localhost:5001/api/health
  - Should return: `{"status": "healthy"}`

- [ ] **Backend can fetch model names**
  - Visit: http://localhost:5001/api/model-names
  - Should return JSON with 48 model names

- [ ] **Frontend starts successfully**
  ```cmd
  cd frontend
  npm start
  ```
  - Should open browser at http://localhost:3000

- [ ] **Frontend can communicate with backend**
  - Open http://localhost:3000
  - Model dropdown should be populated with options
  - No CORS errors in browser console (F12)

---

## 🛠️ Windows-Specific Troubleshooting

### Issue: "Python is not recognized as an internal or external command"

**Solution:**
1. Re-install Python and check ✅ "Add Python to PATH"
2. Or manually add Python to PATH:
   - Search for "Environment Variables" in Windows
   - Edit "Path" under User Variables
   - Add: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python3xx`
   - Add: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python3xx\Scripts`

### Issue: "mysql is not recognized"

**Solution:**
Add MySQL to PATH:
1. Press `Win + X` → System → Advanced System Settings
2. Click "Environment Variables"
3. Edit "Path" under System Variables
4. Add: `C:\Program Files\MySQL\MySQL Server 8.0\bin`
5. Click OK and restart Command Prompt

### Issue: "Port 5001 is already in use"

**Solution:**
```cmd
# Find process using port 5001
netstat -ano | findstr :5001

# Kill the process (replace PID with actual number)
taskkill /PID <PID> /F

# Or change the port in backend/app.py
# Find the last line and change:
app.run(debug=True, port=5002)  # Changed from 5001 to 5002
```

### Issue: "Access denied" when starting MySQL

**Solution:**
Run Command Prompt as Administrator:
- Right-click on Command Prompt
- Select "Run as administrator"
- Then try MySQL commands

### Issue: Edge WebDriver version mismatch

**Solution:**
1. Check Edge version: `edge://settings/help`
2. Download matching WebDriver version
3. Replace the old `msedgedriver.exe`

### Issue: "Permission denied" when accessing download folder

**Solution:**
1. Right-click the folder → Properties → Security
2. Ensure your user has "Full Control"
3. Or choose a different download folder (like Desktop)

### Issue: Cannot connect to MySQL - "Connection refused"

**Solution:**
1. Check MySQL service is running:
   ```cmd
   sc query MySQL80
   ```
2. Start if not running:
   ```cmd
   net start MySQL80
   ```
3. Check firewall isn't blocking port 3306:
   - Windows Defender Firewall → Allow an app
   - Ensure MySQL is allowed

---

## 📊 Database Schema Overview

The application uses 4 main tables:

### 1. `model_names` table
Stores model name to ID mappings (48 records)

| Column | Type | Description |
|--------|------|-------------|
| id | INT | Auto-increment primary key |
| model_name | VARCHAR(100) | Display name (e.g., "G97NC_T09") |
| model_id | VARCHAR(100) | System ID (e.g., "23_OSCP_GMT9_T09") |
| created_at | TIMESTAMP | Creation timestamp |

### 2. `model_mapping` table
Stores reverse mapping: ID to names (42 records)

| Column | Type | Description |
|--------|------|-------------|
| id | INT | Auto-increment primary key |
| model_id | VARCHAR(100) | System ID |
| model_names | TEXT | Comma-separated display names |
| created_at | TIMESTAMP | Creation timestamp |

### 3. `infolink_servers` table
Stores InfoLink server names (301 records)

| Column | Type | Description |
|--------|------|-------------|
| id | INT | Auto-increment primary key |
| server_name | VARCHAR(100) | Server name |
| server_type | ENUM | 'current', 'reference', or 'both' |
| is_active | BOOLEAN | Active status |
| created_at | TIMESTAMP | Creation timestamp |

### 4. `countries` table
Stores country names (169 records)

| Column | Type | Description |
|--------|------|-------------|
| id | INT | Auto-increment primary key |
| country_name | VARCHAR(100) | Country name |
| country_type | ENUM | 'current', 'reference', or 'both' |
| is_active | BOOLEAN | Active status |
| created_at | TIMESTAMP | Creation timestamp |

---

## 🔐 Security Recommendations for Windows

### 1. Secure MySQL Installation

**Change root password periodically:**
```sql
mysql -u root -p
ALTER USER 'root'@'localhost' IDENTIFIED BY 'NewStrongPassword123!';
FLUSH PRIVILEGES;
EXIT;
```

**Don't forget to update passwords in:**
- `backend/app.py`
- `backend/setup_database.py`

### 2. Use Environment Variables (Advanced)

Instead of hardcoding passwords, use Windows environment variables:

**Set environment variables in Windows:**
```cmd
setx DB_PASSWORD "YourMySQLPassword"
setx DNA_USERNAME "Yash"
setx DNA_PASSWORD "Yash@2003"
```

**Update `backend/app.py`:**
```python
import os

# Database credentials
DB_PASSWORD = os.getenv('DB_PASSWORD', 'Yash@8855')

# Application credentials  
USERNAME = os.getenv('DNA_USERNAME', 'Yash')
PASSWORD = os.getenv('DNA_PASSWORD', 'Yash@2003')
```

### 3. Windows Firewall Configuration

If accessing from other devices on network:

```cmd
# Allow Flask app through firewall
netsh advfirewall firewall add rule name="DNA Automation Backend" dir=in action=allow protocol=TCP localport=5001

# Allow React app through firewall
netsh advfirewall firewall add rule name="DNA Automation Frontend" dir=in action=allow protocol=TCP localport=3000
```

---

## 🔄 Updating the Database

### Adding New Models

Edit `backend/setup_database.py`, add to `model_mapping`:

```python
model_mapping = {
    # Existing models...
    
    # Add new model
    "26_NEW_MODEL_ID": "NewModelName_T09",
}
```

Then re-run:
```cmd
python setup_database.py
```

### Adding New InfoLink Servers

Edit `backend/setup_database.py`, add to `INFOLINK_SERVERS`:

```python
INFOLINK_SERVERS = [
    # Existing servers...
    "T-INFOLINK2025-1009",  # Add new server
]
```

Then re-run:
```cmd
python setup_database.py
```

### Resetting Database

To completely reset and rebuild:

```sql
mysql -u root -p
DROP DATABASE dna_automation;
EXIT;
```

Then run setup again:
```cmd
python setup_database.py
```

---

## 📝 Quick Command Reference

### MySQL Commands (Windows)
```cmd
# Start MySQL
net start MySQL80

# Stop MySQL
net stop MySQL80

# Login to MySQL
mysql -u root -p

# Check MySQL version
mysql --version

# Backup database
mysqldump -u root -p dna_automation > backup.sql

# Restore database
mysql -u root -p dna_automation < backup.sql
```

### Application Commands
```cmd
# Start Backend
cd backend
python app.py

# Start Frontend
cd frontend
npm start

# Setup Database
cd backend
python setup_database.py

# Check Backend Health
curl http://localhost:5001/api/health

# View Model Names
curl http://localhost:5001/api/model-names
```

### Python Commands
```cmd
# Install all dependencies
pip install -r requirements.txt

# Install specific package
pip install flask

# List installed packages
pip list

# Check Python version
python --version
```

---

## ✨ Summary of Changes for Windows

### Configuration Files to Update:

1. **`backend/app.py`** (Lines to modify):
   - Line 36: `driver_path` → Windows path with `r"C:\..."` format
   - Line 37: `download_dir` → Your Windows downloads folder
   - Line 47: `DB_PASSWORD` → Your MySQL password

2. **`backend/setup_database.py`** (Lines to modify):
   - Line 11: `DB_PASSWORD` → Your MySQL password

### Required Software:
- ✅ Python 3.8+ (with pip)
- ✅ MySQL Server 8.0+ (Community Edition)
- ✅ Microsoft Edge WebDriver
- ✅ Node.js 16+ (with npm)

### Database Setup:
- ✅ Run `python setup_database.py`
- ✅ Verify 48 model names, 301 servers, 169 countries

---

## 🎉 You're Ready!

Your DNA Automation Portal database is now fully set up on Windows!

**Next Steps:**
1. Start the backend: `python backend/app.py`
2. Start the frontend: `npm start` (in frontend folder)
3. Open browser: http://localhost:3000
4. Begin automating! 🚀

**Need help?** Refer to:
- `SETUP_GUIDE.md` - General setup guide
- `QUICKSTART.md` - Quick start guide
- `README.md` - Project overview

---

**💡 Pro Tip:** Bookmark this page and keep it handy for future Windows deployments!
