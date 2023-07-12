from sklearn.linear_model import PassiveAggressiveClassifier

params = {
    "max_iter":50
}

from timeit import default_timer as timer
start = timer()
model = PassiveAggressiveClassifier(**params).fit(tfidf_train, y_train)
train_patched = timer() - start
f"Intel® extension for Scikit-learn time: {train_patched:.2f} s"

y_pred = model.predict(tfidf_test)

from sklearn.metrics import accuracy_score
score = accuracy_score(y_test,y_pred)
