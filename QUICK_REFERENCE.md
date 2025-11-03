# DNA Automation - Quick Reference Card

## 🚀 Start Commands

### Current Device (Quick Start)
```bash
# Terminal 1 - Backend
cd /Users/yasshh/Downloads/Project_DNA/backend
python3 app.py

# Terminal 2 - Frontend  
cd /Users/yasshh/Downloads/Project_DNA/frontend
npm start
```

## 🌐 URLs
- **Frontend**: http://localhost:3000
- **Backend**: http://localhost:5001
- **Streamlit** (alternative): `streamlit run Project.py`

## 🔧 New Device Setup (One-time)

### 1. Install Prerequisites
```bash
# Python 3.8+
python3 --version

# Node.js 16+
node --version

# MySQL
mysql --version
```

### 2. Configuration Files to Update
| File | Line | What to Change |
|------|------|----------------|
| `backend/app.py` | 27 | Edge driver path |
| `backend/app.py` | 28 | Download directory |
| `backend/app.py` | 38 | MySQL password |
| `backend/setup_database.py` | 11 | MySQL password |
| `Project.py` | 27 | Edge driver path |
| `Project.py` | 28 | Download directory |

### 3. Setup Commands
```bash
# Install Python dependencies
cd backend
pip3 install -r requirements.txt

# Setup database
python3 setup_database.py

# Install Node dependencies
cd ../frontend
npm install
```

## 📊 Database Info
- **Database Name**: `dna_automation`
- **Tables**: 
  - `model_names` (48 entries)
  - `model_mapping` (42 entries)
- **Reset Database**: `python3 setup_database.py`

## 🔍 API Endpoints
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/health` | GET | Health check |
| `/api/model-names` | GET | Get model list |
| `/api/run-automation` | POST | Run automation |
| `/api/download-excel` | GET | Download Excel |
| `/api/get-data` | GET | Get processed data |

## 📦 Dependencies

### Backend (Python)
```
flask==3.0.0
flask-cors==4.0.0
pandas==2.1.3
selenium==4.15.2
mysql-connector-python==8.2.0
openpyxl==3.1.2
```

### Frontend (Node.js)
```
react@18.2.0
antd@5.12.0
axios@1.6.0
```

## 🐛 Quick Fixes

### Port Already in Use
```bash
# Kill backend (port 5001)
lsof -ti:5001 | xargs kill -9

# Kill frontend (port 3000)
lsof -ti:3000 | xargs kill -9
```

### Database Connection Error
```bash
# Restart MySQL
brew services restart mysql  # macOS

# Check MySQL status
mysql -u root -p
```

### Missing Dependencies
```bash
# Backend
pip3 install -r backend/requirements.txt

# Frontend
cd frontend && npm install
```

## 📂 Important Files
- `SETUP_GUIDE.md` - Complete setup instructions
- `MODEL_DATA_UPDATE_SUMMARY.md` - Model data info
- `README.md` - Project overview
- `QUICKSTART.md` - Quick start guide

## ✅ Verify Setup
```bash
# Test backend
curl http://localhost:5001/api/health

# Test database
curl http://localhost:5001/api/model-names

# Access frontend
open http://localhost:3000
```

## 🎯 Model Data Summary
- **Total Models**: 42 Model IDs
- **Total Entries**: 48 Display Names
- **Series**: 2023, 2024, 2025
- **Versions**: T09, T10

---
**For detailed setup instructions, see `SETUP_GUIDE.md`**
