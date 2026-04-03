
import pandas as pd

# Load parquet file
df = pd.read_parquet("yellow_tripdata_2026-01.parquet")

# OPTIONAL: take a smaller sample (recommended)
df = df.head(1000)

# Convert to CSV
df.to_csv("yellow_trip_sample.csv", index=False)

print("Conversion done!")
