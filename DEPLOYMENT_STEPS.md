# DNA Automation Portal - Deployment Steps

## Prerequisites
- Access to organization network (http://107.108.175.239:8000)
- MySQL installed with credentials: username=root, password=root
- Node.js and npm installed
- Python 3 installed with required packages
- Microsoft Edge and EdgeDriver installed

## Setup Steps

### 1. Database Setup
```bash
cd backend
python3 setup_database.py
```
This creates the `dna_automation` database and populates it with model names, countries, and InfoLink servers.

### 2. Update Driver Path (if needed)
Edit `backend/app.py` line 35:
```python
driver_path = r"C:\Users\yash.v1\Documents\Web Scapping Project\edgedriver_win64\msedgedriver.exe"
```
Update this to match your EdgeDriver location on the organization machine.

### 3. Start Backend Server
```bash
cd backend
python3 app.py
```
Backend will run on: http://localhost:5001

### 4. Start Frontend Server
```bash
cd frontend
npm install  # First time only
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

### Issue: No data displayed after automation
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

### Issue: Web scraping fails
**Cause**: Not on organization network or EdgeDriver path wrong
**Solution**:
- Ensure you're on the machine with network access to internal site
- Update `driver_path` in `backend/app.py`
- Verify EdgeDriver version matches Edge browser version

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
