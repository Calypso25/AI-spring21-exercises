import pandas as pd

import sweetviz as sv

df = pd.read_csv(r'C:\Users\gabri\Documents\Github\AI-spring21-exercises\M4_Feature_Eng\Datasets\predict-future-sales\sales_train.csv')

sweet_report = sv.analyze(df)
sweet_report.show_html('sweet_report.html')