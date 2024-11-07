import mimetypes
import base64

from .base import *


def image_to_data_url(path) -> str | None:
    mimetype, _ = mimetypes.guess_type(path)

    if mimetype is None:
        return None

    with open(path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("utf-8")

    return f"data:{mimetype};base64,{encoded}"


class Stage(BuildStage):
    def task(self):
        if "icon" not in self.state.config["search"]:
            raise KeyNotFoundInConfigError("search/icon")

        image_path = Path(self.state.config["search"]["icon"])
        log(f"📷 {image_path}")

        if not image_path.is_file():
            log("Could not find the specified icon image file at:", color="red", bold=True)
            log(image_path)
            log("Make sure that the file exists and that there is no typo in the config file.", color="red")
            raise InterruptBuild

        log("Converting image... ", end="")
        encoded = image_to_data_url(image_path)
        log("Done!", color="green")

        if not encoded:
            log("Could not convert the specified icon image file at:", color="red", bold=True)
            log(image_path)
            log("This probably means, that the script had an issue while trying to guess what type of image "
                "it is. Make sure that your file is in a supported format.", color="red")
            raise InterruptBuild

        self.state.config["search"]["icon"] = encoded
