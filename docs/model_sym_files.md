---
layout: default
nav_order: 5
---

# SYM model definitions

Two components are needed to run the model:

* the model definition, expressed as a set of equations in the SYM language; and 

* the data used to calibrate the model parameters and to provide starting values
when generating baseline projections.

Input and output data vary depending on the model version, this repository stores those for the teaching version of the model, model 2R164. The algorithm or computing logic is packaged into a Python package which can be installed into one's local machine.

Documentation of the SYM definition of the teaching model can be found [here](../model/sym/model_2R_164.html). It includes definitions of sets, variables, parameters and equations. This documnentation is key
to understanding the model and to designing your own simulations. But before using the model documentation, 
it is helpful to understand a bit more about the SYM model definition language and what to expect in a model
definition.

# Country and sector codes

COUNTRIES:  
U, USA, United States  
N, NUS, Not United States

SECTORS:  
01 Energy  
02 Non Energy

Y. Capital goods for firms  
Z. Household capital goods

# Sets

Because a same type of variable can be used to describe different objects, e.g. country U and country N both have their GDP values. 
Thus, variables must be defined over sets. 

A set is a collection of distinct objects or elements, which are used to define variables, parameters and equations.

# Variables

## Variable Names

Variable names consist of the main name followed by relevant qualifier based on predefined **sets** enclosed within parentheses.

Examples:

Government debt in the USA is BOND(UU) where BOND is the main variable identifier and the qualifier contained in () is UU which is the country code for the USA.

The capital stock in sector 1 in the USA is defined as CAP(a01,UU) where CAP is the main variable idenitifier the first qualifier in () is the sector number and the second qualifier in the country code UU.

## Variable Types

end = normal endogenous  
ets = endogenous with lead  
cos = costate (or jumping variable - value is an integral of future variables)   
stl = state with lags  
sta = state (value is predetermined in period t)  
exo = exogenous (value is fixed)  

## Variable units:

pct = log or index  
del = percentage point  
gdp = normalized by gdp  
usgdp = normalized by US gdp  
cent = cents per unit  

## User configurable variables

Some variables can be set by users to design their own experiments.

Note that only exogenous variables and to the initial value of the state variables are configurable when designing simulations.  

Some parameters are also configurable, see next section below.

# Parameters <a id="parameters"></a>

Like variables, parameters are also defined over sets. 

When users adjust parameters, (usually) the entire dynamic of the model will change. 
Thus, (some) parameters can be altered when users design their own experiments.
Those user-defined parameters can be altered in [setparameters.csv](4model_files.md#setparameters).

However, it is currently not supported to load parameters changes from a csv file like you do to variables,
i.e. users cannot specify dynamics to parameters. If you need to see the effects of parameter changes,
you need to run different simulations separately and check their difference in simulation results manually.

# Equations

Like variables, equations are also defined over sets.

## The sym directory and its contents

The sym directory stores machine generated contents that are used by the gcubed Python module (.py, .lis and .csv files) and 
the [model definitions information page](../model/sym/model_2R_164.html).

Currently in this directory, all files needed are already generated, so you do not need to run any of the commands below. 
But FYI, the *.sym files are used to generate the other files in that directory, by running the SYM processor <SYM>, sym4mac.exe on MacOS or sym4win.exe on Windows.

If the root file of the SYM model definition (the *.sym files) is called ggg2r170.sym, then the command to generate these files is:
```
<SYM> -python ggg2r170.sym model_<VERSION>_<NUMBER>.py
```

To generate the HTML documentation of the model, run:
```
<SYM> -html ggg2r170.sym model_<VERSION>_<NUMBER>.html
```

Both of these commands should be run from within the sym subdirectory documented above. In other words, you will need to run command like this to change your location before you run your .exe:
```
cd path/where/you/extract/this/repo/model_model_files/sym
```
where cd is a common command in both Windows and MacOS, standing for 'change directory'.
  

