import pandas as pd

#INPUT

#INITIALIZING MATRIX

s=[]
df=pd.DataFrame(columns=list(' '+A), index=list(' '+B)) #empty matrix leave a space at 1st column and row

def overlap():


#initialize first row to every sequence
for c in range(len(s)+1): #since we added a space to build the matrix correctly we need to add 1 to the length of the string in order to reach the end
    df.iloc[0, c] =0

#initialize first column to every sequence
for r in range(len(s)+1):
    df.iloc[r, 0]= 0



