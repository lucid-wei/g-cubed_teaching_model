---
layout: default
nav_order: 3
---

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

| Field                                 | Current Value      | Other Valid Values | Brief                                                                                                                                                                                                                              | Roles in the gcubed Python module                                                                                                                                                                                                                                                                                        |
|---------------------------------------|--------------------|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version                               | 2R                 | 6G, 20C, 20J, 20R  | The model version (number of regions followed by a letter indicating model type e.g. 2R)                                                                                                                                           | Determine sectors in the model, locate SYM generated Python equations file.                                                                                                                                                                                                                                              |
| Build                                 | 164                | 170, 170logv3      | The model build - must start with a positive integer but can include other letters and digits (no spaces or punctuation though).                                                                                                   | Same as above. Different builds of the same version impact calculation procedure, often a new build has new features or bug fixes.                                                                                                                                                                                       |
| Debugging                             | 1                  | 0                  | Set to 1 if debugging and 0 otherwise. This affects model logging verbosity. [Location in source code](./gcubed/base.html#gcubed.base.Base.DOING_DETAILED_DEBUG)                                                                   | Impact the amount of information you see in log file and terminal. (A feature under development, currently has no big impact for gcubed-1.0.0)                                                                                                                                                                           |
| SymInputFile                          | ggg2r164.sym       | e.g. ggg20c169.sym | The root SYM file containing the model definition.                                                                                                                                                                                 | Determine the [absolute path of the sym input file](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.sym_input_file) to be processed by the sym processor to produce the sym details for the model and the model equations in Python.                                                     |
| Database                              | DATAvR2018.csv     | Not available      | The database of values for the model variables in a range of years.                                                                                                                                                                | Determine the [absolute path of the database file](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.database_file) to be loaded by gcubed.data.database.Database which calls [load_data function.](./gcubed/base.html#gcubed.base.Base.load_data)                                         |
| BaseYear                              | 2018               | Not available      | The base year of the database that is loaded. [Location in source code](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.base_year)                                                                 | The year in which all indexes are based at 1 (so their log values are 0). Databases can be rebased to different years.                                                                                                                                                                                                   |
| UserParameters                        | setparameters.csv  | Not available      | The user-specified parameter values.                                                                                                                                                                                               | Determine the [absolute path of the parameters file](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.parameters_file) to be loaded by [gcubed.model_parameters.parameters.Parameters](./gcubed/model_parameters/parameters.html#gcubed.model_parameters.parameters.Parameters.validate). |
| IOTables                              | IOTABLESvR2011.csv | Not available      | The IO tables used for parameter calibration.                                                                                                                                                                                      | Determine the [absolute path of the IO data file](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.io_table_file) to be loaded by [gcubed.io_data.IOData](./gcubed/io_data.html).                                                                                                         |
| Productivity                          | prodmat.csv        | Not available      | The productivity parameters.                                                                                                                                                                                                       | Determine the [absolute path of the productivity file](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.productivity_file) to be loaded by [gcubed.baseline.productivity.Productivity](./gcubed/baseline/productivity.html).                                                              |
| Population                            | modpop.csv         | Not available      | Population growth data.                                                                                                                                                                                                            | Determine the [absolute path of the population data file](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.population_file) to be loaded by [gcubed.baseline.population.Population](./gcubed/baseline/population.html).                                                                   |
| AutonomousEnergyEfficiencyImprovement | aeeinew.csv        | Not available      | The AEEI data file.                                                                                                                                                                                                                | Determine the [absolute path of the AEEI data file](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.aeei_file) to be loaded by [gcubed.baseline.energy_usage_efficiency.EnergyUsageEfficiency](./gcubed/baseline/energy_usage_efficiency.html).                                          |
| CalibrationYear                       | 2011               | Not available      | Related to the year used to create the database. [Location in source code](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.calibration_year)                                                       | Used to calibrate non-user-defined parameters in [gcubed.model](./gcubed/model.html) and load rhs vectors in [gcubed.linearisation.model_solver.ModelSolver](./gcubed/linearisation/model_solver.html).                                                                                                                  |
| LinearisationYear                     | 2011               | Not available      | Year determining the data used to linearise the model to generate baseline projections. [Location in source code](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.linearisation_year)              | Year around which the model is transformed from non-linear to linear by [gcubed.linearisation.linear_model.LinearModel](./gcubed/linearisation/linear_model.html), so that the model can be solved.                                                                                                                      |
| CalibrationOfCarbonCoefficientsYear   | 2015               | Not available      | The year used to calibrate carbon emissions coefficients. [Location in source code](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.calibration_of_carbon_coefficients_year)                       | Used to read emissions parameters from database by __set_emissions_parameters() in [gcubed.model_parameters.parameters.Parameters](./gcubed/model_parameters/parameters.html).                                                                                                                                           |
| FirstProjectionYear                   | 2018               | Not available      | The first year to create model projections for. There must be data in the database for this year. [Location in source code](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.first_projection_year) | Used to create various projections, e.g. [gcubed.baseline.effective_labour_productivity.EffectiveLabourProductivity._configure_ROGY](./gcubed/baseline/effective_labour_productivity.html#gcubed.baseline.effective_labour_productivity.EffectiveLabourProductivity._configure_ROGY), [gcubed.baseline.productivity.Productivity._create_productivity_projections]().                                                                                                |
| LastProjectionYear                    | 2100               | Not available      | The last year to generate projections for. [Location in source code](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.last_projection_year)                                                         | Used in combination with FirstProjectionYear to create various projections, examples are the same as above.                                                                                                                                                                                                              |
| StableManifoldTolerance               |                    |                    |                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                          |
| StableManifoldMaximumIterations       |                    |                    |                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                          |
| NeutralRealInterestRate               |                    |                    |                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                          |

