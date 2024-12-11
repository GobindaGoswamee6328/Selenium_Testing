import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Load the Iris dataset
file_path = "D:/Iris2.csv"
data = pd.read_csv(file_path)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Example Selenium operation
url = "https://trytestingthis.netlify.app/"
driver.get(url)

# Optional: Interact with the webpage (example)
print("Page title is:", driver.title)

# Close the browser
driver.quit()

# Visualization: Scatter Plot (Sepal Length vs. Sepal Width)
plt.figure(figsize=(8, 6))
for species in data['Species'].unique():
    subset = data[data['Species'] == species]
    plt.scatter(subset['PetalLengthCm'], subset['PetalWidthCm'], label=species)

plt.title('Petal Length vs Petal Width')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend()
plt.grid(True)

# Save the plot to a file
plt.savefig('scatter_plot.png')

# Show the plot
plt.show()
