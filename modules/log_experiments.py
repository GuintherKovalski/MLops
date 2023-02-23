
import mlflow
import time
import json
class Hiper:
    f = open('data/configurations/configurations.json')
    parameters = json.load(f)

class MlFlow:
    def __init__(self) -> None:
        mlflow.set_experiment(experiment_name = Hiper.parameters["Experiment Name"])
        
    def log_result(self,paramters,metrics):

        with mlflow.start_run(run_name = paramters["model_name"]+"-"+str(time.time())):
            print(paramters)
            mlflow.log_params(paramters)
            mlflow.log_metrics(metrics)