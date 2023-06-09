---
layout: default
nav_order: 4
---

# SYM - the model definition language

The entities and economic relationships between them are described using a set of equations.
Those equations define the model and they are expressed using 
[the SYM language](https://pjwilcoxen.github.io/sym/).

Such model definitions are referred to as SYM model definitions and they are stored in SYM files.

The SYM files for a given model are included in 
[the set of files needed to run a model](model_sym_files.md).

Software is need to process the SYM files for a model to generate the files used to run the model
in Python and to generate suitably usable HTML documentation of the model. Those files,
generated by the SYM processor are also  included in 
[the set of files needed to run a model](model_sym_files.md).

The SYM processor is an executable file. It is available in a version that can be
run on both

* [Windows](../sym/sym4win.exe) and
* [MacOS](../sym/sym4mac.exe).

To change a model's equations, you need to edit the SYM model definitions and then run them
through the SYM processor to update the various generated files.

These changes may also require alterations to the model database and other inputs, depending 
on the changes that have been made. If the changes are fundamental enough, them may require
modifications to the Python package for G-Cubed.

## SYM model documentation

The SYM processor can transform the model definitions into a single HTML page that documents
the model.

An example is the documentation of the teaching model can be found [here](../model/sym/model_2R_164.html).

The documentation sets out:

* definitions of various sets
* definitions of the model variables and their type and their units etc.
* the model parameters 
* the model equations. 

This documentation is key to understanding the model and to designing your own simulations. 
But before using the model documentation, it is helpful to understand a bit more about the 
SYM model definition language and what to expect in a model definition. That understanding
can be developed by reviewing [the SYM language](https://pjwilcoxen.github.io/sym/).

# Sets

A given variable can be required in a model for various combinations of sectors and regions etc.

For example, in the teaching model, region `UU`, the United States and region `NN`, all other countries, 
both track their nominal GDP. Thus, the nominal GDP variable must be defined over the regions set.

Nominal GDP for the USA will be named `GDPN(UU)` and nominal GDP for all other countries combined
will be named `GDPN(NN)`.

A set is a collection of distinct objects or elements, which are used to define variables, parameters and equations.

In larger models, for example, with many sectors and many regions, these sets can be subsetted in
various ways as part of the model definition. This subsetting is evident in the documentation of
the model definition.

## Region and sector codes

Two types of sets are central to G-Cubed models, a set for regions and a set for sectors.

### The regions set

In the teaching model the `regions` set contains 2 regions:

`UU`, United States  
`NN`, Not United States

### The sectors set

In the teaching model the `sectors` set contains 2 sectors:
  
* `a01` The sector that produces energy
* `a02` The sector that produces all other material goods and 
services (but not capital for production or households)

All G-Cubed models have two additional sectors built into them:

* `Y` The sector that produces capital for firms
* `Z` The sector that produces capital for households

Care needs to be taken because these two capital-producing sectors 
are not explicitly included in the sectors set of G-Cubed models.

# Variables

G-Cubed models include many different variables. The name of each variable
has two components:

1. A prefix, starting with a letter and then followed by zero or more letters and digits.
2. An optional suffix, contained within round brackets, `()`, that specifies which members of
associated sets, the variable relates to, e.g. `GDPN(UU)` is nominal GDP, identified by the prefix,
for the United States, identified by the suffix that contains the regions set member for the United States.

## Variable Types

The variables have different types.

* `end` = normal endogenous variables
* `ets` = expected next period values of endogenous variables
* `cos` = costate (or jumping variables - that depend on expectations of the future)
* `sta` = state variables
* `stl` = state variables lagged by one period
* `exo` = exogenous variables.

Only exogenous variables do not have their own equations in the SYM model definition. Their
values, in all years, are determined outside of the system.

## Variable units:

All variables are expressed in their own units of measurement. Several units of measurement are 
usable within G-Cubed. These are:

pct = log or index
del = percentage point  
gdp = normalized by gdp  
usgdp = normalized by US gdp  
cent = cents per unit  
dollar = US dollars

## Variable Names

Variable names consist of the main name followed by relevant qualifier based on 
predefined **sets** enclosed within parentheses.

Examples:

Government debt in the USA is BOND(UU) where BOND is the main variable identifier and the qualifier contained in () is UU which is the country code for the USA.

The capital stock in sector 1 in the USA is defined as CAP(a01,UU) where CAP is the main variable idenitifier the first qualifier in () is the sector number and the second qualifier in the country code UU.

# Parameters <a id="parameters"></a>

Unlike variables, parameters remain constant throughout the projections generated by a model.

Like variables, parameters can also be defined over sets. The syntax for parameter names
is the same as that for variables.

When users adjust parameters, (usually) the entire dynamic of the model will change. 
Thus, (some) parameters can be altered when users design their own experiments.
Those user-defined parameters can be altered in [setparameters.csv](model_data_files.md#user-defined-parameters).

# Equations

Like variables, equations are also defined over sets.

The sets associated with an equation are explicit in the model documentation.

Model equations are divided into 4 groups:

1. State variable equations
2. Costate variable equations
3. Equations describing the formation of expected next-period values for endogenous variables
4. Endogenous variables

These groups of equations and the way that they are expressed and manipulated to solve the model
are explained in [the G-Cubed model solution documentation](papers/Solving%20G-Cubed%20without%20policy%20optimisation.pdf).