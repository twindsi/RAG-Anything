"""RAG-Anything: A multimodal RAG framework that can process and understand any type of content.

This package provides tools for building Retrieval-Augmented Generation (RAG) pipelines
that handle text, images, tables, equations, and other modalities.

Project home: https://github.com/HKUDS/RAG-Anything
"""

from raganything.raganything import RAGAnything
from raganything.modalprocessor import ModalProcessor

__version__ = "0.1.0"
__author__ = "RAG-Anything Contributors"
__license__ = "MIT"

# Expose version info as a tuple for easier programmatic comparison
VERSION_INFO = tuple(int(x) for x in __version__.split("."))

__all__ = [
    "RAGAnything",
    "ModalProcessor",
    "VERSION_INFO",
    "__version__",
]
