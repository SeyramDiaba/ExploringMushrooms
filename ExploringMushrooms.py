import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import codecademylib3

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()

# Graphing each categorical variable using a for loop
for column in columns:
  #print(column)
  sns.countplot(df[column], order = df[column].value_counts().index)
  plt.xticks(rotation =30, fontsize = 10)
  plt.xlabel(column, fontsize = 12)
  plt.title(column + ' Value Counts', fontsize =15)
  plt.show()
  plt.clf()

  # else: 
  #   plt.pie(df[column].value_counts(),labels = df[column])
  #   plt.title(column + ' Value Counts', fontsize =15)
  #   plt.show()
  #   plt.clf()


  # if len(df[column].unique()) < 6:
  #   plt.pie(df[column].value_counts(),labels = df[column])
  #   plt.title(column + ' Value Counts', fontsize =15)
  #   plt.show()
  #   plt.clf()

# Exciting insights about mushroom data
# *Most top surfaces of mushrooms in this dataset are scaly rather than smooth.
# *All mushrooms captured in the dataset have a Veil Type being partial
# *Mushrooms thrive best in the Woods


