import pandas as pd

df = pd.read_csv("Hostel.csv")

df.to_json('Hostel.json', index=False, lines=True)