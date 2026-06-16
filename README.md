PROJECT SUMMARY-CivilMate is a Python-based construction material estimation toolkit developed for Civil Engineering applications. It provides concrete, brickwork, and steel estimators with cost calculation and report generation in TXT, Excel, and PDF formats.

# CivilMate

CivilMate is a Python-based construction material estimation toolkit developed for Civil Engineering applications.

## Features

### Concrete Estimator

* Calculates cement requirements
* Calculates sand requirements
* Calculates aggregate requirements
* Generates cost estimates

### Brickwork Estimator

* Calculates brick quantity
* Calculates mortar requirements
* Generates cost estimates

### Steel Estimator

* Calculates steel weight
* Generates cost estimates

## Export Options

* TXT Reports
* Excel Reports (.xlsx)
* PDF Reports

## Project Metadata

Each report includes:

* Project Name
* Client Name
* Estimate ID
* Date

## Technologies Used

* Python
* OpenPyXL
* ReportLab

## Technologies Used

* Object-Oriented Programming
* File Handling
* Excel Automation (OpenPyXL)
* PDF Generation (ReportLab)
* Engineering CalculationsL
* Project Architecture
* Git and Github

## Project Structure

```text
CivilMate/
├── calculators/
│   ├── __init__.py
│   ├── concrete.py
│   ├── brickwork.py
│   └── steel.py
│
├── exports/
│   ├── Excel/
│   │   ├── concrete_export.py
│   │   ├── brickwork_export.py
│   │   └── steelwork_export.py
│   │
│   ├── Pdf/
│   │   ├── concrete_export_pdf.py
│   │   ├── brickwork_export_pdf.py
│   │   └── steel_export_pdf.py
│   │
│   └── TXT/
│       └── TXT_EXPORT.py
│
├── data/
│   └── rates.py
│
├── engine.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Install dependencies:

pip install -r requirements.txt

## Run Application

python main.py

## Future Improvements

* GUI Version
* Additional Civil Engineering Calculators
* BOQ Generator
