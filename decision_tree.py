#-------------------------------------------------------------------------
# AUTHOR: Abdur Rahman
# FILENAME: decision_tree.py
# SPECIFICATION: Builds a decision tree using the ID3 algorithm for contact lens recommendation
# FOR: CS 4210- Assignment #1
# TIME SPENT: 1 hour
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
import copy

from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

X = copy.deepcopy(db)
ones = ["Young","Myope","No","Normal","No"]
twos = ["Presbyopic","Hypermetrope","Yes","Reduced","Yes"]
#transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
i = 0
while i< len(X):
    j=0
    while j< len(X[i])-1:
        if(X[i][j] in ones):
            X[i][j] = 1
        elif(X[i][j] in twos):
            X[i][j] = 2
        else:
            X[i][j] = 3
        j+=1
    del X[i][-1]
    i+=1


#transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
# Y =
i = 0
while i< len(db):
    current = 0
    if(db[i][4]=="No"):
        current = 1
    else:
        current = 2
    Y.append(current)
    i+=1

print(Y)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy', )
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()
