# Importing the libraries 
import pandas
# Loading the dataset
Data = pandas.read_csv('data/diabetic_data.csv')



### Creating data dictionaries for specific categorical columns 
# Assigning the desired columns to a list
columns = ['race', 'gender', 'age', 'weight', 'payer_code', 'medical_specialty', 'max_glu_serum', 'A1Cresult', 'metformin', 'insulin', 'change', 'diabetesMed', 'readmitted']
# Defining a function to create data dictionaries for the desired columns
def create_data_dictionary(Data, columns):
    data_dictionaries = {}
    for col in columns:
        unique_values = Data[col].unique()
        data_dict = dict(zip(unique_values, range(len(unique_values))))
        data_dictionaries[col] = data_dict
        print(f"Data Dictionary for df.{col}:")
        print(data_dict)
        print()
    return data_dictionaries
# Calling the function to create the data dictionaries
data_dictionaries = create_data_dictionary(Data, columns)

# Defining a function to group the values in a column by a specified range
def group_by_range(df, col_name, n):
    df_sorted = df.sort_values(col_name)
    min_val = df_sorted[col_name].min()
    max_val = df_sorted[col_name].max()
    num_groups = int((max_val - min_val) / n) + 1
    group_labels = [f"{min_val + i*n}-{min_val + (i+1)*n-1}" for i in range(num_groups)]
    df_sorted[col_name] = pandas.cut(df_sorted[col_name], bins=num_groups, labels=group_labels, include_lowest=True)
    return df_sorted
# Calling the function to group the values in the 'time_in_hospital' column by a range of 5
Data = group_by_range(Data, 'time_in_hospital', 5)


### Cleaning the dataset
# Replacing '?' and empty cells with NaN
Data.replace('?', pandas.np.nan, inplace=True)
Data.replace('', pandas.np.nan, inplace=True)
# Dropping the cells with Nan values
Data = Data.dropna()
# Counting the number of NaN values remaining in each column to ensure dataset was cleaned properly
print(Data.isna().sum())



### Reformatting Categorial Columns with their corresponding dictionary values
for col, data_dict in data_dictionaries.items():
    Data[col].replace(data_dict, inplace=True)



### Exporting the data dictionaries to an Excel file
writer = pandas.ExcelWriter('data/diabetic_data_dictionaries.xlsx')
for col, data_dict in data_dictionaries.items():
    pandas.DataFrame.from_dict(data_dict, orient="index").to_excel(writer, sheet_name=col)
writer.save()



### Removing the unwanted columns
Data = Data [['encounter_id', 'patient_nbr', 'race', 'gender', 'age', 'weight', 'payer_code', 'medical_specialty', 'max_glu_serum', 'A1Cresult', 'metformin', 'insulin', 'change', 'diabetesMed', 'readmitted']]



### Exporting the cleaned dataset
Data.to_csv('data/new_diabetic_data_cleaned.csv', index=False)