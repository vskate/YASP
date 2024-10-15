import importlib.util

from .base import *


def check_if_module_exists(name: str):
    return importlib.util.find_spec(name) is not None


class Stage(BuildStage):
    dependencies = {
        "yaml": {
            "name": "PyYAML",
            "instructions": {
                "debian": "sudo apt install python3-yaml",
                "arch": "yay -S python-yaml",
                "pip": "pip install pyyaml"
            }
        },
        "sass": {
            "name": "libsass",
            "instructions": {
                "debian": "sudo apt install python3-libsass",
                "arch": "yay -S python-libsass",
                "pip": "pip install libsass"
            }
        },
        "jinja2": {
            "name": "Jinja2",
            "instructions": {
                "debian": "sudo apt install python3-jinja2",
                "arch": None,
                "pip": "pip install jinja2"
            }
        }
    }

    instructions_platforms = {
        "debian": "Debian/Ubuntu-based systems",
        "arch": "Arch-based systems",
        "pip": "Windows/Other"
    }

    def task(self) -> bool:
        failures = [
            dependency
            for dependency in self.dependencies.keys()
            if not check_if_module_exists(dependency)
        ]

        if len(failures) == 0:
            return True

        log("Failed to resolve one or more dependencies:", color="red", bold=True)

        for dependency_name in failures:
            log(f"- {self.dependencies[dependency_name]['name']}", color="red")
            log("\tInstall it using one of these commands depending on your platform:")

            for platform, command in self.dependencies[dependency_name]["instructions"].items():
                if command is None:
                    continue

                log(f"\t{self.instructions_platforms[platform]}: ", bold=True, end="")
                log(command)
