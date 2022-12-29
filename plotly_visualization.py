import plotly.express as px

# First, import the load_csv function from the loadCSV module
from loadCSV import load_csv

# Prompt the user to enter the name of the CSV file
file_name = input('Enter the name of the CSV file: ')

# Load the CSV file into a Pandas dataframe
df = load_csv(file_name)

# Use Plotly to create a scatter plot of the data
# fig = px.scatter(df, x='x_column', y='y_column')
# fig.show()

# Use Plotly to create a line plot of the data
# fig = px.line(df, x='x_column', y='y_column')
# fig.show()

# Use Plotly to create a bar plot of the data
# fig = px.bar(df, x='x_column', y='y_column')
# fig.show()

# Use Plotly to create a histogram of the data
# fig = px.histogram(df, x='x_column')
# fig.show()

# Use Plotly to create a box plot of the data
# fig = px.box(df, y='y_column')
# fig.show()

# Use Plotly to create a scatter matrix of the data
# fig = px.scatter_matrix(df)
# fig.show()
