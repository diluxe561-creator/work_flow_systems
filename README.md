# PROFESSIONAL PRODUCTIVITY & BILLING SUITE

A comprehensive Python CLI tool designed for freelancers to organize their business structure. Unlike basic trackers, this suite creates a linked hierarchy between your professional profile, multiple clients, and specific project folders.

---

## 🚀 KEY FEATURES
- Profile Identity: Set up a permanent business persona with billing details.
- Hierarchical Tracking: Link work logs to specific Projects, which are linked to specific Clients.
- Advanced Invoice Formatting: Generates high-contrast, professional PDF invoices with categorized headers.
- Automated Math: Handles all sub-totals and grand-total calculations across multiple project logs.

---

## 🛠️ INSTALLATION

1. Ensure Python 3.x is installed.
2. Install the necessary data and PDF libraries:
   pip install pandas fpdf

3. Run the script:
   python productivity_suite.py

---

## 📊 DATA ARCHITECTURE



The suite organizes data in four logical layers:
1. FREELANCER: Your business name and contact info.
2. CLIENTS: A registry of companies you work with.
3. PROJECTS: Specific engagements (e.g., "Q1 Social Media" or "Web Rebuild").
4. LOGS: The individual tasks, hours, and rates that make up an invoice.

---

## 🖥️ WORKFLOW

1. [Setup Profile]: Enter your info (only needs to be done once).
2. [Record New Client]: Assign a Client ID (like 'C1').
3. [Create Project]: Assign a Project ID (like 'P1') to a Client ID.
4. [Record Work]: Log tasks using the Project ID.
5. [Generate Invoice]: Enter a Client ID to automatically pull all related project logs into one PDF.

---

## 📁 FILE OUTPUTS
- Invoice_[ClientName].pdf  # Professional billing document for your clients.

---

## 📝 REQUIREMENTS
- Python 3.x
- pandas
- fpdf

---

Turn your daily tasks into professional revenue tracking.
