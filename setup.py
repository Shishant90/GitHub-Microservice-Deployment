from setuptools import setup, find_packages

setup(
    name="github-microservice-deployment",
    version="1.0.0",
    description="CI/CD Pipeline for GitHub Microservice Deployment",
    author="Shishant Kanojia",
    author_email="shishant@example.com",
    packages=find_packages(),
    install_requires=[
        "flask==2.3.3",
        "pytest==7.4.2",
        "requests==2.31.0",
        "gunicorn==21.2.0",
        "docker==6.1.3",
        "kubernetes==27.2.0",
        "ansible==8.5.0",
        "boto3==1.28.85",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)