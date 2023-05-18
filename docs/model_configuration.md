---
layout: default
nav_order: 3
---
# The files associated with the G-Cubed teaching model
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>


# Model usage

Running a model entails generation of a set of baseline projections. Projections
are values for each variable in the model, for each of the years from the start
of the projections to the end of the projections, potentially spanning many decades.

A simulation experiment also generates simulation projections that can be compared 
to the baseline projections.

The baseline projections and the simulation projections will naturally depend in which 
model is being run.

# Different models

G-Cubed supports simulation experiments using a variety of model versions. These versions differ
in terms of the regions included in the model, the sectors in each region, and the economic
relationships embodied in the equations describing the model version.

Model versions also differ in terms of how the model parameters are calibrated using the available
data about each region in the model. The calibration rules are built into G-Cubed and cannot be modified.

However, you can modify the data used to do parameter calibration, you can modify the data used to set up 
a model simulation, and you can modify the shocks that impact the simulated economy, through the course
of the model projections.

All of files that specify the details (including the data) for a model version need to be in
a set of files with a specific organisation within directories. 

This document sets out how the files must be stored, and how the data files must be formatted.

## Model identification

A specific model is identified by the combination of its version and its build. A particular model version 
can have many different builds.

### Model versions

Version codes have two parts, a number and a letter. The number indicates the number of regions
in the version of the model. The letter is used to differentiate versions of the model that have
different regions, even if the number of regions is the same. The letter is capitalised.

Thus, model `2R` has 2 regions. Model `20J` has 20 regions. Model `20C` also has 20 regions but the regions
are different from those in model version `20J`.

### Model builds

Model versions are improved over time. Each improvement is released as a new build of the model version.

Model builds are also identified by a number and an optional string of other letters amd digits. Examples include
`164`, `170`, and `170log`.

The prefix number in the model build increases over time. The suffix in the model build differentiates models
of the same generation if they differ in material ways.

# The files required to run a G-Cubed model
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

A specific version of a G-Cubed model requires a number of files to run. These files are organised into a root directory with a set of subdirectories. The gcubed package will load these files and produce certain outputs into this root directory.

All directories have lower-case names. This must not be changed because G-Cubed is case sensitive.

The file names that include parts like <PART> are to be substituted as follows:
* <VERSION> replace with the version of the model, e.g. `2R`, `20C`, etc.
* <BUILD> replace with the build of the model, e.g. `169`, `170`, `170log` etc.
* <NUMBER> replace with the build number of the model: e.g. `170` if the build is `17log`.
* <?> For anything else in <> use whatever text you want, 
but make sure that it matches the file name details given in the model configuration file,
the `<CONFIGURATION>.csv` file that must be in the root directory of the 
model's directory structure.

The model version and the model build values used in file naming must match their 
values in the model configuration file.

```
├── <ROOT_DIRECTORY>
├── <CONFIGURATION>.csv
├── data
│   │   ├── <DATABASE>.csv
│   │   ├── <IOTABLES>.csv
│   │   ├── <SETPARAMETERS>.csv
│   │   ├── <POPULATION>.csv
│   │   ├── <PRODUCTIVITY>.csv
│   │   ├── <AEEINEW>.csv
├── sym
│   │   ├── <ROOTSYMFILE>.sym
│   │   ├── *.sym
│   │   ├── model_<VERSION>_<NUMBER>_eqnmap.sym
│   │   ├── model_<VERSION>_<NUMBER>_optmap.sym
│   │   ├── model_<VERSION>_<NUMBER>_varmap.sym
│   │   ├── model_<VERSION>_<NUMBER>_varinfo.sym
│   │   ├── model_<VERSION>_<NUMBER>_vars.sym
│   │   ├── model_<VERSION>_<NUMBER>.lis
│   │   ├── model_<VERSION>_<NUMBER>.py
├── simulations
│   ├── <EXPERIMENT1>
│   │   ├── <EXPERIMENT1_DESIGN>.csv
│   │   ├── <LAYER1_DATA>.csv
│   │   ├── ...
│   ├── <EXPERIMENT2>
│   │   ├── <EXPERIMENT2_DESIGN>.csv
│   │   ├── <LAYER1_DATA>.csv
│   │   ├── <LAYER2_DATA>.csv
│   │   ├── ...
│   ├── ...
├── python
│   ├── run.py
│   ├── results_<GENERATION-TIMESTAMP>
│   │   ├── baseline_projections.csv
│   │   ├── deviation_projections.csv
│   │   ├── simulation_projections.csv
│   │   ├── run.log
```


The simulations subdirectory and the python subdirectory are optional but the data and the sym subdirectories
must exist and they must contain the necessary files.


## The configuration file

The `<CONFIGURATION>.csv` model configuration file contains all of the 
information needed to load a specific model. It must be in the root directory.

You can model your own configuration file on the [configuration file for the teaching model](../model/configuration2R164.csv)

The configuration file sets up all of the details of the model that is to be used. This includes:

* the files where parameter calibration and initial variable state data are stored
* settings affecting parameter calibration
* settings affecting model linearisation
* settings for how the model is 'solved'
* settings affecting the baseline projections

All of these settings are detailed in [the documentation of the Model Configuration API](gcubed/model_configuration.html).

This file is loaded by [gcubed.model_configuration.ModelConfiguration.load_configuration_details](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.load_configuration_details) during running. 
The details of each field is shown below.

<style>
    table {
        width: 106%;
        table-layout: fixed;
    }
    
    th:nth-child(1),
    td:nth-child(1) {
        width: 13%;
    }
    
    th:nth-child(2),
    td:nth-child(2) {
        width: 13%;
    }
    
    th:nth-child(3),
    td:nth-child(3) {
        width: 10%;
    }
    th:nth-child(4),
    td:nth-child(4) {
        width: 30%;
    }
    th:nth-child(5),
    td:nth-child(5) {
        width: 40%;
    }
</style>

[location_ModelConfiguration]: ./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration
Note: You may find more documentations if you jump into the links like '[Location in source code]' below.
[first_projection_year]: ./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.first_projection_year
[configure_ROGY]: ./gcubed/baseline/effective_labour_productivity.html#gcubed.baseline.effective_labour_productivity.EffectiveLabourProductivity._configure_ROGY
[Parameters.validate]: ./gcubed/model_parameters/parameters.html#gcubed.model_parameters.parameters.Parameters.validate
[create_productivity_projections]: ./gcubed/baseline/productivity.html#gcubed.baseline.productivity.Productivity._create_productivity_projections
[_load_energy_usage_efficiency_data]: ./gcubed/baseline/energy_usage_efficiency.html#gcubed.baseline.energy_usage_efficiency.EnergyUsageEfficiency._load_energy_usage_efficiency_data

| Field                                 | Current Value      | Other Valid Values | Brief                                                                                                                                                                                                                     | Roles in the gcubed python module                                                                                                                                                                                                                                                                                                   |
|---------------------------------------|--------------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version                               | 2R                 | 6G, 20C, 20J, 20R  | The model version (number of regions followed by a letter indicating model type e.g. 2R)                                                                                                                                  | Determine sectors in the model, locate SYM generated Python equations file.                                                                                                                                                                                                                                                         |
| Build                                 | 164                | 170, 170logv3      | The model build - must start with a positive integer but can include other letters and digits (no spaces or punctuation though).                                                                                          | Same as above. Different builds of the same version impact calculation procedure, often a new build has new features or bug fixes.                                                                                                                                                                                                  |
| Debugging                             | 1                  | 0                  | Set to 1 if debugging and 0 otherwise. This affects model logging verbosity. [Location in source code](./gcubed/base.html#gcubed.base.Base.DOING_DETAILED_DEBUG)                                                          | Impact the amount of information you see in log file and terminal. (A feature under development, currently has no big impact for gcubed-1.0.0)                                                                                                                                                                                      |
| SymInputFile                          | ggg2r164.sym       | e.g. ggg20c169.sym | The root SYM file containing the model definition.                                                                                                                                                                        | Determine the [absolute path of the sym input file](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.sym_input_file) to be processed by the sym processor to produce the sym details for the model and the model equations in Python.                                                                |
| Database                              | DATAvR2018.csv     | Not available      | The database of values for the model variables in a range of years.                                                                                                                                                       | Determine the [absolute path of the database file](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.database_file) to be loaded by gcubed.data.database.Database which calls [load_data function.](./gcubed/base.html#gcubed.base.Base.load_data)                                                    |
| BaseYear                              | 2018               | Not available      | The base year of the database that is loaded. [Location in source code](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.base_year)                                                        | The year in which all indexes are based at 1 (so their log values are 0). Databases can be rebased to different years.                                                                                                                                                                                                              |
| UserParameters                        | setparameters.csv  | Not available      | The user-specified parameter values.                                                                                                                                                                                      | Determine the [absolute path of the parameters file](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.parameters_file) to be loaded by [gcubed.model_parameters.parameters.Parameters][Parameters.validate].                                                                                         |
| IOTables                              | IOTABLESvR2011.csv | Not available      | The IO tables used for parameter calibration.                                                                                                                                                                             | Determine the [absolute path of the IO data file](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.io_table_file) to be loaded by [gcubed.io_data.IOData](./gcubed/io_data.html#gcubed.io_data.IOData._load_io_tables).                                                                              |
| Productivity                          | prodmat.csv        | Not available      | The productivity parameters.                                                                                                                                                                                              | Determine the [absolute path of the productivity file](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.productivity_file) to be loaded by [gcubed.baseline.productivity.Productivity](./gcubed/baseline/productivity.html#gcubed.baseline.productivity.Productivity._load_productivity_parameters). |
| Population                            | modpop.csv         | Not available      | Population growth data.                                                                                                                                                                                                   | Determine the [absolute path of the population data file](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.population_file) to be loaded by [gcubed.baseline.population.Population](./gcubed/baseline/population.html#gcubed.baseline.population.Population._load_population_growth_rates).          |
| AutonomousEnergyEfficiencyImprovement | aeeinew.csv        | Not available      | The AEEI data file.                                                                                                                                                                                                       | Determine the [absolute path of the AEEI data file](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.aeei_file) to be loaded by [gcubed.baseline.energy_usage_efficiency.EnergyUsageEfficiency][_load_energy_usage_efficiency_data].                                                                 |
| CalibrationYear                       | 2011               | Not available      | Related to the year used to create the database. [Location in source code](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.calibration_year)                                              | Used to calibrate non-user-defined parameters in [gcubed.model.__init__](./gcubed/model.html).                                                                                                                                                                                                                                      |
| LinearisationYear                     | 2011               | Not available      | Year determining the data used to linearise the model to generate baseline projections. [Location in source code](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.linearisation_year)     | Year around which the model is transformed from non-linear to linear by [gcubed.linearisation.linear_model.LinearModel.__init__](./gcubed/linearisation/linear_model.html), so that the model can be solved.                                                                                                                        |
| CalibrationOfCarbonCoefficientsYear   | 2015               | Not available      | The year used to calibrate carbon emissions coefficients. [Location in source code](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.calibration_of_carbon_coefficients_year)              | Used to read emissions parameters from database by [_set_emissions_parameters() in gcubed.model_parameters.parameters.Parameters](./gcubed/model_parameters/parameters.html#gcubed.model_parameters.parameters.Parameters._set_emissions_parameters).                                                                               |
| FirstProjectionYear                   | 2018               | Not available      | The first year to create model projections for. There must be data in the database for this year. [Location in source code][first_projection_year]                                                                        | Used to create various projections, e.g. [gcubed.baseline.effective_labour_productivity.EffectiveLabourProductivity._configure_ROGY][configure_ROGY], [gcubed.baseline.productivity.Productivity._create_productivity_projections][create_productivity_projections].                                                                |
| LastProjectionYear                    | 2100               | Not available      | The last year to generate projections for. [Location in source code](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.last_projection_year)                                                | Used in combination with FirstProjectionYear to create various projections, examples are the same as above.                                                                                                                                                                                                                         |
| StableManifoldTolerance               | 1e-9               | By use case        | Convergence criterion when solving for the stable manifold. [Location in source code](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.stable_manifold_tolerance)                          | If H1 or H2 matrix alters in magnitude larger than this value, iteration continues, see [gcubed.linearisation.stable_manifold.StableManifold.solve](./gcubed/linearisation/stable_manifold.html#gcubed.linearisation.stable_manifold.StableManifold.solve).                                                                         |
| StableManifoldMaximumIterations       | 1000               | By use case        | Maximum number of iterations allowed while solving for the stable manifold. [Location in source code](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.stable_manifold_maximum_iterations) | If number of iterations reach this limit before converging, iteration stops and raises an error, see [gcubed.linearisation.stable_manifold.StableManifold.solve](./gcubed/linearisation/stable_manifold.html#gcubed.linearisation.stable_manifold.StableManifold.solve).                                                            |
| NeutralRealInterestRate               | 0.036              | Not available      | The neutral real interest rate as a decimal rather than percentage. [Location in source code](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.neutral_real_interest_rate)                 | Used to replace database value of interest rate variables ('INPL', 'INPN', 'INTF', 'INTL', 'INTN', 'INTR') at linearisation year and first projection year, see usages of [gcubed.data.database.Database.rhs_vector_value()](./gcubed/data/database.html#gcubed.data.database.Database.rhs_vector_value)                            |

<style>
/* Reset CSS */
table {
    table-layout: fixed;
    width: 100%;
}

th:nth-child(n+1),
td:nth-child(n+1) {
    width: auto;
    word-wrap: break-word;
}

</style>


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

The simulations folder contains one folder for each simulation experiment being conducted with the model.

The experiment folder names are user-determined. Each experiment folder contains an experiment design CSV file that configures the experiment, documenting
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
cd path/where/you/extract/this/repo/model_model_files/sym
```
where cd is a common command in both Windows and MacOS, standing for 'change directory'.
  