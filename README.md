# HHA 550 - Assignment # 6

This repository represents the completion of HHA 550 Assignment # 6

Instructions:

Select the provided clinical dataset and perform the ETL process (the same Diabetes Dataset)
Normalize the data  
Create a data dictionary for the data. 
Submit the clean dataset as a csv and the data dictionary as a Word document 

### Thought Process ###

From an analytical standpoint the dataset is very massive and contains a significant portion of missing and unidentifiable data. In addition to this it is made up of a lot of columns with varying data type such as categorical, non-binary, and non-continuous data. The main goal of this assignment was to clean, organize and prepare the data for analysis. To begin, the data dictionary within the "IDs_Mapping" were utilized to convert the numerical values within the 'admission_type_id', 'discharge_disposition_id', and 'admission_source_id' columns to categorical. With this step completed I moved onto assessing and selecting 16 columns within the diabetic_data dataset. 

Columns: ['race', 'gender', 'age', 'weight', 'admission_type_id', 'discharge_disposition_id', 'admission_source_id', 'payer_code', 'medical_specialty', 'max_glu_serum', 'A1Cresult', 'metformin', 'insulin', 'change', 'diabetesMed', 'readmitted']

Data dictionaries were created from these columns using the unique values within those columns. These associated data dictionaries were exported in an excel file (diabetic_data_dictionaries) with each data dictionary represented in its own respective worksheet within the Excel. These data dictionaries were also utilized to remap/reformat the original diabetic_data, converting the data within those columns to numerical. The data was subsequently cleaned by removing any rows empty cells or cells containing "?". The cleanliness of the dataset was also verified. 