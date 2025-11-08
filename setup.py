from setuptools import setup, find_packages

setup(
    name="biomed_rag",
    version="0.1.0",
    description="Explainable Biomedical RAG System with Trust Scoring",
    packages=find_packages(exclude=("tests", "notebooks")),
    python_requires=">=3.10",
    install_requires=[
        "torch",
        "transformers",
        "sentence-transformers",
        "faiss-cpu",
        "rank-bm25",
        "captum",
    ],
    extras_require={
        "dev": ["pytest", "pytest-cov"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
