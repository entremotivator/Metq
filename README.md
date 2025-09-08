# Meticulous Quality - AI Automation Platform

A comprehensive AI automation platform specifically designed for cleaning business CEOs to manage their operations, workflows, and client relationships.

## 🚀 Features

### 🤖 AI Automation Dashboard
- Lead generation tracking and analytics
- Revenue growth monitoring (300% average increase)
- Time savings metrics (75% operations automation)
- Customer retention tracking (90% retention rate)

### 🔄 N8N Workflow Management
- **Pre-built Workflows**: Lead Generation Bot, Appointment Scheduler, Customer Follow-up, Invoice Generator
- **Webhook Management**: Create and test custom webhooks
- **Real-time Monitoring**: Track workflow execution and performance
- **Analytics Dashboard**: Comprehensive automation analytics

### 📊 CSV Data Management
- **File Operations**: Upload, view, edit, and delete CSV files
- **Category Organization**: Clients, Workflows, Automations, Reports
- **Data Filtering**: Advanced filtering and search capabilities
- **Merge Functionality**: Combine multiple CSV files

### 📈 Business Analytics
- Client distribution and performance metrics
- Service category analysis
- Weekly performance trends
- Revenue projections and ROI analysis

### 👥 Client Management
- Complete client portfolio tracking
- Contract management and renewal tracking
- Satisfaction score monitoring
- Revenue analysis by client type

### ⚙️ Settings & Configuration
- AI automation configuration
- Dashboard customization
- Security settings
- Communication preferences

## 🛠 Installation

### Prerequisites
- Python 3.11+
- pip package manager

### Setup Instructions

1. **Extract the ZIP file**
   ```bash
   unzip meticulous-quality-ai-platform.zip
   cd cleaning_ai_platform
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the platform**
   - Open your browser and go to `http://localhost:8501`
   - The platform will be available with all features

## 📁 Project Structure

```
cleaning_ai_platform/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── utils/
│   └── n8n_integration.py         # N8N workflow and CSV management utilities
├── pages/
│   └── n8n_workflows.py           # N8N workflows management page
├── data/
│   ├── sample_workflows.json      # Sample N8N workflow configurations
│   ├── clients/                   # Client data CSV files
│   │   ├── clients.csv
│   │   └── leads.csv
│   ├── automations/               # Automation logs and data
│   │   └── automation_logs.csv
│   ├── workflows/                 # Workflow data (empty initially)
│   └── reports/                   # Generated reports (empty initially)
└── assets/                        # Images and media assets
    ├── meticulous_quality_logo.png
    └── financial_background.mp4
```

## 🔧 Configuration

### N8N Integration
The platform includes built-in N8N workflow management. To connect to an actual N8N instance:

1. Update the `N8NAgent` configuration in `utils/n8n_integration.py`
2. Set your N8N server URL and API key
3. Deploy the pre-built workflows to your N8N instance

### CSV Data Management
- Sample data is pre-loaded for demonstration
- Upload your own CSV files through the CSV Management interface
- Data is organized by categories for easy management

### Webhook Configuration
- Create webhooks through the Webhooks tab
- Test webhooks with sample JSON data
- Monitor webhook usage and performance

## 📊 Sample Data

The platform comes with pre-loaded sample data:

- **Clients**: 5 sample cleaning business clients
- **Leads**: 5 sample leads with different statuses
- **Automation Logs**: 10 sample workflow execution logs

## 🎨 Branding

The platform uses Meticulous Quality's premium branding:
- **Colors**: Dark gold (#FFD700) and dark theme
- **Typography**: Playfair Display for headers, Inter for body text
- **Design**: Professional, elegant, and modern interface

## 🔄 Automation Workflows

### Pre-built Workflows:

1. **Lead Generation Bot**
   - Webhook-triggered lead capture
   - Data validation and CSV storage
   - Automatic email notifications

2. **Appointment Scheduler**
   - Daily cron-based scheduling
   - Appointment reminder system
   - Client notification automation

3. **Customer Follow-up Assistant**
   - Post-service survey automation
   - Customer satisfaction tracking
   - Feedback collection and analysis

4. **Invoice Generator**
   - Monthly automated invoice creation
   - Contract-based billing
   - Email delivery system

## 📈 Analytics & Reporting

- **Workflow Execution Trends**: Track automation performance over time
- **Success Rates**: Monitor workflow reliability
- **Performance Metrics**: Analyze execution duration and efficiency
- **Records Processed**: Track data processing volumes

## 🔐 Security Features

- Session-based authentication
- Secure file handling
- Data validation and sanitization
- Error handling and logging

## 🚀 Deployment

### Local Development
```bash
streamlit run app.py --server.port=8501
```

### Production Deployment
The platform can be deployed to:
- Streamlit Cloud
- Heroku
- AWS/GCP/Azure
- Docker containers

## 📞 Support

For technical support or questions about Meticulous Quality's AI automation services:
- Website: https://meticulousquality.com/
- Email: support@meticulousquality.com

## 📄 License

© 2025 Meticulous Quality. All rights reserved.

---

**Built with AI & Automation for Cleaning Business CEOs**

