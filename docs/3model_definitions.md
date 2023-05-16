---
layout: default
nav_order: 3
---
# [Model definitions](../model_2R_164/sym/model_2R_164.html)

Two components are needed to run the model, simply put, input data (of various kinds) and the algorithm.   
Input and output data vary depending on the model version, this repository stores those for the teaching version of the model, model 2R164. The algorithm or computing logic is packaged into a python package which can be installed into one's local machine.

The model definitions for this particular model version can be found in 
[this link or the one above](../model_2R_164/sym/model_2R_164.html), which includes definitions of sets, variables, parameters and equations.

This file will be referenced a lot when you design your own simulations. But before reading the model definitions, a few conventions should be kept in mind to understand that file:

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
