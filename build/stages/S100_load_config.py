from .base import *

import yaml


class Stage(BuildStage):
    @staticmethod
    def setup_args(parser: ArgumentParser):
        parser.add_argument(
            "-c", "--config",
            type=str,
            default="config.yaml",
            help="Specify the path to the configuration file"
        )

    def task(self):
        config_path = Path(self.arguments.config)

        if not config_path.is_file():
            log(f"Could not find a config file at:", color="red", bold=True)
            log(config_path.resolve())
            log("The build script cannot continue without it.", color="red")
            raise InterruptBuild

        with open(config_path, "r") as f:
            config = yaml.safe_load(f)

        self.state.config = config
