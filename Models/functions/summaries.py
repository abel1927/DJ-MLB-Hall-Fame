from sklearn.metrics import accuracy_score, roc_auc_score

def summary(clf, X_test, y_test, name):
    print(f"Clasificador --> {name}")
    print("--------------------------")
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test,y_pred)
    print(f"ACC:{round(acc*100,3)}") 

    y_probs = clf.predict_proba(X_test)
    auc = roc_auc_score(y_test, y_probs[:,1])
    print(f"AUC: {round(auc, 4)}")
    print("---------------------------")