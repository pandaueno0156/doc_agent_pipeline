# src/llm/base.py

from abc import ABC, abstractmethod

class BaseLLM(ABC):
    """Base class for all LLM implementations.
    Every LLM must implement the following methods.
    """
    @abstractmethod
    def ocr(self, text: str) -> str:
        """
        Extract structured data from raw text.

        Args:
            text: Raw OCR input text.

        Returns:
            str: JSON string output from the LLM.
        """
        pass
    