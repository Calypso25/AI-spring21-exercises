import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv(r'C:\Users\gabri\Documents\Github\AI-spring21-exercises\M4_Feature_Eng\FE7 - Optuna\oct2015.csv')

design_report = ProfileReport(df)
design_report.to_file(output_file='report.html')