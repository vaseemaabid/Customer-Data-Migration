import pandas as pd

df = pd.read_csv("customer_data.csv")

print("Validation Results:")

for index, row in df.iterrows():

    email = str(row['Email'])
    phone = str(row['Phone'])

    if '@' not in email:
        print(f"Invalid Email: {email}")

    if len(phone) != 10:
        print(f"Invalid Phone: {phone}")
