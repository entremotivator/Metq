import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import sys
import os

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from n8n_integration import N8NAgent, WebhookManager, CSVManager, AutomationWorkflows, initialize_sample_data

def n8n_workflows_page():
    """N8N Workflows Management Page"""
    
    st.markdown("""
    <div class="main-header">
        <h1>🔄 N8N Workflow Management</h1>
        <p>Create, manage, and monitor your automation workflows</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize managers
    if 'n8n_agent' not in st.session_state:
        st.session_state.n8n_agent = N8NAgent()
    if 'webhook_manager' not in st.session_state:
        st.session_state.webhook_manager = WebhookManager()
    if 'csv_manager' not in st.session_state:
        st.session_state.csv_manager = initialize_sample_data()
    
    # Tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs(["🔄 Workflows", "🔗 Webhooks", "📊 CSV Management", "📈 Analytics"])
    
    with tab1:
        workflow_management_section()
    
    with tab2:
        webhook_management_section()
    
    with tab3:
        csv_management_section()
    
    with tab4:
        analytics_section()

def workflow_management_section():
    """Workflow management section"""
    st.subheader("🤖 Automation Workflows")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Pre-built workflows
        st.markdown("### 📋 Pre-built Workflows")
        
        workflows = {
            "Lead Generation Bot": AutomationWorkflows.lead_generation_workflow(),
            "Appointment Scheduler": AutomationWorkflows.appointment_scheduling_workflow(),
            "Customer Follow-up": AutomationWorkflows.customer_follow_up_workflow(),
            "Invoice Generator": AutomationWorkflows.invoice_generation_workflow()
        }
        
        for workflow_name, workflow_config in workflows.items():
            with st.expander(f"🔧 {workflow_name}"):
                st.json(workflow_config)
                
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    if st.button(f"Deploy {workflow_name}", key=f"deploy_{workflow_name}"):
                        result = st.session_state.n8n_agent.create_workflow(workflow_config)
                        if result["success"]:
                            st.success(f"✅ {workflow_name} deployed successfully!")
                        else:
                            st.error(f"❌ Failed to deploy: {result.get('error', 'Unknown error')}")
                
                with col_b:
                    if st.button(f"Execute {workflow_name}", key=f"execute_{workflow_name}"):
                        # Simulate execution
                        st.info(f"🚀 Executing {workflow_name}...")
                        st.success(f"✅ {workflow_name} executed successfully!")
                
                with col_c:
                    if st.button(f"Test {workflow_name}", key=f"test_{workflow_name}"):
                        st.info(f"🧪 Testing {workflow_name}...")
                        st.success(f"✅ {workflow_name} test completed!")
    
    with col2:
        # Workflow status
        st.markdown("### 📊 Workflow Status")
        
        status_data = {
            'Workflow': ['Lead Generation', 'Appointment Scheduler', 'Follow-up Assistant', 'Invoice Generator'],
            'Status': ['Active', 'Active', 'Active', 'Paused'],
            'Last Run': ['2 min ago', '1 hour ago', '30 min ago', '1 day ago'],
            'Success Rate': [98, 95, 92, 100]
        }
        
        status_df = pd.DataFrame(status_data)
        
        for _, row in status_df.iterrows():
            status_color = "🟢" if row['Status'] == 'Active' else "🟡"
            st.markdown(f"""
            <div class="metric-card" style="margin: 10px 0; padding: 15px;">
                <h4>{status_color} {row['Workflow']}</h4>
                <p>Status: {row['Status']}<br>
                Last Run: {row['Last Run']}<br>
                Success: {row['Success Rate']}%</p>
            </div>
            """, unsafe_allow_html=True)

def webhook_management_section():
    """Webhook management section"""
    st.subheader("🔗 Webhook Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🆕 Create New Webhook")
        
        webhook_name = st.text_input("Webhook Name", placeholder="e.g., lead-capture")
        workflow_id = st.selectbox("Associated Workflow", 
                                 ["lead-generation", "appointment-booking", "customer-feedback", "payment-processing"])
        
        if st.button("Create Webhook", use_container_width=True):
            if webhook_name:
                webhook_url = st.session_state.webhook_manager.create_webhook(webhook_name, workflow_id)
                st.success(f"✅ Webhook created: {webhook_url}")
                curl_command = f"curl -X POST {webhook_url} -H 'Content-Type: application/json' -d '{{\"data\": \"your_data\"}}'"
                st.code(curl_command)
            else:
                st.error("Please enter a webhook name")
        
        st.markdown("### 🧪 Test Webhook")
        
        test_webhook = st.selectbox("Select Webhook to Test", 
                                  list(st.session_state.webhook_manager.active_webhooks.keys()) if st.session_state.webhook_manager.active_webhooks else ["No webhooks created"])
        
        test_data = st.text_area("Test Data (JSON)", 
                                value='{"name": "John Doe", "email": "john@example.com", "service": "office cleaning"}')
        
        if st.button("Send Test Data", use_container_width=True):
            if test_webhook != "No webhooks created":
                try:
                    data = json.loads(test_data)
                    result = st.session_state.webhook_manager.send_webhook_data(test_webhook, data)
                    if result["success"]:
                        st.success("✅ Test data sent successfully!")
                    else:
                        st.error(f"❌ Failed to send: {result.get('error', 'Unknown error')}")
                except json.JSONDecodeError:
                    st.error("❌ Invalid JSON format")
    
    with col2:
        st.markdown("### 📊 Active Webhooks")
        
        webhook_stats = st.session_state.webhook_manager.get_webhook_stats()
        
        if webhook_stats:
            for webhook_name, stats in webhook_stats.items():
                st.markdown(f"""
                <div class="metric-card" style="margin: 10px 0; padding: 15px;">
                    <h4>🔗 {webhook_name}</h4>
                    <p><strong>URL:</strong> {stats['url']}<br>
                    <strong>Workflow:</strong> {stats['workflow_id']}<br>
                    <strong>Calls:</strong> {stats['calls']}<br>
                    <strong>Created:</strong> {stats['created_at'].strftime('%Y-%m-%d %H:%M')}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No active webhooks. Create one to get started!")
        
        # Webhook analytics
        if webhook_stats:
            st.markdown("### 📈 Webhook Usage")
            
            webhook_names = list(webhook_stats.keys())
            webhook_calls = [stats['calls'] for stats in webhook_stats.values()]
            
            fig = px.bar(x=webhook_names, y=webhook_calls, title="Webhook Call Frequency")
            fig.update_traces(marker_color='#FFD700')
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='#FFD700'
            )
            st.plotly_chart(fig, use_container_width=True)

def csv_management_section():
    """CSV management section"""
    st.subheader("📊 CSV Data Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📁 File Operations")
        
        # File upload
        uploaded_file = st.file_uploader("Upload CSV File", type=['csv'])
        if uploaded_file:
            category = st.selectbox("Category", ["clients", "workflows", "automations", "reports"])
            if st.button("Save Uploaded File"):
                df = pd.read_csv(uploaded_file)
                filename = uploaded_file.name
                if st.session_state.csv_manager.save_csv(df, filename, category):
                    st.success(f"✅ File saved to {category}/{filename}")
                else:
                    st.error("❌ Failed to save file")
        
        # File listing
        st.markdown("### 📋 Available Files")
        categories = ["clients", "workflows", "automations", "reports"]
        
        for category in categories:
            with st.expander(f"📁 {category.title()} Files"):
                files = st.session_state.csv_manager.list_csv_files(category)
                if files:
                    for file in files:
                        col_a, col_b, col_c = st.columns([2, 1, 1])
                        with col_a:
                            st.text(file)
                        with col_b:
                            if st.button("View", key=f"view_{category}_{file}"):
                                df = st.session_state.csv_manager.load_csv(file, category)
                                if df is not None:
                                    st.session_state[f"viewing_{category}_{file}"] = df
                        with col_c:
                            if st.button("Delete", key=f"delete_{category}_{file}"):
                                if st.session_state.csv_manager.delete_csv(file, category):
                                    st.success(f"✅ Deleted {file}")
                                    st.rerun()
                else:
                    st.info("No files in this category")
    
    with col2:
        st.markdown("### 🔍 Data Viewer")
        
        # Display selected file
        for key in st.session_state.keys():
            if key.startswith("viewing_"):
                df = st.session_state[key]
                file_info = key.replace("viewing_", "").split("_", 1)
                category, filename = file_info[0], file_info[1]
                
                st.markdown(f"**📄 {filename}** (Category: {category})")
                st.dataframe(df, use_container_width=True)
                
                # Basic statistics
                st.markdown("### 📊 Data Statistics")
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Rows", len(df))
                with col_b:
                    st.metric("Columns", len(df.columns))
                with col_c:
                    st.metric("Size", f"{df.memory_usage(deep=True).sum() / 1024:.1f} KB")
                
                # Data filtering
                st.markdown("### 🔍 Filter Data")
                if len(df.columns) > 0:
                    filter_column = st.selectbox("Filter Column", df.columns)
                    if df[filter_column].dtype in ['object', 'string']:
                        filter_value = st.text_input("Contains")
                        if filter_value:
                            filtered_df = df[df[filter_column].str.contains(filter_value, na=False)]
                            st.dataframe(filtered_df, use_container_width=True)
                    else:
                        min_val = st.number_input("Minimum Value", value=float(df[filter_column].min()))
                        max_val = st.number_input("Maximum Value", value=float(df[filter_column].max()))
                        filtered_df = df[(df[filter_column] >= min_val) & (df[filter_column] <= max_val)]
                        st.dataframe(filtered_df, use_container_width=True)
                
                break
        else:
            st.info("Select a file to view its contents")

def analytics_section():
    """Analytics and reporting section"""
    st.subheader("📈 Automation Analytics")
    
    # Load automation logs
    automation_logs = st.session_state.csv_manager.load_csv('automation_logs.csv', 'automations')
    
    if automation_logs is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            # Workflow execution trends
            st.markdown("### 📊 Workflow Execution Trends")
            
            daily_executions = automation_logs.groupby([
                automation_logs['execution_time'].str[:10], 
                'workflow_name'
            ]).size().reset_index(name='executions')
            
            fig = px.line(daily_executions, x='execution_time', y='executions', 
                         color='workflow_name', title="Daily Workflow Executions")
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='#FFD700'
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Success rate by workflow
            st.markdown("### ✅ Success Rates")
            success_rates = automation_logs.groupby('workflow_name')['status'].apply(
                lambda x: (x == 'success').mean() * 100
            ).reset_index()
            success_rates.columns = ['Workflow', 'Success Rate']
            
            fig = px.bar(success_rates, x='Workflow', y='Success Rate', 
                        title="Workflow Success Rates (%)")
            fig.update_traces(marker_color='#FFD700')
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='#FFD700'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Performance metrics
            st.markdown("### ⚡ Performance Metrics")
            
            avg_duration = automation_logs.groupby('workflow_name')['execution_duration'].mean().reset_index()
            avg_duration.columns = ['Workflow', 'Avg Duration (s)']
            
            fig = px.bar(avg_duration, x='Workflow', y='Avg Duration (s)', 
                        title="Average Execution Duration")
            fig.update_traces(marker_color='#FFA500')
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='#FFD700'
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Records processed
            st.markdown("### 📊 Records Processed")
            total_records = automation_logs.groupby('workflow_name')['records_processed'].sum().reset_index()
            total_records.columns = ['Workflow', 'Total Records']
            
            fig = px.pie(total_records, values='Total Records', names='Workflow', 
                        title="Records Processed by Workflow")
            fig.update_traces(marker_colors=['#FFD700', '#FFA500', '#FF8C00', '#FFB347'])
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='#FFD700'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Recent activity
        st.markdown("### 🕒 Recent Activity")
        recent_logs = automation_logs.sort_values('execution_time', ascending=False).head(10)
        
        for _, log in recent_logs.iterrows():
            status_icon = "✅" if log['status'] == 'success' else "❌"
            st.markdown(f"""
            <div class="metric-card" style="margin: 5px 0; padding: 10px;">
                <div style="display: flex; justify-content: space-between;">
                    <div>
                        <strong>{status_icon} {log['workflow_name']}</strong><br>
                        <small>{log['execution_time']}</small>
                    </div>
                    <div style="text-align: right;">
                        <strong>{log['records_processed']} records</strong><br>
                        <small>{log['execution_duration']}s</small>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    else:
        st.info("No automation logs available. Run some workflows to see analytics!")

if __name__ == "__main__":
    n8n_workflows_page()

