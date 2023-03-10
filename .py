# Importing the libraries 
import pandas
from openpyxl import load_workbook

# Loading the datasets
Diabetes_Data = pandas.read_csv('data/diabetic_data.csv')
IDs_Mapping_Data_Dictionaries = load_workbook('data\IDs_mapping.xlsx')

### Extracting the data dictionaries from the IDs_mapping Excel file in order to map the categorical columns to their corresponding values
IDs_Data_Dictionaries = {}
# Iterating through the sheets in the Excel file and creating a dictionary for each sheet
for sheet_name in IDs_Mapping_Data_Dictionaries.sheetnames:
    IDs_Mapping_Data_Dictionaries = pandas.read_excel('data\IDs_mapping.xlsx', sheet_name=sheet_name)
    Dictionary_Name = sheet_name.replace(" ", "_").lower()
    Data_Dictionary = dict(zip(IDs_Mapping_Data_Dictionaries.iloc[:, 0], IDs_Mapping_Data_Dictionaries.iloc[:, 1]))
    IDs_Data_Dictionaries[Dictionary_Name] = Data_Dictionary
# Mapping the categorical columns to their corresponding values
for Dictionary_Name, Data_Dictionary in IDs_Data_Dictionaries.items():
    Matching_Columns = [col for col in Diabetes_Data.columns if col == Dictionary_Name]
    for col in Matching_Columns:
        Diabetes_Data[col] = Diabetes_Data[col].map(Data_Dictionary)



### Creating data dictionaries for specific categorical columns 
# Assigning the desired columns to a list
columns = ['race', 'gender', 'age', 'weight', 'admission_type_id', 'discharge_disposition_id', 'admission_source_id', 'payer_code', 
           'medical_specialty', 'max_glu_serum', 'A1Cresult', 'metformin', 'insulin', 'change', 'diabetesMed', 'readmitted']
# Defining a function to create data dictionaries for the desired columns
def create_data_dictionary(Diabetes_Data, columns):
    data_dictionaries = {}
    for col in columns:
        unique_values = Diabetes_Data[col].unique()
        data_dict = dict(zip(unique_values, range(len(unique_values))))
        data_dictionaries[col] = data_dict
        print(f"Data Dictionary for df.{col}:")
        print(data_dict)
        print()
    return data_dictionaries
data_dictionaries = create_data_dictionary(Diabetes_Data, columns)



### Cleaning the dataset
# Replacing '?' and empty cells with NaN
Diabetes_Data.replace('?', pandas.np.nan, inplace=True)
Diabetes_Data.replace('', pandas.np.nan, inplace=True)
# Dropping the cells with Nan values
Diabetes_Data = Diabetes_Data.dropna()
# Counting the number of NaN values remaining in each column to ensure dataset was cleaned properly
print(Diabetes_Data.isna().sum())



### Reformatting Categorical Columns with their corresponding dictionary values
for col, data_dict in data_dictionaries.items():
    Diabetes_Data[col].replace(data_dict, inplace=True)
### Exporting the data dictionaries to an Excel file
writer = pandas.ExcelWriter('data/diabetic_data_dictionaries.xlsx')
for col, data_dict in data_dictionaries.items():
    pandas.DataFrame.from_dict(data_dict, orient="index").to_excel(writer, sheet_name=col)
writer.save()



### Removing the unwanted columns
Diabetes_Data = Diabetes_Data [['encounter_id', 'patient_nbr', 'race', 'gender', 'age', 'weight', 'admission_type_id', 'discharge_disposition_id', 'admission_source_id',
            'payer_code', 'medical_specialty', 'max_glu_serum', 'A1Cresult', 'metformin', 'insulin', 'change', 'diabetesMed', 'readmitted']]
### Exporting the cleaned dataset
Diabetes_Data.to_csv('New_Diabetic_Data.csv', index=False)