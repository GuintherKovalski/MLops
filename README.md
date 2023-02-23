# MLflow + scikit-learn + gridsearch base code

This is base project to track, reproduce and versioning experiments. This implements a gridsearch on hiper parameters of a collection of tree based models from scikit-learn + xgboost, train and test and log the results with MLflow.
 
## Installation
### Prerequisites
* Docker installed.

run:
`docker build -t mlops:latest .`

## Usage
run `bash run_container.sh`

visualize results in `results/[experiment_name].csv` or run `sudo docker run -it --privileged -v $(pwd):/home --network host mlops:latest mlflow ui` and acess





