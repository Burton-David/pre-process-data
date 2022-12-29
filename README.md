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

## API_importer
This class provides a variety of functions for retrieving data from an API and returning it as a Pandas DataFrame. The get_data function sends a request to the API and returns the data as a DataFrame. The other functions build on this function to provide additional functionality, such as pagination, date range filtering, location filtering, ID-based filtering, and search query-based filtering.

To use these functions, you would first create an instance of the APIImporter class, passing in the API URL as an argument. Then, you could call any of the functions on the instance, passing in the necessary arguments. For example:
~~~api = APIImporter('https://my-api.com')
df = api.get_data('endpoint', params={'param1': 'value1', 'param2': 'value2'})~~~ 

## data_encoder
This class provides a variety of functions for encoding and decoding data. The base64_encode and base64_decode functions use base64 encoding to encode and decode data. The rot13_encode and rot13_decode functions use ROT13 encoding to encode and decode data. The xor_encode and xor_decode functions use XOR encryption to encode and decode data.

To use these functions, you would first create an instance of the DataEncoder class. Then, you could call any of the functions on the instance, passing in the necessary arguments. For example:

~~~encoder = DataEncoder()
encoded_data = encoder.base64_encode(b'Hello, World!')
print(encoded_data)  # Output: SGVsbG8sIFdvcmxkIQ==
decoded_data = encoder.base64_decode(encoded_data)
print(decoded_data)  # Output: b'Hello, World!'~~~

