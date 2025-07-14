Retail Orders Data Pipeline using Python and MySQL
Project Overview

This project demonstrates an end-to-end data pipeline using Python to:
- Download a retail dataset from Kaggle
- Clean and transform the data
- Load it into a MySQL database using SQLAlchemy


Requirements:

Before running the script, install the following Python packages:

pip install pandas sqlalchemy pymysql kaggle

1. Kaggle API Setup

To download data from Kaggle, you must have a Kaggle account.

Steps:
1. Go to https://www.kaggle.com/account
2. Scroll down to the 'API' section.
3. Click 'Create New API Token'.
4. A file named kaggle.json will be downloaded.
5. Move this file to a known directory (e.g., ~/.kaggle on Linux/macOS or C:\Users\<username>\.kaggle on Windows).

On UNIX-like systems, set permissions with:
chmod 600 ~/.kaggle/kaggle.json

2. Setting MySQL Credentials

You will need the following MySQL connection details:

- Username (e.g., root)
- Password (your MySQL password)
- Host (usually localhost)
- Port (default is 3306)
- Database (must be created manually, e.g., test)

To create the database, use:
CREATE DATABASE test;

3. Editing the Script

In the Python script, update the following lines with your own values:

user = 'root'
password = 'your_password_here'
host = 'localhost'
port = '3306'
database = 'test'

4. Running the Script

Once configured, run the script with:

python main_script.py

The script will:
- Authenticate your Kaggle account
- Download the dataset orders.csv from Kaggle
- Unzip and clean the data
- Create new columns (discount, sale_price, profit)
- Load the final DataFrame into a MySQL table named df_orders



Key Concepts Learned

- Kaggle API integration
- Data cleaning and feature engineering using Pandas
- Database connectivity with SQLAlchemy
- Assigning explicit data types for reliability



