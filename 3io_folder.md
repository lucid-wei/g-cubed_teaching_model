---
layout: default
nav_order: 3
---

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
  