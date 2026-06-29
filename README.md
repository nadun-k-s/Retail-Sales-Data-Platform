# 🚀 Retail Sales Data Platform

> **An End-to-End Event-Driven Data Engineering Pipeline using AWS, Snowflake, Docker, Python and Power BI**

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge\&logo=python)
![Snowflake](https://img.shields.io/badge/Snowflake-Data%20Warehouse-29B5E8?style=for-the-badge\&logo=snowflake)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange?style=for-the-badge\&logo=amazonaws)
![Docker](https://img.shields.io/badge/Docker-Container-blue?style=for-the-badge\&logo=docker)
![Power BI](https://img.shields.io/badge/Power%20BI-Analytics-F2C811?style=for-the-badge\&logo=powerbi)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

# 📌 Overview

The **Retail Sales Data Platform** is a production-style, event-driven data engineering solution that automates retail data ingestion, transformation, and analytics using modern cloud technologies.

CSV files uploaded to Amazon S3 automatically trigger an AWS Lambda containerized application. The Lambda securely retrieves Snowflake credentials from AWS Secrets Manager and executes SQL stored procedures to process data through RAW, STAGING, and MART layers inside Snowflake.

The processed data is optimized for reporting and business intelligence using a dimensional (Star Schema) data model.

---

# 🏗 Solution Architecture

> Replace the image path below with your architecture diagram.

```text
architecture/aws-architecture.png
```

---

# 🚀 Architecture Overview

```
CSV Upload
     │
     ▼
Amazon S3
     │
Object Created Event
     │
     ▼
AWS Lambda (Docker Container)
     │
AWS Secrets Manager
     │
     ▼
Snowflake
     │
 ┌───────────────┐
 │     RAW       │
 └───────────────┘
         │
         ▼
 ┌───────────────┐
 │   STAGING     │
 └───────────────┘
         │
         ▼
 ┌───────────────┐
 │     MART      │
 └───────────────┘
         │
         ▼
Power BI Dashboard
```

---

# ⚙ Technology Stack

| Category              | Technologies                                           |
| --------------------- | ------------------------------------------------------ |
| Cloud                 | AWS Lambda, Amazon S3, Amazon ECR, AWS Secrets Manager |
| Data Warehouse        | Snowflake                                              |
| Programming           | Python                                                 |
| Database              | SQL                                                    |
| Containerization      | Docker                                                 |
| Data Modeling         | Star Schema                                            |
| Business Intelligence | Power BI                                               |
| Version Control       | Git & GitHub                                           |

---

# ✨ Features

* Event-driven ETL using Amazon S3 notifications
* Serverless processing with AWS Lambda
* Docker-based Lambda deployment
* Secure credential management using AWS Secrets Manager
* Snowflake cloud data warehouse
* Automated SQL Stored Procedures
* RAW → STAGING → MART architecture
* Star Schema dimensional model
* ETL Audit Logging
* Power BI ready analytics layer
* Modular ETL pipeline
* Production-style architecture

---

# 📂 Repository Structure

```
Retail-Sales-Data-Platform
│
├── architecture/
│
├── aws/
│   └── lambda/
│
├── snowflake/
│
├── data/
│
├── docs/
│
├── powerbi/
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# 📊 Data Warehouse Architecture

```
RAW
│
├── CUSTOMERS
├── PRODUCTS
└── SALES

        │

        ▼

STAGING
│
├── STG_CUSTOMERS
├── STG_PRODUCTS
└── STG_SALES

        │

        ▼

MART
│
├── DIM_CUSTOMER
├── DIM_PRODUCT
└── FACT_SALES
```

---

# 🔄 ETL Workflow

1. CSV files uploaded into Amazon S3
2. S3 ObjectCreated event triggers AWS Lambda
3. Lambda retrieves credentials from AWS Secrets Manager
4. Lambda connects to Snowflake
5. Stored Procedures execute ETL
6. Data moves through RAW → STAGING → MART
7. ETL Audit Log is updated
8. Power BI consumes MART tables

---

# 🔐 Security

* AWS Secrets Manager for credentials
* IAM Roles with least privilege
* Containerized Lambda deployment
* Secure Snowflake authentication
* No hardcoded credentials

---

# 📈 Data Model

The analytical layer follows a **Star Schema** consisting of:

### Dimension Tables

* DIM_CUSTOMER
* DIM_PRODUCT

### Fact Tables

* FACT_SALES

This model enables fast analytical queries and efficient Power BI reporting.

---

# 🚀 Deployment

## Clone Repository

```bash
git clone https://github.com/<your-username>/Retail-Sales-Data-Platform.git
```

---

## Build Docker Image

```bash
docker build \
-t retail-snowflake-etl .
```

---

## Push to Amazon ECR

```bash
docker push <your-ecr-uri>
```

---

## Deploy AWS Lambda

Create a Lambda using the container image from Amazon ECR.

---

## Configure Trigger

```
Amazon S3

↓

Object Created Event

↓

AWS Lambda
```

---

# 📷 Project Screenshots

## AWS Architecture

```
docs/screenshots/architecture.png
```

---

## AWS Lambda

```
docs/screenshots/lambda-success.png
```

---

## Amazon S3

```
docs/screenshots/s3-bucket.png
```

---

## Snowflake

```
docs/screenshots/snowflake.png
```

---

## ETL Audit Log

```
docs/screenshots/etl-audit-log.png
```

---

# 🎯 Future Enhancements

* GitHub Actions CI/CD
* Terraform Infrastructure as Code
* Snowflake Streams
* Snowflake Tasks
* EventBridge Integration
* CloudWatch Monitoring
* Data Quality Validation
* Email Notifications
* Unit Testing
* dbt Integration

---

# 📚 Learning Outcomes

This project demonstrates practical experience with:

* Data Engineering
* Event-Driven Architecture
* Cloud Computing
* Serverless Computing
* Data Warehousing
* ETL Development
* Snowflake
* AWS
* Docker
* Python
* SQL
* Business Intelligence

---

# 👨‍💻 Author

**Nadun Kaushalya**

Backend Software Engineer | Data Engineer

---