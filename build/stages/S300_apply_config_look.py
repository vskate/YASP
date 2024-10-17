from .base import *


class Stage(BuildStage):
    def task(self):
        if "center_vertically" not in self.state.config["look"]:
            raise KeyNotFoundInConfigError("look/center_vertically")

        center_vert = self.state.config["look"]["center_vertically"]

        if "border_radius" not in self.state.config["look"]:
            raise KeyNotFoundInConfigError("look/border_radius")

        border_radius = self.state.config["look"]["border_radius"]

        scss_content = (f"$centerVertically: {center_vert};\n"
                        f"$borderRadius: {border_radius};\n")

        self.state.scss_sources.append(scss_content)
