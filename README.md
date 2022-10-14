# deb-packages-tool

Debian uses *deb packages to deploy and upgrade software. The packages are stored in repositories and each repository contains the so called "Contents index". The format of that file is well described here https://wiki.debian.org/RepositoryFormat#A.22Contents.22_indices
 
Your task is to develop a python command line tool that takes the architecture (amd64, arm64, mips etc.) as an argument and downloads the compressed Contents file associated with it from a Debian mirror. The program should parse the file and output the statistics of the top 10 packages that have the most files associated with them.
 
An example output could be:
 
$ ./package_statistics.py amd64
1. <package name 1>         <number of files>
2. <package name 2>         <number of files>
......
10. <package name 10>         <number of files>
 
You can use the following Debian mirror http://ftp.uk.debian.org/debian/dists/stable/main/. Please do try to follow Python's best practices in your solution. Hint: there are tools that can help you verify your code is compliant. In-line comments are appreciated.

## GitHub Workflow

Defined in [workflow.yaml](.github/workflows/workflow.yaml)

Just change the name of the `<image name>`

## pyenv?

If you use `pyenv`, create a virtualenv

```bash
pyenv virtualenv 3.10 <venv name>
```

or load existing one

```bash
pyenv local <venv name>
```

Get `<ven name>` with:

```bash
pyenv which python
```

## Requirements.txt

### first install

```bash
pip install -r requirements.txt
```

### Add packages

Packages should be added to the [`requirements.in`](requirements.in) or to the [`dev-requirements.in`](dev-requirements.in).

After this, use `pip-compile` to translate these to [`requirements.txt`](requirements.txt) and [`dev-requirements.txt`](dev-requirements.txt).

```bash
pip-compile requirements.in
pip-compile dev-requirements.in
```

### Install and Uninstall packages

Packages can be installed with

```bash
pip-sync requirements.txt dev-requirements.txt
```

This will install all the packages specified in the requirement files and will uninstall the ones that are not.


## Docker Image

For local testing, continue reading.


### Build Image

In order to build the image manually, run

```bash
IMAGE_NAME=<image name>
TAG=1
docker build -t $IMAGE_NAME:$TAG .
```

### Run Image

```bash
docker run $IMAGE_NAME:$TAG hello
```
