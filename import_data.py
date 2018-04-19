from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd


file = r'data/DST/SP2_0C_DST/02_24_2016_SP20-2_0C_DST_80SOC.xls'
df = pd.read_excel(open(file,'rb'), sheet_name='Channel_1-006')


# get colum names
# print(list(df))

print(df['Current(A)']).plot()
