import pandas as pd
PATH = 'Config/vehicle_parking_fees.csv'
df = pd.read_csv(PATH)
vehicles_fees = df.to_dict(orient='records')