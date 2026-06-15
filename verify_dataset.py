import pandas as pd

# Load the dataset
df = pd.read_csv('data/SMSSpamCollection', sep='\t', header=None, names=['label', 'message'])

# Save as CSV
df.to_csv('data/spam_data.csv', index=False)

print("✓ Dataset saved as: data/spam_data.csv")
print(f"Total messages: {len(df)}")
print(f"Spam: {(df['label'] == 'spam').sum()}")
print(f"Ham: {(df['label'] == 'ham').sum()}")