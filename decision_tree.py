from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.tree import DecisionTreeClassifier

from data import y_to_float


def run_decision_tree(X_train, X_test, y_train, y_test):
    y_train_f = y_to_float(y_train)
    y_test_f = y_to_float(y_test)

    classifier = DecisionTreeClassifier()
    classifier.fit(X_train, y_train_f)
    y_pred = classifier.predict(X_test)

    print("Decision Tree")
    print(confusion_matrix(y_test_f, y_pred))
    print(classification_report(y_test_f, y_pred))
    print(accuracy_score(y_test_f, y_pred))
