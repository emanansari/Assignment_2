from abc import ABC, abstractmethod
from typing import Any, List


class MLModel(ABC):
    @abstractmethod
    def train(self, data: List[Any]) -> None:
        pass

    @abstractmethod
    def predict(self, input_data: Any) -> Any:
        pass
