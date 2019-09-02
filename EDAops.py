import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import itertools as it


def plot(df,ab,type):
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
            sns.scatterplot(b[0],b[1],data = df,ax = axis)
        plt.tight_layout()
        plt.show()

        
        
    if type == "cq":
        fig = plt.figure(figsize = (30,30))
        for index,b in enumerate(ab):
            axis = fig.add_subplot(rows,cols,index+1)
            sns.boxplot(b[0],b[1],data = df,ax=axis)
        plt.tight_layout()
        plt.show()
    
   
    
def bivariate(df):
    numerical = list(df.select_dtypes(include = 'number').columns)
    categorical = list(df.select_dtypes(include = 'object').columns)

    qq = list(it.combinations(numerical,2))  ###list of tuples
    cq = list(it.product(categorical,numerical))

    plot(df,qq,type = "qq")
    plot(df,cq,type = "cq")



if __name__ == "__main__":
    df = pd.read_csv("train.csv")
    df['Survived'] = df['Survived'].astype("object")
    df['Pclass'] = df['Pclass'].astype("object")
    df['SibSp'] = df['SibSp'].astype("object")
    df['Parch'] = df['Parch'].astype("object")
    df.drop(columns = ['PassengerId','Name','Ticket','Cabin'],inplace = True)
    bivariate(df)






    
