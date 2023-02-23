# MLflow + scikit-learn + gridsearch base code

This is base project to track, reproduce and versioning experiments which implements a gridsearch of parameter in tree bases models from scikit-learn and log the results with mlops.
 
## Installation
### Prerequisites
* A realsense camera.
* Python installed.

run:
`docker build -t mlops:latest .`

## Usage
run `bash run_container.sh`

visualize results in `results/[experiment_name].csv` or run `sudo docker run -it --privileged -v $(pwd):/home --network host mlops:latest mlflow ui` and acess





