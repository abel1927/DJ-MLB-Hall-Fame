from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression, Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

from Models.functions.learning_curve import learning_curves_describe
from Models.functions.metrics import train_with_cv, show_baseline_score


def performance_comparer(X, y):
    print('DecisionTree Gini depth=4')
    dtg4_clf = DecisionTreeClassifier(criterion='gini', max_depth=4)
    dtg4_metric = train_with_cv(dtg4_clf, X, y, n_splits=50)
    learning_curves_describe(dtg4_clf,X,y)

    print('DecisionTree Entropy depth=4')
    dte4_clf = DecisionTreeClassifier(criterion='entropy', max_depth=4)
    dte4_metric = train_with_cv(dte4_clf, X, y)
    learning_curves_describe(dte4_clf,X,y)

    print('DecisionTree Entropy depth=3')
    dte3_clf = DecisionTreeClassifier(criterion='entropy', max_depth=3)
    dte3_metric = train_with_cv(dte3_clf, X, y)
    learning_curves_describe(dte3_clf,X,y)

    print('DecisionTree Entropy depth=3')
    svmp_clf = SVC(probability=True, kernel='poly')
    svmp_metric = train_with_cv(svmp_clf, X, y)
    learning_curves_describe(svmp_clf,X,y)

    print('SVM kernel=poly')
    svmp_clf = SVC(probability=True, kernel='poly')
    svmp_metric = train_with_cv(svmp_clf, X, y)
    learning_curves_describe(svmp_clf,X,y)

    print('SVM kernel=rbf')
    svmr_clf = SVC(probability=True, kernel='rbf')
    svmr_metric = train_with_cv(svmr_clf, X, y)
    learning_curves_describe(svmr_clf,X,y)

    print('Random Forest estimators=100')
    rfg100_clf = RandomForestClassifier()
    rfg100_metric = train_with_cv(rfg100_clf, X, y)
    learning_curves_describe(rfg100_clf,X,y)

    print('Random Forest estimators=10')
    rfg10_clf = RandomForestClassifier(n_estimators=10)
    rfg10_metric = train_with_cv(rfg10_clf, X, y)
    learning_curves_describe(rfg10_clf,X,y)

    print('Random Forest estimators=5')
    rfg5_clf = RandomForestClassifier(n_estimators=5)
    rfg5_metric = train_with_cv(rfg5_clf, X, y)
    learning_curves_describe(rfg5_clf,X,y)

    print('Naive Bayes')
    nb_clf = GaussianNB()
    nb_metric = train_with_cv(nb_clf, X, y)
    learning_curves_describe(nb_clf,X,y)

    print('3NN')
    knn3_clf = KNeighborsClassifier(n_neighbors=3)
    knn3_metric = train_with_cv(knn3_clf, X, y)
    learning_curves_describe(knn3_clf,X,y)

    print('5NN')
    knn5_clf = KNeighborsClassifier(n_neighbors=5)
    knn5_metric = train_with_cv(knn5_clf, X, y)
    learning_curves_describe(knn5_clf,X,y)

    print('10NN')
    knn10_clf = KNeighborsClassifier(n_neighbors=10)
    knn10_metric = train_with_cv(knn10_clf, X, y)
    learning_curves_describe(knn10_clf,X,y)

    print('GradientBoosting')
    gb_clf = GradientBoostingClassifier(n_estimators=100, max_depth=3)
    gb_metric = train_with_cv(gb_clf, X, y)
    learning_curves_describe(gb_clf,X,y)

    print('LogisticRegression')
    lr_clf = LogisticRegression(max_iter=10000, solver="liblinear")
    lr_metric = train_with_cv(lr_clf, X, y)
    learning_curves_describe(lr_clf,X,y)
    

    label = ['dtg4','dte4', 'dte3','svm_r','svm_p', 'knn5', 'knn3', 'knn10','lr', 'gbc']
    auc_s = [dtg4_metric[1], dte4_metric[1], dte3_metric[1], svmr_metric[1], svmp_metric[1], knn5_metric[1], knn3_metric[1], knn10_metric[1], lr_metric[1], gb_metric[1]]
    acc_s = [dtg4_metric[0], dte4_metric[0], dte3_metric[0], svmr_metric[0], svmp_metric[0], knn5_metric[0], knn3_metric[0], knn10_metric[0], lr_metric[0], gb_metric[0]]
    color = ['blue', 'violet', 'pink', 'green', 'black', 'yellow', 'cyan', 'orange', 'red', 'lime']