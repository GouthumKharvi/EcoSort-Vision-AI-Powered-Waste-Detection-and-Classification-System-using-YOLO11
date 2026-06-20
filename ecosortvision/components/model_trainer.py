import os,sys
import yaml
from ecosortvision.utils.main_utils import read_yaml_file
from ecosortvision.logger import logging
from ecosortvision.exception import AppException
from ecosortvision.entity.config_entity import ModelTrainerConfig
from ecosortvision.entity.artifacts_entity import ModelTrainerArtifact



class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
    ):
        self.model_trainer_config = model_trainer_config


    

    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            logging.info("Unzipping data")
            os.system("unzip waste_detection.zip")
            os.system("rm waste_detection.zip")

            with open("data.yaml", 'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])

            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)

            # config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")

            config = read_yaml_file(f"ultralytics/ultralytics/cfg/models/11/yolo11.yaml")

            config['nc'] = int(num_classes)





            #My sir code 


            # with open(f'yolov5/models/custom_{model_config_file_name}.yaml', 'w') as f:
            #     yaml.dump(config, f)

        #     with open(f'ultralytics/ultralytics/cfg/models/11/custom_yolo11.yaml','w') as f:
        #         yaml.dump(config, f)

        #     os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results  --cache")
        #     os.system("cp yolov5/runs/train/yolov5s_results/weights/best.pt yolov5/")
        #     os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
        #     os.system(f"cp yolov5/runs/train/yolov5s_results/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")
           
        #     os.system("rm -rf yolov5/runs")
        #     os.system("rm -rf train")
        #     os.system("rm -rf valid")
        #     os.system("rm -rf data.yaml")

        #     model_trainer_artifact = ModelTrainerArtifact(
        #         trained_model_file_path="yolov5/best.pt",
        #     )

        #     logging.info("Exited initiate_model_trainer method of ModelTrainer class")
        #     logging.info(f"Model trainer artifact: {model_trainer_artifact}")

        #     return model_trainer_artifact


        # except Exception as e:
        #     raise AppException(e, sys)







            #MY Updated code 

            with open(f'ultralytics/ultralytics/cfg/models/11/custom_yolo11.yaml','w') as f:
                 yaml.dump(config, f)

            os.system(
                f'python -c "from ultralytics import YOLO; '
                f'model=YOLO(\'ultralytics/ultralytics/cfg/models/11/custom_yolo11.yaml\'); '
                f'model.load(\'{self.model_trainer_config.weight_name}\'); '
                f'model.train(data=\'data.yaml\', '
                f'epochs={self.model_trainer_config.no_epochs}, '
                f'imgsz=640, '
                f'batch={self.model_trainer_config.batch_size}, '
                f'cache=False, '
                f'name=\'garbage_detection\')"'
            )


            os.system("cp runs/detect/garbage_detection/weights/best.pt ultralytics/")

            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)

            os.system(f"cp runs/detect/garbage_detection/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")

            # os.system("rm -rf runs")
            # os.system("rm -rf train")
            # os.system("rm -rf valid")
            # os.system("rm -rf data.yaml")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="ultralytics/best.pt"
            )


            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact

        except Exception as e:
                raise AppException(e, sys)