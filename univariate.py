import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


class Univariate:
    
    def __init__(self, df):
        self.df = df
        self.cat = [c for i, c in enumerate(df.columns) if df.dtypes[i] in [np.object]]
        self.quant = [c for i, c in enumerate(df.columns) if df.dtypes[i] in [np.int64,np.float64]]
        
    
    def quant_measures(self):

        measures =[]
        for i in self.quant:
            data = {'mean':np.mean(self.df[i]), 
                    'median':self.df[i].median(), 
                    'mode':str(self.df[i].mode()).split('\n')[0].split(' ')[-1], 
                    'Standard Deviation':np.std(self.df[i]),
                    '25th %':self.df[i].quantile(0.25),
                    '75th %':self.df[i].quantile(0.75),
                   }
            measures.append(data)

        return pd.DataFrame(measures, index=[self.quant])
    
    def cat_measures(self):

        measures1 =[]
        for i in self.cat:
            data1 = {'Count':(self.df[i].value_counts()).to_dict(), 
                     'Count%':(self.df[i].value_counts()/self.df.shape[0]*100).round(2).to_dict()
                    }
            
            measures1.append(data1)

        return pd.DataFrame(measures1, index=[self.cat])
    
    
    def visualize(self):
        
        def uni_plot(self,ab,type):

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

            if type=='q_hist':
                plt.figure(figsize=(15,12))
                for i,j in enumerate(ab):
                    plt.subplot(rows,cols,i+1)
                    plt.xlabel(j)
                    plt.ylabel('Frequency')
                    plt.hist(self.df[j])
                plt.show()
            
            if type=='q_box':
                plt.figure(figsize=(15,12))
                for i,j in enumerate(ab):
                    plt.subplot(rows,cols,i+1)
                    plt.xlabel(j)
                    plt.ylabel('Frequency')
                    plt.boxplot(self.df[j])
                plt.show()

            if type=='c_pie':
                plt.figure(figsize=(15,12))
                for i,j in enumerate(ab):
                    plt.subplot(rows,cols,i+1)
                    plt.title(j)
                    plt.pie(self.df[j].value_counts(), labels=list(dict(self.df[j].value_counts()).keys()),
                            shadow=True, autopct='%.2f')
                plt.show()
                    
        uni_plot(self,self.quant,'q_hist')
        uni_plot(self,self.quant,'q_box')
        uni_plot(self,self.cat,'c_pie')