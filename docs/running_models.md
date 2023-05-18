---
layout: default
nav_order: 6
---
# Running a simulation experiment using G-Cubed.

Make sure [your Python environment is properly set up](2env_setup.md) and make sure that the `gcubed` Python package has been installed.

Modify the following Python script to run the model. An example of this script is contained in the Python directory of the model (`python/run.py`).

```
from gcubed.runners.simple_runner import SimpleRunner

# Working directory - where you will store outputs from the run.
# Configuration file location relative to the working directory.
# Experiment file location relative to the model simulations folder.
runner: SimpleRunner = SimpleRunner(
    working_directory="path/where/you want/the/results/to/be/saved/",
    configuration_file="relative/path/from/working/directory/to/configuration2R164.csv", 
    experiment_design_file="experiment1/design.csv"
    )

runner.run()
```

To execute this script, make sure your current directory is the one that contains the `run.py` script and then,
at the command prompt, run either:

```
python run.py
```

If you encounter some error saying Python is nowhere to be found, (assuming you already installed Python), you may not have configured your PATH environment variables so your computer does not know where to find your installed Python executable. Here is [a guide for fixing this problem](https://stackoverflow.com/questions/6318156/adding-python-to-path-on-windows).

After a successful run, you will see the results generated in a folder (also under the *model_files/python/* subfolder), with ``baseline_projections.csv`, `deviation_projections.csv`, `simulation_projections.csv` and a log file with messages about the progress of the model run and any problems that arose.
