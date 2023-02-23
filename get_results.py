import mlflow
from mlflow.entities import ViewType

for exp in mlflow.search_experiments():
    print("exp.experiment_id",exp.experiment_id)

all_experiments = [exp.experiment_id for exp in mlflow.search_experiments()]
runs = mlflow.search_runs(experiment_ids=all_experiments, run_view_type=ViewType.ALL)

print(type(runs))