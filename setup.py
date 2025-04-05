from setuptools import setup, find_packages

setup(
    name="WordToNumber",  
    version="1.0.2",  
    packages=find_packages(), 
    license=open('LICENSE').read(),
    test_suite='tests', 
    author="Santosh Bhandari", 
    author_email="info@bhandari-santosh.com.np", 
    description="A Python library for converting words to numbers.",  
    long_description=open('README.md').read(), 
    long_description_content_type="text/markdown", 
    url="https://github.com/santoshvandari/WordToNumber",
    keywords=["word to number", "number conversion", "text processing"], 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent", 
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Topic :: Software Development :: Libraries :: Python Modules",
       
    ],
)
