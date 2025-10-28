# 🧬 DNA Automation Portal

A modern React-based web application with Ant Design UI for automating web scraping and data comparison tasks using Selenium.

## 🎯 Features

- **Modern React UI**: Beautiful, responsive interface built with Ant Design
- **Dynamic Row Input**: Add unlimited comparison rows with intuitive table interface
- **Real-time Progress**: Visual feedback during automation process
- **Batch Processing**: Process multiple comparisons in a single run
- **Excel Generation**: Automatically creates master Excel files with comparison data
- **RESTful API**: Flask backend with clean API endpoints

## 📋 Project Structure

```
Project_DNA/
├── frontend/               # React application
│   ├── src/
│   │   ├── App.js         # Main React component
│   │   ├── App.css        # Styling
│   │   └── index.js       # Entry point
│   ├── public/
│   └── package.json
├── backend/               # Flask API
│   ├── app.py            # API server & automation logic
│   └── requirements.txt  # Python dependencies
└── README.md
```

## 🚀 Installation & Setup

### Prerequisites

- **Node.js** (v16 or higher)
- **Python** 3.7+
- **Microsoft Edge Browser**
- **Edge WebDriver** (msedgedriver.exe)

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Configure paths in `backend/app.py`:
   - Update `driver_path` to your Edge WebDriver location
   - Update `download_dir` to your desired output location

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install Node dependencies:
```bash
npm install
```

## 🏃 Running the Application

### Start Backend Server

```bash
cd backend
python app.py
```

The Flask API will start on `http://localhost:5000`

### Start Frontend Development Server

In a new terminal:

```bash
cd frontend
npm start
```

The React app will open automatically at `http://localhost:3000`

## 📝 Usage

1. **Access Portal**: Open `http://localhost:3000` in your browser
2. **Enter Data**: Fill in the comparison data for each row:
   - **Ref. Server**: Reference server (Staging/Production)
   - **Curr. Server**: Current server (Staging/Production)
   - **Model ID Ref.**: Reference model identifier
   - **Model ID Curr.**: Current model identifier
   - **Country Ref.**: Reference country code
   - **Country Curr.**: Current country code
   - **InfoLink Ver. Ref.**: Reference InfoLink version
   - **InfoLink Ver. Curr.**: Current InfoLink version
3. **Add Rows**: Click "Add Row" to add more comparisons
4. **Run Automation**: Click "Run Automation" to start processing
5. **Wait**: The process will take several minutes depending on row count
6. **Success**: Master Excel file will be created and opened automatically

## 🔑 Credentials

- **Username**: Yash
- **Password**: Yash@2003

*(Hardcoded in backend for website authentication)*

## 📊 Input Columns

| Column | Description | Example |
|--------|-------------|---------|
| Ref. Server | Reference server type | Staging/Production |
| Curr. Server | Current server type | Staging/Production |
| Model ID Ref. | Reference model ID | G95SC |
| Model ID Curr. | Current model ID | G95SD |
| Country Ref. | Reference country | US |
| Country Curr. | Current country | US |
| InfoLink Ver. Ref. | Reference version | 1.0 |
| InfoLink Ver. Curr. | Current version | 2.0 |

## 🛠️ Technology Stack

### Frontend
- React 18
- Ant Design 5
- Axios
- React Scripts

### Backend
- Flask 3.0
- Flask-CORS
- Selenium WebDriver
- Pandas
- OpenPyXL

## 🔧 Configuration

### Backend Configuration (`backend/app.py`)

```python
driver_path = r"C:\path\to\msedgedriver.exe"
download_dir = r"C:\path\to\output\directory"
website = "http://107.108.175.239:8000/DashBoard/dataPage"
```

### Frontend Proxy (`frontend/package.json`)

```json
"proxy": "http://localhost:5000"
```

## 📦 Build for Production

### Frontend Build

```bash
cd frontend
npm run build
```

This creates an optimized production build in the `frontend/build` directory.

### Backend Production

For production deployment, consider using:
- **Gunicorn**: `gunicorn -w 4 -b 0.0.0.0:5000 app:app`
- **Docker**: Containerize both frontend and backend
- **Nginx**: Serve React build and reverse proxy to Flask

## ⚠️ Important Notes

- Ensure Edge WebDriver version matches your Edge browser version
- The automation process requires stable internet connection
- Temporary CSV files are stored in system temp directory during processing
- Master Excel file is saved to the configured `download_dir`
- The portal validates all fields before running automation

## 🐛 Troubleshooting

**Backend won't start:**
- Check if port 5000 is available
- Verify all Python dependencies are installed
- Ensure Edge WebDriver path is correct

**Frontend won't connect to backend:**
- Verify backend is running on port 5000
- Check proxy configuration in `package.json`
- Look for CORS errors in browser console

**Automation fails:**
- Verify website URL is accessible
- Check Edge WebDriver compatibility
- Ensure credentials are correct
- Review backend logs for detailed errors

## 📄 License

Internal use only - DNA Automation Portal
