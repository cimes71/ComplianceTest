This program uses the Selenium Webdriver to create a BOT.

The util package contains a configs.py that declares some constants used to pull from the OS environment.  

It also reads in a .ini file to pull xpath information used in the BOT navigation, and used to define where to enter data, and what data to get from the responses.

Currently, BotProc creates the driver, peforms a login function, and processes a list provided to the the process search list method, and gets data from the response page for each search element in the list.

config file (not included in the repo) defines these sections

[Login]

[Navigation]

[Search]

[Data]

While this code is public, it will need to be customized.  I chose to add the ex paths to the configs because it makes the code a bit cleaner and you don't have to worry about adding escape characters.
