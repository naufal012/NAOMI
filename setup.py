from setuptools import setup, find_packages

setup(
    name="naomi",
    version="0.1",
    install_requires=["torch>=1.8", "numpy", "pandas"],
    py_modules=[           # list every .py file you want to import
        "model",
        "model_utils",
        "helpers",
        "train",
    ],
    description="NAOMI: Non-Autoregressive Multiresolution Imputation model",
    author="Felix Liu et al.",
    url="https://github.com/naufal012/NAOMI",
)
