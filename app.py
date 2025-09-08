import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import os
import sys

# Add pages to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'pages'))
from n8n_workflows import n8n_workflows_page

# Page configuration
st.set_page_config(
    page_title="Meticulous Quality - AI Automation Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Meticulous Quality branding
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;500;600&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
    }
    
    .css-1d391kg {
        background: linear-gradient(180deg, #1a1a1a 0%, #2d2d2d 50%, #1a1a1a 100%);
        border-right: 2px solid #FFD700;
    }
    
    .css-17eq0hr {
        background: linear-gradient(180deg, #1a1a1a 0%, #2d2d2d 50%, #1a1a1a 100%);
        color: #FFD700;
        font-family: 'Inter', sans-serif;
    }
    
    .logo-container {
        text-align: center;
        padding: 20px 0;
        border-bottom: 1px solid rgba(255, 215, 0, 0.3);
        margin-bottom: 20px;
    }
    
    .main-header {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 50%, #1a1a1a 100%);
        border: 2px solid rgba(255, 215, 0, 0.3);
        padding: 30px;
        border-radius: 16px;
        color: #FFD700;
        margin-bottom: 30px;
        font-family: 'Playfair Display', serif;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        border: 1px solid rgba(255, 215, 0, 0.3);
        padding: 20px;
        border-radius: 12px;
        color: #FFD700;
        margin: 15px 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(255, 215, 0, 0.2);
        border-color: #FFD700;
    }
    
    .nav-button {
        background: linear-gradient(135deg, rgba(255, 215, 0, 0.1) 0%, rgba(255, 215, 0, 0.05) 100%);
        border: 1px solid rgba(255, 215, 0, 0.3);
        border-radius: 12px;
        padding: 12px 16px;
        margin: 8px 0;
        color: #FFD700;
        text-decoration: none;
        display: block;
        transition: all 0.4s ease;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
    }
    
    .nav-button:hover {
        background: linear-gradient(135deg, rgba(255, 215, 0, 0.2) 0%, rgba(255, 215, 0, 0.1) 100%);
        border-color: #FFD700;
        transform: translateX(8px);
    }
    
    .nav-button.active {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
        border-color: #FFD700;
        color: #1a1a1a;
        font-weight: 600;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

def create_sidebar():
    """Create sidebar with navigation"""
    with st.sidebar:
        # Logo
        st.markdown("""
        <div class="logo-container">
            <h2 style="color: #FFD700; font-family: 'Playfair Display', serif; margin: 0;">
                🤖 Meticulous Quality
            </h2>
            <p style="color: rgba(255, 215, 0, 0.8); font-size: 0.9rem; margin: 5px 0 0 0;">
                AI Automation for Cleaning CEOs
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation
        st.markdown("### 🧭 Navigation")
        
        # Page selection
        page = st.selectbox(
            "Select Page",
            ["🏠 Dashboard", "📊 Business Analytics", "🤖 AI Automation", "👥 Client Management", "📈 Growth Metrics", "🔄 N8N Workflows", "⚙️ Settings"],
            key="page_selector"
        )
        
        # Quick Stats
        st.markdown("### 📊 Quick Stats")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Active Clients", "47", "+5")
        with col2:
            st.metric("Revenue Growth", "300%", "+25%")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("AI Automations", "156", "+12")
        with col2:
            st.metric("Time Saved", "2,400hrs", "+180hrs")
        
        # Settings
        st.markdown("### ⚙️ Settings")
        auto_refresh = st.checkbox("Auto-refresh data", value=True)
        refresh_interval = st.slider("Refresh interval (minutes)", 1, 30, 5)
        
        # Footer
        st.markdown("""
        <div style="text-align: center; padding: 20px 0; color: rgba(255, 215, 0, 0.7); 
                    font-size: 0.85rem; border-top: 1px solid rgba(255, 215, 0, 0.2); margin-top: 20px;">
            Built with AI & Automation<br>
            © 2025 Meticulous Quality
        </div>
        """, unsafe_allow_html=True)
        
        return page

def dashboard_page():
    """Main dashboard page"""
    st.markdown("""
    <div class="main-header">
        <h1>🤖 AI Automation Dashboard</h1>
        <p>Transform your cleaning business with intelligent automation systems</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>🎯 Lead Generation</h3>
            <h2>847</h2>
            <p>New leads this month<br><span style="color: #90EE90;">+23% vs last month</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>💰 Revenue Increase</h3>
            <h2>300%</h2>
            <p>Average client growth<br><span style="color: #90EE90;">Triple your sales</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>⏰ Time Savings</h3>
            <h2>75%</h2>
            <p>Operations automation<br><span style="color: #90EE90;">24/7 efficiency</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>🔄 Retention Rate</h3>
            <h2>90%</h2>
            <p>Customer retention<br><span style="color: #90EE90;">AI-powered service</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Monthly Revenue Growth")
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        revenue = [50000, 75000, 120000, 180000, 250000, 350000]
        
        fig = px.line(x=months, y=revenue, title="Revenue Growth Trajectory")
        fig.update_traces(line_color='#FFD700', line_width=3)
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='#FFD700'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🤖 AI Automation Impact")
        categories = ['Lead Gen', 'Scheduling', 'Follow-ups', 'Billing', 'Reports']
        automation_rates = [95, 88, 92, 85, 90]
        
        fig = px.bar(x=categories, y=automation_rates, title="Automation Efficiency by Category")
        fig.update_traces(marker_color='#FFD700')
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='#FFD700'
        )
        st.plotly_chart(fig, use_container_width=True)

def business_analytics_page():
    """Business analytics page"""
    st.markdown("""
    <div class="main-header">
        <h1>📊 Business Analytics</h1>
        <p>Deep insights into your cleaning business performance</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Client Performance Metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🏢 Client Distribution")
        client_types = ['Residential', 'Commercial', 'Industrial']
        client_counts = [25, 15, 7]
        
        fig = px.pie(values=client_counts, names=client_types, title="Client Type Distribution")
        fig.update_traces(marker_colors=['#FFD700', '#FFA500', '#FF8C00'])
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='#FFD700'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("💼 Service Categories")
        services = ['Regular Cleaning', 'Deep Cleaning', 'Carpet Cleaning', 'Window Cleaning']
        bookings = [120, 45, 30, 25]
        
        fig = px.bar(x=services, y=bookings, title="Monthly Service Bookings")
        fig.update_traces(marker_color='#FFD700')
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='#FFD700',
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        st.subheader("📅 Weekly Performance")
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        efficiency = [85, 92, 88, 95, 90, 78, 65]
        
        fig = px.line(x=days, y=efficiency, title="Weekly Efficiency Trends")
        fig.update_traces(line_color='#FFD700', line_width=3)
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='#FFD700'
        )
        st.plotly_chart(fig, use_container_width=True)

def ai_automation_page():
    """AI automation management page"""
    st.markdown("""
    <div class="main-header">
        <h1>🤖 AI Automation Center</h1>
        <p>Manage and monitor your AI automation systems</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Automation Status
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🔄 Active Automations")
        
        automations = [
            {"name": "Lead Generation Bot", "status": "Active", "leads_today": 23, "efficiency": 95},
            {"name": "Appointment Scheduler", "status": "Active", "bookings_today": 18, "efficiency": 88},
            {"name": "Follow-up Assistant", "status": "Active", "follow_ups": 45, "efficiency": 92},
            {"name": "Invoice Generator", "status": "Active", "invoices": 12, "efficiency": 98},
            {"name": "Customer Support Bot", "status": "Active", "tickets": 8, "efficiency": 85}
        ]
        
        for automation in automations:
            st.markdown(f"""
            <div class="metric-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h4>{automation['name']}</h4>
                        <p>Status: <span style="color: #90EE90;">{automation['status']}</span></p>
                    </div>
                    <div style="text-align: right;">
                        <h3>{automation['efficiency']}%</h3>
                        <p>Efficiency</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("⚡ Quick Actions")
        
        if st.button("🚀 Deploy New Bot", use_container_width=True):
            st.success("New automation bot deployment initiated!")
        
        if st.button("📊 Generate Report", use_container_width=True):
            st.success("Automation performance report generated!")
        
        if st.button("🔧 System Maintenance", use_container_width=True):
            st.info("System maintenance scheduled!")
        
        if st.button("📞 AI Phone Assistant", use_container_width=True):
            st.success("AI phone assistant activated!")

def client_management_page():
    """Client management page"""
    st.markdown("""
    <div class="main-header">
        <h1>👥 Client Management</h1>
        <p>Manage your cleaning business clients and relationships</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Client Overview
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Clients", "47", "+5 this month")
    with col2:
        st.metric("Active Contracts", "42", "+3 this month")
    with col3:
        st.metric("Avg Contract Value", "$2,850", "+$450")
    
    # Client List
    st.subheader("📋 Client Portfolio")
    
    clients_data = {
        'Client Name': ['ABC Office Complex', 'Downtown Restaurant', 'Medical Center', 'Retail Store Chain', 'Manufacturing Plant'],
        'Type': ['Commercial', 'Commercial', 'Healthcare', 'Retail', 'Industrial'],
        'Monthly Value': ['$3,500', '$2,200', '$4,800', '$6,200', '$8,500'],
        'Contract Status': ['Active', 'Active', 'Active', 'Renewal', 'Active'],
        'AI Automation': ['Full', 'Partial', 'Full', 'Full', 'Custom'],
        'Satisfaction': [98, 95, 99, 92, 96]
    }
    
    df = pd.DataFrame(clients_data)
    st.dataframe(df, use_container_width=True)
    
    # Client Satisfaction Chart
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("😊 Client Satisfaction Scores")
        fig = px.bar(df, x='Client Name', y='Satisfaction', title="Client Satisfaction Ratings")
        fig.update_traces(marker_color='#FFD700')
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='#FFD700',
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("💰 Revenue by Client Type")
        type_revenue = {'Commercial': 45000, 'Healthcare': 28000, 'Industrial': 35000, 'Retail': 22000}
        
        fig = px.pie(values=list(type_revenue.values()), names=list(type_revenue.keys()), 
                     title="Revenue Distribution by Client Type")
        fig.update_traces(marker_colors=['#FFD700', '#FFA500', '#FF8C00', '#FFB347'])
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='#FFD700'
        )
        st.plotly_chart(fig, use_container_width=True)

def growth_metrics_page():
    """Growth metrics and forecasting page"""
    st.markdown("""
    <div class="main-header">
        <h1>📈 Growth Metrics</h1>
        <p>Track your business growth and AI automation ROI</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Growth KPIs
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Monthly Recurring Revenue", "$127,500", "+$23,400")
    with col2:
        st.metric("Customer Acquisition Cost", "$145", "-$35")
    with col3:
        st.metric("Lifetime Value", "$8,450", "+$1,200")
    with col4:
        st.metric("Churn Rate", "2.1%", "-0.8%")
    
    # Growth Projections
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Revenue Projection")
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        actual = [50000, 75000, 120000, 180000, 250000, 350000, None, None, None, None, None, None]
        projected = [None, None, None, None, None, 350000, 425000, 510000, 615000, 740000, 890000, 1070000]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=months[:6], y=actual[:6], mode='lines+markers', 
                                name='Actual Revenue', line=dict(color='#FFD700', width=3)))
        fig.add_trace(go.Scatter(x=months[5:], y=projected[5:], mode='lines+markers', 
                                name='Projected Revenue', line=dict(color='#FFA500', width=3, dash='dash')))
        
        fig.update_layout(
            title="Revenue Growth Trajectory",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='#FFD700'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🎯 AI ROI Analysis")
        categories = ['Lead Generation', 'Scheduling', 'Customer Service', 'Billing', 'Marketing']
        roi_values = [450, 320, 280, 380, 290]
        
        fig = px.bar(x=categories, y=roi_values, title="AI Automation ROI by Category (%)")
        fig.update_traces(marker_color='#FFD700')
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='#FFD700',
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig, use_container_width=True)

def settings_page():
    """Settings and configuration page"""
    st.markdown("""
    <div class="main-header">
        <h1>⚙️ Settings & Configuration</h1>
        <p>Configure your AI automation platform settings</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🤖 AI Configuration")
        
        ai_aggressiveness = st.slider("AI Lead Generation Aggressiveness", 1, 10, 7)
        auto_follow_up = st.checkbox("Automatic Follow-up Messages", value=True)
        ai_scheduling = st.checkbox("AI-Powered Scheduling", value=True)
        smart_pricing = st.checkbox("Dynamic Pricing AI", value=False)
        
        st.subheader("📊 Dashboard Settings")
        
        refresh_rate = st.selectbox("Data Refresh Rate", ["Real-time", "Every 5 minutes", "Every 15 minutes", "Hourly"])
        chart_theme = st.selectbox("Chart Theme", ["Dark Gold", "Light", "High Contrast"])
        notifications = st.checkbox("Push Notifications", value=True)
    
    with col2:
        st.subheader("🔐 Security Settings")
        
        two_factor = st.checkbox("Two-Factor Authentication", value=True)
        api_access = st.checkbox("API Access Enabled", value=False)
        data_backup = st.selectbox("Data Backup Frequency", ["Daily", "Weekly", "Monthly"])
        
        st.subheader("📞 Communication Settings")
        
        phone_integration = st.checkbox("AI Phone Assistant", value=True)
        email_automation = st.checkbox("Email Automation", value=True)
        sms_notifications = st.checkbox("SMS Notifications", value=True)
        
        if st.button("💾 Save Settings", use_container_width=True):
            st.success("Settings saved successfully!")

def main():
    """Main application function"""
    # Create sidebar and get selected page
    selected_page = create_sidebar()
    
    # Route to appropriate page
    if selected_page == "🏠 Dashboard":
        dashboard_page()
    elif selected_page == "📊 Business Analytics":
        business_analytics_page()
    elif selected_page == "🤖 AI Automation":
        ai_automation_page()
    elif selected_page == "👥 Client Management":
        client_management_page()
    elif selected_page == "📈 Growth Metrics":
        growth_metrics_page()
    elif selected_page == "🔄 N8N Workflows":
        n8n_workflows_page()
    elif selected_page == "⚙️ Settings":
        settings_page()

if __name__ == "__main__":
    main()

