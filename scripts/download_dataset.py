import os
import requests
import zipfile
from tqdm import tqdm


def download_and_extract_ids2017():
    """
    Downloads and extracts the CIC-IDS2017 dataset into a 'data' directory
    at the project root.
    """
    # URL of the dataset zip file
    url = "http://cicresearch.ca/CICDataset/CIC-IDS-2017/Dataset/CIC-IDS-2017/CSVs/MachineLearningCSV.zip"

    # Paths are relative to the script's execution location (project root)
    data_dir = "data"
    zip_path = os.path.join(data_dir, "MachineLearningCSV.zip")
    extracted_path = os.path.join(data_dir, "MachineLearningCVE")

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Created directory: {data_dir}")

    # Check if the dataset is already downloaded and extracted
    if os.path.exists(extracted_path) and os.listdir(extracted_path):
        print("CIC-IDS2017 dataset already exists in the 'data/MachineLearningCVE' directory.")
        print("Skipping download and extraction.")
        return

    # --- Download the file ---
    print(f"Downloading dataset from: {url}")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        total_size = int(response.headers.get('content-length', 0))

        with open(zip_path, 'wb') as f, tqdm(
                desc="Downloading",
                total=total_size,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
        ) as bar:
            for chunk in response.iter_content(chunk_size=8192):
                size = f.write(chunk)
                bar.update(size)

        print("Download complete.")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading the file: {e}")
        return

    # --- Extract the file ---
    print(f"Extracting files from {zip_path}...")
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(data_dir)
        print(f"Successfully extracted dataset to '{data_dir}'")

        if os.path.exists(extracted_path):
            print(f"Verified extraction folder: {extracted_path}")
        else:
            print("Warning: Expected extraction folder not found.")

    except zipfile.BadZipFile:
        print("Error: The downloaded file is not a valid zip file or is corrupted.")
        os.remove(zip_path)
        print(f"Removed corrupted file: {zip_path}")
        return

    # --- Clean up the downloaded zip file ---
    print(f"Removing downloaded zip file: {zip_path}")
    os.remove(zip_path)
    print("Cleanup complete.")


if __name__ == "__main__":
    # This script should be run from the root of the project directory
    download_and_extract_ids2017()
