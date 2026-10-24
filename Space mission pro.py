import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('planets')
df = df.dropna()

print(df)

sns.histplot(data=df, x="orbital_period", bins=20, color='steelblue', log_scale=True)
plt.title('Distribution of planet orbital periods')
plt.xlabel('orbital periods')
plt.ylabel('count')
plt.show()

sns.kdeplot(data=df, x="distance", color='steelblue' )
plt.title('Planet distance (KDE)')
plt.xlabel("Distance from star (AU)")
plt.show()

sns.histplot(data=df, x="distance", kde=True, color='coral')
plt.title('Planet distance - Histogram with KDE curve')
plt.xlabel('Distance from star (AU)')
plt.ylabel('Count')
plt.show()

sns.stripplot(data=df, x="method", y="orbital_period", log_scale = True, hue= 'method')
plt.title('Discovery method vs Orbital period')
plt.xlabel('Discovery method')
plt.ylabel('Orbital period')
plt.show()

sns.stripplot(data=df, x="method", y="distance", hue='method')
plt.title('Discovery method vs Distance from star')
plt.xlabel('Discovery method')
plt.ylabel('Distance from star (AU)')
plt.show()

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("correlation heatmap - Planets numeric data")
plt.show()