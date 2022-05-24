<div id="top"></div>
<!--
*** This template is not my own.
*** Credits go to the original creators: https://github.com/othneildrew/Best-README-Template
-->

[![LinkedIn][linkedin-shield]][linkedin-url]



<br />
<div align="center">

  <h3 align="center">excelBot for Discord</h3>

  <p align="center">
    Small Discord bot that allows you to read and export data from and to Excel files. 
    When reading from the Excel file, the <b>excelBot is capable to mass-assign the roles written in the Excel file to the given people</b>.
    When exporting data, the excelBot <b>creates a new Excel file containing the names and roles</b> of the people present in the channel the command was ran in.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The bot requires some set-up in order to work. The details are described below.

What the bot does:
* When the bot is ready and connected, it'll write to the terminal.   *Example*: 
![image](https://user-images.githubusercontent.com/74076551/170096302-40ba4a1d-e187-4703-a159-a8f31ac9ad2b.png)


* When using the command `$assignRoles`, the bot will read the given file and mass-assign the roles to their respective users


* When using the command `$exportRoles`, the bot will export the roles of all the members in the channel to an Excel file


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

Main language used:

* [Python](https://python.org/)


Packages used:

* [Colr](https://pypi.org/project/Colr/)
* [Pandas](https://pandas.pydata.org/)
* [Dotenv](https://pypi.org/project/python-dotenv/)
* [Discord API](https://discord.com/developers/docs/intro)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Feel free to contact me on Discord for any questions/issues!

Discord: **Heykan#9170**

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: [https://linkedin.com/in/othneildrew](https://www.linkedin.com/in/irismariaradu/)

