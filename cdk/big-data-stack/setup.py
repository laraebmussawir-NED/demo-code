import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="cdk_emr_metastores",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "cdk_emr_metastores"},
    packages=setuptools.find_packages(where="cdk_emr_metastores"),

    install_requires=[
        "aws-cdk.core==1.95.0",
        "aws_cdk.aws_ec2",
        "aws-cdk.aws-rds",
        "aws-cdk.aws-secretsmanager",
        "aws_cdk.aws-emr",
        "aws_cdk.aws-eks",
        "aws_cdk.aws-emrcontainers",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
