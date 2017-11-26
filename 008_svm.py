from sklearn import svm
import pickle
import pandas

#dataframe = pandas.read_csv("file name")

#array = dataframe.values

# kernel = 'rbf' 


model = svm.svc(kernel='linear',c=1,gamma=1)
model.fit(X_train,y_train)
model.score(X_train,y_train)

#predict
predicted = model.predict(x_test)

