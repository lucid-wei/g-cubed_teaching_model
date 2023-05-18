---
layout: default
nav_order: 7
---
# Running a simulation experiment using G-Cubed.

Make sure [your Python environment is properly set up](environment_setup.md) and make sure that the `gcubed` Python package has been installed.

Modify the following Python script to run the model. [An example of this `run.py` script](../model/python/run.py) is available in the teaching model.

To execute this script, make sure your current directory is the one that contains the `run.py` script and then,
at the command prompt, run either:

```
python run.py
```

If you encounter some error saying Python is nowhere to be found, (assuming you already installed Python), you may not have configured your PATH environment variables so your computer does not know where to find your installed Python executable. Here is [a guide for fixing this problem](https://stackoverflow.com/questions/6318156/adding-python-to-path-on-windows).

After a successful run, you will see the results generated in a timestamped results subdirectory of the directory that you ran the command from. The results folder contains three CSV files and a log file:

* `baseline_projections.csv` 
* `deviation_projections.csv`
* `simulation_projections.csv`
* `run.log`

The log file is a text file that contains messages about the progress of the model run and any problems that arose.
