import joblib
mind = joblib.load('dataset.pk1')
mind.predict([[5]])
