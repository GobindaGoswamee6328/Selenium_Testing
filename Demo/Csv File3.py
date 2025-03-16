import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

file_path = "D:/Iris2.csv"
data = pd.read_csv(file_path)


# Custom function to annotate peak values on the diagonal KDE plots
def annotate_kde_peaks(g, features, data):
    for i, feature in enumerate(features):
        ax = g.diag_axes[i]  # Get the diagonal KDE plot axes

        # Find the peak (maximum) value for each species
        for species, color in zip(data['Species'].unique(), sns.color_palette()):
            peak = data.loc[data['Species'] == species, feature].max()
            ax.annotate(f"{species}\n{peak:.2f}",
                        xy=(peak, 0), xytext=(peak, 0.05),  # Position near top
                        color=color, ha='center',
                        arrowprops=dict(arrowstyle="->", color=color, lw=1))


# Features to analyze
features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

# Pair plot
g = sns.pairplot(data, hue="Species", diag_kind="kde", corner=True)

# Annotate the peaks
annotate_kde_peaks(g, features, data)

# Add a title
plt.suptitle('Pair Plot of Sepal and Petal Metrics with Peak Values', y=1.02)  # Title with some spacing
plt.show()
