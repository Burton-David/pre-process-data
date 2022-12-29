import altair as alt

# First, import the load_csv function from the loadCSV module
from loadCSV import load_csv

# Prompt the user to enter the name of the CSV file
file_name = input('Enter the name of the CSV file: ')

# Load the CSV file into a Pandas dataframe
df = load_csv(file_name)

# Use Altair to create a scatter plot of the data
# scatter = alt.Chart(df).mark_point().encode(
#     x='x_column',
#     y='y_column'
# )

# scatter.show()

# Use Altair to create a line plot of the data
# line = alt.Chart(df).mark_line().encode(
#     x='x_column',
#     y='y_column'
# )

# line.show()

# Use Altair to create a bar plot of the data
# bar = alt.Chart(df).mark_bar().encode(
#     x='x_column',
#     y='y_column'
# )

# bar.show()

# Use Altair to create a histogram of the data
# histogram = alt.Chart(df).mark_bar().encode(
#     alt.X('x_column', bin=True),
#     y='count()'
#
# )

# histogram.show()

# Use Altair to create a box plot of the data
# boxplot = alt.Chart(df).mark_boxplot().encode(
#     y='y_column'
# )

# boxplot.show()

# Use Altair to create a scatter matrix of the data
# matrix = alt.Chart(df).mark_circle().encode(
#     alt.X('x_column:Q', scale=alt.Scale(zero=False)),
#     alt.Y('y_column:Q', scale=alt.Scale(zero=False)),
#     color='y_column:Q',
#     size='y_column:Q'
# ).properties(
#     width=150,
#     height=150
# ).facet(
#     row='y_column:Q',
#     column='x_column:Q'
# )

# matrix.show()
