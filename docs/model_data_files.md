---
layout: default
nav_order: 4
---

# Model data files

The data subdirectory contains the data files for the model. All of the data files are in the CSV format.

The files are comma delimited and none of the values in those files are allowed to contain commas.

### The database

The <DATABASE>.csv contains the model database. 

See [the teaching model example](../model/data/DATAvR2018.csv).

It must be populated with data for all variables in the model 
for one or more years leading up to and including 
the first projection year. Data can also be included for years after the first
projection year. Data after the first projection year will be ignored when 
running the model.

Data in this file is considered to be the observed historical data 
for all of the variables in the model. 

The first row of the data file contains the column headings. All other rows
of the datafile contain data, with one row for each variable in the model.
The variables have a strict ordering that must correspond to the ordering of
the variables produced by the SYM processor from the SYM model definition.

You can find the variables in the model, in this strict order, in 
[the varmap file](../model/sym/model_2R_164_varmap.csv).

Following the variables names, are 
descriptions, units of measurement, and country/region code.

More detailed definitions of the variables are in 



### The input/output tables for all regions

The <IOTABLES>.csv contains the Input/Output tables for all regions.


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
More information on parameters please check [related model definitions section](sym_model_definitions.md#parameters).

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

