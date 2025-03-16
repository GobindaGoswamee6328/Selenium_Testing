import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "D:\Iris2.csv"
data = pd.read_csv(file_path)

# Drop rows with missing values to clean the dataset
cleaned_data = data.dropna()

# Create a new column that combines Sepal and Petal dimensions
cleaned_data['Combined'] = (
    cleaned_data['SepalLengthCm'] +
    cleaned_data['SepalWidthCm'] +
    cleaned_data['PetalLengthCm'] +
    cleaned_data['PetalWidthCm']
)

# Find peak values (maximum 'Combined') for each species
peak_values = cleaned_data.loc[cleaned_data.groupby('Species')['Combined'].idxmax()]

# Set plot style
sns.set(style="whitegrid")

# Create a boxplot to visualize Combined values for each species
plt.figure(figsize=(10, 6))
sns.boxplot(x='Species', y='Combined', data=cleaned_data, palette='viridis')

# Highlight peak values on the plot
for _, row in peak_values.iterrows():
    plt.text(x=row['Species'], y=row['Combined'] + 0.1,
             s=f"Peak: {row['Combined']:.1f}",
             color='red', ha='center', weight='bold')

plt.title("Combined Sepal and Petal Dimensions for Each Species")
plt.ylabel("Combined Sepal and Petal Length/Width")
plt.xlabel("Species")
plt.show()
