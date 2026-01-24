"""
🔥 THE SCREAM MACHINE - Setup Configuration
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="scream-machine",
    version="0.1.0",
    author="Jimmy DeJesus",
    author_email="jimmy@scream-machine.ai",
    description="Revolutionary AI System with Perfect Convergence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jimmyjdejesus/scream-machine",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
    install_requires=[
        "torch>=2.0.0",
        "numpy>=1.24.0",
        "scipy>=1.10.0",
        "transformers>=4.35.0",
        "sentence-transformers>=2.2.0",
        "chromadb>=0.4.0",
        "langchain>=0.1.0",
        "asyncio>=3.4.3",
        "aiohttp>=3.9.0",
        "pandas>=2.0.0",
        "python-dotenv>=1.0.0",
        "pydantic>=2.0.0",
        "rich>=13.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "ruff>=0.1.0",
            "mypy>=1.7.0",
        ],
        "monitoring": [
            "wandb>=0.16.0",
            "loguru>=0.7.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "scream=scream_machine.cli:main",
        ],
    },
)
