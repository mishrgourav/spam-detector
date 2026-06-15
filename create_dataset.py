import pandas as pd
import urllib.request
import zipfile
import os

os.makedirs('data', exist_ok=True)

# Download the dataset
print("Downloading dataset...")
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip"
filename = "data/spam_dataset.zip"

try:
    urllib.request.urlretrieve(url, filename)
    print("✓ Download complete!")
    
    # Extract
    print("Extracting...")
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall('data/')
    print("✓ Extraction complete!")
    
    # Convert to CSV
    print("Creating CSV...")
    df = pd.read_csv('data/SMSSpamCollection', sep='\t', header=None, names=['label', 'message'])
    df.to_csv('data/spam_data.csv', index=False)
    print("✓ CSV created!")
    
    print(f"\nDataset ready:")
    print(f"Total: {len(df)} messages")
    print(f"Spam: {(df['label'] == 'spam').sum()}")
    print(f"Ham: {(df['label'] == 'ham').sum()}")
    
except Exception as e:
    print(f"Error: {e}")