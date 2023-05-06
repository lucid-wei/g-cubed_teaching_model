---
layout: default
nav_order: 3
---
# [Model definitions](./model_2R_164/sym/model_2R_164.html)

The model definitions for this particular model version can be found in 
[this link](./model_2R_164/sym/model_2R_164.html), which includes definitions of sets, variables, parameters and equations.

This file will be referenced a lot when you design your own simulations. But before reading the model definitions, 
a few conventions should be kept in mind to understand that file:

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

A set is a collection of distinct objects or elements, which are used to define variables.

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

WHICH ONES???????

# Parameters

Like variables, parameters are also defined over sets. 

When users adjust parameters, (usually) the entire dynamic of the model will change. 
Thus, (some) parameters can be altered when users design their own experiments.

WHICH ONES???????

# Equations

Like variables, equations are also defined over sets.
