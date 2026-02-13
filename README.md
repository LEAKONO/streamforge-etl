# StreamForge ETL Pipeline

An ETL pipeline that fetches live currency exchange rates from [ExchangeRate-API.com](https://www.exchangerate-api.com/), transforms the data, validates it, loads it into a PostgreSQL database, and creates a backup in Parquet format.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

---

## Features

- Extracts live exchange rates using the ExchangeRate-API.com API
- Transforms and cleans the data using pandas
- Validates data before loading
- Loads exchange rates into PostgreSQL
- Creates a local backup in Parquet format
- Fully configurable via `.env` file

---

## Requirements

- Python 3.12+
- PostgreSQL 16+
- Python packages:
  - `pandas`
  - `requests`
  - `sqlalchemy`
  - `python-dotenv`
  - `pyarrow` (for Parquet backups)
  - `psycopg2-binary`

---

## Setup

1. **Clone the repository**

```bash
git clone 'https://github.com/LEAKONO/streamforge-etl'
cd streamforge-etl
```
## Create and activate virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

## Install dependencies
```
pip install -r requirements.tx

```
## Usage

 Run the ETL pipeline:
```
python3 main.py
```