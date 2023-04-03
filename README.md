# HHA 550 - Diabetic Data 

.py File: 

From an analytical standpoint, the dataset is very massive and contains a significant portion of missing and unidentifiable data. In addition to this, it contains a lot of columns with categorical, non-binary, and non-continuous data. The main goal of this assignment was to clean, organize and prepare the data. 
The Python script I generated performs various operations on the diabetes dataset. I started by first importing the required libraries, including pandas, numpy, and load_workbook from openpyxl.
To start I went through the dataset to see what I felt needed changing/reformatting. First I reformatted the dataset by replacing the 'ch' values in the 'change' column with 'change'. This was simply my preference. I then defined a function named 'group_by_range' to group the values in a column by a specified range. The function itself takes in a dataframe, column name, and a range number as inputs, and returns a sorted dataframe with the values in the specified column grouped by a specified range. I then utilized the 'group_by_range' function on the 'time_in_hospital', 'num_lab_procedures', 'num_medications', 'number_outpatient', 'number_emergency', 'number_inpatient', and 'number_diagnoses' columns of the dataset. I did this as these columns had numerical values that I first wanted to convert to a categorical range to allow for numerical categorical conversion later. 

Next, I utilized the data dictionaries with the 'IDs_mapping.xlsx' to remap the numerical values of the  admission_type_id, discharge_disposition_id, and admission_source_id columns in the dataset with the data dictionary descriptions from the 'IDs_mapping.xlsx' file. I then reformated the 'diag_1', 'diag_2', and 'diag_3' columns into their ICD-9 code descriptions. First I replaced 'E' and 'V' character values within these columns with '10' and '20', respectively. This would allow me to round up the decimal values within the 3 columns. After this, I defined a dictionary named icd_code_ranges that maps ranges of ICD codes to their associated descriptions. I then wrote a function called "icd_code_to_description" that takes a number as input and returns its corresponding description according to the icd_code_ranges dictionary. By doing so I was able to apply the icd_code_to_description function to each of the 'diag_1', 'diag_2', and 'diag_3' columns to convert their values to their respective ICD code descriptions.
After this step, all the columns within the diabetic dataset were now in categorical format and I could move ahead with generating the data dictionaries for each column and reassigning the categorical values to numerical categorical. To accomplish this I first defined a list of categorical columns of interest and then generated a function called "create_data_dictionary" to create a data dictionary for each categorical column. For each column, the function extracts the unique values, assigns each a unique integer value, and stores the mapping in a dictionary. The function prints the resulting data dictionary for each column and returns all the data dictionaries. With the data dictionaries generated, I could quickly clean the data by replacing any/all cells containing '?' with NaN. After cleaning the dataset I could then take data dictionaries I created from the dataset prior to reformatting the columns of the dataset. As such, I replaced the categorical value with its corresponding integer value in the data dictionary. Finally, I exported the data dictionaries to an Excel file and the updated diabetic data to a CSV file.


.ipynb File:

