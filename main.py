import pandas as pd

df = pd.read_csv("Dados aula 1.csv", encoding="UTF-8", sep=";", usecols=["AddressID"])

print(df.head())
