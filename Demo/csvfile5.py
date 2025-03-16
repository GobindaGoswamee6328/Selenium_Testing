import pandas as pd

# Load the dataset
file_path = "D:/Iris2.csv"
dataset = pd.read_csv(file_path)

# Step 1: Handle missing values
# Fill numeric columns with the mean of the column
dataset['SepalLengthCm'].fillna(dataset['SepalLengthCm'].mean(), inplace=True)
dataset['SepalWidthCm'].fillna(dataset['SepalWidthCm'].mean(), inplace=True)
dataset['PetalLengthCm'].fillna(dataset['PetalLengthCm'].mean(), inplace=True)
dataset['PetalWidthCm'].fillna(dataset['PetalWidthCm'].mean(), inplace=True)

# Fill categorical columns with the most frequent value
dataset['Species'].fillna(dataset['Species'].mode()[0], inplace=True)

# Step 2: Define metrics for testing
# Metric 1: Average petal area (PetalLengthCm * PetalWidthCm) per species
dataset['PetalArea'] = dataset['PetalLengthCm'] * dataset['PetalWidthCm']
average_petal_area = dataset.groupby('Species')['PetalArea'].mean()

# Metric 2: Average sepal area (SepalLengthCm * SepalWidthCm) per species
dataset['SepalArea'] = dataset['SepalLengthCm'] * dataset['SepalWidthCm']
average_sepal_area = dataset.groupby('Species')['SepalArea'].mean()

# Metric 3: Count of entries per species
species_count = dataset['Species'].value_counts()

# Display the metrics
print("Average Petal Area per Species:")
print(average_petal_area)

print("\nAverage Sepal Area per Species:")
print(average_sepal_area)

print("\nCount of Entries per Species:")
print(species_count)
