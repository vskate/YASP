from .base import *


class Stage(BuildStage):
    # noinspection DuplicatedCode
    def task(self):
        if "theme" not in self.state.config["look"]:
            raise KeyNotFoundInConfigError("look/theme")

        theme_name = self.state.config["look"]["theme"]
        theme_dir = self.root_dir_path / "themes" / theme_name
        theme_name = theme_dir.name

        if not theme_dir.is_dir():
            theme_dir = Path(theme_name)

            if not theme_dir.is_dir():
                log(f"Theme \"{theme_name}\" doesn't exist!", color="red", bold=True)
                log(theme_dir)
                log(f"Make sure there are no typos in the config file or the theme directory name and that the theme "
                    f"exists at the path shown above.", color="red")
                raise InterruptBuild

        theme_file_path = theme_dir / "theme.scss"

        if not theme_file_path.is_file():
            log(f"The directory for the \"{theme_name}\" theme exists, but there is no theme.scss file inside it!",
                color="red", bold=True)
            log("Make sure there is no typo in the name of the file.", color="red")
            raise InterruptBuild

        with open(theme_file_path, "r") as f:
            theme_content = f.read()
            self.state.scss_sources.append(theme_content)

        log(f"🎨 {theme_name} ", end="")
        log(f"({theme_file_path})", color="gray")
