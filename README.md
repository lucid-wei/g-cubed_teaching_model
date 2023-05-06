# Introduction
This is a documentation for users of the python-implemented G-Cubed model.  

Two components are needed to run the model, simply put, input data (of various kinds) and the algorithm. Input and output data vary depending on the model version, this repository stores those for the teaching version of the model, model 2R164. The algorithm or computing logic is packaged into a python package which can be installed into one's local machine.
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

# The G-Cubed model IO folder

The G-Cubed model requires a number of files to run. These files are organised into a folder with a set of subfolders. The gcubed package will load these files and produce certain outputs into this folder.  

The lower-case names of the subfolders are built-in for this particular model, and should not be changed during typical usage. The capitalised names of folder and files can be altered at your discretion, depending on your use case. 

The names that include parts like <PART> are to be substituted as follows:
* <VERSION> replace with the version of the model, e.g. '2R', '20C', etc.
* <NUMBER> replace with the number of the model, e.g. '169', '170'.

The model version and the model number need to match their values in the CONFIGURATION.CSV file that is in the ROOT_DIRECTORY.

```
├── ROOT_DIRECTORY
├── CONFIGURATION.CSV
├── data
│   │   ├── DATABASE.csv
│   │   ├── IOTABLES.csv
│   │   ├── SETPARAMETERS.csv
│   │   ├── POPULATION.csv
│   │   ├── PRODUCTIVITY.csv
│   │   ├── AEEINEW.csv
├── sym
│   │   ├── *.sym
│   │   ├── model_<VERSION>_<NUMBER>_eqnmap.sym
│   │   ├── model_<VERSION>_<NUMBER>_optmap.sym
│   │   ├── model_<VERSION>_<NUMBER>_varmap.sym
│   │   ├── model_<VERSION>_<NUMBER>_varinfo.sym
│   │   ├── model_<VERSION>_<NUMBER>_vars.sym
│   │   ├── model_<VERSION>_<NUMBER>.lis
│   │   ├── model_<VERSION>_<NUMBER>.py
├── simulations
│   ├── EXPERIMENT1
│   │   ├── EXPERIMENT1_DESIGN.csv
│   │   ├── LAYER1_DATA.csv
│   │   ├── ...
│   ├── EXPERIMENT2
│   │   ├── EXPERIMENT2_DESIGN.csv
│   │   ├── LAYER1_DATA.csv
│   │   ├── LAYER2_DATA.csv
│   │   ├── ...
│   ├── ...
```

### The data folder and its contents

The data folder contains the CSV data files defining the model.

### The simulations folder and its contents

The simulations folder contains the one folder for each simulation experiment being conducted with the model.

### The experiment folder names are user-determined.

Each experiment folder contains an experiment design CSV file that configures the experiment, documenting
the layers of adjustments to variables that are to be applied in specific years through the projections.

### The sym folder and its contents

If necessary, the *.sym files in the sym folder should be used to generate the other files in that folder, by running the SYM processor <SYM>, sym4mac.exe on MacOS or sym4win.exe on Windows.

If the root file of the SYM model definition (the *.sym files) is called ggg2r170.sym, then the command to generate these files is:
```
<SYM> -python ggg2r170.sym model_<VERSION>_<NUMBER>.py
```

To generate the HTML documentation of the model, run:
```
<SYM> -html ggg2r170.sym model_<VERSION>_<NUMBER>.html
```

Both of these commands should be run from within the sym subfolder documented above. In other words, you will need to run command like this to change your location before you run your .exe:
```
cd path/where/you/extract/this/repo/model_IO_folder/sym
```
where cd is a common command in both Windows and MacOS, standing for 'change directory'.
  
# Running the G-Cubed using your own Python script.

Modify the following python script to run the model. An example of this script is contained in the python directory of the model (python/run.py).

```
from gcubed.runner import Runner

# Working directory - where you will store outputs from the run.
# Configuration file location relative to the working directory.
# Experiment file location relative to the model simulations folder.
runner: Runner = Runner(
    working_directory="path/where/you want/the/results/to/be/saved/",
    configuration_file="relative/path/from/working/directory/to/configuration2R164.csv", 
    experiment_design_file="experiment1/design.csv"
    )

runner.run()
```

To execute this script, run the following command under the *IO_folder/python/* subfolder:
  ```
python run.py
  ```
If you encounter some error saying python is nowhere to be found, (assuming you already install python) this means you have not configured system PATH environment variables thus your terminal does not know where to find your installed python executable. Here is [a guide for this issue](https://stackoverflow.com/questions/6318156/adding-python-to-path-on-windows).

After a successful run, you will see the results generated in a folder (also under the *IO_folder/python/* subfolder), with baseline_projections.csv, deviation_projections.csv, simulation_projections.csv and a log file recording the process or problems during the computation process.

More specific use case examples please see another documentation .md file.
