from pandas import Series
from numpy import mean
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedKFold

def clasifier_ft_importance_experiments(clsf_instance, data_features, target, is_coef=False, n_splits=50):
    sk = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=737)
    features_imp = Series([0]*len(data_features.columns), index=data_features.columns)
    fold = 0
    for train_idx, _ in sk.split(data_features, target):
        fold += 1
        X_train = data_features.loc[train_idx]
        y_train = target.loc[train_idx]
        clsf_instance.fit(X_train, y_train)
        feat_imp = None
        if is_coef:
            feat_imp = Series(clsf_instance.coef_[0], index=data_features.columns)
        else:
            feat_imp = Series(clsf_instance.feature_importances_, index=data_features.columns)
        features_imp = features_imp + feat_imp
    features_imp = features_imp.divide(other=fold)
    return features_imp


def plot_feature_importance(feature_imp):
    "Grafica la importancia de cada característica"
    _, axes = plt.subplots(figsize=(10, 6))
    sns.barplot(x=feature_imp, y=feature_imp.index)
    plt.xlabel('Feature Importance Score')
    plt.ylabel('Features')
    plt.title("Visualizing Important Features", pad=15, size=14)