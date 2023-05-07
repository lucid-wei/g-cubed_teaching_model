---
layout: default
nav_order: 4
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
├── python
│   ├── run.py
│   ├── RESULTS_GENERTION-TIME
│   │   ├── baseline_projections.csv
│   │   ├── deviation_projections.csv
│   │   ├── simulation_projections.csv
│   │   ├── run.log
```

## The configuration file

The configuration2R164.csv defines which files gcubed python module needs to read from, which years gcubed uses for its algorithms, 
and a few other configurable options during its calculation.

Usually information in this file does not need to be changed.

## The data folder and its contents

The data folder contains the CSV data files defining the model, including:

### DATABASE.csv

Is DATAvR2018.csv for model 2R164. 

Data in this file is considered to be the real data of the world economy. Following the variables names, are 
descriptions, units of measurement, and country/region code.

More detailed definitions of the variables are in 

### IOTABLES.csv

Is IOTABLESvR2011.csv for model 2R164.

Each region has an IO table, which has the following structure: columns correspond to uses of the inputs and each row is a different input:

| Input\Output | a01 | …   | a0N | C   | I   | G   | X   | M   |
|--------------| --- | --- | --- | --- | --- | --- | --- | --- |
| g01          |     |     |     |     |     |     |     |     |
| :            |     |     |     |     |     |     |     |     |
| g0N          |     |     |     |     |     |     |     |     |
| M            |     |     |     |     |     |     |     |     |
| K            |     |     |     |     |     |     |     |     |
| L            |     |     |     |     |     |     |     |     |

Note that industry a0N produces good g0N. 

For model 2R164, a01 is energy sector,a02 is non-energy sector.

All model versions include:  
- M is a sector-specific material.  
- K is capital.  
- L is labour.  

There are 2 sectors not in the IO table but reflected in variable names (e.g. SHLY):
- Sector Y is the sector that produces the capital used in production.  
- Sector Z produces household capital.  

Note that sectors Y and Z are dummy sectors that buy output from the other sectors to create investment goods and this cumulates into the capital stock of sectors y and Z.   
When firms buy investment goods they by a package good from sector Y that goes into K in sector i.   
Households draw a return from the capital stock that is in sector Z. It is in fact the outcome of their investment decisions on durable goods.   
They carry many of the parameter names used in other sectors but they are not traded.

### SETPARAMETERS.csv <a id="setparameters"></a>

This file contains user-defined parameters.  
More information on parameters please check [related model definitions section](3model_definitions.md#parameters).

### POPULATION.csv

The modpop.csv records annual population growth rates data for all regions, expressed such that a value of 1 is a 1% growth rate.

This data is supposed to be generated from the [GTAP database](https://www.gtap.agecon.purdue.edu/databases/) and already processed,
users usually do not need to change. 

### PRODUCTIVITY.csv

The prodmat.csv file specifies productivity growth rates for all years in the projection.
It contains:  
- productivity growth in each year of the projection for each sector of the US. A value of 1 implies a 1% simple annual growth rate.  
- productivity convergence rates in each year of the projection for each sector of the US. A value of 1 implies a convergence rate of 1% (Note: Currently convergence rates are not used in the productivity level projections process.)  
- For each non-US region, for each sector, specify the starting period fraction of US productivity for the same sector (a value of 1 implies the same productivity). This is only required in the initial period.  
- For each non-US region, for each sector, in each year of the projection, specify the catch-up rate as that non-US region’s sector catches up to the productivity of the same sector in the US. A value of 0.02 implies that the gap in productivity from the previous year declines by 2% to determine the new gap to US productivity. Note that this is not the same as the productivity growth rate information.

The processed population data are then combined with processed productivity data to calculate the effective labour productivity,
defined as AL: the product of labour and productivity as per Solow-Swan.

### AEEINEW.csv

The aeeinew.csv file records data on Autonomous energy efficiency improvement.  
See McKibbin and Wilcoxen (2013) [A global approach to energy and environment: the G-Cubed model](https://www.researchgate.net/publication/285239562_A_global_approach_to_energy_and_environment_the_G-Cubed_model) for details of AEEI.


## The simulations folder and its contents

The simulations folder contains the one folder for each simulation experiment being conducted with the model.

## The experiment folder names are user-determined.

Each experiment folder contains an experiment design CSV file that configures the experiment, documenting
the layers of adjustments to variables that are to be applied in specific years through the projections.

## The sym folder and its contents

The sym folder stores machine generated contents that are used by the gcubed python module (.py, .lis and .csv files) and 
the [model definitions information page](../model_2R_164/sym/model_2R_164.html).

Currently in this folder, all files needed are already generated, so you do not need to run any of the commands below. 
But FYI, the *.sym files are used to generate the other files in that folder, by running the SYM processor <SYM>, sym4mac.exe on MacOS or sym4win.exe on Windows.

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
  