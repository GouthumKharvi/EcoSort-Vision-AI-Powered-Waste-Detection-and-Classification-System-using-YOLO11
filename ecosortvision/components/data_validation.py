import os,sys
import shutil
from ecosortvision.logger import logging
from ecosortvision.exception import AppException
from ecosortvision.entity.config_entity import DataValidationConfig
from ecosortvision.entity.artifacts_entity import (DataIngestionArtifact,
                                                 DataValidationArtifact)






class DataValidation:
    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_validation_config: DataValidationConfig,
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config

        except Exception as e:
            raise AppException(e, sys) 
        


    
    # def validate_all_files_exist(self)-> bool:
    #     try:
    #         validation_status = None

    #         all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)

    #         for file in all_files:
    #             if file not in self.data_validation_config.required_file_list:
    #                 validation_status = False
    #                 os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
    #                 with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
    #                     f.write(f"Validation status: {validation_status}")
    #             else:
    #                 validation_status = True
    #                 os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
    #                 with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
    #                     f.write(f"Validation status: {validation_status}")

    #         return validation_status


    #     except Exception as e:
    #         raise AppException(e, sys)
        





    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None

            base_path = self.data_ingestion_artifact.feature_store_path
            all_files = os.listdir(base_path)

            # Original validation logic
            for file in all_files:
                if file not in self.data_validation_config.required_file_list:
                    validation_status = False
                else:
                    validation_status = True

            # ----------------------------
            # Additional Validation Checks
            # ----------------------------

            required_dirs = [
                "train/images",
                "train/labels",
                "valid/images",
                "valid/labels",
                "test/images",
                "test/labels"
            ]

            for directory in required_dirs:
                dir_path = os.path.join(base_path, directory)

                if not os.path.exists(dir_path):
                    logging.info(f"Missing directory: {directory}")
                    validation_status = False

            # Check image-label counts
            splits = ["train", "valid", "test"]

            for split in splits:
                images_path = os.path.join(base_path, split, "images")
                labels_path = os.path.join(base_path, split, "labels")

                if os.path.exists(images_path) and os.path.exists(labels_path):

                    image_count = len(os.listdir(images_path))
                    label_count = len(os.listdir(labels_path))

                    logging.info(
                        f"{split} -> Images: {image_count}, Labels: {label_count}"
                    )

                    if image_count != label_count:
                        validation_status = False

            # Check data.yaml exists and is not empty
            yaml_path = os.path.join(base_path, "data.yaml")

            if not os.path.exists(yaml_path):
                validation_status = False

            elif os.path.getsize(yaml_path) == 0:
                validation_status = False

            # Write validation status
            os.makedirs(
                self.data_validation_config.data_validation_dir,
                exist_ok=True
            )

            with open(
                self.data_validation_config.valid_status_file_dir,
                "w"
            ) as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise AppException(e, sys)

    
    def initiate_data_validation(self) -> DataValidationArtifact: 
        logging.info("Entered initiate_data_validation method of DataValidation class")
        try:
            status = self.validate_all_files_exist()
            data_validation_artifact = DataValidationArtifact(
                validation_status=status)

            logging.info("Exited initiate_data_validation method of DataValidation class")
            logging.info(f"Data validation artifact: {data_validation_artifact}")

            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())

            return data_validation_artifact

        except Exception as e:
            raise AppException(e, sys)
        