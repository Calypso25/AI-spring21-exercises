from autoviz.AutoViz_Class import AutoViz_Class
AV = AutoViz_Class()
import pandas as pd
df = pd.read_csv(r'C:\Users\gabri\Documents\Github\AI-spring21-exercises\M4_Feature_Eng\Datasets\predict-future-sales\sales_train.csv')
AV.AutoViz(df)