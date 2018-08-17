# XKCD
xkcd, sometimes styled _XKCD_ is a [webcomic](https://en.wikipedia.org/wiki/Webcomic) created by American author [Randall Munroe](https://en.wikipedia.org/wiki/Randall_Munroe). It is a comic of Romance, Sarcasm, Math and Language.
<br>
<p align="center">
  <img src="assets/xkcd.png" width="350"/>
</p>


 ## About
 **xkcd** is a command line tool written in Python which will fetch you the comics right in the terminal. This tool uses the [xkcd API](https://xkcd.com/json.html) to get the image and the [Click](http://click.pocoo.org/) python package to wrap the script into a beautiful command line interface tool. 
 <p></p>
 
 **Supports only Python 3.x and Unix Based OS only for now. Windows update coming later :)**

## Installation

* Clone the repository (Fork it as well if you'd like to update it or modify it)

  ```
  $ git clone https://github.com/itsron717/XKCD.git
  ```

* Move inside the repository

  ```
  $ cd XKCD
  ```

* Install the necessary dependencies
  
  ```
  $ pip install -r requirements.txt
  ```
 
* Install the package locally

  ```
  $ pip install --editable .
  ```
* Now the package is successfully installed. Run it using the command

  ```
  $ xkcd
  ```
* Instruction on how to use the package and it's arguments can be found using ` --help ` 

  ```
  $ xkcd --help
  ```
 Feel free to contribute! Let me know if there are any issues with the installation or running of the package using the GitHub issues. All suggestion are welcome.

## License
 
The MIT License (MIT)

Copyright (c) 2018 [Rounak Vyas](https://www.linkedin.com/in/itsron143/)
