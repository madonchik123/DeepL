from setuptools import setup, find_packages

setup(
    name="deepl_translate",
    version="0.1.0",
    description="DeepL Translate API Client for Python",
    url="https://github.com/yourusername/deepl_translate",
    author="madonchik123",
    author_email="gamzat1234531@example.com",
    packages=find_packages(),
    test_suite='tests',
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)