import pickle
import sklearn as sk
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

class Model:

    def scale_data(self, df_object):
        scaler = StandardScaler()
        return scaler.fit_transform(df_object)

    def calculate_anomoly_cutoff(self, df_object, normal_rows):
        return 1 - (len(normal_rows)/(len(df_object))) 

    def train_model(self, object, contaminations, n_jobs= -1):
        ifm = IsolationForest(contamination = contaminations,
                                           n_jobs = n_jobs)
        print("fitting model...")
        return ifm.fit(object)
    
    def load_model(self, path = "src/model.fit"):
        with open(path, 'rb') as model_in:
            return pickle.load(model_in)

    def save_model(self, model, path = "src/model.fit"):
        with open(path, 'wb') as model_out:
            pickle.dump(model, model_out)

    def classify(self, model, np_object):
        return model.predict(np_object)    
