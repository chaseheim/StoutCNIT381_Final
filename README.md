## Project Overview

This bot is designed interact and monitor the network on the following topology.
The requirements for this project were to have several different methods of interacting with the network. This includes one Netmiko skill, one RESTCONF skill, one Ansible skill, one Genie skill, and a disaster recovery skill.

With ansible, the bot enables and captures debuging logs. With netmiko, it captures the running configurations. With restconf, it obtain detailed information for the network interface GigabitEthernet2 port.

![Network Design](/topology.jpg?)

## Getting Started

The `WebexBot.py` file is the main file for this project. It contains the code that creates and adds skills to the Webex Teams bot. The skills are called from their own fils that all end in ...Test.py 

### Dependencies

There are several python modules that are required to replicate this project. Additionally, the bot uses ngrok to forward its requests from the Webex API to the python terminal.

* This was created on an Ubuntu Linux VM running these aformentioned modules. 
* Need the pip3 modules: Paramiko/Netmiko, RESTCONF/NETCONF, Ansible, and Python 
* The bot was created on developers.webex.com and can be used on teams.webex.com

### Setting up a Webex App (Bot)

1. Navigate to developers.webex.com and create an account
2. Sign into developers and navigate to [your webex apps](https://developer.webex.com/my-apps)
3. Create a new app
4. Select type Bot
5. Name your bot, give it an email and fill in other required fields
6. Save your bot's access token. It will be used when setting up the python files

### Installing

1. Download or pull the repo and unpack all contents in the same directory in your development environment
2. Open the `WebexBot.py` file in your IDE of choice
3. Replace the bot information on lines `36` through `39`
```
### Configure the Webex Teams Bot ###
# Bot Details
bot_email = '' #Fill in your Teams Bot email#
teams_token = '' #Fill in your Teams Bot Token#
bot_url = '' #Fill in the ngrok forwarding address#
bot_app_name = '' #Give your bot a name#
```
![Directory Layout](directory.png)

### Executing program

* Start a new terminal (cmd line) and run the code 'ngrok http 5000'
* This will host the bot on your computer, temporarly 
* Copy the url from the ngrok to the 381bot.py file and save
* Run the 381bot.py file using the command 'python3 381bot.py' within Visual Studio
* You may need to change which directory is active within the Visual Studio terminal to run properly
* Proceed to teams.webex.com and begin messaging the bot. Saying 'Hello' will prompt the bot with available commands.

![Talking Bot](https://github.com/chaseheim/StoutCNIT381_Final/blob/botresponse.jpeg?raw=true)

## Common Help

If the running config becomes too large, it gets saved to runningConfigs/running_config_<ip>_<timecode>.txt



## Authors

Contributors names and contact info

Chase Heim
Chue Andy Yang
Cody Droes


## Version History


* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE file for details
