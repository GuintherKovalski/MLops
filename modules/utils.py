import os
class Path:
    @staticmethod
    def handler(results_folder = "results", experiment_folder = "experiment_name" ) -> None:
        
        if not os.path.exists(results_folder):
            os.makedirs(results_folder)

        if not os.path.exists(results_folder+"/"+experiment_folder):
            os.makedirs(results_folder+"/"+experiment_folder)
        