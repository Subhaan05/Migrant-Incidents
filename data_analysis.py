# Importing Modules
import pandas as pd
import matplotlib.pyplot as plt

# Function to clean the data
def cleaning_data():
    # Reading the dataset
    data = pd.read_csv('Missing_Migrants_Global_Figures_allData.csv')

    # Columns dropping
    unwanted_columns = ['Main ID', 'Incident ID', 'UNSD Geographical Grouping', 'URL', 'Source Quality', 'Information Source']
    data = data.drop(columns=unwanted_columns)

    # Columns renaming
    columns_names = {
        'Region of Incident': 'Incident Region',
        'Date of Incident': 'Incident Date',
        'Year of Incident': 'Incident Year',
        'Number of Dead': 'Death Toll',
        'Minimum Estimated Number of Missing': 'Estimated Missing Count',
        'Total Number of Dead and Missing': 'Total Missing and Dead',
        'Number of Survivors': 'Survivors Count',
        'Number of Females': 'Females Count',
        'Number of Males': 'Males Count',
        'Number of Children': 'Children Count',
        'Country of Origin': 'Origin Country',
        'Region of Origin': 'Origin Region',
        'Country of Incident': 'Incident Country',
        'Location of Death': 'Incident Location',
    }
    data.rename(columns=columns_names, inplace=True)

    # Set Null to 0 for death toll
    data['Death Toll'] = data['Death Toll'].fillna(0)

    return data

data = cleaning_data()

#Visualisations

# Yearly Trends in Migrant Deaths and Missing Cases
yearly = data.groupby('Incident Year')[['Death Toll', 'Estimated Missing Count',]].sum()
yearly.plot(kind='bar', figsize=(12, 8), stacked=True, edgecolor='black')
plt.title('Yearly Trends in Migrant Deaths and Missing Cases')
plt.ylabel('Count')
plt.xlabel('Year')
plt.xticks(rotation=0)
plt.legend(loc="upper left")
plt.savefig('Visualisations/yearly_trends.png')
