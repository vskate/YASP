# YASP - Yet Another Start Page

![yasp demo gif](YASP_demo.gif)

***YASP*** is a clean and minimal start page, written entirely in HTML and SCSS, with support for custom themes and declarative configuration.

### Themes
All built-in themes can be found inside the `themes` folder.

Each theme has it's own directory with a `theme.scss` file, which defines the page colors and miscellaneous properties.

Visit the wiki for information on how to build your own theme!

### Fonts
All built-in fonts can be found inside the `fonts` folder.

Each font has it's own directory with the font files themselves and a `font.scss` file containing an appropriate `@font-face` definition and information about the font's actual name and how much space it requires in order not to clip into text.

Font definitions are written in a way, so that they are able to either use the included font file or the locally installed version of it.

Visit the wiki for information on how to include your own font!

## Configuration and build

### Creating the config file
The process of *building* your start page is a procedure which turns your `config.yaml` file into an HTML file which fully encapsulates the page and it's styles.
Everything happens inside the `build` directory, so it's a good idea to navigate to it before starting the build.

> [!NOTE]
> Your configuration file doesn't exist by default. Be sure to name it `config.yaml` or else it won't be recognised.

The configuration file takes the form of a YAML document with the following structure:
- `look` - Information about how the page looks
  - `theme` - Name of a built-in theme
    - Can also be an **absolute** or **relative** path to a locally available theme directory with a `theme.scss` file.
  - `font` - Name of a built-in font
    - Can also be an **absolute** or **relative** path to a locally available font directory with a `font.scss` file.
  - `image` - Path to an image to be displayed as the side "banner" picture
    - Can be either an **absolute** or **relative** path to a valid image file.
  - `message` - The welcome message displayed above the links
    - The text is directly injected into the HTML document, so any valid HTML is allowed and won't be sanitized.
  - `center_vertically` - Whether you want the contents to be centered vertically or not.
    - can be either **true** or **false**.
  - `border_radius` - Radius of the rounded corners of the border.
    - Can be **0** for none, or another number in pixels, of how big the radius is.
- `sections` - Defines the lists of links visible on the page
  - See the wiki for details on how the `sections` object is interpreted, although it's easy to understand from the example config provided below.
- `page` - Various metadata for the HTML document
  - `lang` - The language defined in the HTML tag (`<html lang="{lang}">`). Set to the same language as your browser to avoid auto-translation prompts
  - `title` - The title of the document (`<title>{title}</title>`) which will be displayed as the name of a new tab
- `search` - Search bar settings
  - `placeholder` - The placeholder text visible in the search box when it's empty

**All relative paths are resolved relative to the directory from which the build script is ran.**

<details>
<summary><b>Example configuration</b></summary>

```yaml
look:
  theme: catppuccin-macchiato
  font: UbuntuMono
  image: lucy_cyberpunk.png
  message: Hello, {name}!
sections:
  "uni":
    "github": {icon: "", url: "https://github.com"}
    "leetcode": {icon: "󰰍", url: "https://leetcode.com"}
    "itslearning": {icon: "󰑴", url: "https://sdu.itslearning.com"}
    "mail": {icon: "", url: "https://outlook.office.com"}
  "entertainment":
    "youtube": {icon: "", url: "https://youtube.com"}
    "reddit": {icon: "󰑍", url: "https://reddit.com"}
    "netflix": {icon: "󰝆", url: "https://netflix.com"}
page:
  lang: en
  title: startpage
search:
  placeholder: Search using DuckDuckGo
```

</details>

### Building your config
In order to turn your config into a working web page, you only need to run the `build/build.py` script.
```bash
cd build
python build.py
```

> [!TIP]
> It's recommended to start the build script when *inside* the `build` directory, to avoid issues with relative paths.

Your `index.html` file should now be located at `dist/index.html`.

## Looking for more tips?
Visit the wiki to learn more about how to customize your start page beyond the built-in stuff, configure the start page in various browsers and how you can contribute to the project!
