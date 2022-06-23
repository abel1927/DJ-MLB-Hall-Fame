from sklearn.model_selection import GridSearchCV

def model_parameter_optimization(estimator, params, X_train, y_train, scoring='roc_auc',cv=30, refit=False):

    grid = GridSearchCV(
        estimator  = estimator,
        param_grid = params,
        scoring    = scoring,
        n_jobs     = -1,
        cv         = cv, 
        refit      = refit,
        verbose    = 0,
        return_train_score = True
      )

    grid.fit(X = X_train, y = y_train)
    print("Mejores hiperparámetros encontrados (cv)")
    print("----------------------------------------")
    print(grid.best_params_, ":", grid.best_score_, grid.scoring)

    model = grid.best_estimator_
    return model