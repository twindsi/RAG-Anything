"""RAG-Anything: A multimodal RAG framework that can process and understand any type of content.

This package provides tools for building Retrieval-Augmented Generation (RAG) pipelines
that handle text, images, tables, equations, and other modalities.

Project home: https://github.com/HKUDS/RAG-Anything

Note: This is a personal fork for learning and experimentation.
Original project: https://github.com/HKUDS/RAG-Anything
"""

from raganything.raganything import RAGAnything
from raganything.modalprocessor import ModalProcessor

__version__ = "0.1.0"
__author__ = "RAG-Anything Contributors"
__license__ = "MIT"

# Expose version info as a tuple for easier programmatic comparison
VERSION_INFO = tuple(int(x) for x in __version__.split("."))

# Minimum supported Python version for this package
MIN_PYTHON_VERSION = (3, 8)

# Minimum recommended Python version (3.10+ gives better match/case and type union syntax)
RECOMMENDED_PYTHON_VERSION = (3, 10)

__all__ = [
    "RAGAnything",
    "ModalProcessor",
    "VERSION_INFO",
    "MIN_PYTHON_VERSION",
    "RECOMMENDED_PYTHON_VERSION",
    "__version__",
]
