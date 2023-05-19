---
layout: default
nav_order: 3
---


# G-Cubed model overview

{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

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
```


The simulations subdirectory and the python subdirectory are optional but the data and the sym subdirectories
must exist and they must contain the necessary files.

## The files in the data directory

For details, review [the data file documentation](model_data_files.md).

## The files in the sym directory

For details, review [the sym file documentation](model_sym_files.md).

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

This file is loaded by [gcubed.model_configuration.ModelConfiguration.load_configuration_details](./gcubed/model_configuration.html#gcubed.model_configuration.ModelConfiguration.load_configuration_details).
