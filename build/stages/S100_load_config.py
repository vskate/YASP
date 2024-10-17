from .base import *

import yaml


class Stage(BuildStage):
    def task(self):
        config_path = self.build_dir_path / "config.yaml"

        if not config_path.is_file():
            log(f"Could not find a config file at:", color="red", bold=True)
            log(config_path)
            log("The build script cannot continue without it.", color="red")
            raise InterruptBuild

        with open(config_path, "r") as f:
            config = yaml.safe_load(f)

        self.state.config = config
