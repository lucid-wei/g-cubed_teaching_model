---
layout: default
nav_order: 5
---

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
  

