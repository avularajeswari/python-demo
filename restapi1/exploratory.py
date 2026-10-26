
import pandas as pd

# Load employee data
df = pd.read_csv("employee.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Remove extra spaces from text columns
for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = df[col].astype("string").str.strip()

print("=== DATA OVERVIEW ===")
print(df.head())
print("\nColumns:", df.columns.tolist())

# 1. SUMMARY STATISTICS
print("\n=== 1. SUMMARY STATISTICS ===")

numeric_cols = df.select_dtypes(include="number").columns

summary = df[numeric_cols].agg(
    ["mean", "median", "min", "max", "std"]
)

print(summary.round(2))


# 2. GROUPBY AGGREGATION
print("\n=== 2. DEPARTMENT COMPARISON ===")

if "department" in df.columns:
    metrics = {
        col: ["mean", "min", "max", "count"]
        for col in numeric_cols
    }

    if metrics:
        department_summary = df.groupby("department").agg(metrics)
        print(department_summary.round(2))
    else:
        print("No numeric columns available.")

# Compare employees by city
if "city" in df.columns and len(numeric_cols) > 0:
    print("\n=== CITY COMPARISON ===")
    print(df.groupby("city")[list(numeric_cols)].mean().round(2))

# Compare employees by gender
if "gender" in df.columns and len(numeric_cols) > 0:
    print("\n=== GENDER COMPARISON ===")
    print(df.groupby("gender")[list(numeric_cols)].mean().round(2))


# 3. CORRELATIONS: TOP 3 RELATIONSHIPS
print("\n=== 3. TOP 3 CORRELATIONS ===")

if len(numeric_cols) >= 2:
    corr_matrix = df[numeric_cols].corr()

    pairs = corr_matrix.where(
        pd.DataFrame(
            True,
            index=corr_matrix.index,
            columns=corr_matrix.columns
        ).where(
            pd.DataFrame(
                False,
                index=corr_matrix.index,
                columns=corr_matrix.columns
            ),
            True
        )
    )

    # Keep only unique pairs and remove self-correlations
    pairs = corr_matrix.where(
        pd.DataFrame(
            [[i < j for j in range(len(numeric_cols))]
             for i in range(len(numeric_cols))],
            index=numeric_cols,
            columns=numeric_cols
        )
    )

    top3 = pairs.stack().dropna()
    top3 = top3.reindex(
        top3.abs().sort_values(ascending=False).index
    ).head(3)

    print(top3.round(3))
else:
    print("At least two numeric columns are required.")


# 4. ANSWER BUSINESS QUESTIONS WITH NUMBERS
print("\n=== 4. BUSINESS QUESTIONS ===")

# Question 1: How many employees are there?
print("1. Total employees:", len(df))

# Question 2: What is the average salary?
if "salary" in df.columns:
    print("2. Average salary:", round(df["salary"].mean(), 2))
else:
    print("2. Average salary: salary column not found.")

# Question 3: Which department has the highest average salary?
if "department" in df.columns and "salary" in df.columns:
    avg_salary = df.groupby("department")["salary"].mean()
    if not avg_salary.dropna().empty:
        print("3. Highest average salary department:",
              avg_salary.idxmax())
        print("   Average salary:", round(avg_salary.max(), 2))

# Question 4: Which city has the most employees?
if "city" in df.columns:
    city_counts = df["city"].value_counts()
    if not city_counts.empty:
        print("4. City with most employees:", city_counts.idxmax())
        print("   Employee count:", int(city_counts.max()))

# Question 5: What is the average age?
if "age" in df.columns:
    print("5. Average age:", round(df["age"].mean(), 2))


# 5. MERGE DEPARTMENT BUDGET TABLE
print("\n=== 5. MERGE DEPARTMENT BUDGET ===")

if "department" in df.columns:
    budget_data = pd.DataFrame({
        "department": ["HR", "IT", "Finance", "Sales"],
        "budget": [100000, 250000, 180000, 200000]
    })

    merged_df = pd.merge(
        df,
        budget_data,
        on="department",
        how="left"
    )

    print(merged_df.head())

    merged_df.to_csv("employee_with_budget.csv", index=False)
    print("Saved: employee_with_budget.csv")
else:
    print("Department column not found; budget merge skipped.")
#--bonus:pivot Table
# Create pivot table
pivot = pd.pivot_table(
    df,
    index="department",
    values="salary",
    aggfunc="mean"
)
print("Pivot Table:")
print(pivot)
