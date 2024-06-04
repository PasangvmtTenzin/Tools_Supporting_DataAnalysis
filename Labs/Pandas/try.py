import pandas as pd
import numpy as np


column = [1, 2, 4, 3]
row = [6, 7, 7, 8]

column = pd.DataFrame({'column':column, 'ok':row})

print(column)