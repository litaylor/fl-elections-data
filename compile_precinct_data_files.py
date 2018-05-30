import csv
import pandas as pd
import numpy as np
import os
from os import listdir

precinct_files = os.listdir('data/2012')

i = 0

all_data = []

for precinct_file in precinct_files:
    print(precinct_file)
    precinct_data = pd.read_csv('data/2012/'+precinct_file,delimiter='\t', header=None)
    precinct_data.columns = ['County_Code','County_Name','Election_Number','Election_Date','Election_Name','Unique_Precinct_Identifier','Precinct_Polling_Location','Total_Registered_Voters','Total_Registered_Republicans','Total_Registered_Democrats','Total_Registered_All_Other_Parties','Contest_Name','District','Contest_Code','Candidate','Candidate_Party','Candidate_Florida_Voter_Registration_Sytem_ID_Number','DOE_Assigned_Candidate_Number','Vote_Total']
    precinct_president_data = precinct_data[precinct_data['Contest_Code'] == 100000]
    all_data.append(precinct_president_data)
    # if i<2:
    #     i+=1

all_data = pd.concat(all_data, axis=0)
all_data.columns = ['County_Code','County_Name','Election_Number','Election_Date','Election_Name','Unique_Precinct_Identifier','Precinct_Polling_Location','Total_Registered_Voters','Total_Registered_Republicans','Total_Registered_Democrats','Total_Registered_All_Other_Parties','Contest_Name','District','Contest_Code','Candidate','Candidate_Party','Candidate_Florida_Voter_Registration_Sytem_ID_Number','DOE_Assigned_Candidate_Number','Vote_Total']

print(all_data)
all_data.to_csv('data/2012_presidential.csv', sep=',', encoding='utf-8')
