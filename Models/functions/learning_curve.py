from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
import numpy as np


def plot_learning_curve(estimator, features, target, metric, train_sizes, cv):
    
    train_sizes, train_scores, validation_scores = learning_curve(
    estimator, features, target, train_sizes =
    train_sizes,
    cv = cv, scoring = metric)
    train_scores_mean = -train_scores.mean(axis=1) if metric == 'neg_mean_squared_error' else train_scores.mean(axis = 1)
    validation_scores_mean = -validation_scores.mean(axis=1) if metric == 'neg_mean_squared_error' else validation_scores.mean(axis = 1)

    plt.plot(train_sizes, train_scores_mean, label = 'Training')
    plt.plot(train_sizes, validation_scores_mean, label = 'Validation')

    y_label = metric.upper() if metric != 'neg_mean_squared_error' else 'MSE'
    plt.ylabel(y_label, fontsize = 14)
    plt.xlabel('Training set size', fontsize = 14)
    title =  y_label + ' Learning curves'
    plt.title(title, fontsize = 18, y = 1.03)
    plt.legend()


def learning_curves_describe(estimator, features, target, train_sizes=[.1, .2, .3, .4, .5, .6, .7, .8, .9], cv=50):
    plt.figure(figsize = (16,5))
    ms = [('neg_mean_squared_error',1),('accuracy',2),('roc_auc',3)]
    for m,i in ms:
        plt.subplot(1,3,i)
        plot_learning_curve(estimator, features, np.ravel(target), m, train_sizes=train_sizes, cv=cv)
