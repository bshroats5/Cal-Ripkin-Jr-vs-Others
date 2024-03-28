import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importing the data from Excel
CalStats = pd.read_excel('CalStats1.xlsx')
BarryStats = pd.read_excel('BarryStats1.xlsx')
DerekStats = pd.read_excel('DerekStats1.xlsx')
ChipperStats = pd.read_excel('ChipperStats1.xlsx')
AndreltonStats = pd.read_excel('AndreltonStats1.xlsx')
FreddieStats = pd.read_excel('FreddieStats1.xlsx')

# Creating a new column for the player's name
CalStats['Player'] = 'Cal Ripken Jr.'
BarryStats['Player'] = 'Barry Larkin'
DerekStats['Player'] = 'Derek Jeter'
ChipperStats['Player'] = 'Chipper Jones'
AndreltonStats['Player'] = 'Andrelton Simmons'
FreddieStats['Player'] = 'Freddie Freeman'

# Combining all the data into one DataFrame
df = pd.concat([CalStats, BarryStats, DerekStats, ChipperStats, AndreltonStats, FreddieStats])

# Showing the first 5 rows of the DataFrame
print(df.head())

# Showing the last 5 rows of the DataFrame
print(df.tail())

# Show me the columns of the DataFrame
print(df.columns)

# Visualizing the data

sns.set(style='whitegrid')
sns.set_palette('pastel')
sns.set_context('talk')

# Creating a boxplot of the data
plt.figure(figsize=(12, 8))
sns.boxplot(x='Player', y='HR', data=df)
plt.title('Home Runs by Player')
plt.show()

# Visualize the average number of games played by player
plt.figure(figsize=(12, 8))
sns.barplot(x='Player', y='G', data=df)
plt.title('Average Number of Games Played by Player')
plt.show()

# Visualize the average number of hits by player
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Player', y='H', data=df)
plt.title('Average Number of Hits by Player')
plt.show()

# Visualize the average WAR by player with labels
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Player', y='WAR', data=df)
plt.title('Average WAR by Player')
plt.show()



