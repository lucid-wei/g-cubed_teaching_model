---
layout: default
nav_order: 2
---

# Environment setup 
## Setup Python:
One needs to install python in his/her local machine. It is recommended to use python 3.10+, since older version was not tested during development.

Various commands below should be executed in PowerShell/cmd.exe for Windows and terminal for MacOS.

### Windows installation

Install on Windows from [the Python site](https://www.python.org/downloads/windows/).

### Mac installation

To install the latest Python using homebrew on Mac:

```
brew install python
```

### Python package management 
Python itself cannot do too much, it needs all kinds of packages for all kinds of purposes (including the newly developed gcubed package). Pip is widely used for managing python's packages.  

To install pip in your local machine, please check:

[Pip official website for installation](https://packaging.python.org/en/latest/tutorials/installing-packages/)  
and  
[Instructions for installing pip on Windows](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)  

The gcubed package needs some dependencies during its calculation, such as:  

* [pandas](https://pandas.pydata.org/)
* [numpy](https://numpy.org/)
* [scipy](https://scipy.org/)
* [regex](https://pypi.org/project/regex/)

But they are not needed to be installed manually, when you install the gcubed package, pip can automatically check which packages are missing in your local environment and install them.  

Thus, make sure pip is properly setup before you install the gcubed package.

## G-Cubed package installation
The first thing you need to do is to download this repository from [this link](https://github.com/lucid-wei/g-cubed_teaching_model/archive/refs/heads/main.zip), and extract the files.  

Then you can find the binary distribution of the G-Cubed package in gcubed_distribution/ directory, with filename gcubed-*version*-py3-none-any.whl.
The current package version is 1.0.0 but this may evolve relatively quickly. 

To install the whl package, run the following command in your terminal:

```
pip install ./gcubed-*version*-py3-none-any.whl
```

To uninstall:

```
pip uninstall gcubed
```
You will probably need to reinstall gcubed if there is a version update.
