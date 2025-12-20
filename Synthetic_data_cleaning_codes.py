import pandas as pd

# Load synthetic dataset
df = pd.read_csv('Sythetic_Tenant_Data.csv')
print("Shape of synthetic dataset:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values per column:")
missing = df.isnull().sum()
print(missing[missing > 0])

if missing.sum() == 0:
    print("No missing values found.")
else:
    print(f"Total missing values: {missing.sum()}")

print("\nUnique values in 'verification':")
print(df['verification'].value_counts(dropna=False))
df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')
print(f"\nDate conversion - missing after conversion: {df['join_date'].isnull().sum()}")

print(f"\nDuplicate rows: {df.duplicated().sum()}")

print("\nUnique values in categorical columns:")
for col in ['district', 'verification', 'country']:
    print(f"\n{col}:")
    print(df[col].value_counts(dropna=False).head())

verification_mode = df['verification'].mode()[0]
print(f"\nMode of verification column: {verification_mode}")

df['verification'].fillna(verification_mode, inplace=True)
print(f"Missing values after filling with mode: {df['verification'].isnull().sum()}")

print("\nUpdated verification distribution:")
print(df['verification'].value_counts())

print("\nNumerical column ranges:")
num_cols = ['latitude', 'longitude', 'lifetime_bookings', 'avg_rating', 'cancellation_rate']
for col in num_cols:
    print(f"{col}: min={df[col].min():.2f}, max={df[col].max():.2f}")

print("\nFinal check:")
print(f"Shape: {df.shape}")
print(f"Missing values total: {df.isnull().sum().sum()}")
print(f"Data types:\n{df.dtypes}")

output_filename = 'Synthetic_Tenant_Data_CLEANED.csv'
df.to_csv(output_filename, index=False)
print(f"\nCleaned dataset saved as: {output_filename}")