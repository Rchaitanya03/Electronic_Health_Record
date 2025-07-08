# Electronic Health Record (EHR) Data Quality Auditor

This project analyzes Electronic Health Record (EHR) data for completeness, consistency, and potential errors, and generates a clean Electronic Health Record.

---

## Features

- Missing value detection
- Invalid age/gender identification
- Unusual weight difference detection
- Modular structure (easy to extend)

## Sample Checks Included :
1)Missing Values Summary
2)Missing or Invalid Age
3)Invalid Gender
4)Weight Drop Issues
5)Missing Discharge Status

## project Structure

ehr-data-quality-auditor/
├── data/
│ └── EHR.csv # Raw EHR data
├── modules/
│ ├── ingestion.py # Loads the data
│ ├── validation.py # Contains validation checks
│ └── report_generator.py # Formats results (text and HTML)
├── main.py # Terminal-based manual data entry
├── requirements.txt # Dependencies
└── README.md # You're reading this

