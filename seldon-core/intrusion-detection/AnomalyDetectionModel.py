# Ref: https://github.com/SeldonIO/seldon-core/tree/v1.17.1/wrappers/s2i/python/test
from alibi_detect.saving import load_detector
from mlserver import MLModel
import numpy as np
import json
import constants.vae as vae_constants
from loguru import logger

# For serializing Numpy arrays
class NumpyArrayEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NumpyArrayEncoder, self).default(obj)

class AnomalyDetectionModel(MLModel):
    def __init__(self):
        print("Initializing AnomalyDetectionModel!")
        self.model = load_detector(vae_constants.WEIGHTS_PATH)

    def predict(self, input_data, features_names):
        preds = self.model.predict(
            input_data,
            return_instance_score=vae_constants.RETURN_INSTANCE_SCORE,
            return_feature_score=vae_constants.RETURN_FEATURE_SCORE,
        )
        preds = json.dumps(preds, cls=NumpyArrayEncoder)
        logger.info(preds)
        return preds
