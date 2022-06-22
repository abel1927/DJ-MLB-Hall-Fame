from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

from Models.functions.learning_curve import learning_curves_describe

def print_metric(metric):
    print(f"mACC:{metric[0]}\nmAUC:{metric[1]}")
    print("<----------------------------------->\n")

def plot_scenario(label,auc_s,acc_s,color):
    fig, ax = plt.subplots()
    ax.set_xlabel("ROC_AUC")
    ax.set_ylabel("ACC")
    for i in range(len(label)):
        ax.scatter(auc_s[i], acc_s[i], c=color[i],label=label[i],
                   alpha=1, edgecolors='none')
    ax.legend()
    ax.grid(True)

    plt.show()

def performance_comparer(X, y):
    print('DecisionTree Gini depth=4')
    dtg4_clf = DecisionTreeClassifier(criterion='gini', max_depth=4)
    dtg4_metric = learning_curves_describe(dtg4_clf,X,y)#train_with_cv(dtg4_clf, X, y, n_splits=50)
    print_metric(dtg4_metric)

    print('DecisionTree Entropy depth=4')
    dte4_clf = DecisionTreeClassifier(criterion='entropy', max_depth=4)
    dte4_metric = learning_curves_describe(dte4_clf,X,y)#train_with_cv(dte4_clf, X, y)
    print_metric(dte4_metric)

    print('DecisionTree Gini depth=3')
    dtg3_clf = DecisionTreeClassifier(criterion='gini', max_depth=3)
    dtg3_metric = learning_curves_describe(dtg3_clf,X,y)#train_with_cv(dte3_clf, X, y)
    print_metric(dtg4_metric)    

    print('DecisionTree Entropy depth=3')
    dte3_clf = DecisionTreeClassifier(criterion='entropy', max_depth=3)
    dte3_metric = learning_curves_describe(dte3_clf,X,y)#train_with_cv(dte3_clf, X, y)
    print_metric(dte4_metric)    

    print('SVM kernel=poly')
    svmp_clf = SVC(probability=True, kernel='poly')
    svmp_metric = learning_curves_describe(svmp_clf,X,y)#train_with_cv(svmp_clf, X, y)
    print_metric(svmp_metric)

    print('SVM kernel=rbf')
    svmr_clf = SVC(probability=True, kernel='rbf')
    svmr_metric = learning_curves_describe(svmr_clf,X,y)#train_with_cv(svmr_clf, X, y)
    print_metric(svmr_metric)

    print('Random Forest estimators=10')
    rfg10_clf = RandomForestClassifier(n_estimators=10)
    rfg10_metric = learning_curves_describe(rfg10_clf,X,y)#train_with_cv(rfg10_clf, X, y)
    print_metric(rfg10_metric)

    print('Random Forest estimators=5')
    rfg5_clf = RandomForestClassifier(n_estimators=5)
    rfg5_metric = learning_curves_describe(rfg5_clf,X,y)#train_with_cv(rfg5_clf, X, y)
    print_metric(rfg5_metric)

    print('Naive Bayes')
    nb_clf = GaussianNB()
    nb_metric = learning_curves_describe(nb_clf,X,y)#train_with_cv(nb_clf, X, y)
    print_metric(nb_metric)

    print('3NN')
    knn3_clf = KNeighborsClassifier(n_neighbors=3)
    knn3_metric = learning_curves_describe(knn3_clf,X,y)#train_with_cv(knn3_clf, X, y)
    print_metric(knn3_metric)

    print('5NN')
    knn5_clf = KNeighborsClassifier(n_neighbors=5)
    knn5_metric = learning_curves_describe(knn5_clf,X,y)#train_with_cv(knn5_clf, X, y)
    print_metric(knn5_metric)

    print('10NN')
    knn10_clf = KNeighborsClassifier(n_neighbors=10)
    knn10_metric = learning_curves_describe(knn10_clf,X,y)#train_with_cv(knn10_clf, X, y)
    print_metric(knn10_metric)

    #print('GradientBoosting')
    #gb_clf = GradientBoostingClassifier(n_estimators=100, max_depth=3)
    #gb_metric = learning_curves_describe(gb_clf,X,y)#train_with_cv(gb_clf, X, y)
    #print_metric(gb_metric)

    print('LogisticRegression')
    lr_clf = LogisticRegression(max_iter=10000, solver="liblinear")
    lr_metric = learning_curves_describe(lr_clf,X,y)#train_with_cv(lr_clf, X, y)
    print_metric(lr_metric)
    

    label = ['dtg4','dte4', 'dte3','svm_r','svm_p', 'knn5', 'knn3', 'knn10','lr', 'rf10', 'rf5', 'nb', 'dtg3']
    auc_s = [dtg4_metric[1], dte4_metric[1], dte3_metric[1], svmr_metric[1], svmp_metric[1], knn5_metric[1], knn3_metric[1], knn10_metric[1], lr_metric[1], rfg10_metric[1], rfg5_metric[1], nb_metric[1], dtg3_metric[1]]
    acc_s = [dtg4_metric[0], dte4_metric[0], dte3_metric[0], svmr_metric[0], svmp_metric[0], knn5_metric[0], knn3_metric[0], knn10_metric[0], lr_metric[0], rfg10_metric[0], rfg5_metric[0], nb_metric[0], dtg3_metric[0]]
    color = ['blue', 'violet', 'pink', 'green', 'black', 'yellow', 'cyan', 'orange', 'red', 'lime', 'peru', 'magenta', 'dimgray']

    plot_scenario(label,auc_s, acc_s, color)

def selected_performance_comparer(X, y):

    print('DecisionTree Gini depth=4')
    dtg4_clf = DecisionTreeClassifier(criterion='gini', max_depth=4)
    dtg4_metric = learning_curves_describe(dtg4_clf,X,y)#train_with_cv(dtg4_clf, X, y, n_splits=50)
    print_metric(dtg4_metric)

    print('DecisionTree Entropy depth=4')
    dte4_clf = DecisionTreeClassifier(criterion='entropy', max_depth=4)
    dte4_metric = learning_curves_describe(dte4_clf,X,y)#train_with_cv(dte4_clf, X, y)
    print_metric(dte4_metric)

    print('DecisionTree Gini depth=3')
    dtg3_clf = DecisionTreeClassifier(criterion='gini', max_depth=3)
    dtg3_metric = learning_curves_describe(dtg3_clf,X,y)#train_with_cv(dte3_clf, X, y)
    print_metric(dtg4_metric)    

    print('DecisionTree Entropy depth=3')
    dte3_clf = DecisionTreeClassifier(criterion='entropy', max_depth=3)
    dte3_metric = learning_curves_describe(dte3_clf,X,y)#train_with_cv(dte3_clf, X, y)
    print_metric(dte4_metric) 

    print('LogisticRegression')
    lr_clf = LogisticRegression(max_iter=10000, solver="liblinear")
    lr_metric = learning_curves_describe(lr_clf,X,y)#train_with_cv(lr_clf, X, y)
    print_metric(lr_metric) 

    print('Random Forest estimators=3')
    rfg3_clf = RandomForestClassifier(n_estimators=3)
    rfg3_metric = learning_curves_describe(rfg3_clf,X,y)#train_with_cv(rfg10_clf, X, y)
    print_metric(rfg3_metric)

    print('Random Forest estimators=2')
    rfg2_clf = RandomForestClassifier(n_estimators=2)
    rfg2_metric = learning_curves_describe(rfg2_clf,X,y)#train_with_cv(rfg5_clf, X, y)
    print_metric(rfg2_metric)

    label = ['dtg4','dte4', 'dte3','dtg3','lr', 'rf2', 'rf3']
    auc_s = [dtg4_metric[1], dte4_metric[1], dte3_metric[1], dtg3_metric[1], lr_metric[1], rfg2_metric[1], rfg3_metric[1]]
    acc_s = [dtg4_metric[0], dte4_metric[0], dte3_metric[0], dtg3_metric[0], lr_metric[0], rfg2_metric[0], rfg3_metric[0]]
    color = ['blue', 'violet', 'green', 'black', 'yellow', 'cyan', 'red']

    plot_scenario(label,auc_s, acc_s, color)