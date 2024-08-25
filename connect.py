import os
from astrapy import DataAPIClient

# Initialize the client
IBMWATSON_API_KEY = os.getenv("ASTRACS_TOKEN")
client = DataAPIClient("AstraCS:tGfhKLuZbnZlZbsuOkEWzJIj:b5293c8e951204c4f32de04aa042c5c6462b78325ce17acaba03c626c36b4e57")
db = client.get_database_by_api_endpoint(
  "https://533dfa71-2957-4385-b817-ef29ed129044-us-east-2.apps.astra.datastax.com"
)

print(f"Connected to Astra DB: {db.list_collection_names()}")