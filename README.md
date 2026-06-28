# 🚔 Chicago Crime Analytics Platform

<!-- <p align="center">
  <img src="assets/images/logo.png" alt="Chicago Crime Analytics Platform" width="180"/>
</p> -->

<p align="center">
An End-to-End Crime Intelligence & Business Analytics Platform built using
🌐 Live Application

🔗 Streamlit App: https://chicago-crime-analytics-platform.streamlit.app/

📂 GitHub Repository

🔗 Source Code: https://github.com/YedukondaluCheeraboina/chicago-crime-analytics-platform

# 📖 Table of Contents

- Project Overview
- Key Features
- Dashboard Modules
- Technology Stack
- System Architecture
- ETL Workflow
- Project Structure
- Database Design
- Installation Guide
- Configuration
- Running the Application
- Dashboard Walkthrough
- Export Features
- Future Enhancements
- Author
- License

---

# 📌 Project Overview

The **Chicago Crime Analytics Platform** is a comprehensive Business Intelligence and Crime Analytics application developed to analyze historical crime records published by the Chicago Police Department (CPD).

The platform transforms raw crime datasets into interactive dashboards, analytical reports, statistical insights, and downloadable business reports through an end-to-end ETL and visualization pipeline.

Unlike traditional analytical scripts, this platform provides a modern web-based interface built with **Streamlit**, allowing users to explore crime trends, identify hotspots, monitor arrest patterns, and generate professional reports through an intuitive dashboard.

The project demonstrates practical implementation of:

- End-to-End ETL Pipeline
- Data Cleaning & Preprocessing
- Feature Engineering
- MySQL Data Warehouse
- Interactive Business Dashboards
- Statistical Analysis
- Crime Trend Visualization
- PDF, Excel & CSV Reporting
- Modular Streamlit Application Architecture

---

# ✨ Key Features

## 🚔 Interactive Dashboard

- Executive KPI Cards
- Crime Trend Analysis
- Dynamic Filtering
- Business Insights
- Interactive Visualizations

---

## 📊 Crime Analysis

- Crime Category Analysis
- District-wise Crime Analysis
- Community-wise Crime Analysis
- Monthly Crime Distribution
- Crime Hotspot Map
- Executive Insights
- Export Reports

---

## 📈 Statistical Analysis

- Distribution Analysis
- Correlation Analysis
- Outlier Detection
- Hourly Crime Distribution
- Arrest Rate Statistics
- Interactive Statistical Charts

---

## 🗄 MySQL Reports

- Yearly Crime Report
- Crime Category Report
- Arrest Summary Report
- Community Report
- Interactive Report Dashboard
- Export to PDF, Excel & CSV

---

## ℹ️ Project Information

- Project Overview
- Technology Stack
- Architecture
- Module Information
- Developer Information
- Project Status

---

# 🖥 Dashboard Modules

The platform is organized into multiple interactive dashboard modules, each designed to provide specific analytical capabilities.

| Module | Description |
|---------|-------------|
| 🏠 Dashboard | Executive overview with KPIs, yearly trends, arrest statistics and quick insights |
| 🚔 Crime Analysis | Analyze crime categories, districts, communities, monthly trends and hotspot locations |
| 📊 Statistical Analysis | Statistical summaries, distributions, correlations, outlier detection and hypothesis-driven insights |
| 🗄 MySQL Reports | Business reports generated from MySQL summary tables and database views |
| ℹ️ Project Information | Project overview, architecture, technology stack and developer information |

---

# 📸 Dashboard Preview

> **Replace the placeholders below with screenshots after deployment.**

## 🏠 Dashboard

```
assets/screenshots/dashboard.png
```

---

## 🚔 Crime Analysis

```
assets/screenshots/crime_analysis.png
```

---

## 📊 Statistical Analysis

```
assets/screenshots/statistical_analysis.png
```

---

## 🗄 MySQL Reports

```
assets/screenshots/mysql_reports.png
```

---

## ℹ️ Project Information

```
assets/screenshots/project_information.png
```

---

# 🛠 Technology Stack

## Programming Language

- Python 3.13

## Frontend

- Streamlit

## Backend

- Python

## Database

- MySQL

## Data Processing

- Pandas
- NumPy

## Data Visualization

- Plotly
- Matplotlib

## Statistical Analysis

- SciPy
- NumPy

## Database Connectivity

- SQLAlchemy
- PyMySQL
- MySQL Connector

## Report Generation

- ReportLab
- OpenPyXL

---

# 🏗 System Architecture

```text
                    Chicago Crime Dataset
                             │
                             ▼
                     Data Loading Module
                             │
                             ▼
                    Data Cleaning Module
                             │
                             ▼
                 Feature Engineering Module
                             │
                             ▼
                    MySQL Data Warehouse
                             │
            ┌────────────────┼────────────────┐
            │                │                │
            ▼                ▼                ▼
     Dashboard        Statistical       MySQL Reports
      Analytics         Analysis           Module
            │                │                │
            └────────────────┼────────────────┘
                             ▼
                  Streamlit Web Application
                             │
                             ▼
                     Interactive Dashboard
```

---

# 🔄 ETL Workflow

```text
CSV Crime Dataset
        │
        ▼
Load Raw Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Processed Dataset
        │
        ▼
MySQL Database
        │
        ▼
Summary Tables
        │
        ▼
Database Views
        │
        ▼
Interactive Dashboards
        │
        ▼
PDF / Excel / CSV Reports
```

---

# 📊 Core Functionalities

✔ Interactive Dashboard

✔ Dynamic Filtering

✔ Business Intelligence Reports

✔ Crime Trend Analysis

✔ Statistical Analysis

✔ MySQL Reporting

✔ Interactive Visualizations

✔ Hotspot Identification

✔ PDF Report Generation

✔ Excel Export

✔ CSV Export

✔ Modular Architecture

✔ Responsive Streamlit UI

---

# 📁 Project Structure

```text
Chicago_Crime_Analytics_Platform/

│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── database_schema.sql
│
├── assets/
│   ├── images/
│   ├── css/
│   ├── icons/
│   └── screenshots/
│
├── cleaned_data/
│
├── datasets/
│
├── feature_engineered_data/
│
├── graphs/
│
├── reports/
│
├── scripts/
│   ├── load_data.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── mysql_connection.py
│   ├── load_to_mysql.py
│   ├── exploratory_analysis.py
│   ├── statistical_analysis.py
│   ├── mysql_summary_tables.py
│   ├── mysql_views.py
│   ├── mysql_reporting.py
│   └── mysql_visualization.py
│
├── streamlit_app/
│   ├── components/
│   ├── pages/
│   ├── utils/
│   └── app.py
│
└── utils/
```

---

# 🗄 Database Design

The application uses **MySQL** as the primary analytical database.

### Main Tables

| Table | Purpose |
|---------|----------|
| crime | Stores cleaned crime records |
| crime_yearly_summary | Stores yearly crime statistics |
| crime_category_summary | Stores crime category statistics |
| crime_community_summary | Stores community-level summaries |

---

### Database Views

| View | Description |
|------|-------------|
| vw_crime_yearly | Yearly crime summary |
| vw_crime_category | Crime category report |
| vw_arrest_summary | Arrest statistics |
| vw_community_summary | Community crime report |

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/chicago-crime-analytics-platform.git
```

---

## Navigate to Project

```bash
cd chicago-crime-analytics-platform
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Configuration

Before running the project, configure your MySQL database.

Create a database:

```sql
CREATE DATABASE chicago_crime_db;
```

Run the schema:

```sql
SOURCE database_schema.sql;
```

> Database credentials will be configured through environment variables (recommended) or a local configuration file.

---

# ▶ Running the Application

## Execute ETL Pipeline

```bash
python main.py
```

---

## Launch Streamlit Dashboard

```bash
streamlit run streamlit_app/app.py
```

---

Open your browser:

```
http://localhost:8501
```

---

# 📊 Dashboard Walkthrough

## 🏠 Dashboard

Provides a high-level overview of crime statistics.

Features:

- KPI Cards
- Crime Trends
- Arrest Analysis
- Executive Summary
- Dynamic Filters

---

## 🚔 Crime Analysis

Provides interactive crime exploration.

Includes:

- Crime Categories
- District Analysis
- Community Analysis
- Monthly Distribution
- Heatmaps
- Business Insights
- Export Reports

---

## 📈 Statistical Analysis

Supports advanced statistical exploration.

Includes:

- Distribution Analysis
- Correlation Analysis
- Outlier Detection
- Crime Intensity
- Statistical Charts

---

## 🗄 MySQL Reports

Business reporting module.

Includes:

- Yearly Report
- Category Report
- Arrest Report
- Community Report
- Export Center

---

## ℹ Project Information

Project documentation dashboard.

Includes:

- Project Overview
- Architecture
- Technology Stack
- Modules
- Developer Information

---

# 📤 Export Features

The platform supports exporting analytical reports in multiple formats for business reporting and offline analysis.

| Format | Supported |
|---------|-----------|
| 📄 CSV | ✅ |
| 📗 Excel (.xlsx) | ✅ |
| 📕 PDF Report | ✅ |

Export functionality is available in:

- Crime Analysis
- MySQL Reports

---

# 💡 Business Insights

The platform provides valuable analytical insights, including:

- Identification of high-crime districts
- Community-wise crime distribution
- Monthly crime trends
- Crime category analysis
- Arrest rate monitoring
- Hotspot identification
- Executive KPI reporting
- Statistical summaries
- Interactive business dashboards

These insights assist in understanding crime patterns and support data-driven decision making.

---

# 🚀 Future Enhancements

The platform is designed with modularity and scalability in mind. Future enhancements may include:

- AI-based Crime Prediction
- Machine Learning Models
- Real-time Crime Data Streaming
- REST API Integration
- User Authentication & Role-Based Access
- Interactive GIS Crime Maps
- Automated Email Reports
- Cloud Deployment (Azure / AWS / Render)
- Docker Containerization
- CI/CD Pipeline
- Unit & Integration Testing

---

# 🎯 Learning Outcomes

This project demonstrates practical experience in:

- Python Programming
- ETL Pipeline Development
- Data Cleaning & Preprocessing
- Feature Engineering
- MySQL Database Design
- SQL Reporting
- Streamlit Application Development
- Interactive Dashboard Design
- Statistical Analysis
- Data Visualization
- Report Generation
- Modular Software Architecture
- Business Intelligence Development

---

# 🤝 Contributing

Contributions are welcome.

If you'd like to improve the project:

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

Please ensure that code follows the existing project structure and coding conventions.

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for complete details.

---

# 👨‍💻 Author

**Yedukondalu Cheeraboina**

Software Developer | Python | SQL | Streamlit | MySQL | Data Analytics

---

## Connect

- GitHub: https://github.com/YedukondaluCheeraboina
- LinkedIn: https://www.linkedin.com/in/yedukondalucheeraboina/

---

# ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🛠 Suggest improvements
- 🐞 Report issues

Your support is greatly appreciated.

---

# 📷 Project Gallery

After deployment, replace these placeholders with actual screenshots.

| Dashboard | Crime Analysis |
|-----------|----------------|
| `assets/screenshots/dashboard.png` | `assets/screenshots/crime_analysis.png` |

| Statistical Analysis | MySQL Reports |
|----------------------|---------------|
| `assets/screenshots/statistical_analysis.png` | `assets/screenshots/mysql_reports.png` |

| Project Information |
|---------------------|
| `assets/screenshots/project_information.png` |

---

<p align="center">

**🚔 Chicago Crime Analytics Platform**

*Empowering Crime Intelligence through Data Analytics and Interactive Business Dashboards.*

Version **1.0**

</p>