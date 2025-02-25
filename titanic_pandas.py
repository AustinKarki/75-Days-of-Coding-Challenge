# -*- coding: utf-8 -*-
"""Titanic Pandas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jF8NEJ5vMMW5DyjtzwdcxZzTBPryQgWp
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
df=pd.read_csv("/content/drive/MyDrive/Techaxis/Titanic-Dataset.csv")
df

import numpy as np

df.head(10)

df.sample(10)

df.tail(10)

df.shape

df.info()

df.isnull().sum()

df.describe()

df[["Name","Age","Survived"]].head(5)

a=df.loc[(df["Sex"]=="female") & (df["Survived"]==1)]
a

b=df.loc[df["Age"] < 18]
b

df["FamilySize"]=df["SibSp"]+df["Parch"] +1 #as family size cannot be zero
df

passenger = (df["Pclass"] == 1) & (df["Survived"] == 1)
df.loc[passenger]

df["Age"].median()

df=df.fillna(df["Age"].median())
df

df.loc[df["Fare"] > 75]

y = lambda x: "Adult" if (x>18 and x<60) else "Child" if x <18 else "Seniour"
df["Age Category"]= df["Age"].apply(y)
df

df["Age Category"].value_counts()

w=df.groupby("Pclass")

w["Fare"].mean()

r=df.groupby("Embarked")

r["Fare"].mean()

w["Survived"].sum()

df["Age"].agg(["max","min"])

df.loc[df["Age"]==0.42]