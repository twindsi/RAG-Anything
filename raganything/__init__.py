"""RAG-Anything: A multimodal RAG framework that can process and understand any type of content.

This package provides tools for building Retrieval-Augmented Generation (RAG) pipelines
that handle text, images, tables, equations, and other modalities.
"""

from raganything.raganything import RAGAnything
from raganything.modalprocessor import ModalProcessor

__version__ = "0.1.0"
__author__ = "RAG-Anything Contributors"
__license__ = "MIT"

__all__ = [
    "RAGAnything",
    "ModalProcessor",
    "__version__",
]
