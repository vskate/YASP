import sys
from pathlib import Path
import importlib.util
import json
import argparse

from stages.base import BuildState, InterruptBuild, KeyNotFoundInConfigError, log

build_dir_path = Path(__file__).parent
stages_dir_path = build_dir_path / "stages"
root_dir_path = build_dir_path.parent

with open(stages_dir_path / "run.json", "r") as f:
    stages_to_run = json.load(f)


def import_stage(name):
    return importlib.import_module(f"stages.{name}")


state = BuildState()
stage_modules = []

args_parser = argparse.ArgumentParser()

for stage_name in stages_to_run:
    stage_module = import_stage(stage_name)
    stage_module.Stage.setup_args(args_parser)
    stage_modules.append(stage_module)


arguments = args_parser.parse_args()


for stage_module in stage_modules:
    stage_instance = stage_module.Stage(state, root_dir_path, build_dir_path, arguments)

    try:
        stage_instance.task()
    except InterruptBuild:
        sys.exit(1)
    except KeyNotFoundInConfigError as e:
        log(f"Key \"{e.key_path}\" not found in config.", color="red", bold=True)
        log("Refer to the documentation for instructions on how to correctly create a config file.", color="red")
        sys.exit(1)
