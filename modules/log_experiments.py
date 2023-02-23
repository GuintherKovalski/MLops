
import mlflow
from mlflow.entities import ViewType
from modules.utils import Path
import time
import json
import pandas as pd
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

    def save_results(self):
        id = mlflow.get_experiment_by_name(Hiper.parameters["Experiment Name"])

        for exp in mlflow.search_experiments():
            if id.experiment_id == exp.experiment_id:
                runs = mlflow.search_runs(experiment_ids=[exp.experiment_id], run_view_type=ViewType.ALL)
        
        Path.handler(results_folder = "results",  
                    experiment_folder = Hiper.parameters["Experiment Name"])

        runs.to_csv("results/" + 
                    Hiper.parameters["Experiment Name"] + "/" +
                    Hiper.parameters["Experiment Name"] +".csv")