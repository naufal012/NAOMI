from setuptools import setup, find_packages

setup(
    name="naomi",
    version="0.1",
    packages=find_packages(),
    install_requires=["torch>=1.8", "numpy", "pandas"],
    description="NAOMI: Non-Autoregressive Multiresolution Imputation model",
    author="Felix Liu et al.",
    url="https://github.com/felixykliu/NAOMI",
)
