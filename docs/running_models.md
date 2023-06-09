---
layout: default
nav_order: 8
---
# Running a model

Make sure [your Python environment is properly set up](environment_setup.md) and make sure that the `gcubed` Python package has been installed.

Follow the instructions provided in [the documentation of the SimpleRunner](gcubed/runners/simple_runner.html) to create
a Python script called, say, `run.py`. An example of the relevant Python code is provided in the API documentation.

To execute your script, make sure your current directory is the one that contains the script and then,
at the command prompt, run:

```
python run.py
```

If you encounter some error saying Python is nowhere to be found, (assuming you already installed Python), you may not have configured your PATH environment variables so your computer does not know where to find your installed Python executable. Here is [a guide for fixing this problem](https://stackoverflow.com/questions/6318156/adding-python-to-path-on-windows).

