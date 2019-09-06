
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools as it


class Bivariate:    
    
    def __init__(self, df):
        
        self.df = df
        self.cat = [c for i, c in enumerate(df.columns) if df.dtypes[i] in [np.object]]
        self.quant = [c for i, c in enumerate(df.columns) if df.dtypes[i] in [np.int64,np.float64]]

    def bi(self):
        

        def plot(ab,type):
            if len(ab) == 1:
                cols = 1
            elif len(ab) == 2:
                cols = 2
            else:
                cols = 3


            if len(ab) % cols !=0:
                rows = (len(ab) // cols) + 1
            else :
                rows = len(ab) // cols

            if type == "qq":
                fig = plt.figure(figsize = (30,30))
                for index,b in enumerate(ab):
                    axis = fig.add_subplot(rows,cols,index+1)
                    sns.scatterplot(b[0],b[1],data = self.df,ax = axis)
                plt.tight_layout()
                plt.show()



            if type == "cq":
                fig = plt.figure(figsize = (30,30))
                for index,b in enumerate(ab):
                    axis = fig.add_subplot(rows,cols,index+1)
                    sns.boxplot(b[0],b[1],data = self.df,ax=axis)
                plt.tight_layout()
                plt.show()



        qq = list(it.combinations(self.quant,2))  
        cq = list(it.product(self.cat,self.quant))
        
        plot(qq,'qq')
        plot(cq,'cq')




