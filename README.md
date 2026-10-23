utomated E-Commerce ETL Pipeline

This repository contains a complete Data Engineering ETL pipeline that processes raw e-commerce data and loads it into a SQL database.

Files in this repository:

generate_big_data.py: A script that generates a raw dataset of 5,000+ rows with deliberate anomalies (nulls, duplicates) to simulate real-world messy data.

etl_pipeline.py: The core pipeline script that extracts the CSV data, transforms it using Pandas, and loads it into a local SQLite database.

raw_ecommerce_5000.csv: The initial raw dataset.

How to run it:

Run generate_big_data.py to create the raw CSV file.

Run etl_pipeline.py to execute the extraction, cleaning, and database loading process.

The output will be a fully structured ecommerce_data_warehouse.db database file.
