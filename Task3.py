import pandas as pd
df=pd.read_csv("orders.csv")
df["customer_id"] = pd.to_numeric(
    df["customer_id"], errors="coerce"
)
print(df.isna())
print(df.sum())
print(df.duplicated())
df=df.drop_duplicates()
median_val=df['amount'].median()
print(f"Median used:{median_val}")
df['amount']=df['amount'].fillna(median_val)
df['order_id']=df['order_id'].astype(str)
result=df.groupby('customer_id').agg(
    total=('amount','sum'),
    orders=('order_id','count')
).reset_index()
print("\nFinal Result:")
print(result)