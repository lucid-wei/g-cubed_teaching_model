from gcubed.runners.simple_runner import SimpleRunner

runner = SimpleRunner(
    working_directory=".",
    configuration_file="configuration2R164.csv",
    experiment_design_file="experiment1/design.csv",
)
runner.save_results = True
runner.annotate_results = True
runner.run()
