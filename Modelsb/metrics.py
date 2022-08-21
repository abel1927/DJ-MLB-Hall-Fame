from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.metrics import cohen_kappa_score
from sklearn.model_selection import StratifiedKFold
import numpy as np

def train_with_cv(clf, X, y, cv=StratifiedKFold, n_splits=50, verbose=False):
    sk = cv(n_splits=n_splits, shuffle=True, random_state=529)
    fold = 0
    aucs,accs,cks = [],[],[]
    for train_idx, val_idx in sk.split(X, y):
        X_tr = X.loc[train_idx]
        y_tr = y.loc[train_idx]
        X_val = X.loc[val_idx]
        y_val = y.loc[val_idx]
        # Fit Model on Train
        clf.fit(X_tr, np.ravel(y_tr))
        pred_proba = clf.predict_proba(X_val)[:,1]
        pred = clf.predict(X_val)
        auc_score = roc_auc_score(y_val, pred_proba)
        acc_score = accuracy_score(y_val, pred)
        ck_score = cohen_kappa_score(y_val, pred)
        if verbose:
            print(f"======= Fold {fold} ========")
            print(
                f"El AUC en el conjunto de validación es {auc_score:0.4f}"
            )
            print(
                f"El ACC en el conjunto de validación es {acc_score:0.4f}"
            )
            print(
                f"El CK en el conjunto de validación es {ck_score:0.4f}"
            )
        fold += 1
        aucs.append(auc_score)
        accs.append(acc_score)
        cks.append(ck_score)
    oof_auc = np.mean(aucs)
    oof_acc = np.mean(accs)
    oof_cks = np.mean(cks)
    print(f'El resultado AUC promediado es {oof_auc:0.4f}')
    print(f'El resultado ACC promediado es {oof_acc:0.4f}')
    print(f'El resultado CK promediado es {oof_cks:0.4f}')
    return oof_acc, oof_auc, oof_cks
    

def show_baseline_score(y_val, baseline):
    acc_score = accuracy_score(y_pred=baseline, y_true=y_val)
    auc_score = roc_auc_score(y_score=baseline, y_true=y_val)
    print(f"Accuracy: {acc_score:0.4f}")
    print(f"AUC: {auc_score:0.4f}")