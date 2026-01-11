import pandas as pd
from fpdf import FPDF
from datetime import datetime

class ProductivitySuite:
    def __init__(self):
        # Professional Profile (The Freelancer)
        self.freelancer = {}
        self.clients = {}  
        self.projects = [] 
        self.work_logs = [] 

    def setup_freelancer(self):
        print("\n--- 👤 SETUP YOUR PROFILE ---")
        self.freelancer['name'] = input("Your Name/Business Name: ")
        self.freelancer['email'] = input("Your Email: ")
        self.freelancer['address'] = input("Your Address: ")
        print("✅ Profile Setup Complete!")

    def add_client(self):
        print("\n--- ➕ RECORD NEW CLIENT ---")
        cid = input("Enter Client ID (e.g., C1): ")
        name = input("Client Business Name: ")
        email = input("Client Billing Email: ")
        self.clients[cid] = {"name": name, "email": email}
        print(f"✅ Client '{name}' added.")

    def add_project(self):
        print("\n--- 📁 CREATE PROJECT ---")
        print(f"Available Clients: {list(self.clients.keys())}")
        cid = input("Enter Client ID for this project: ")
        if cid not in self.clients:
            print("❌ Client ID not found!")
            return
        pid = input("Enter Project ID (e.g., P1): ")
        name = input("Project Name (e.g., Website Build): ")
        self.projects.append({"project_id": pid, "client_id": cid, "name": name})
        print(f"✅ Project '{name}' recorded.")

    def log_work(self):
        print("\n--- ⏳ RECORD WORK/TASKS ---")
        pid = input("Enter Project ID: ")
        task = input("What did you do? ")
        hours = float(input("Hours worked: "))
        rate = float(input("Hourly rate ($): "))
        
        self.work_logs.append({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "project_id": pid,
            "task": task,
            "hours": hours,
            "rate": rate,
            "total": hours * rate
        })
        print("✅ Work logged successfully.")

    def generate_invoice(self):
        print("\n--- 📄 GENERATE PDF INVOICE ---")
        cid = input("Enter Client ID to bill: ")
        if cid not in self.clients: return
        
        client = self.clients[cid]
        client_projs = [p['project_id'] for p in self.projects if p['client_id'] == cid]
        logs = [log for log in self.work_logs if log['project_id'] in client_projs]

        # PDF Logic
        pdf = FPDF()
        pdf.add_page()
        
        # 1. Header (Freelancer Info)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 8, self.freelancer['name'], ln=True)
        pdf.set_font("Arial", size=10)
        pdf.cell(0, 5, self.freelancer['address'], ln=True)
        pdf.cell(0, 5, self.freelancer['email'], ln=True)
        pdf.ln(10)

        # 2. Bill To
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "BILL TO:", ln=True)
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 6, client['name'], ln=True)
        pdf.cell(0, 6, client['email'], ln=True)
        pdf.ln(10)

        # 3. Table Header
        pdf.set_fill_color(50, 50, 50)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(30, 10, "Date", 1, 0, 'C', True)
        pdf.cell(80, 10, "Project/Task", 1, 0, 'C', True)
        pdf.cell(20, 10, "Hours", 1, 0, 'C', True)
        pdf.cell(30, 10, "Rate", 1, 0, 'C', True)
        pdf.cell(30, 10, "Total", 1, 1, 'C', True)

        # 4. Table Rows
        pdf.set_text_color(0, 0, 0)
        grand_total = 0
        for entry in logs:
            p_name = next(p['name'] for p in self.projects if p['project_id'] == entry['project_id'])
            pdf.cell(30, 10, entry['date'], 1)
            pdf.cell(80, 10, f"{p_name}: {entry['task']}", 1)
            pdf.cell(20, 10, str(entry['hours']), 1, 0, 'C')
            pdf.cell(30, 10, f"${entry['rate']}", 1, 0, 'C')
            pdf.cell(30, 10, f"${entry['total']}", 1, 1, 'C')
            grand_total += entry['total']

        # 5. Grand Total
        pdf.ln(5)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(160, 10, "TOTAL DUE:", 0, 0, 'R')
        pdf.cell(30, 10, f"${grand_total}", 1, 1, 'C')

        filename = f"Invoice_{client['name']}.pdf"
        pdf.output(filename)
        print(f"🚀 SUCCESS! '{filename}' is ready for your client.")

# --- RUNNING THE SUITE ---
suite = ProductivitySuite()
suite.setup_freelancer() # Record you
suite.add_client()       # Record client
suite.add_project()      # Record project
suite.log_work()         # Record work
suite.generate_invoice() # Generate PDF