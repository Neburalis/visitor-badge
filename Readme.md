# Visitor Badge

<p align="center">
    <img src="https://img.shields.io/github/last-commit/neburalis/visitor-badge?style=flat">
    <img src="https://img.shields.io/badge/License-AGPL-blue?style=flat">
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&amp;logo=Python&amp;logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat&amp;logo=FastAPI&amp;logoColor=white" alt="FastAPI">
    <img src="https://img.shields.io/badge/Docker%20Compose-2496ED?style=fflat&logo=docker&logoColor=white">
    <img src="https://img.shields.io/badge/postgresql-4169e1?style=flat&logo=postgresql&logoColor=white">
</p>

**Count visitors for your README.md, Issues, and PRs on GitHub with just one line of markdown code.**

## Features

- **Easy Integration**: Add just one line to your README.md or any other part of GitHub to count visitors.
- **Customizable Label and Color**: Customize the badge text and color to match your style.
- **Unique Page Identifiers**: Use different `page_id` values for different pages, repositories, or even individual issues and pull requests.

## Project Homepage

> [http://badge.neburalis.ru](http://badge.neburalis.ru)

## Usage

- **Standard Style**

  ```markdown
  ![Visitor Badge](http://badge.neburalis.ru/visitors/{your_page_id})
  ```

  Replace `{your_page_id}` with a unique identifier for your page or repository.

  **Recommendations for using `page_id`:**

  - For repositories and README.md:
    `{your_username}.{your_repository}`

    ```markdown
    ![Visitor Badge](http://badge.neburalis.ru/visitors/neburalis.visitor-badge)
    ```

    ![Visitor Badge](http://badge.neburalis.ru/visitors/neburalis.visitor-badge)

  - For issues:
    `{your_username}.{your_repository}.issue.{issue_number}`

    ```markdown
    ![Visitor Badge](http://badge.neburalis.ru/visitors/neburalis.visitor-badge.issue.1)
    ```

    ![Visitor Badge](http://badge.neburalis.ru/visitors/neburalis.visitor-badge.issue.1)

- **Custom Badge Label** (default is `visitors`)

  ```markdown
  ![Visitor Badge](http://badge.neburalis.ru/visitors/neburalis.visitor-badge?label=MyVisitors)
  ```

  ![Visitor Badge](http://badge.neburalis.ru/visitors/neburalis.visitor-badge?label=MyVisitors)

- **Custom Color**

  ```markdown
  ![Visitor Badge](http://badge.neburalis.ru/visitors/{your_page_id}?color=blue)
  ```
  ![Visitor Badge](http://badge.neburalis.ru/visitors/neburalis.visitor-badge?color=blue)

  Or use a HEX color code (don't forget to encode the `#` symbol as `%23`):

  ```markdown
  ![Visitor Badge](http://badge.neburalis.ru/visitors/{your_page_id}?color=%23ff69b4)
  ```
  ![Visitor Badge](http://badge.neburalis.ru/visitors/neburalis.visitor-badge?color=%23ff69b4)

<details>
<summary>Available Colors</summary>

You can use the following colors to customize your badge. The color can be specified by name or in HEX format (e.g., `#FF0000` for red).

- **Primary Colors:**
  - BLACK: `#000000`
  - WHITE: `#FFFFFF`
  - RED: `#FF0000`
  - GREEN: `#00FF00`
  - BLUE: `#0000FF`
  - YELLOW: `#FFFF00`
  - CYAN: `#00FFFF`
  - MAGENTA: `#FF00FF`

- **Additional Colors:**
  - NAVY: `#000080`
  - DARKBLUE: `#00008B`
  - MEDIUMBLUE: `#0000CD`
  - DARKGREEN: `#006400`
  - TEAL: `#008080`
  - DARKCYAN: `#008B8B`
  - DEEPSKYBLUE: `#00BFFF`
  - DARKTURQUOISE: `#00CED1`
  - MIDNIGHTBLUE: `#191970`
  - DODGERBLUE: `#1E90FF`
  - FORESTGREEN: `#228B22`
  - SEAGREEN: `#2E8B57`
  - ROYALBLUE: `#4169E1`
  - STEELBLUE: `#4682B4`
  - INDIGO: `#4B0082`
  - DARKOLIVEGREEN: `#556B2F`
  - CADETBLUE: `#5F9EA0`
  - CORNFLOWERBLUE: `#6495ED`
  - REBECCAPURPLE: `#663399`
  - SLATEBLUE: `#6A5ACD`
  - OLIVEDRAB: `#6B8E23`
  - LIGHTSLATEGRAY: `#778899`
  - MEDIUMSLATEBLUE: `#7B68EE`
  - LAWNGREEN: `#7CFC00`
  - CHARTREUSE: `#7FFF00`
  - AQUAMARINE: `#7FFFD4`
  - MAROON: `#800000`
  - PURPLE: `#800080`
  - OLIVE: `#808000`
  - GRAY: `#808080`
  - SKYBLUE: `#87CEEB`
  - LIGHTSKYBLUE: `#87CEFA`
  - BLUEVIOLET: `#8A2BE2`
  - DARKRED: `#8B0000`
  - DARKMAGENTA: `#8B008B`
  - SADDLEBROWN: `#8B4513`
  - DARKSEAGREEN: `#8FBC8F`
  - LIGHTGREEN: `#90EE90`
  - MEDIUMPURPLE: `#9370DB`
  - DARKVIOLET: `#9400D3`
  - PALEGREEN: `#98FB98`
  - DARKORCHID: `#9932CC`
  - YELLOWGREEN: `#9ACD32`
  - SIENNA: `#A0522D`
  - BROWN: `#A52A2A`
  - DARKGRAY: `#A9A9A9`
  - LIGHTBLUE: `#ADD8E6`
  - GREENYELLOW: `#ADFF2F`
  - PALETURQUOISE: `#AFEEEE`
  - LIGHTSTEELBLUE: `#B0C4DE`
  - POWDERBLUE: `#B0E0E6`
  - FIREBRICK: `#B22222`
  - DARKGOLDENROD: `#B8860B`
  - MEDIUMORCHID: `#BA55D3`
  - ROSYBROWN: `#BC8F8F`
  - DARKKHAKI: `#BDB76B`
  - SILVER: `#C0C0C0`
  - MEDIUMVIOLETRED: `#C71585`
  - INDIANRED: `#CD5C5C`
  - PERU: `#CD853F`
  - CHOCOLATE: `#D2691E`
  - TAN: `#D2B48C`
  - LIGHTGRAY: `#D3D3D3`
  - THISTLE: `#D8BFD8`
  - ORCHID: `#DA70D6`
  - GOLDENROD: `#DAA520`
  - PALEVIOLETRED: `#DB7093`
  - CRIMSON: `#DC143C`
  - GAINSBORO: `#DCDCDC`
  - PLUM: `#DDA0DD`
  - BURLYWOOD: `#DEB887`
  - LIGHTCYAN: `#E0FFFF`
  - LAVENDER: `#E6E6FA`
  - DARKSALMON: `#E9967A`
  - VIOLET: `#EE82EE`
  - PALEGOLDENROD: `#EEE8AA`
  - LIGHTCORAL: `#F08080`
  - KHAKI: `#F0E68C`
  - ALICEBLUE: `#F0F8FF`
  - HONEYDEW: `#F0FFF0`
  - AZURE: `#F0FFFF`
  - SANDYBROWN: `#F4A460`
  - WHEAT: `#F5DEB3`
  - BEIGE: `#F5F5DC`
  - WHITESMOKE: `#F5F5F5`
  - MINTCREAM: `#F5FFFA`
  - GHOSTWHITE: `#F8F8FF`
  - SALMON: `#FA8072`
  - ANTIQUEWHITE: `#FAEBD7`
  - LINEN: `#FAF0E6`
  - LIGHTGOLDENRODYELLOW: `#FAFAD2`
  - OLDLACE: `#FDF5E6`
  - ORANGE: `#FE7D37`
  - FUCHSIA: `#FF00FF`
  - DEEPPINK: `#FF1493`
  - ORANGERED: `#FF4500`
  - TOMATO: `#FF6347`
  - HOTPINK: `#FF69B4`
  - CORAL: `#FF7F50`
  - DARKORANGE: `#FF8C00`
  - LIGHTSALMON: `#FFA07A`
  - ORANGE_2: `#FFA500`
  - LIGHTPINK: `#FFB6C1`
  - PINK: `#FFC0CB`
  - GOLD: `#FFD700`
  - PEACHPUFF: `#FFDAB9`
  - NAVAJOWHITE: `#FFDEAD`
  - MOCCASIN: `#FFE4B5`
  - BISQUE: `#FFE4C4`
  - MISTYROSE: `#FFE4E1`
  - BLANCHEDALMOND: `#FFEBCD`
  - PAPAYAWHIP: `#FFEFD5`
  - LAVENDERBLUSH: `#FFF0F5`
  - SEASHELL: `#FFF5EE`
  - CORNSILK: `#FFF8DC`
  - LEMONCHIFFON: `#FFFACD`
  - FLORALWHITE: `#FFFAF0`
  - SNOW: `#FFFAFA`
  - LIGHTYELLOW: `#FFFFE0`
  - IVORY: `#FFFFF0`

To use the color in the URL, you can specify its name (e.g., `red`) or HEX code (e.g., `%23FF0000` for red).

</details>

- **Combining Custom Label and Color**

  ```markdown
  ![Visitor Badge](http://badge.neburalis.ru/visitors/neburalis.visitor-badge?label=Visitors&color=red)
  ```

  ![Visitor Badge](http://badge.neburalis.ru/visitors/neburalis.visitor-badge?label=Visitors&color=red)

- **Using Spaces in the Label**

  Replace spaces with `%20` or URL-encode your label.

  ```markdown
  ![Visitor Badge](http://badge.neburalis.ru/visitors/neburalis.visitor-badge?label=My%20Visitors)
  ```

  ![Visitor Badge](http://badge.neburalis.ru/visitors/neburalis.visitor-badge?label=My%20Visitors)

## Deployment

The project is implemented using Docker, Docker Compose, FastAPI, and PostgreSQL.

### Prerequisites

- Docker
- Docker Compose

### Installation and Startup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/neburalis/visitor-badge.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd visitor-badge
   ```

3. **Build and run the containers:**

   ```bash
   docker-compose up -d
   ```

4. **Verify the service is running:**

   Open [http://localhost:8000/visitors/test](http://localhost:8000/visitors/test) in your browser.

To deploy the service with URL access, you also need to set up Nginx as a reverse proxy server.

### Configuration

By default, the project uses a local PostgreSQL database configured in `docker-compose.yml`.

**If you want to use an external database:**

1. **Uncomment** the line with `DATABASE_URL: "${DATABASE_URL}"` in the `environment` section for the `app` service in `docker-compose.yml`.
2. **Comment out** or remove the `db` service in `docker-compose.yml` as well as the dependency on it from the `app` service.
3. When starting the container, pass the `DATABASE_URL` environment variable with the URL of your external database.

**Start with an external database:**

```bash
DATABASE_URL="postgresql://user:password@host:port/database" docker-compose up -d
```

## Project Structure

```
visitor-badge/
├── .dockerignore
├── .gitignore
├── Dockerfile
├── Makefile
├── bin/
│   └── sync_ignore.py
├── app/
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   └── models.py
├── docker-compose.yml
├── favicon.ico
└── pyproject.toml
```

## FAQ

**Q: Is this free?**

**A:** Yes, using this service is completely free. If you liked the project, please give it a star on GitHub and share it with others! However, keep in mind that this is a public service, and there is no guarantee that the visitor counter will always be accurate or available. Use it at your own discretion.

**Q: Does this service support HTTPS?**

**A:** Currently, the service does not support HTTPS. Since this is a fully public service, this does not affect security, but please consider this when using it.

## What's Next

- ~~**HTML version of readme**: I will convert this readme into a nice html file and it will be available on the main badge.neburalis.ru page.~~
- **New parameters**: do not increment the counter, format the digit
- **Basic Anti-Abuse Protection**: I'll add restrictions to prevent increasing the counter using curl and wget. I'll try using IP address limitations, but this might block GitHub, so this will be tested carefully.
- **Statistics**: Ability to view statistics for 7 days, a month, and more (like the repository stars graph but with views).
- **More Badges**: I don't have ideas for other badges yet, but if they come up, I'll definitely implement them.
- **Feedback**: We're always open to your suggestions and comments!

## Acknowledgments

This project was inspired by the following repositories:

- [jwenjian/visitor-badge](https://github.com/jwenjian/visitor-badge)
- [hehuapei/visitor-badge](https://github.com/hehuapei/visitor-badge)

## Motivation

This project was created primarily as a way to practice additional skills. Although the code in the project is very simple, it helped me improve my knowledge in using Make, Docker, and Docker Compose, as well as in proxying and redirecting traffic using Nginx. It's a full-fledged, albeit small, project that I'm proud of and not ashamed to show as an example of my work.

## License

This project is distributed under the AGPL license. See the [LICENSE](LICENSE) file for details.
