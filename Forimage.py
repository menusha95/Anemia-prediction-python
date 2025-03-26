from sklearn import model_selection
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.model_selection import train_test_split
from pandas.plotting import scatter_matrix

url = ('/Users/menusha/Desktop/TestPY/Anemia_NEW_edit.csv')
anemia = pd.read_csv(url, header = 0)
anemia['class'].value_counts()

scatter_matrix(anemia)
plt.show()

