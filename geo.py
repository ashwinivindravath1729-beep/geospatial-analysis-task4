import pandas as pd
import numpy as np

print("=" * 55)
print("   GEOSPATIAL DATA ANALYSIS — TASK 4")
print("=" * 55)

# Step 1: Create location-based sales dataset
data = {
    'store_id': [1,2,3,4,5,6,7,8,9,10],
    'city': ['New York','Los Angeles','Chicago','Houston','Phoenix',
              'Philadelphia','San Antonio','San Diego','Dallas','San Jose'],
    'state': ['NY','CA','IL','TX','AZ','PA','TX','CA','TX','CA'],
    'latitude': [40.71,34.05,41.85,29.76,33.44,
                 39.95,29.42,32.72,32.78,37.33],
    'longitude': [-74.00,-118.24,-87.65,-95.36,-112.07,
                  -75.16,-98.49,-117.15,-96.79,-121.88],
    'monthly_sales': [250000,180000,120000,95000,75000,
                      60000,55000,80000,110000,140000],
    'store_size_sqft': [5000,4200,3800,3200,2800,
                        2500,2600,3000,3500,3900],
    'customers_per_day': [850,620,480,380,300,
                          240,260,320,420,500],
    'competitor_stores': [12,8,6,4,3,2,3,4,5,7],
    'existing_store': [1,1,1,1,0,0,0,1,1,1]
}

df = pd.DataFrame(data)

# Step 2: Regions with high demand but no store
expansion_data = {
    'region': ['Brooklyn NY','Sacramento CA','Austin TX',
                'Memphis TN','Denver CO','Portland OR',
                'Las Vegas NV','Atlanta GA','Miami FL','Seattle WA'],
    'state': ['NY','CA','TX','TN','CO','OR','NV','GA','FL','WA'],
    'latitude': [40.67,38.57,30.26,35.14,39.73,
                 45.52,36.17,33.74,25.77,47.60],
    'longitude': [-73.94,-121.46,-97.74,-90.04,-104.98,
                  -122.67,-115.13,-84.38,-80.19,-122.33],
    'demand_score': [92,85,88,72,80,75,78,83,87,89],
    'population_density': [35000,8000,12000,6500,9000,
                           7500,6000,10000,15000,11000],
    'avg_income': [65000,58000,72000,45000,68000,
                   62000,55000,60000,58000,75000],
    'competitor_stores': [5,3,4,2,3,2,4,3,5,4]
}

df2 = pd.DataFrame(expansion_data)

print(f"\n✅ Existing stores: {len(df)}")
print(f"✅ Expansion regions analyzed: {len(df2)}")

# Step 3: Existing store performance
print("\n--- EXISTING STORE PERFORMANCE ---")
perf = df[['city','state','monthly_sales','customers_per_day','competitor_stores']].sort_values('monthly_sales', ascending=False)
print(perf.to_string(index=False))

# Step 4: Sales by state
print("\n--- SALES BY STATE ---")
state_sales = df.groupby('state').agg(
    Total_Sales=('monthly_sales','sum'),
    Avg_Sales=('monthly_sales','mean'),
    Stores=('store_id','count')
).round(2).sort_values('Total_Sales', ascending=False)
print(state_sales.to_string())

# Step 5: Top expansion regions
print("\n--- TOP EXPANSION REGIONS (by demand score) ---")
df2['expansion_score'] = (
    df2['demand_score'] * 0.4 +
    (df2['avg_income'] / 1000) * 0.3 +
    (df2['population_density'] / 1000) * 0.2 -
    df2['competitor_stores'] * 0.1
).round(2)

top3 = df2.sort_values('expansion_score', ascending=False).head(3)
print(top3[['region','state','demand_score','avg_income',
             'population_density','expansion_score']].to_string(index=False))

# Step 6: Best 3 locations to expand
print("\n--- RECOMMENDED 3 NEW STORE LOCATIONS ---")
for i, row in top3.iterrows():
    print(f"  {list(top3.index).index(i)+1}. {row['region']}, {row['state']}")
    print(f"     Demand Score     : {row['demand_score']}")
    print(f"     Avg Income       : ${row['avg_income']:,}")
    print(f"     Population Density: {row['population_density']:,}/sqmi")
    print(f"     Expansion Score  : {row['expansion_score']}")
    print()

# Step 7: Key insights
print("--- KEY INSIGHTS ---")
print("1. New York & California have highest sales — strong markets")
print("2. Texas has multiple stores but room for more growth")
print("3. Seattle, Brooklyn & Austin are top expansion targets")
print("4. High income + high demand = best expansion formula")
print("5. Avoid areas with 5+ competitor stores")

# Save
df.to_csv('existing_stores.csv', index=False)
df2.to_csv('expansion_regions.csv', index=False)
print("\n✅ Saved to existing_stores.csv and expansion_regions.csv!")
print("\n🎉 Geospatial Data Analysis — COMPLETE!")