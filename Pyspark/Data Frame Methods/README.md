# DataFrame Methods Overview: 

DataFrames are a fundamental structure in data processing and analysis, resembling a table with rows and columns. In this guide, we'll explore various methods used with DataFrames, specifically focusing on three categories: Actions, Tranformations, and Functions/Methods

## 1. Actions

Actions are operations that trigger computation and return values. They are used to view or retrieve data from a DataFrame.

### Examples
    ```
        df.show()  # Displays the first 20 rows of the DataFrame
        num_rows = df.count() # Gets the total row count
        first_row = df.first() # Retrieves the first rows
        first_n_rows = df.take(5) # Retrieves the first 5 rows
        rows = df.collect() # Collects all rows into a list
    ```
## 2. Transformations

Transformations are operations tjat produce new DataFrames. They do not trigger computation immediately but define a new DataFrame based on the transformation applied.

### Examples
     ```
        filtered_df = df.filter(df['age'] > 30) # Filters row where age is grater than 30
        selected_df = df.select('name','age') # Selects only the 'name' and 'age' columns
        grouped_df = df.groupBy('department').count() # Groups by 'department' and counts rows in each group
        sorted_df = df.orderBy(df['age'].desc()) # Sorts by 'age' in descending order
     ```

## 3. Functions/Methods

Functions/Methods are utilities that allow for manipulation of DataFrames, including column operations, type conversion, and handling missing data

### Examples

1. **Column Operations: 'withColumn','drop','rename'**
      ```
        modified_df = df.withColumn('age_double', df['age'] * 2)  # Adds a new column with age doubled
        
      ```
2. **Type conversion: cast.**
      ```
        df_with_casted_column = df.withColumn('age', df['age'].cast('string'))  # Casts the 'age' column to string type

      ```

3. **Handling missing data: fillna, dropna**

    ```
       df_no_nulls = df.fillna({'age': 0})  

    ```

### Conclusion

Data Frames offer a wide range of methods for data manipulation and analysis. Understanding the differences between Actions, Transformations, and Functions/Methods is crucial in effectively utilizing DataFrames in data processing and analysis.


    

