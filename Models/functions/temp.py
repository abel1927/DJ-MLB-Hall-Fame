#from numpy import std
#from sklearn.model_selection import cross_val_score, RepeatedStratifiedKFold
#from sklearn.pipeline import Pipeline
#from sklearn.feature_selection import RFE, RFECV

# def get_models_pipelines(n_features=10):
# 	models = dict()

# 	rfe = RFE(estimator=LogisticRegression(max_iter=10000, solver="liblinear"), n_features_to_select=n_features)
# 	model = DecisionTreeClassifier()
# 	models['lr'] = Pipeline(steps=[('s',rfe),('m',model)])

# 	rfe = RFE(estimator=GaussianNB(), n_features_to_select=n_features)
# 	model = DecisionTreeClassifier()
# 	models['nb'] = Pipeline(steps=[('s',rfe),('m',model)])

# 	rfe = RFE(estimator=DecisionTreeClassifier(), n_features_to_select=n_features)
# 	model = DecisionTreeClassifier()
# 	models['dtg4'] = Pipeline(steps=[('s',rfe),('m',model)])

# 	rfe = RFE(estimator=SVC(), n_features_to_select=n_features)
# 	model = DecisionTreeClassifier()
# 	models['svm r'] = Pipeline(steps=[('s',rfe),('m',model)])

# 	rfe = RFE(estimator=GradientBoostingClassifier(n_estimators=100, learning_rate=1,max_depth=4), n_features_to_select=n_features)
# 	model = DecisionTreeClassifier()
# 	models['gbc'] = Pipeline(steps=[('s',rfe),('m',model)])
# 	return models

#def evaluate_model(model, X, y, eval='accuracy'):
#	cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=5, random_state=1)
#	scores = cross_val_score(model, X, y, scoring=eval, cv=cv, n_jobs=-1)
#	return scores
#
##from matplotlib import pyplot
#
#def run_test(title, n_features=10):
#	models = get_models_pipelines(n_features)
#	results, names = [], []
#	for name, model in models.items():
#		scores = evaluate_model(model, X, np.ravel(y))
#		results.append(scores)
#		names.append(name)
#		print('>%s %.3f (%.3f)' % (name, mean(scores), std(scores)))
#	plt.boxplot(results, labels=names, showmeans=True)
#	plt.title(title)
#	plt.show()