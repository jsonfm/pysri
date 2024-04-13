from abc import ABC, abstractmethod
from typing import Any


class SRIBaseService(ABC):
    @abstractmethod
    def authorize_document(cls, params: dict[str, Any], ):
        pass