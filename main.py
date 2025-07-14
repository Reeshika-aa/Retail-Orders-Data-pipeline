import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
import os

# Step 1: Authenticate Kaggle API
api = KaggleApi()
api.authenticate()


# Step 2: Download the dataset from Kaggle
dataset_name = 'ankitbansal06/retail-orders'
file_name = 'orders.csv'

# Download specific file to current directory
api.dataset_download_file(dataset=dataset_name, file_name=file_name, path='.')

# Step 3: Extract CSV file from the downloaded ZIP
import zipfile
with zipfile.ZipFile(f'{file_name}.zip', 'r') as zip_ref:
    zip_ref.extractall()

# Step 4: Load CSV and handle missing values
df = pd.read_csv(file_name, na_values=['Not Available', 'unknown'])

# Step 5: Clean column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Step 6: Derive new columns
df['discount'] = df['list_price'] * df['discount_percent'] * 0.01
df['sale_price'] = df['list_price'] - df['discount']
df['profit'] = df['sale_price'] - df['cost_price']

# Step 7: Convert 'order_date' to datetime
df['order_date'] = pd.to_datetime(df['order_date'], format="%Y-%m-%d")

# Step 8: Drop unnecessary columns
df.drop(columns=['list_price', 'cost_price', 'discount_percent'], inplace=True)

# Step 9: Create SQLAlchemy engine for MySQL
from sqlalchemy import create_engine
user = '***'
password = '***'
host = 'localhost'
port = '***'
database = 'test'  

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')

# Step 10: Upload DataFrame to MySQL
from sqlalchemy.types import Integer, String, Date, DECIMAL
df.to_sql(
    name='df_orders',
    con=engine,
    if_exists='replace',  
    index=False,
    dtype={
        'order_id': Integer(),
        'order_date': Date(),
        'ship_mode': String(20),
        'segment': String(20),
        'country': String(20),
        'city': String(20),
        'state': String(20),
        'postal_code': String(20),
        'region': String(20),
        'category': String(20),
        'sub_category': String(20),
        'product_id': String(50),
        'quantity': Integer(),
        'discount': DECIMAL(7, 2),
        'sale_price': DECIMAL(7, 2),
        'profit': DECIMAL(7, 2)
    }
)

print("Data successfully loaded into MySQL 'df_orders' table with custom schema.")

