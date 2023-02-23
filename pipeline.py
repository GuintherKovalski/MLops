from modules.validation      import Validate
from modules.data            import Data
from modules.log_experiments import MlFlow
from modules.gridsearch      import GridSeach
from modules.models          import Models 
       
class Pipeline:

    def __init__(self):

        self.data        = Data()
        self.models      = Models()
        self.grid_search = GridSeach()
        self.validate    = Validate()
        self.mlFlow      = MlFlow()

    def train(self,model,X_train,y_train):

        model.fit(X_train,y_train)

        return model


    def initialize_model(self,model_name,parameter):

        if model_name in self.models.emsemble_names:
            for decision_tree_parameter in self.grid_search.iterate_by_name("DecisionTreeClassifier"):
                model = self.models.instantiate(model_name,(parameter,decision_tree_parameter)) 
                 
        else:
            model = self.models.instantiate(model_name,parameter)
        
        parameter["model_name"] = model_name

        return model

    
    def fit(self):
        
        self.datasets = self.data.generate()
        for X, y in self.datasets:
            X_train, X_test, y_train, y_test = self.data.transform.split(X, y)
            X_train, X_test                  = self.data.transform.normalize(X_train,X_test)
            for model_name,parameter in self.grid_search.generate_parameter():
                model   = self.initialize_model(model_name,parameter)
                model   = self.train(model,X_train,y_train)
                metrics = self.validate.eval(model,X_test,X_train,y_train,y_test)
                self.mlFlow.log_result(parameter,metrics)

        self.mlFlow.save_results()


if __name__ == "__main__":

    pipeline = Pipeline()
    pipeline.fit()





    





