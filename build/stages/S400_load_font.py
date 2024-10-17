from .base import *


class Stage(BuildStage):
    # noinspection DuplicatedCode
    def task(self):
        if "font" not in self.state.config["look"]:
            raise KeyNotFoundInConfigError("look/font")

        font_name = self.state.config["look"]["font"]
        font_dir = self.root_dir_path / "fonts" / font_name
        font_name = font_dir.name

        if not font_dir.is_dir():
            font_dir = Path(font_name)

            if not font_dir.is_dir():
                log(f"Font \"{font_name}\" doesn't exist!", color="red", bold=True)
                log(font_dir)
                log(f"Make sure there are no typos in the config file or the font directory name and that the font "
                    f"exists at the path shown above.", color="red")
                raise InterruptBuild

        font_file_path = font_dir / "font.scss"

        if not font_file_path.is_file():
            log(f"The directory for the \"{font_name}\" font exists, but there is no font.scss file inside it!",
                color="red", bold=True)
            log("Make sure there is no typo in the name of the file.", color="red")
            raise InterruptBuild

        with open(font_file_path, "r") as f:
            font_content = f.read()
            self.state.scss_sources.append(font_content)

        log(f"📝 {font_name} ", end="")
        log(f"({font_file_path})", color="gray")
