import json
import pickle
from abstract import MLModel


class ModelSaver():
    def _save_json(self, model: MLModel, path: str) -> None:
        with open(path, "w") as f:
            json.dump(model.parameters, f)

    def _load_json(self, model: MLModel, path: str) -> None:
        with open(path, "r") as f:
            params = json.load(f)
        model.parameters = params

    def _save_pkl(self, model: MLModel, path: str) -> None:
        with open(path, "wb") as f:
            pickle.dump(model.parameters, f)

    def _load_pkl(self, model: MLModel, path: str) -> None:
        with open(path, "rb") as f:
            params = pickle.load(f)
        model.parameters = params

    def save(self, model: MLModel, path: str, format: str = "json") -> None:
        if format == "json":
            self._save_json(model, path)
        elif format in ("pkl", "pickle"):
            self._save_pkl(model, path)
        else:
            raise ValueError(f"Invalid format {format}.  \
                + 'json' and 'pkl are valid formats'")

    def load(self, model: MLModel, path: str, format: str = "json") -> None:
        if not isinstance(path, str):
            raise TypeError(f"path: expected str, got {type(path)}")
        if format == "json":
            self._load_json(model, path)
        elif format in ("pkl", "pickle"):
            self._load_pkl(model, path)
        else:
            raise ValueError(f"Invalid format {format}. \
                + 'json' and 'pkl are valid formats'")
