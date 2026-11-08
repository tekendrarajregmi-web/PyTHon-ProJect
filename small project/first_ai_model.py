from sklearn.tree import DecisionTreeClassifier as dtc

# Added the missing comma between the 4th and 5th items
x_train = [ 
    [150,6], [130,6.8], [125,5.9], [124,5.5], 
    [100,4], [90,3.8], [95,4], [90,3] 
]
y_train = [ "Apple", "Apple", "Apple", "Apple", "orange", "orange", "orange", "orange" ]

model = dtc()
model.fit(x_train, y_train)

x_test = [[123,5.9]]
prediction = model.predict(x_test)

print("predict output is: ", prediction[0])
