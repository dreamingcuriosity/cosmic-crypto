from setuptools import setup, find_packages

setup(
    name="cosmic_crypto",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["Pillow"],
    python_requires=">=3.10",
    description="Overkill cryptography with cosmic random images",
    author="ZaiperUnbound",
    url="https://github.com/dreamingcuriosity/cosmic-crypto",
)
