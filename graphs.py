import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("employee.csv")
#bar graphs
plt.figure()
avg_salary=df.groupby('department')['salary'].mean()
bars=plt.bar(avg_salary.index,avg_salary.values)
plt.title('Average Salary per Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.tight_layout()
plt.savefig('bar_avg_salary.png')
plt.close()  
# histogram
plt.figure()
plt.hist(df['salary'],bins=5,edgecolor='black')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('frequency')
plt.tight_layout()
plt.legend()  
plt.savefig('hist_salary.png') 
plt.show()
#sactter
plt.figure()
for dept in df['department'].unique():
    sub=df[df['department']==dept]
    plt.scatter(sub['id'],sub['salary'],label=dept)
plt.title('ID vs Salary by department')
plt.xlabel('ID')
plt.ylabel('salary')
plt.tight_layout()
plt.legend()  
plt.savefig('scatter_id_salary.png')
plt.show()
#line
plt.figure()
months=['jan','feb','mar','apr','may','jun']
sales=[12,15,14,18,22,25]
plt.plot(months,sales,marker='o')
plt.title("Monthly Sales(jan to jun)")
plt.xlabel('Month')
plt.ylabel('sales')
plt.tight_layout()
plt.legend()  
plt.savefig('lines_sales.png')
plt.show()
print("All 4 pngs saved")
# bonus challenges
fig, axs=plt.subplots(2,2, figsize=(12,8))
#bar
avg=df.groupby('department')['salary'].mean()
axs[0,0].bar(avg.index,avg.values)
axs[0,0].set_title('Avg Salary per dept')
#hist
axs[0,1].hist(df['salary'],bins=5)
axs[0,1].set_title('Salary Distribution')
#scatter
for dept in df['department'].unique():
    sub=df[df['department']==dept]
    axs[1,0].scatter(sub['id'],sub['salary'],label=dept)
axs[1,0].legend()
axs[1,0].set_title('ID vs Salary')
#line
onths=['jan','feb','mar','apr','may','jun']
sales=[12,15,14,18,22,25]
axs[1,1].plot(months,sales,marker='o')
axs[1,1].set_title('Monthly Sales')
plt.tight_layout()
plt.savefig("all_charts.png")
plt.show()

