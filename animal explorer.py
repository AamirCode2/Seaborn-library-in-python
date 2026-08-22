import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')
df = df.dropna()

print("First 5 rows: ")
print(df.head())
print()
print(df.info())
print()
print(df.describe())
print()
print("Species: ", df['species']. unique())
print("Islands: ", df['island']. unique())

sns.histplot(data=df, x="body_mass_g", bins=20, color='steelblue')
plt.title('Distribution of penquin body mass')
plt.xlabel('Body Mass (grams)')
plt.ylabel('Count')
plt.show()

sns.kdeplot(data=df, x='flipper_length_mm', hue='species', fill=True)
plt.title('Flipper Length Shape by species (KDE)')
plt.xlabel("Flipper length (mm)")
plt.show()

sns.histplot(data=df, x="Flipper_length_mm", kde=True, color='coral')
plt.title('Flipper length - Histogram with KDE curve')
plt.xlabel('Flipper length (mm)')
plt.ylabel('Count')
plt.show()

sns.scatterplot(data=df, x="Flipper_length_mm", y="body_mass_g", hue="species")
plt.title('Flipper length vs Body Mass by species')
plt.xlabel('Flipper length (mm)')
plt.ylabel('Body Mass (grams)')
plt.show()

corr = df.corr(numeric_only=True)
print("Correlation table: ")
print(corr)
print()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("correlation heatmap - penguin measurements")
plt.show()