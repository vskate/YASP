from .base import *

import jinja2 as j2
import sass


class Stage(BuildStage):
    def task(self):
        sources_path = self.build_dir_path / "sources"
        html_output_path = self.build_dir_path.parent / "dist" / "index.html"

        self.state.additional_render_vars = {}

        scss_string = "\n".join(self.state.scss_sources)

        try:
            compiled_css = sass.compile(string=scss_string, output_style="compressed")
        except sass.CompileError as e:
            log("Failed to compile your theme/font:", color="red", bold=True)
            log(e, color="red")
            raise InterruptBuild

        j2_env = j2.Environment(loader=j2.FileSystemLoader(sources_path), autoescape=j2.select_autoescape())

        try:
            index_template = j2_env.get_template("index.j2")
        except j2.TemplateNotFound:
            log(f"Could not find page template at:", color="red", bold=True)
            log(sources_path / "index.j2")
            log("The build script cannot continue without it.", color="red")
            raise InterruptBuild

        self.state.additional_render_vars["styles"] = compiled_css

        index_content = index_template.render(**self.state.config, builder=self.state.additional_render_vars)

        with open(html_output_path, "w") as f:
            f.write(index_content)

        log(f"✅ Compiled to: {html_output_path}", color="green", bold=True)
