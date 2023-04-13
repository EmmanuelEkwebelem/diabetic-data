# HHA 550 - Diabetic Data 

.py File: 

From an analytical standpoint, the dataset is very massive and contains a significant portion of missing and unidentifiable data. In addition to this, it contains a lot of columns with categorical, non-binary, and non-continuous data. The main goal of this assignment was to clean, organize and prepare the data. 
The Python script I generated performs various operations on the diabetes dataset. I started by first importing the required libraries, including pandas, numpy, and load_workbook from openpyxl.
To start I went through the dataset to see what I felt needed changing/reformatting. First I reformatted the dataset by replacing the 'ch' values in the 'change' column with 'change'. This was simply my preference. I then defined a function named 'group_by_range' to group the values in a column by a specified range. The function itself takes in a dataframe, column name, and a range number as inputs, and returns a sorted dataframe with the values in the specified column grouped by a specified range. I then utilized the 'group_by_range' function on the 'time_in_hospital', 'num_lab_procedures', 'num_medications', 'number_outpatient', 'number_emergency', 'number_inpatient', and 'number_diagnoses' columns of the dataset. I did this as these columns had numerical values that I first wanted to convert to a categorical range to allow for numerical categorical conversion later. 

Next, I utilized the data dictionaries with the 'IDs_mapping.xlsx' to remap the numerical values of the  admission_type_id, discharge_disposition_id, and admission_source_id columns in the dataset with the data dictionary descriptions from the 'IDs_mapping.xlsx' file. I then reformated the 'diag_1', 'diag_2', and 'diag_3' columns into their ICD-9 code descriptions. First I replaced 'E' and 'V' character values within these columns with '10' and '20', respectively. This would allow me to round up the decimal values within the 3 columns. After this, I defined a dictionary named icd_code_ranges that maps ranges of ICD codes to their associated descriptions. I then wrote a function called "icd_code_to_description" that takes a number as input and returns its corresponding description according to the icd_code_ranges dictionary. By doing so I was able to apply the icd_code_to_description function to each of the 'diag_1', 'diag_2', and 'diag_3' columns to convert their values to their respective ICD code descriptions.
After this step, all the columns within the diabetic dataset were now in categorical format and I could move ahead with generating the data dictionaries for each column and reassigning the categorical values to numerical categorical. To accomplish this I first defined a list of categorical columns of interest and then generated a function called "create_data_dictionary" to create a data dictionary for each categorical column. For each column, the function extracts the unique values, assigns each a unique integer value, and stores the mapping in a dictionary. The function prints the resulting data dictionary for each column and returns all the data dictionaries. With the data dictionaries generated, I could quickly clean the data by replacing any/all cells containing '?' with NaN. After cleaning the dataset I could then take data dictionaries I created from the dataset prior to reformatting the columns of the dataset. As such, I replaced the categorical value with its corresponding integer value in the data dictionary. Finally, I exported the data dictionaries to an Excel file and the updated diabetic data to a CSV file.


.ipynb File:

The Jupyter Notebook code provided aims to gain insights and explore the dataset related to diabetic patients and their readmission within 30 days. The first section assesses the distribution of patients who had a readmission within 30 days versus those who did not. The code highlights the count and percentage of patients who were readmitted within 30 days. The associated histogram highlights the imbalance within the dataset as only 11.23% of patients were readmitted within 30 days. The missingness within the data was assessed with the missing() function, which indicated both the number and percentage of missing values in each column of the dataset. The weight column had the most missing data at 98% followed by the medical specialty column at 49%. After this, the missingno package was used to visualize the missing data in a bar and matrix plot.  The univariate analysis was used to illustrate the numerical features of the dataset, such as age, time in the hospital, and the number of medications in order to identify any potential relationships or patterns in the data. Additionally, the skewness of each column was calculated, providing insight into the distribution of the data. Finally, the code calculates the correlation matrix of the dataset and identifies the top 10 features that are most strongly correlated with the target variable, for example, the number of inpatient visits and procedures, have a moderately positive correlation with readmitted. This might suggest that patients with a high number of inpatient visits or procedures may be more likely to have a readmission within 30 days. Overall, the goal of the notebook was to provide insights into the diabetic patient data and the readmission rates within 30 days through the use of many techniques including analysis and visualization.

The next few sections contain the machine learning process which involves several steps, starting from cleaning and preprocessing the data to evaluating the performance of the model. For our analysis, we began by dropping columns that were either missing data or columns that we did not consider relevant for the ML. After this, duplicates within the dataset were assessed and removed. With the cleaning and preprocessing completed, we moved onto splitting the data into train, validation, and test sets. The dataset that we worked with in this analysis was imbalanced, meaning that the number of patients that were <30 readmitted was significantly less represented >30 readmitted. To address this imbalance, we employed a technique called oversampling, where we sampled the minority class to match the size of the majority class. This resulted in a balanced dataset, which allowed us to build a model that performed better on both classes. We then standardized the data using the StandardScaler from Scikit-learn to ensure that all features have the same scale. Next, we created linear and logistic regression, KNN, stochastic gradient descent, and K-means models and evaluated their performance on the validation set. We calculated various metrics, including AUC, accuracy, recall, precision, specificity, and prevalence, to assess the model's performance.
The Linear Regression algorithm resulted in an AUC of 0.564, an accuracy of 0.549, a recall of 0.546, a precision of 0.134, and a specificity of 0.549. The Logistic Regression algorithm had similar results with an AUC of 0.564, an accuracy of 0.564, a recall of 0.529, a precision of 0.136, and a specificity of 0.568. The K-Nearest Neighbors algorithm performed slightly better with an AUC of 0.576, an accuracy of 0.615, a recall of 0.497, a precision of 0.147, and a specificity of 0.542. The Stochastic Gradient Descent algorithm had similar results to Logistic Regression with an AUC of 0.564, an accuracy of 0.564, a recall of 0.529, a precision of 0.136, and a specificity of 0.568. The K-Means algorithm, with three clusters, resulted in an AUC of 0.482, an accuracy of 0.676, a recall of 0.233, a precision of 0.101, and a specificity of 0.733.

Overall, the K-Nearest Neighbors algorithm resulted in the best outcome for this dataset. It had the highest accuracy and specificity, which means that it correctly predicted the positive cases and negative cases with high accuracy. However, the precision was still relatively low, indicating that there were some false positives.

