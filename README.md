# 📊 CSV to JSON Data Converter

A lightweight Python automation script designed to parse comma-separated tabular data (CSV) and seamlessly transform it into a structured, human-readable JSON format. This project demonstrates core data manipulation, file I/O operations, and localized ETL (Extract, Transform, Load) pipelines.

## 🚀 Key Features

* *In-Memory Data Simulation:* Generates mock sales data directly within the script to simulate external file feeds.
* *Automated Parsing:* Utilizes Python's native csv.DictReader to automatically map tabular columns into structural key-value pairs (dictionaries).
* *Structured Exporting:* Formats and writes the processed dataset into an indented, production-ready sales.json file.

## 🛠️ Tech Stack

* *Language:* Python 3
* *Libraries:* csv (Tabular data handling), json (Data serialization)

## 📋 How It Works

1. *Extraction:* The script reads a tabular text block containing mock catalog items (Laptop, Mouse, etc.) and their respective quantities.
2. *Transformation:* The raw text is written to a local ventas.csv file, then extracted into a dynamic Python dictionary list.
3. *Loading:* The structured list is serialized with a 4-space indentation and successfully exported into ventas.json.
