from setuptools import setup, find_packages

setup(
    name="my_library",  # Replace with the name of your library
    version="0.1",  # Replace with the version you want
    packages=find_packages(),  # Automatically finds all packages in the project
    install_requires=[],  # List your library's dependencies here if any
    test_suite='tests',  # Points to your test directory
    author="Santosh Bhandari",  # Your name
    author_email="your_email@example.com",  # Your email address
    description="A Python library for [add description]",  # Short description of your library
    long_description=open('README.md').read(),  # Reads the contents of your README file
    long_description_content_type="text/markdown",  # Specifies the format of the long description
    url="https://github.com/yourusername/my_library",  # Replace with your GitHub repository URL
    classifiers=[
        "Programming Language :: Python :: 3",  # Python version
        "License :: OSI Approved :: MIT License",  # Specify the license you're using
        "Operating System :: OS Independent",  # OS Compatibility
    ],
)
