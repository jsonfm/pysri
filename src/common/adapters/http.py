from typing import Any
from abc import ABC, abstractmethod


class HTTPAdapter(ABC):
    @abstractmethod
    @classmethod
    def get(cls, params: dict[str, Any], headers: dict[str, Any], data: dict[str, Any], json: dict[str, Any]):
        pass