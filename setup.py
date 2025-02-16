
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="tfq-tool",            
    version="2.0.0",            
    author="Talal",
    description="is a command-line utility for extracting text from various file formats, including text files, PDFs, Word documents, spreadsheets, and code files in popular programming languages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tfq0/TFQ_tool",
    packages=find_packages(),
    install_requires=[
        "PyPDF2",
        "python-docx",
        "openpyxl",
        "pdfminer.six",
        
    ],
    entry_points={
        "console_scripts": [
            "tfq_tool=TFQ_tool.tfq_tool:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
