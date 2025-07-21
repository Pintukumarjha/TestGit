import pandas as pd

data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}

data1={'Name':['Pintu','Aman'],'Age':[30,40],'Address':['Delhi','Noida']}

df = pd.DataFrame(data)
df1=pd.DataFrame(data1)
#print(df)
print(df1)

#print(df['Name'])  # Output: Series with ['Alice', 'Bob']