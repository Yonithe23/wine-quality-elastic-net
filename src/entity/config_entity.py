from dataclasses import dataclass
from pathlib import Path

@dataclass 
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_file_path: Path
    unzip_dir: Path
@dataclass 
class DataValidationConfig:
    root_dir: Path
    data_path: Path
    status_file: str
    all_schema: dict
@dataclass
class DataTransformationConfig:
    data_path: Path
    root_dir: Path
    train_path: Path
    test_path: Path
    preprocessor_path: Path
@dataclass
class ModelTrainerConfig:
    trained_model_path: Path
    test_path: Path
    root_dir: Path
    metrics_path: Path
    evaluation_report_path: Path