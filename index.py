import numpy as np
import pandas as pd
import lab3

pd.set_option('precision', 2)
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)
pd.set_option('display.width', 1000)

df = pd.read_csv('mlbootcamp5_train.csv', ';')

lab3.question_1(df)
lab3.question_2(df)
lab3.question_3(df)
lab3.question_4(df)
lab3.question_5(df)
lab3.question_6(df)
lab3.question_7(df)
