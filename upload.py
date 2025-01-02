import os
from dotenv import load_dotenv
from google.cloud import storage

load_dotenv()

def upload_file(bucket_name, source_file, blob_destination_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_destination_name)

    blob.upload_from_filename(source_file)

if __name__ == "__uplaod__":
    bucket_name =  os.getenv("STORAGE_BUCKET_NAME")
    source_file = "Apocolypse Food Prep.xlsx"
    blob_destination_name = os.getenv("BLOB_NAME")
    upload_file(bucket_name=bucket_name, source_file=source_file, blob_destination_name=blob_destination_name)