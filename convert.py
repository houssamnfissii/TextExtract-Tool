import pandas as pd
import json

# Step 1: Load the CSV file (no header)
df = pd.read_csv("excel.csv", header=None)

# Step 2: Get all domain names from column B
domains = df[1].dropna().tolist()  # column index 1 = column B

# Step 3: Save to JSON
with open("domains.json", "w", encoding="utf-8") as f:
    json.dump(domains, f, indent=4)

print(f"✅ Saved {len(domains)} domains to domains.json")
