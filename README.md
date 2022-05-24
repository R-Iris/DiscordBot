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
        <li><a href="#Compiling">Compiling</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
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

_If you wish to use this bot, please follow the guidelines here_

### Prerequisites

* Download Python 3.9.0 and above
* If you're on Windows, bind your PATH environment variable to Python
* Check that your installation was sucessful by running `python --version` in your terminal. The output should be `Python 3.x.x` with the version you installed
* Install pip package manager by running `py get-pip.py` in your terminal
* To check if the installation was successful, run `pip --version` in your terminal 




_________________________________________________________________________________________________________________________


* Download the source code and the `.env.example` in a folder
* Remove the suffix `.example`, so you should now have a file called `.env`
* Create a **bot** from the [Discord Developer Portal](https://discord.com/developers/docs/intro) and obtain its token
* Paste the token into the `.env` file. You now have something such as: `DISCORD_TOKEN = 'YOUR TOKEN'`
* Create an Excel file in the folder. You can name it whatever you wish, but in this example I will name mine `roles.xlsx`
* Copy the absolute path to the `.env` file. You now have something such as 

`READER_FILE_PATH = 'C:\Users\yourName\Desktop\DiscordBot\roles.xlsx'`



* Write down the name of your server in the `.env` file in the `SERVER_NAME` field




Your `.env` file should look something along these lines when done:

```
DISCORD_TOKEN = 'YOUR TOKEN'
READER_FILE_PATH = 'C:\Users\yourName\Desktop\DiscordBot\roles.xlsx
SERVER_NAME = 'BotTesting'
```

### Compiling

_Below are the instructions on how to make the Python code into an application_

1. Run `pip install pyinstaller` in your terminal
2. Reach the folder containing the code from your terminal by using `cd folder_location`
3. Run `pyinstaller --onefile botMain.py`


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Here are some screenshots of the different commands and ther outputs




**Command `$assignRoles`** :footprints:


Sample format of the `roles.xlsx` file:

| Username | Role |
| :---:   | :-: | 
| Heykan | BotCreater |
| Dummy  | BotCreater |
| Heykan | Dummy      |
| Pirate | BotTester  |





Sample output:


![image](https://user-images.githubusercontent.com/74076551/170108213-b59ebd68-9488-4d2b-8ebb-21244fd53acd.png)



_Note: The counting of rows start at index 0_




____________________




**Command `$exportRoles`** :speaking_head:


Sample output from the terminal:


![image](https://user-images.githubusercontent.com/74076551/170109707-30094450-36ea-416b-9a85-c2fb7819d59f.png)



Sample output from the Excel file:

![image](https://user-images.githubusercontent.com/74076551/170109849-b1ec9d34-c9cd-4677-b869-6f1acb030322.png)
![image](https://user-images.githubusercontent.com/74076551/170109962-0a0a90e7-3725-47c8-b0f9-430a7cd44ef9.png)





<p align="right">(<a href="#top">back to top</a>)</p>





<!-- CONTACT -->
## Contact

Feel free to contact me on Discord for any questions/issues!

Discord: **Heykan#9170**

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: [https://linkedin.com/in/othneildrew](https://www.linkedin.com/in/irismariaradu/)

