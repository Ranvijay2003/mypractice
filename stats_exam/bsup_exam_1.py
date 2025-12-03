import pandas as panda

df=panda.read_csv("prac1.csv")
print(df.head())

score=df['marks']
print("\n---statis result")
print("mean:",score.mean())
print("median:",score.median())
print("mode:",score.mode())