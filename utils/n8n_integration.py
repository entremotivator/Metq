import requests
import json
import pandas as pd
from datetime import datetime
import streamlit as st
import os
from typing import Dict, List, Any, Optional

class N8NAgent:
    """N8N Workflow Agent for automation management"""
    
    def __init__(self, base_url: str = "http://localhost:5678", api_key: str = None):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            'Content-Type': 'application/json',
            'X-N8N-API-KEY': api_key if api_key else 'demo-api-key'
        }
    
    def create_workflow(self, workflow_data: Dict) -> Dict:
        """Create a new n8n workflow"""
        try:
            response = requests.post(
                f"{self.base_url}/api/v1/workflows",
                headers=self.headers,
                json=workflow_data
            )
            return {"success": True, "data": response.json()}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def execute_workflow(self, workflow_id: str, input_data: Dict = None) -> Dict:
        """Execute an n8n workflow"""
        try:
            payload = {"input": input_data} if input_data else {}
            response = requests.post(
                f"{self.base_url}/api/v1/workflows/{workflow_id}/execute",
                headers=self.headers,
                json=payload
            )
            return {"success": True, "data": response.json()}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_workflow_status(self, execution_id: str) -> Dict:
        """Get workflow execution status"""
        try:
            response = requests.get(
                f"{self.base_url}/api/v1/executions/{execution_id}",
                headers=self.headers
            )
            return {"success": True, "data": response.json()}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def list_workflows(self) -> Dict:
        """List all available workflows"""
        try:
            response = requests.get(
                f"{self.base_url}/api/v1/workflows",
                headers=self.headers
            )
            return {"success": True, "data": response.json()}
        except Exception as e:
            return {"success": False, "error": str(e)}

class WebhookManager:
    """Webhook management for n8n integration"""
    
    def __init__(self, webhook_base_url: str = "http://localhost:5678/webhook"):
        self.webhook_base_url = webhook_base_url
        self.active_webhooks = {}
    
    def create_webhook(self, webhook_name: str, workflow_id: str) -> str:
        """Create a webhook endpoint"""
        webhook_url = f"{self.webhook_base_url}/{webhook_name}"
        self.active_webhooks[webhook_name] = {
            "url": webhook_url,
            "workflow_id": workflow_id,
            "created_at": datetime.now(),
            "calls": 0
        }
        return webhook_url
    
    def send_webhook_data(self, webhook_name: str, data: Dict) -> Dict:
        """Send data to a webhook"""
        if webhook_name not in self.active_webhooks:
            return {"success": False, "error": "Webhook not found"}
        
        try:
            webhook_url = self.active_webhooks[webhook_name]["url"]
            response = requests.post(webhook_url, json=data)
            self.active_webhooks[webhook_name]["calls"] += 1
            return {"success": True, "response": response.json()}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_webhook_stats(self) -> Dict:
        """Get webhook statistics"""
        return self.active_webhooks

class CSVManager:
    """Comprehensive CSV data management system"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.ensure_data_directory()
    
    def ensure_data_directory(self):
        """Ensure data directory exists"""
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(f"{self.data_dir}/clients", exist_ok=True)
        os.makedirs(f"{self.data_dir}/workflows", exist_ok=True)
        os.makedirs(f"{self.data_dir}/automations", exist_ok=True)
        os.makedirs(f"{self.data_dir}/reports", exist_ok=True)
    
    def save_csv(self, data: pd.DataFrame, filename: str, category: str = "general") -> bool:
        """Save DataFrame to CSV"""
        try:
            filepath = f"{self.data_dir}/{category}/{filename}"
            data.to_csv(filepath, index=False)
            return True
        except Exception as e:
            st.error(f"Error saving CSV: {str(e)}")
            return False
    
    def load_csv(self, filename: str, category: str = "general") -> Optional[pd.DataFrame]:
        """Load CSV file as DataFrame"""
        try:
            filepath = f"{self.data_dir}/{category}/{filename}"
            if os.path.exists(filepath):
                return pd.read_csv(filepath)
            return None
        except Exception as e:
            st.error(f"Error loading CSV: {str(e)}")
            return None
    
    def list_csv_files(self, category: str = "general") -> List[str]:
        """List all CSV files in a category"""
        try:
            category_path = f"{self.data_dir}/{category}"
            if os.path.exists(category_path):
                return [f for f in os.listdir(category_path) if f.endswith('.csv')]
            return []
        except Exception as e:
            st.error(f"Error listing CSV files: {str(e)}")
            return []
    
    def delete_csv(self, filename: str, category: str = "general") -> bool:
        """Delete a CSV file"""
        try:
            filepath = f"{self.data_dir}/{category}/{filename}"
            if os.path.exists(filepath):
                os.remove(filepath)
                return True
            return False
        except Exception as e:
            st.error(f"Error deleting CSV: {str(e)}")
            return False
    
    def merge_csv_files(self, filenames: List[str], output_filename: str, category: str = "general") -> bool:
        """Merge multiple CSV files"""
        try:
            dataframes = []
            for filename in filenames:
                df = self.load_csv(filename, category)
                if df is not None:
                    dataframes.append(df)
            
            if dataframes:
                merged_df = pd.concat(dataframes, ignore_index=True)
                return self.save_csv(merged_df, output_filename, category)
            return False
        except Exception as e:
            st.error(f"Error merging CSV files: {str(e)}")
            return False
    
    def filter_csv_data(self, filename: str, filters: Dict, category: str = "general") -> Optional[pd.DataFrame]:
        """Filter CSV data based on conditions"""
        try:
            df = self.load_csv(filename, category)
            if df is None:
                return None
            
            for column, condition in filters.items():
                if column in df.columns:
                    if isinstance(condition, dict):
                        if 'min' in condition:
                            df = df[df[column] >= condition['min']]
                        if 'max' in condition:
                            df = df[df[column] <= condition['max']]
                        if 'equals' in condition:
                            df = df[df[column] == condition['equals']]
                        if 'contains' in condition:
                            df = df[df[column].str.contains(condition['contains'], na=False)]
            
            return df
        except Exception as e:
            st.error(f"Error filtering CSV data: {str(e)}")
            return None

class AutomationWorkflows:
    """Pre-built automation workflows for cleaning businesses"""
    
    @staticmethod
    def lead_generation_workflow() -> Dict:
        """Lead generation automation workflow"""
        return {
            "name": "Lead Generation Bot",
            "nodes": [
                {
                    "name": "Webhook Trigger",
                    "type": "n8n-nodes-base.webhook",
                    "parameters": {
                        "path": "lead-generation",
                        "httpMethod": "POST"
                    }
                },
                {
                    "name": "Process Lead Data",
                    "type": "n8n-nodes-base.function",
                    "parameters": {
                        "functionCode": """
                        const leadData = items[0].json;
                        return [{
                            json: {
                                name: leadData.name,
                                email: leadData.email,
                                phone: leadData.phone,
                                service_type: leadData.service_type,
                                lead_source: leadData.lead_source,
                                created_at: new Date().toISOString(),
                                status: 'new'
                            }
                        }];
                        """
                    }
                },
                {
                    "name": "Save to CSV",
                    "type": "n8n-nodes-base.csv",
                    "parameters": {
                        "operation": "write",
                        "fileName": "leads.csv"
                    }
                },
                {
                    "name": "Send Welcome Email",
                    "type": "n8n-nodes-base.emailSend",
                    "parameters": {
                        "subject": "Welcome to Meticulous Quality Cleaning",
                        "text": "Thank you for your interest in our cleaning services!"
                    }
                }
            ]
        }
    
    @staticmethod
    def appointment_scheduling_workflow() -> Dict:
        """Appointment scheduling automation workflow"""
        return {
            "name": "Appointment Scheduler",
            "nodes": [
                {
                    "name": "Schedule Trigger",
                    "type": "n8n-nodes-base.cron",
                    "parameters": {
                        "triggerTimes": {
                            "hour": 9,
                            "minute": 0
                        }
                    }
                },
                {
                    "name": "Load Pending Appointments",
                    "type": "n8n-nodes-base.csv",
                    "parameters": {
                        "operation": "read",
                        "fileName": "appointments.csv"
                    }
                },
                {
                    "name": "Send Reminders",
                    "type": "n8n-nodes-base.function",
                    "parameters": {
                        "functionCode": """
                        const appointments = items[0].json;
                        const tomorrow = new Date();
                        tomorrow.setDate(tomorrow.getDate() + 1);
                        
                        return appointments.filter(apt => 
                            new Date(apt.date).toDateString() === tomorrow.toDateString()
                        ).map(apt => ({
                            json: {
                                client_email: apt.client_email,
                                appointment_time: apt.time,
                                service_type: apt.service_type
                            }
                        }));
                        """
                    }
                }
            ]
        }
    
    @staticmethod
    def customer_follow_up_workflow() -> Dict:
        """Customer follow-up automation workflow"""
        return {
            "name": "Customer Follow-up Assistant",
            "nodes": [
                {
                    "name": "Daily Trigger",
                    "type": "n8n-nodes-base.cron",
                    "parameters": {
                        "triggerTimes": {
                            "hour": 10,
                            "minute": 0
                        }
                    }
                },
                {
                    "name": "Load Completed Services",
                    "type": "n8n-nodes-base.csv",
                    "parameters": {
                        "operation": "read",
                        "fileName": "completed_services.csv"
                    }
                },
                {
                    "name": "Filter Recent Completions",
                    "type": "n8n-nodes-base.function",
                    "parameters": {
                        "functionCode": """
                        const services = items[0].json;
                        const threeDaysAgo = new Date();
                        threeDaysAgo.setDate(threeDaysAgo.getDate() - 3);
                        
                        return services.filter(service => 
                            new Date(service.completed_date) >= threeDaysAgo &&
                            !service.follow_up_sent
                        ).map(service => ({
                            json: service
                        }));
                        """
                    }
                },
                {
                    "name": "Send Follow-up Survey",
                    "type": "n8n-nodes-base.emailSend",
                    "parameters": {
                        "subject": "How was your cleaning service?",
                        "text": "We'd love to hear about your experience!"
                    }
                }
            ]
        }
    
    @staticmethod
    def invoice_generation_workflow() -> Dict:
        """Invoice generation automation workflow"""
        return {
            "name": "Invoice Generator",
            "nodes": [
                {
                    "name": "Monthly Trigger",
                    "type": "n8n-nodes-base.cron",
                    "parameters": {
                        "triggerTimes": {
                            "day": 1,
                            "hour": 8,
                            "minute": 0
                        }
                    }
                },
                {
                    "name": "Load Client Contracts",
                    "type": "n8n-nodes-base.csv",
                    "parameters": {
                        "operation": "read",
                        "fileName": "client_contracts.csv"
                    }
                },
                {
                    "name": "Generate Invoices",
                    "type": "n8n-nodes-base.function",
                    "parameters": {
                        "functionCode": """
                        const contracts = items[0].json;
                        const currentMonth = new Date().getMonth() + 1;
                        
                        return contracts.filter(contract => 
                            contract.billing_cycle === 'monthly' &&
                            contract.status === 'active'
                        ).map(contract => ({
                            json: {
                                client_id: contract.client_id,
                                amount: contract.monthly_amount,
                                due_date: new Date(new Date().setDate(30)).toISOString(),
                                invoice_number: `INV-${Date.now()}-${contract.client_id}`,
                                created_at: new Date().toISOString()
                            }
                        }));
                        """
                    }
                },
                {
                    "name": "Save Invoices",
                    "type": "n8n-nodes-base.csv",
                    "parameters": {
                        "operation": "write",
                        "fileName": "invoices.csv"
                    }
                }
            ]
        }

def initialize_sample_data():
    """Initialize sample CSV data for the system"""
    csv_manager = CSVManager()
    
    # Sample client data
    clients_data = pd.DataFrame({
        'client_id': ['C001', 'C002', 'C003', 'C004', 'C005'],
        'name': ['ABC Office Complex', 'Downtown Restaurant', 'Medical Center', 'Retail Store', 'Manufacturing Plant'],
        'email': ['contact@abcoffice.com', 'manager@downtown.com', 'admin@medcenter.com', 'info@retailstore.com', 'ops@manufacturing.com'],
        'phone': ['555-0101', '555-0102', '555-0103', '555-0104', '555-0105'],
        'service_type': ['Commercial', 'Restaurant', 'Healthcare', 'Retail', 'Industrial'],
        'monthly_amount': [3500, 2200, 4800, 6200, 8500],
        'status': ['active', 'active', 'active', 'renewal', 'active'],
        'created_at': pd.date_range('2024-01-01', periods=5, freq='M')
    })
    csv_manager.save_csv(clients_data, 'clients.csv', 'clients')
    
    # Sample leads data
    leads_data = pd.DataFrame({
        'lead_id': ['L001', 'L002', 'L003', 'L004', 'L005'],
        'name': ['John Smith', 'Sarah Johnson', 'Mike Wilson', 'Lisa Brown', 'David Lee'],
        'email': ['john@email.com', 'sarah@email.com', 'mike@email.com', 'lisa@email.com', 'david@email.com'],
        'phone': ['555-1001', '555-1002', '555-1003', '555-1004', '555-1005'],
        'service_type': ['Residential', 'Commercial', 'Deep Cleaning', 'Carpet Cleaning', 'Window Cleaning'],
        'lead_source': ['Website', 'Referral', 'Google Ads', 'Social Media', 'Cold Call'],
        'status': ['new', 'contacted', 'quoted', 'converted', 'lost'],
        'created_at': pd.date_range('2024-12-01', periods=5, freq='D')
    })
    csv_manager.save_csv(leads_data, 'leads.csv', 'clients')
    
    # Sample automation logs
    automation_logs = pd.DataFrame({
        'log_id': range(1, 11),
        'workflow_name': ['Lead Generation Bot'] * 3 + ['Appointment Scheduler'] * 3 + ['Follow-up Assistant'] * 2 + ['Invoice Generator'] * 2,
        'execution_time': pd.date_range('2024-12-01', periods=10, freq='H'),
        'status': ['success'] * 8 + ['failed', 'success'],
        'records_processed': [5, 3, 7, 12, 8, 15, 6, 4, 0, 25],
        'execution_duration': [2.5, 1.8, 3.2, 4.1, 2.9, 5.5, 1.2, 0.8, 0.0, 8.7]
    })
    csv_manager.save_csv(automation_logs, 'automation_logs.csv', 'automations')
    
    return csv_manager

