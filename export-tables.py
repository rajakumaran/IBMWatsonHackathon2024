import os
import csv
from astrapy import DataAPIClient

# Initialize the client
# IBMWATSON_API_KEY = os.getenv("ASTRACS_TOKEN")
client = DataAPIClient("AstraCS:tGfhKLuZbnZlZbsuOkEWzJIj:b5293c8e951204c4f32de04aa042c5c6462b78325ce17acaba03c626c36b4e57")
db = client.get_database_by_api_endpoint(
  "https://533dfa71-2957-4385-b817-ef29ed129044-us-east-2.apps.astra.datastax.com"
)

# Get the list of tables (collections)
tables = db.list_collection_names()
print(f"Connected to Astra DB: {tables}")

# Export each table to a CSV file
for table in tables:
    # Get the table data
    table_data = list(db.get_collection(table).find())  # convert to a list

    # Create a CSV writer
    with open(f"{table}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row (assuming the first document has all the fields)
        if table_data:
            writer.writerow(table_data[0].keys())

            # Write the data rows
            for doc in table_data:
                writer.writerow(doc.values())

    print(f"Table {table} exported to {table}.csv")