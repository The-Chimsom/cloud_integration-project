from google.cloud import storage
from dotenv import dotenv_values

config = dotenv_values(".env")

def upload_file(bucket_name, source_file, blob_destination_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_destination_name)

    blob.upload_from_filename(source_file)

    print(
        f"File {source_file} uploaded to {blob_destination_name} in {bucket_name}."
    )

if __name__ == "__main__":
    bucket_name =  config["STORAGE_BUCKET_NAME"]
    source_file = "Apocolypse Food Prep.xlsx"
    blob_destination_name = config["BLOB_NAME"]
    upload_file(bucket_name=bucket_name, source_file=source_file, blob_destination_name=blob_destination_name)