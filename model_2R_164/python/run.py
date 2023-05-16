from gcubed.runners.simple_runner import SimpleRunner

# Working directory - where you will store outputs from the run.
# Configuration file location relative to the working directory.
# Experiment file location relative to the model simulations folder.
runner: SimpleRunner = SimpleRunner(
    working_directory=".",
    configuration_file="../configuration2R164.csv", 
    experiment_design_file="experiment1/design.csv"
    )

runner.run()
