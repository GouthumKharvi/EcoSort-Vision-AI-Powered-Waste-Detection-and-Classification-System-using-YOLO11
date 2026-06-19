import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s]: %(message)s"
)

project_name = "ecosortvision"

list_of_files = [

    ".github/workflows/.gitkeep",

    "artifacts/.gitkeep",

    "data/.gitkeep",

    "flowcharts/.gitkeep",

    "research/trials.ipynb",

    "templates/index.html",

    "config/config.yaml",
    "static/css/style.css",
    "static/js/script.js",
    "static/images/.gitkeep",

    f"{project_name}/__init__.py",

    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/yolo_trainer.py",
    f"{project_name}/components/classifier_trainer.py",
    f"{project_name}/components/prediction.py",

    f"{project_name}/constants/__init__.py",
    f"{project_name}/constants/application.py",
    f"{project_name}/constants/training_pipeline/__init__.py",

    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifacts_entity.py",

    f"{project_name}/exception/__init__.py",

    f"{project_name}/logger/__init__.py",

    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",

    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",

    f"{project_name}/config/configuration.py",

    "app.py",

    "Dockerfile",

    "requirements.txt",

    "setup.py",

    "README.md",

    ".gitignore"
]

for filepath in list_of_files:

    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(
            f"Creating directory: {filedir}"
        )

    if (
        not os.path.exists(filepath)
        or os.path.getsize(filepath) == 0
    ):
        with open(filepath, "w") as f:
            pass

        logging.info(
            f"Creating empty file: {filepath}"
        )

    else:
        logging.info(
            f"{filename} already exists"
        )