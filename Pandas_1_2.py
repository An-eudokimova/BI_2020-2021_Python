# Task_1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv('https://raw.githubusercontent.com/Serfentum/bf_course/master/14.pandas/train.csv')

sns.set(style="darkgrid")
col = sns.color_palette("muted")

train[['A', 'T', 'G', 'C']].plot(kind='bar', stacked=True, figsize=(10, 6))
plt.xlabel("position")
plt.ylabel("Number of reads")
plt.title("Distribution of nucleotide frequencies by position", fontsize=20)
plt.xticks(np.arange(train.shape[0]), train['pos'], fontsize=8, rotation=45)
plt.show()


# Task_2
train_part = train.loc[train.matches > train['matches'].mean()]
train_part = train_part[['pos', 'reads_all', 'mismatches',
                         'deletions', 'insertions']]
# print(train_part.head())
train_part.to_csv("train_part.csv", index=False)