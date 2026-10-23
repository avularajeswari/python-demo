import pandas as pd
customer_df=pd.read_csv("customer.csv")
orders_df=pd.read_csv("orders.csv")
customer_df["customer_id"] = pd.to_numeric(
    customer_df["customer_id"], errors="coerce"
)
orders_df["customer_id"] = pd.to_numeric(
    orders_df["customer_id"], errors="coerce"
)
inner_merged=pd.merge(orders_df, customer_df, on="customer_id", how="inner")
print(f"Inner join rows:{len(inner_merged)}(customer 104 dropped)")
left_merged=pd.merge(customer_df, orders_df, on="customer_id", how="left", indicator=True)
no_order_name=left_merged[left_merged['_merge']=='left_only']['customer_name'].values[0]
print(f"No orders:{no_order_name}")
outer_merged=pd.merge(orders_df, customer_df, on="customer_id", how="outer", indicator=True)
unmatched_order_id=outer_merged[outer_merged['_merge']=='left_only']['customer_id'].values[0]
print(f"order without customer:customer_id{int(unmatched_order_id)}")
print("Bonus Challenges")
jan_orders=pd.DataFrame({'order_id':[10,11],'customer_id':[101,102],'amount':[500,200]})
feb_orders=pd.DataFrame({'order_id':[12,13],'customer_id':[103,101],'amount':[350,400]})
concat_orders=pd.concat([jan_orders,feb_orders], ignore_index=True)
grouped_result=concat_orders.groupby('customer_id')['amount'].sum()
print(grouped_result)