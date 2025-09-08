# Installation Guide - Meticulous Quality AI Platform

## 🚀 Quick Start

### Step 1: System Requirements
- **Python**: 3.11 or higher
- **Operating System**: Windows, macOS, or Linux
- **RAM**: Minimum 4GB, Recommended 8GB
- **Storage**: 500MB free space

### Step 2: Download and Extract
1. Download the `meticulous-quality-ai-platform.zip` file
2. Extract to your desired location:
   ```bash
   unzip meticulous-quality-ai-platform.zip
   cd cleaning_ai_platform
   ```

### Step 3: Install Python Dependencies
```bash
# Install all required packages
pip install -r requirements.txt

# Or install individually:
pip install streamlit==1.28.1
pip install pandas==2.1.1
pip install plotly==5.17.0
pip install numpy==1.24.3
pip install gspread==5.11.3
pip install google-auth==2.23.3
```

### Step 4: Run the Application
```bash
# Start the Streamlit server
streamlit run app.py

# Or specify a custom port
streamlit run app.py --server.port=8502
```

### Step 5: Access the Platform
- Open your web browser
- Navigate to `http://localhost:8501` (or your custom port)
- The platform will load with all features available

## 🔧 Advanced Configuration

### Environment Variables
Create a `.env` file in the project root:
```env
# N8N Configuration
N8N_BASE_URL=http://localhost:5678
N8N_API_KEY=your-api-key-here

# Google Sheets Integration
GOOGLE_SHEETS_CREDENTIALS_PATH=data/gsheets_auth/service_account.json

# Platform Settings
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

### Google Sheets Integration Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable Google Sheets API
4. Create service account credentials
5. Download JSON key file
6. Place in `data/gsheets_auth/service_account.json`

### N8N Integration Setup
1. Install N8N locally or use cloud instance:
   ```bash
   npm install n8n -g
   n8n start
   ```
2. Access N8N at `http://localhost:5678`
3. Create API key in N8N settings
4. Update configuration in `utils/n8n_integration.py`

## 🐳 Docker Deployment

### Build Docker Image
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Run with Docker
```bash
# Build the image
docker build -t meticulous-quality-ai .

# Run the container
docker run -p 8501:8501 meticulous-quality-ai
```

## ☁️ Cloud Deployment

### Streamlit Cloud
1. Push code to GitHub repository
2. Connect to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy directly from repository

### Heroku Deployment
1. Create `Procfile`:
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```
2. Deploy to Heroku:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### AWS/GCP/Azure
- Use container services (ECS, Cloud Run, Container Instances)
- Deploy using Docker image
- Configure load balancer and SSL certificates

## 🔍 Troubleshooting

### Common Issues

**1. Import Errors**
```bash
# Solution: Ensure all dependencies are installed
pip install -r requirements.txt --upgrade
```

**2. Port Already in Use**
```bash
# Solution: Use different port
streamlit run app.py --server.port=8502
```

**3. CSV Files Not Loading**
```bash
# Solution: Check file permissions
chmod 755 data/
chmod 644 data/*/*.csv
```

**4. N8N Connection Failed**
- Verify N8N server is running
- Check API key configuration
- Ensure network connectivity

### Performance Optimization

**1. Enable Caching**
```python
# Already implemented in the code
@st.cache_data
def load_data():
    # Data loading logic
```

**2. Optimize Memory Usage**
```bash
# Set environment variables
export STREAMLIT_SERVER_MAX_UPLOAD_SIZE=200
export STREAMLIT_SERVER_MAX_MESSAGE_SIZE=200
```

**3. Database Configuration**
- Use PostgreSQL for production
- Configure connection pooling
- Enable query optimization

## 📊 Data Migration

### Import Existing Data
1. Prepare CSV files with correct headers
2. Use CSV Management interface to upload
3. Verify data integrity through Data Viewer

### Export Data
1. Access CSV Management tab
2. Select files to download
3. Use merge functionality for combined exports

## 🔐 Security Configuration

### Authentication Setup
```python
# Add to app.py for authentication
import streamlit_authenticator as stauth

# Configure authentication
authenticator = stauth.Authenticate(
    credentials,
    'cleaning_ai_platform',
    'auth_key',
    cookie_expiry_days=30
)
```

### SSL Configuration
```bash
# For production deployment
streamlit run app.py --server.enableCORS=false --server.enableXsrfProtection=true
```

## 📞 Support

### Getting Help
- Check the README.md for feature documentation
- Review sample data in `data/` directories
- Test with pre-built workflows

### Contact Information
- Technical Support: support@meticulousquality.com
- Documentation: https://meticulousquality.com/docs
- Community: https://meticulousquality.com/community

---

**Installation Complete! 🎉**

Your Meticulous Quality AI Automation Platform is ready to transform your cleaning business operations.

