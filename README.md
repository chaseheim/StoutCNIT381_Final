# Bank of America Network Bot

A bot designed to monitor a bank's internet connection.

## Description

This bot is designed to monitor for a change in IP addresses in the 172.16.0.0/24 network.
It then changes the second address to match the change in the first, accordingly.
The bot is also designed to enable and capture debuging logs with Ansible, capture running configurations
with Paramiko, and obtain detailed information for network ports with RESTCONF
![Network Design](https://github.com/chaseheim/StoutCNIT381_Final/blob/topology.jpeg?raw=true)

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
