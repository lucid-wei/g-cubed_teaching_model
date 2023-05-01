---
layout: default
nav_order: 4
---
# Running the G-Cubed using your own Python script.

Modify the following python script to run the model. An example of this script is contained in the python directory of the model (python/run.py).

```
from gcubed.runner import Runner

# Working directory - where you will store outputs from the run.
# Configuration file location relative to the working directory.
# Experiment file location relative to the model simulations folder.
runner: Runner = Runner(
    working_directory="path/where/you want/the/results/to/be/saved/",
    configuration_file="relative/path/from/working/directory/to/configuration2R164.csv", 
    experiment_design_file="experiment1/design.csv"
    )

runner.run()
```

To execute this script, run the following command under the *IO_folder/python/* subfolder:
  ```
python run.py
  ```
If you encounter some error saying python is nowhere to be found, (assuming you already install python) this means you have not configured system PATH environment variables thus your terminal does not know where to find your installed python executable. Here is [a guide for this issue](https://stackoverflow.com/questions/6318156/adding-python-to-path-on-windows).

After a successful run, you will see the results generated in a folder (also under the *IO_folder/python/* subfolder), with baseline_projections.csv, deviation_projections.csv, simulation_projections.csv and a log file recording the process or problems during the computation process.

More specific use case examples please see another documentation .md file.
