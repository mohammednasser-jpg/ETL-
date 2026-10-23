import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("Generating 5000 rows of messy e-commerce data...")

np.random.seed(42)
num_rows = 5000

# Generate random dates within a year
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=np.random.randint(0, 365)) for _ in range(num_rows)]

data = {
    'OrderID': np.random.randint(100000, 999999, num_rows),
    'Customer_ID': np.random.randint(1000, 2000, num_rows),
    'Order_Date': dates,
    'Category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Sports', 'Toys'], num_rows),
    'Price': np.random.uniform(10, 1000, num_rows),
    'Quantity': np.random.randint(1, 10, num_rows),
    'Payment_Method': np.random.choice(['Credit Card', 'PayPal', 'Cash', np.nan], num_rows) # Intentional nulls
}

df_massive = pd.DataFrame(data)

# Inject deliberate messiness to demonstrate data engineering skills
# Injecting Nulls (Missing values)
df_massive.loc[np.random.choice(df_massive.index, 300, replace=False), 'Price'] = np.nan
df_massive.loc[np.random.choice(df_massive.index, 150, replace=False), 'Quantity'] = np.nan

# Injecting duplicate rows
df_massive = pd.concat([df_massive, df_massive.sample(200)]) 

# Save the raw data to a CSV file
df_massive.to_csv('raw_ecommerce_5000.csv', index=False)
print(f"Done! Created 'raw_ecommerce_5000.csv' with {len(df_massive)} rows.")