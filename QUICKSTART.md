# 🚀 Quick Start Guide - DNA Automation Portal

Follow these steps to get the DNA Automation Portal up and running quickly.

## ⚡ Quick Setup (5 minutes)

### Step 1: Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### Step 2: Install Frontend Dependencies

```bash
cd ../frontend
npm install
```

### Step 3: Configure Backend (Important!)

Edit `backend/app.py` and update these paths:

```python
# Line 24
driver_path = r"YOUR_PATH_TO\msedgedriver.exe"

# Line 25
download_dir = r"YOUR_DESIRED_OUTPUT_FOLDER"
```

## 🎬 Running the Portal

### Terminal 1 - Start Backend:

```bash
cd backend
python app.py
```

You should see:
```
Starting Flask server...
Backend API running on http://localhost:5000
```

### Terminal 2 - Start Frontend:

```bash
cd frontend
npm start
```

Browser will automatically open at `http://localhost:3000`

## ✅ Test the Portal

1. You'll see the **DNA Automation** portal with a green header
2. One row will be pre-loaded with dropdown menus and input fields
3. Try adding a new row by clicking **"Add Row"** button
4. Fill in sample data:
   - Ref. Server: `Staging`
   - Curr. Server: `Production`
   - Model ID Ref.: `G95SC`
   - Model ID Curr.: `G95SD`
   - Country Ref.: `US`
   - Country Curr.: `US`
   - InfoLink Ver. Ref.: `1.0`
   - InfoLink Ver. Curr.: `2.0`
5. Click **"Run Automation"** to test (will show confirmation modal)

## 📝 Sample Input Data

Here's a complete example row you can use for testing:

| Field | Value |
|-------|-------|
| Ref. Server | Staging |
| Curr. Server | Production |
| Model ID Ref. | G95SC |
| Model ID Curr. | G95SD |
| Country Ref. | US |
| Country Curr. | US |
| InfoLink Ver. Ref. | 23_OSCS_GMT9_T09 |
| InfoLink Ver. Curr. | 23_OSCS_GMT9_T09 |

## ❓ Troubleshooting

### Port Already in Use?

**Backend (Port 5000):**
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9
```

**Frontend (Port 3000):**
```bash
# Kill process on port 3000
lsof -ti:3000 | xargs kill -9
```

### Can't Connect Frontend to Backend?

Check `frontend/package.json` has this line:
```json
"proxy": "http://localhost:5000"
```

### Backend Errors?

- Verify Edge WebDriver path is correct
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (needs 3.7+)

### Frontend Won't Start?

- Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`
- Clear npm cache: `npm cache clean --force`
- Check Node version: `node --version` (needs v16+)

## 🎯 Next Steps

Once everything is running:

1. **Add Multiple Rows**: Click "Add Row" to create batch comparisons
2. **Fill Data**: Enter all 8 columns for each row
3. **Run Automation**: Process all rows at once
4. **Check Output**: Master Excel file will be created in your configured `download_dir`

## 💡 Tips

- **Delete Rows**: Use the red trash icon on the right of each row
- **Validation**: Portal validates all fields before running
- **Progress Bar**: Shows real-time progress during automation
- **Batch Mode**: Add multiple rows for efficient batch processing

---

**Need Help?** Check the main README.md for detailed documentation.
