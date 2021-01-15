"""
    Autorzy: Tomasz Mnich, Wojciech Szypelt
    Program klasyfikujący Irysy

"""

"""
    Import wymaganych pakietów w celu obslugi programu
"""

from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC


"""
     Zaladowanie odpowiedniej bazy danych z danymi do klasyfikatora
"""
iris_data = read_csv('iris.csv')

"""
    Podział danych na podzbiory do nauki i testowania
"""
D = iris_data.values
X = D[:, 0:4]
y = D[:, 4]
X_tr, X_ts, y_tr, y_ts = train_test_split(X, y, test_size=0.25)

"""
    Wyswietlenie bazy danych
"""
print(D)

"""
    Szkolenie klasyfikatorów przy użyciu SVC
"""
model = SVC()
model.fit(X_tr, y_tr)

"""
    Wizualizacja nieudana i udana (Alfa testy) 
"""
# # Decision Trees classifier
# params = {'random_state': 0, 'max_depth': 8}
# classifier = DeciscionTreeClassifier(**params)
predict_flower = model.predict(X_ts)
print("Accuracy: ", accuracy_score(y_ts, predict_flower))


