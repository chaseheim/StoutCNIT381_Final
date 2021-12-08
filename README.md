# Bank of America Network Bot

This bot is designed to monitor a bank's internet connection.

## Description

This bot is designed interact and monitor the network on the following topology.
The requirements for this project were to have several different methods of interacting with the network. This includes one Netmiko skill, one RESTCONF skill, one Ansible skill, one Genie skill, and a disaster recovery skill.

With ansible, the bot enables and captures debuging logs. With netmiko, it captures the running configurations. With restconf, it obtain detailed information for the network interface GigabitEthernet2 port.
![Network Design](https://github.com/chaseheim/StoutCNIT381_Final/blob/topology.jpg?)

## Getting Started

### Dependencies

* This was created on a Linux VM using Visual Studio Code. Paramiko/Netmiko, RESTCONF/NETCONF, Ansible, and Python 
* libraries will be needed.
* The bot was created on developers.webex.com and can be used on teams.webex.com


### Installing

* Download the entire zip file and unpack all contents in the same folder/directory
* within Visual Studio.
![Directory Layout](https://github.com/chaseheim/StoutCNIT381_Final/blob/directory.jpeg?raw=true)

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
