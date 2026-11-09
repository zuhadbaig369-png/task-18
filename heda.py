import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('StudentsPerformance.csv')

data.head(5)
data.isnull().sum()
data.describe()

labels = ["gender", "race/ethnicity", "parental level of education", "lunch", "test preparation course", "math score", "reading score", "writing score"]

for label in labels:
    print('Distribution of', label)
    sns.countplot(x=data[label])
    plt.show()

l = ["race/ethnicity", "parental level of education"]

for label in l:
    print('Distribution of', label)
    plt.pie(x=data[label].value_counts(), labels=data[label].unique())
    plt.show()

a = ["lunch", "race/ethnicity"]

for label in a:
    print('Distribution of', label)
    sns.countplot(x=data[label], hue=data["gender"])
    plt.show()

b = ["math score", "reading score", "writing score"]

print(data[b].skew().astype(np.int64))