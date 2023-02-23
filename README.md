# MLflow + scikit-learn + gridsearch base code

This is base project to track, reproduce and versioning experiments. This implements a gridsearch on hiper parameters of a collection of tree based models from scikit-learn + xgboost, train and test and log the results with MLflow.
 
## Installation
### Prerequisites
* Docker installed.

run:
`docker build -t mlops:latest .`

## Usage

Edit the configuration file in `data/hiper_parameters/parameters.json` to use different parameters/models.

Edit the configuration file in `data/configurations/configurations.json` with the **experiment name** you are bout to run.

run `bash run_container.sh`

visualize results in `results/[experiment_name].csv` or run `sudo docker run -it --privileged -v $(pwd):/home --network host mlops:latest mlflow ui` and acess

Create a tag for the experiment e.g:

    git add results/*git data/* 
    git tag -a v0.0.1 -m "grid search in tree based models"
    git push origin v0.0.1




