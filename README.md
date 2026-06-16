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

## Skills Demonstrated

*Object-Oriented Programming
*File Handling
*Excel Automation (OpenPyXL)
*PDF Generation (ReportLab)
*Engineering Calculations
*Project Architecture
*Git and Github

## Project Structure

```text
CivilMate/
├── calculators/
│   ├── concrete.py
│   ├── brickwork.py
│   └── steel.py
│
├── exports/
│   ├── Excel/
│   ├── Pdf/
│   └── TXT/
│
├── data/
│   └── rates.py
│
├── engine.py
├── requirements.txt
└── README.md
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
