"""

    Autorzy: Tomasz Mnich, Wojciech Szypelt
    Program klasyfikujący złożoność przetwarzania książek przygotowanych do druku
    w programie Indesign na ePub-y w trzystopniowej skali trudności.
    Liczba danych na dzień dzisiejszy jest zbyt mała aby uzyskać wysoką dokładność.

    Parametry wejsciowe:
    filesSize, files, pages, characterStyles, paragraphStyles,
    cellStyles, tableStyles, tables, objectStyles, stories, paragraphs,
    vectorGraphics, rasterGraphics, languages, fonts, groups, characterStylesRanges.

"""

"""
    Import wymaganych pakietów w celu obslugi programu
"""
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np


"""
     Zaladowanie odpowiedniej bazy danych z danymi do klasyfikatora
"""
book_data = read_csv('book.csv')
"""
    Podział danych na podzbiory do nauki i testowania
"""
D = book_data.values
X = D[:, 1:-1]
y = D[:, -1]
X_tr, X_ts, y_tr, y_ts = train_test_split(X, y, test_size=0.25)

"""
    Wyswietlenie bazy danych
"""

print(D)

"""
    Szkolenie klasyfikatorów przy użyciu SVC
"""
model = SVC(kernel='linear', C=1, gamma=1)
model.fit(X_tr, y_tr)

"""
    Wizualizacja nieudana i udana (Alfa testy) 
"""
#  Decision Trees classifier
# params = {'random_state': 0, 'max_depth': 8}
# classifier = DeciscionTreeClassifier(**params)
# Step 5: Check classifier accuracy on test data and see result
predict_book = model.predict(X_ts)
print("Accuracy: ", accuracy_score(y_ts, predict_book))

x_min, x_max = X[:, 2].min() - 1, X[:, 2].max() + 1
y_min, y_max = X[:, -7].min() - 1, X[:, -7].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max), np.arange(y_min, y_max))
plt.plot(1, 1, 1)

# print(np.c_[xx.ravel(), yy.ravel()])
# Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
# Z = Z.reshape(xx.shape)

plt.xlabel('Liczba stron')
plt.ylabel('Liczba akapitów')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('Stopień trudność przetwarzania książek na ePub-y')
plt.show()

