import seaborn as sns

# First, import the load_csv function from the loadCSV module
from loadCSV import load_csv

# Prompt the user to enter the name of the CSV file
file_name = input('Enter the name of the CSV file: ')

# Load the CSV file into a Pandas dataframe
df = load_csv(file_name)

# Use Seaborn to create a scatter plot of the data
# sns.scatterplot(x='x_column', y='y_column', data=df)

# Use Seaborn to create a line plot of the data
# sns.lineplot(x='x_column', y='y_column', data=df)

# Use Seaborn to create a bar plot of the data
# sns.barplot(x='x_column', y='y_column', data=df)

# Use Seaborn to create a histogram of the data
# sns.histplot(x='x_column', data=df)

# Use Seaborn to create a box plot of the data
# sns.boxplot(y='y_column', data=df)

# Use Seaborn to create a scatter matrix of the data
# sns.pairplot(df)
