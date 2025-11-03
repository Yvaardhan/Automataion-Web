# DNA Automation Portal - Complete Setup Guide

## 🚀 Quick Start (Current Device)

### Running the Project

#### 1. Start Backend (Terminal 1)
```bash
cd /Users/yasshh/Downloads/Project_DNA/backend
python3 app.py
```
**Backend will run on**: http://localhost:5001

#### 2. Start Frontend (Terminal 2)
```bash
cd /Users/yasshh/Downloads/Project_DNA/frontend
npm start
```
**Frontend will run on**: http://localhost:3000

#### 3. Access Application
Open your browser and go to: **http://localhost:3000**

---

## 🔧 Complete Setup for New Device

### Prerequisites

#### 1. **Python 3.8+**
```bash
# Check Python version
python3 --version

# If not installed, download from: https://www.python.org/downloads/
```

#### 2. **Node.js 16+ and npm**
```bash
# Check Node.js version
node --version

# Check npm version
npm --version

# If not installed, download from: https://nodejs.org/
```

#### 3. **MySQL Server**
```bash
# Check MySQL status
mysql --version

# If not installed:
# macOS: brew install mysql
# Windows: Download from https://dev.mysql.com/downloads/mysql/
# Linux: sudo apt-get install mysql-server
```

#### 4. **Microsoft Edge WebDriver**
- Download from: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
- Place `msedgedriver.exe` in a known location
- Note the path for configuration

---

## 📥 Step-by-Step Installation

### Step 1: Clone/Copy Project
```bash
# Copy the entire Project_DNA folder to your desired location
cd /path/to/your/location
```

### Step 2: Backend Setup

#### 2.1 Install Python Dependencies
```bash
cd Project_DNA/backend
pip3 install -r requirements.txt
```

**Required packages** (in `requirements.txt`):
```
flask==3.0.0
flask-cors==4.0.0
pandas==2.1.3
selenium==4.15.2
mysql-connector-python==8.2.0
openpyxl==3.1.2
```

#### 2.2 Configure Database Settings

Edit `backend/app.py` and `backend/setup_database.py`:

```python
# Database credentials (lines 36-39 in app.py)
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "YOUR_MYSQL_PASSWORD"  # Change this!
DB_NAME = "dna_automation"
```

#### 2.3 Configure Edge Driver Path

Edit `backend/app.py` (line 27):

**Windows:**
```python
driver_path = r"C:\Path\To\Your\msedgedriver.exe"
download_dir = r"C:\Users\YourUsername\Downloads"
```

**macOS:**
```python
driver_path = "/usr/local/bin/msedgedriver"
download_dir = "/Users/yourusername/Downloads"
```

**Linux:**
```python
driver_path = "/usr/local/bin/msedgedriver"
download_dir = "/home/yourusername/Downloads"
```

#### 2.4 Setup MySQL Database
```bash
# Start MySQL service
# macOS: brew services start mysql
# Windows: Start MySQL service from Services
# Linux: sudo systemctl start mysql

# Login to MySQL
mysql -u root -p

# Create user if needed (optional)
CREATE USER 'root'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

#### 2.5 Initialize Database
```bash
cd Project_DNA/backend
python3 setup_database.py
```

**Expected Output:**
```
======================================================================
DNA AUTOMATION - DATABASE SETUP
======================================================================

✓ Extracted 48 model name-to-ID mappings
✓ Connected to MySQL server
✓ Database 'dna_automation' created/verified
✓ Table 'model_names' created/verified
✓ Table 'model_mapping' created/verified
✓ Inserted 48 model name-to-ID mappings
✓ Inserted 42 model mappings

✓ Total Model Name-ID Mappings: 48
```

### Step 3: Frontend Setup

#### 3.1 Install Node Dependencies
```bash
cd Project_DNA/frontend
npm install
```

**This will install:**
- React 18.2.0
- Ant Design (antd) 5.12.0
- Axios 1.6.0
- React Scripts 5.0.1

#### 3.2 Configure Backend URL (if needed)

Edit `frontend/package.json` (line 36):
```json
"proxy": "http://localhost:5001"
```

**Note:** Only change if backend runs on different port

---

## 🎯 Running the Application

### Method 1: Using Two Terminals

**Terminal 1 - Backend:**
```bash
cd Project_DNA/backend
python3 app.py
```

**Terminal 2 - Frontend:**
```bash
cd Project_DNA/frontend
npm start
```

### Method 2: Using Streamlit (Alternative)

If you prefer the Streamlit interface:
```bash
cd Project_DNA
streamlit run Project.py
```

---

## 🌐 Access Points

- **React Frontend**: http://localhost:3000
- **Flask Backend API**: http://localhost:5001
- **Streamlit App**: http://localhost:8501 (if running Project.py)

### API Endpoints:
- `GET /api/health` - Health check
- `GET /api/model-names` - Get all model names
- `POST /api/run-automation` - Run automation
- `GET /api/download-excel` - Download Excel file
- `GET /api/get-data` - Get processed data

---

## 📋 Project Structure

```
Project_DNA/
├── backend/
│   ├── app.py                    # Flask backend API
│   ├── setup_database.py         # Database initialization
│   └── requirements.txt          # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── App.js               # React main component
│   │   └── ...
│   ├── package.json             # Node dependencies
│   └── public/
├── Project.py                    # Streamlit alternative
├── requirements.txt              # Streamlit dependencies
├── README.md
├── QUICKSTART.md
└── SETUP_GUIDE.md               # This file
```

---

## 🔑 Configuration Checklist

Before running on a new device, ensure you've configured:

- [ ] MySQL database credentials in `backend/app.py`
- [ ] MySQL database credentials in `backend/setup_database.py`
- [ ] Edge WebDriver path in `backend/app.py`
- [ ] Download directory path in `backend/app.py`
- [ ] Edge WebDriver path in `Project.py` (if using Streamlit)
- [ ] Download directory path in `Project.py` (if using Streamlit)
- [ ] Run database setup script: `python3 setup_database.py`
- [ ] Install all Python dependencies: `pip3 install -r requirements.txt`
- [ ] Install all Node dependencies: `npm install`

---

## 🐛 Troubleshooting

### Backend Issues

#### Issue: "No module named 'flask'"
**Solution:**
```bash
pip3 install flask flask-cors
```

#### Issue: "Can't connect to MySQL server"
**Solution:**
1. Check if MySQL is running
2. Verify credentials in `app.py`
3. Ensure database user has proper permissions

#### Issue: "WebDriver not found"
**Solution:**
1. Download correct Edge WebDriver for your OS
2. Update `driver_path` in `app.py`
3. Ensure file has execute permissions (macOS/Linux)

### Frontend Issues

#### Issue: "npm: command not found"
**Solution:**
Install Node.js from https://nodejs.org/

#### Issue: "Port 3000 already in use"
**Solution:**
```bash
# Kill process on port 3000
lsof -ti:3000 | xargs kill -9

# Or use different port
PORT=3001 npm start
```

#### Issue: "CORS error when calling backend"
**Solution:**
1. Ensure backend is running on port 5001
2. Check `proxy` setting in `package.json`
3. Verify CORS is enabled in `app.py`

---

## 🔐 Security Notes

### Production Deployment

When deploying to production:

1. **Change hardcoded credentials**
   ```python
   # app.py - Use environment variables
   import os
   USERNAME = os.getenv('DNA_USERNAME')
   PASSWORD = os.getenv('DNA_PASSWORD')
   DB_PASSWORD = os.getenv('DB_PASSWORD')
   ```

2. **Use production WSGI server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5001 app:app
   ```

3. **Build React for production**
   ```bash
   cd frontend
   npm run build
   # Serve build folder with nginx or similar
   ```

4. **Enable HTTPS**
   - Use SSL certificates
   - Configure reverse proxy (nginx/Apache)

---

## 📞 Support

### Key Files for Reference:
- `README.md` - Project overview
- `QUICKSTART.md` - Quick start guide
- `MODEL_DATA_UPDATE_SUMMARY.md` - Model data documentation

### Common Commands Quick Reference:

```bash
# Start Backend
cd backend && python3 app.py

# Start Frontend
cd frontend && npm start

# Reset Database
cd backend && python3 setup_database.py

# Check Backend Health
curl http://localhost:5001/api/health

# Install Dependencies
pip3 install -r requirements.txt    # Python
npm install                         # Node.js
```

---

## ✅ Verification Steps

After setup, verify everything works:

1. **Backend Health Check:**
   ```bash
   curl http://localhost:5001/api/health
   # Should return: {"status": "healthy", "message": "Backend is running"}
   ```

2. **Database Connection:**
   ```bash
   curl http://localhost:5001/api/model-names
   # Should return list of 48 model names
   ```

3. **Frontend Access:**
   - Open http://localhost:3000
   - Should see DNA Automation Portal interface
   - Model dropdowns should be populated

---

## 🎉 You're All Set!

Your DNA Automation Portal is now ready to use. Happy automating! 🚀
