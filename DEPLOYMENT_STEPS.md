# DNA Automation Portal - Deployment Steps

## ⚠️ IMPORTANT: Windows-Only Application
**This application MUST run on a Windows machine** due to:
- Microsoft EdgeDriver requirement (Windows-specific automation)
- Access to internal network (http://107.108.175.239:8000)
- Windows file system paths

**Running on Mac/Linux will show**: "Length: 0" error with message about EdgeDriver not found.

## Prerequisites (Windows Machine Required)
- **Windows OS** (tested on Windows 10/11)
- Access to organization network (http://107.108.175.239:8000)
- MySQL installed with credentials: username=root, password=root
- Node.js and npm installed
- Python 3 installed with required packages
- Microsoft Edge and EdgeDriver installed

## Setup Steps (On Windows Office Machine)

### 1. Download EdgeDriver
1. Check your Edge browser version: `edge://version`
2. Download matching EdgeDriver: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
3. Extract `msedgedriver.exe` to a folder (e.g., `C:\EdgeDriver\`)

### 2. Update Driver Path
Edit `backend/app.py` line 36:
```python
driver_path = r"C:\Users\yash.v1\Documents\Web Scapping Project\edgedriver_win64\msedgedriver.exe"
```
Update this to match your EdgeDriver location on Windows.

### 3. Database Setup
```cmd
cd backend
python setup_database.py
```
This creates the `dna_automation` database and populates it with model names, countries, and InfoLink servers.

### 4. Install Python Dependencies
```cmd
cd backend
pip install flask flask-cors pandas selenium mysql-connector-python openpyxl
```

### 5. Start Backend Server
```cmd
cd backend
python app.py
```
Backend will run on: http://localhost:5001

### 6. Install Frontend Dependencies & Start
```cmd
cd frontend
npm install
npm start
```
Frontend will run on: http://localhost:3000

## Testing the Fix

After running automation:

### ✅ You Should See:
1. **Success Message**: "Automation completed successfully! Master Excel file has been created."
2. **Results Section** appears below the input form with:
   - 📊 Automation Results title
   - **Download Excel** button (top right)
   - **Statistics Card** showing:
     - Total Rows
     - Total Columns
     - State 0 (Match) - Green
     - State 1 (Mismatch) - Red
     - State 2.1 (Partial) - Orange
     - State 2.2 (Not Found) - Volcano
   - **Data Table** with all processed data
   - Color-coded rows based on State Value

3. **Browser Console Logs** (press F12):
   - "Response data:" with full response
   - "Data array:" with the data
   - "Columns:" with column names
   - "Statistics:" with stats object
   - "Results data set, length:" with data count
   - "resultsData changed:" when state updates

### ❌ If Results Don't Appear:

1. **Check Browser Console** (F12 → Console tab)
   - Look for the debug logs
   - Check if `response.data.data` has content
   - Verify `resultsData` state is being set

2. **Check Network Tab** (F12 → Network tab)
   - Find the `/api/run-automation` POST request
   - Check the response body has `success: true`, `data`, `columns`, and `statistics`

3. **Verify Backend Response**
   - Backend terminal should show processing logs
   - Check for errors in backend terminal

## Backend API Endpoints

- `POST /api/run-automation` - Runs the automation
  - Returns: `{ success, message, data, columns, statistics }`
  
- `GET /api/download-excel` - Downloads master Excel file
  - Returns: Excel file as blob

- `GET /api/get-data` - Retrieves last automation results without re-running

- `GET /api/model-names` - Gets all model names from database

- `GET /api/infolink-servers` - Gets all InfoLink servers from database

- `GET /api/countries` - Gets all countries from database

## Common Issues

### Issue: "Length: 0" error with empty results (Current Error on Mac)
**Error Display**:
```
Debug Info:
Results Data Type: object
Is Array: Yes
Length: 0
Columns: 2
Has Statistics: Yes
```

**Root Cause**: EdgeDriver not found - Application running on non-Windows machine

**Solution**: 
- ⚠️ **You MUST run this on your Windows office machine**
- The Mac machine cannot execute the Selenium automation
- Transfer the entire project to Windows and run there
- Ensure EdgeDriver is installed on Windows at the configured path

### Issue: EdgeDriver not found on Windows
**Error**: "EdgeDriver not found at: C:\Users\..."

**Solution**:
1. Download EdgeDriver for Windows
2. Extract `msedgedriver.exe` to a permanent location
3. Update `driver_path` in `backend/app.py` line 36
4. Verify the path exists: Open File Explorer and navigate to the path

### Issue: No data displayed after successful automation
**Cause**: Frontend state not updating or backend not returning data
**Solution**: 
- Check browser console for logs
- Verify backend printed "Master Excel file updated with State Value"
- Check Network tab response has `data` array

### Issue: Download button doesn't work
**Cause**: Excel bytes not stored or API endpoint failing
**Solution**:
- Check browser console for download errors
- Verify backend has `/api/download-excel` endpoint running
- Check backend terminal for download request logs

### Issue: Web scraping fails on Windows
**Cause**: Not on organization network or EdgeDriver path wrong
**Solution**:
- Ensure you're on the machine with network access to internal site (http://107.108.175.239:8000)
- Update `driver_path` in `backend/app.py`
- Verify EdgeDriver version matches Edge browser version
- Check website credentials are correct (USERNAME/PASSWORD in app.py)

## Updated Files (Latest Git Commit)

1. `backend/app.py` - Database credentials updated to root/root
2. `backend/setup_database.py` - Database credentials updated to root/root
3. `frontend/src/App.js` - Added:
   - Results display section
   - Download Excel functionality
   - Statistics display
   - Color-coded data table
   - Debug logging

All changes pushed to: https://github.com/Yvaardhan/Automataion-Web
     