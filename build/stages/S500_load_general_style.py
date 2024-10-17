from .base import *


class Stage(BuildStage):
    def task(self):
        sources_path = self.build_dir_path / "sources"
        style_file_path = sources_path / "style.scss"

        if not style_file_path.is_file():
            log(f"Could not find the main page stylesheet at:", color="red", bold=True)
            log(style_file_path)
            log("The build script cannot continue without it.", color="red")
            raise InterruptBuild

        with open(style_file_path, "r") as f:
            style_content = f.read()
            self.state.scss_sources.append(style_content)
