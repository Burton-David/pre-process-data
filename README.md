# pre-process-data

## loadCSV.py
This program first tries to load the CSV file with the default arguments of the read_csv function. If that fails, it tries to load the file with a different delimiter (tab-separated values). If that also fails, it tries to load the file with no header row. If all of these attempts fail, it tries to load the file with a different encoding and a different quoting style. If all attempts fail, it raises a ValueError indicating that the CSV file could not be loaded.

Keep in mind that this approach may not work for all CSV files, as the formatting and structure of CSV files can vary widely. In some cases, you may need to manually inspect and pre-process the CSV file before it can be loaded into a Pandas dataframe.<br>

## explore.ipynb
This Jupyter notebook first imports the necessary modules (Pandas, Matplotlib, and Seaborn) and the load_csv function from the loadCSV module. It then prompts the user to enter the name of the CSV file and loads it into a Pandas dataframe using the load_csv function.

Next, it prints the first few rows of the dataframe using the head function and calculates basic statistics for the numerical columns using the describe function. Finally, it uses the Seaborn library to plot a pairplot of the data, and displays the plot using the show function from Matplotlib.

## clean_data.py
This function performs several steps to clean the data in the input dataframe:

It removes rows with missing values using the dropna function.
It drops duplicate rows using the drop_duplicates function.
It replaces invalid or out-of-range values with NaN using the replace function.
It imputes missing values using the median or mode of the respective column, depending on the data type.
It normalizes numerical columns by subtracting the mean and dividing by the standard deviation, using the mean and std functions.
Finally, the function returns the cleaned dataframe.
## plotly_visualzation.py
This script first imports the load_csv function from the loadCSV module, and then prompts the user to enter the name of the CSV file. It loads the CSV file into a Pandas dataframe using the load_csv function, and then uses various Plotly functions from the express module to create different types of plots.

The x_column and y_column variables should be replaced with the names of the columns in the dataframe that you want to use for the x-axis and y-axis, respectively. The specific columns used will depend on the type of plot being created.

To create a specific type of plot, simply uncomment the appropriate lines of code and specify the columns to use. For example, to create a scatter plot, you can uncomment the lines of code that begin with fig = px.scatter, and specify the x_column and y_column to use.

You can also customize the appearance and behavior of the plots by using additional arguments of the Plotly functions and the various functions in the layout module. For more information on using Plotly with Pandas dataframes, you can check the Plotly documentation: https://plotly.com/python/pandas-backend-overview/

## Altair_visualization.py
This script uses the various Altair functions, such as mark_point, mark_line, mark_bar, and mark_boxplot, to create different types of plots. The x_column and y_column variables should be replaced with the names of the columns in the dataframe that you want to use for the x-axis and y-axis, respectively.

To create a specific type of plot, simply uncomment the appropriate lines of code and specify the columns to use. For example, to create a scatter plot, you can uncomment the lines of code that begin with scatter = alt.Chart(df).mark_point, and specify the x_column and y_column to use.

## Seaborn_visualization.py
This script uses the various Seaborn functions, such as scatterplot, lineplot, barplot, histplot, and pairplot, to create different types of plots. The x_column and y_column variables should be replaced with the names of the columns in the dataframe that you want to use for the x-axis and y-axis, respectively.

To create a specific type of plot, simply uncomment the appropriate lines of code and specify the columns to use. For example, to create a scatter plot, you can uncomment the lines of code that begin with sns.scatterplot, and specify the x_column and y_column to use.

You can also customize the appearance and behavior of the plots by using additional arguments of the Seaborn functions.