import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("prac2.csv")
print(df.head())

for col in df.select_dtypes(include=['object']).columns:
    df[col].value_counts().plot(kind='bar',color="skyblue")
    plt.title(f"Frequency Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.show()
    
for col in df.select_dtypes(include=['int64','float64']).columns:
    plt.hist(df[col],bins=10,color="lightgreen",edgecolor='black')
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()