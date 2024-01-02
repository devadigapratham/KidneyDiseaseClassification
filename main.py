from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline
from cnnClassifier.components.model_evaluation_mlflow import Evaluation
from cnnClassifier.config.configuration import ConfigurationManager

STAGE_NAME = "Data Ingestion Stage" 

try: 
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<") 
    data_ingestion = DataIngestionTrainingPipeline() 
    data_ingestion.main() 
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<")

except Exception as e: 
    logger.exception(e) 
    raise e 
 
STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"******************************")
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<") 
    obj = PrepareBaseModelTrainingPipeline() 
    obj.main() 
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<<<") 
    
except Exception as e:
    logger.exception(e) 
    raise e 

STAGE_NAME = "Training"

try: 
    logger.info(f"*********************************") 
    logger.info(f">>>>>>stage {STAGE_NAME} started <<<<<<<") 
    obj = ModelTrainingPipeline() 
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n") 

except Exception as e:
    logger.exception(e) 
    raise e 
    
STAGE_NAME = "Evaluation Stage" 

class EvaluationPipeline: 
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score() 
        evaluation.log_into_mlflow()

if __name__ == "__main__": 
    try:
        logger.info(f"*********************************")
        logger.info(f">>>>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<")
        obj = EvaluationPipeline() 
        obj.main() 
        logger.info(f">>>>>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<<\n")

    except Exception as e:
        logger.exception(e) 
        raise e 
