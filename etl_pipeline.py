import pandas as pd
import sqlite3

def run_etl_pipeline():
    print("--- 🚀 Starting ETL Pipeline ---")

    # ==========================================
    # 1. EXTRACT
    # ==========================================
    print("1. Extracting data from CSV...")
    df = pd.read_csv('raw_ecommerce_5000.csv')
    print(f"   -> Extracted {len(df)} rows.")

    # ==========================================
    # 2. TRANSFORM
    # ==========================================
    print("2. Transforming and cleaning data...")
    
    # A) Remove duplicates
    df_clean = df.drop_duplicates().copy()
    
    # B) Handle Missing Values (Imputation)
    # Fill missing prices with the mean price of their respective category
    df_clean['Price'] = df_clean.groupby('Category')['Price'].transform(lambda x: x.fillna(x.mean()))
    
    # Fill missing quantities with 1 (assuming at least 1 item was bought)
    df_clean['Quantity'] = df_clean['Quantity'].fillna(1).astype(int)
    
    # Fill missing payment methods with 'Unknown'
    df_clean['Payment_Method'] = df_clean['Payment_Method'].fillna('Unknown')
    
    # C) Feature Engineering
    # Calculate Total Amount for each order
    df_clean['Total_Amount'] = (df_clean['Price'] * df_clean['Quantity']).round(2)
    df_clean['Price'] = df_clean['Price'].round(2)
    
    # D) Standardize Date Format (YYYY-MM-DD)
    df_clean['Order_Date'] = pd.to_datetime(df_clean['Order_Date']).dt.strftime('%Y-%m-%d')

    print(f"   -> Data transformed successfully. Remaining valid rows: {len(df_clean)}")

    # ==========================================
    # 3. LOAD
    # ==========================================
    print("3. Loading data into SQLite Database...")
    
    # Connect to SQLite database (will be created if it doesn't exist)
    conn = sqlite3.connect('ecommerce_data_warehouse.db')
    
    # Load the cleaned dataframe into a SQL table
    df_clean.to_sql('sales_transactions', conn, if_exists='replace', index=False)
    
    # Verify the load process with a SQL query
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM sales_transactions")
    row_count = cursor.fetchone()[0]
    
    conn.close()
    print(f"   -> Successfully loaded {row_count} rows into 'ecommerce_data_warehouse.db'")
    print("--- 🎉 ETL Pipeline Completed Successfully! ---")

if __name__ == "__main__":
    run_etl_pipeline()