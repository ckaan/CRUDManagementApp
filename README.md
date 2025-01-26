# CRUDManagementApp

##### THIS PROJECT IS STILL ON GOING ##### 
Desktop Building Management App with PyQt6

👥 Developers:
@ckaan - Caner Kaan Balseven

Disclaimers:
#### This project was initially based on concepts from SENG265 at University of Victoria but has been heavily modified and expanded to serve as a robust building management system in real world. ####

#### The project is published for recruitment purposes, this project is not a open source!, all rights reserved by Lutin Software Solutions 2025 ####

📌Summary
This project automates financial and tenant management for building managers, ensuring accurate, transparent, and efficient bookkeeping. With planned features like database support, automated alerts, and web access, it aims to be a complete solution for property management.

🏢 Transparent Pro Management – Building Management System


📌 Problem Statement
Managing buildings requires careful tracking of financial records, household information, debts, and transactions. Traditional methods, such as spreadsheets or manual bookkeeping, are inefficient, error-prone, and time-consuming.


Building managers often struggle with:

Tracking payments & debts (who owes what, payment deadlines).
Managing income & expenses (budgeting for maintenance, collecting rent).
Organizing household records (owner/tenant details, SIN, tax information).
Handling bank transactions & financial statements.
Generating reports & audits to maintain transparency.
This project aims to provide a centralized, automated, and easy-to-use software solution that simplifies these tasks.

🎯 Project Goal
The Transparent Pro Management – Building Management System is designed to streamline financial and household record management for residential and commercial buildings. It ensures that all data is securely stored, accessible, and well-organized, reducing the manual workload for property managers.

✅ Objectives

📊 Expense & Income Management
Track expenses for building maintenance, utilities, and services.
Log all income sources (e.g., rent, parking fees, other revenues).
Generate financial summaries for better decision-making.

🏠 Household & Unit Management
Store resident information (household number, tenant details, tax info).
Record vehicle plates, work details, and contact info for each unit.
Maintain a searchable database for quick access to household data.

💳 Financial Tracking & Banking
Log transactions with banks, landlords, and tenants.
Maintain an automated record of payments, debts, and due balances.
Provide insights into overdue payments.

📜 Reporting & Data Transparency
Generate audit reports, turnover reports, and account statements.
Allow landlords/owners to monitor financial health easily.
Offer printable and exportable reports.

🛠️ User-Friendly Interface & Automation
Simple GUI for quick navigation.
Dropdown selection for buildings, households, and accounts.
Auto-save & validation to prevent data loss or incorrect entries.

🚧 Constraints 

📂 Data Persistence & Storage
Ensure secure file storage (JSON-based persistence).
Prevent data duplication or corruption when switching buildings.
Maintain backward compatibility for older records.

🔄 Multi-Building Management
Support multiple buildings, each with unique financial records.
Keep track of transactions without mix-ups between properties.

⚡ Performance & Scalability
Optimize data handling for fast retrieval (efficient queries).
Prevent lagging UI when handling large transaction records.

🔒 Security & Access Control
Implement user authentication to restrict access.
Prevent unauthorized modifications to financial data.
Encrypt sensitive information like SIN and tax numbers.

📊 Usability & Report Generation
Provide export options (CSV, PDF) for financial reports.
Ensure consistent layouts across different views/pages.

💻 Tech Stack
The project is built using:

🖥️ Python & PySide6 (Qt) → GUI
📂 JSON File Storage → Data persistence
🛠️ Object-Oriented Design → Controllers, DAOs, Entities
⚡ Logging & Debugging → Error handling & system logs
🔄 Unit Testing

📌 Features Breakdown
1️⃣ Dashboard
Overview of current finances, tenants, and payments.
Quick-access buttons to major functions.
2️⃣ Household Management
Add/Edit/Delete household records.
Store detailed unit information (names, SIN, work details, etc.).
3️⃣ Expense & Income Tracking
Log income from rent, parking, other sources.
Track expenses for maintenance, utilities, and repairs.
4️⃣ Bank Management
Register bank accounts linked to tenants or building accounts.
Keep track of transactions, loans, and payments.
5️⃣ Reports & Logs
Generate audit trails & balance reports.
Export financial statements in CSV or PDF format.


🛠️ Future Improvements
✅ Database Integration (SQLite/MySQL) instead of JSON storage.
✅ Role-Based Access Control (RBAC) for different user levels.
✅ Automated Payment Reminders & Notifications via email/SMS.
✅ Mobile App Companion for on-the-go access.



















