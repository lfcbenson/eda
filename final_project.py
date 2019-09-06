import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import univariate
import bivariate



if __name__ == "__main__":
    data = pd.read_csv('train.csv')
    data.drop(columns=['PassengerId', 'Name', 'Cabin', 'Ticket'], inplace=True)
    f1 = univariate.Univariate(data)
    print(f1.quant_measures())
    print(f1.cat_measures())
    f1.visualize()
    f2 = bivariate.Bivariate(data)
    f2.bi()
