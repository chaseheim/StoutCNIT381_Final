### General Imports ###
import requests
from requests.api import head
import datetime, time

### Webex Teams Bot ###
from webexteamsbot import TeamsBot
from webexteamsbot.models import Response

### Utilities Libraries ###
import routers

### Import tasks ###
import restconfTask
import ansibleTask
import netmikoTask

# Define router info 
device_address = routers.router['host']
device_username = routers.router['username']
device_password = routers.router['password']

### RESTCONF Setup ###
#Disable SSL certificate warnings
requests.packages.urllib3.disable_warnings()
port = '443'
url_base = ("https://%s/restconf" % device_address)
#Dictionary for custom header keys - Accept and send json yang data (contrary to xml)
headers = {
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json"
}

### Configure the Webex Teams Bot ###
# Bot Details
bot_email = 'benjamin_flinkerton@webex.bot' #Fill in your Teams Bot email#
teams_token = 'NGEzMTQxNTAtMjMzOC00OWMzLTgyMDUtNTU5MTRhY2U0OTA0NWZjNzAzMjctYTI1_P0A1_d6bae168-94e6-4bfa-95a0-88365138f260' #Fill in your Teams Bot Token#
bot_url = "https://0739-97-90-226-103.ngrok.io" #Fill in the ngrok forwarding address#
bot_app_name = 'Benjamin Flinkerton'

# Create a Bot Object
# Note: debug mode prints out more details about processing to terminal
bot = TeamsBot(
    bot_app_name,
    teams_bot_token=teams_token,
    teams_bot_url=bot_url,
    teams_bot_email=bot_email,
    debug=True,
    webhook_resource_event=[
        {"resource": "messages", "event": "created"},
        {"resource": "attachmentActions", "event": "created"},],
)

### RESTCONF Skill ###
def restconf_skill(incoming_msg):
    #Set up response to send data back to webex bot
    response = Response()
    #Call our restconf skill and save returned tuple
    resultTuple = restconfTask.get_int_state(url_base, headers, device_username, device_password)
    #get data out of tuple that is returned from get_int_state
    mac_addr, speed, discontinuity_time, in_octets, in_uni_pkts, in_broad_pkts, in_multi_pkts, out_octets, out_uni_pkts = resultTuple
    #Add data to the response
    response.markdown = "Here is the information I found about GigabitEthernet2:\n=\n"
    response.markdown += mac_addr + '\n'
    response.markdown += speed + '\n'
    response.markdown += discontinuity_time + '\n'
    response.markdown += in_octets + '\n'
    response.markdown += in_uni_pkts + '\n'
    response.markdown += in_broad_pkts + '\n'
    response.markdown += in_multi_pkts + '\n'
    response.markdown += out_octets + '\n'
    response.markdown += out_uni_pkts + '\n'
    return response

### Ansible Skill ###
def ansible_skill(incoming_msg):
    #Set up response to send data back to webex bot
    response = Response()
    #Call the skill, the debug data is stored in ./debug-logs
    ansibleTask.ansible_skill()
    response.markdown = "I have finished the execution of debug! The files are stored in my /debug-logs folder!"
    return response

### Netmiko Skill ###
def netmiko_skill(incoming_msg):
    #Set up response to send data back to webex bot
    response = Response()
    #Returned data is the running config
    runningConfig = netmikoTask.showRun(device_address, device_username, device_password)
    #Check the length, must be under 7439 bytes for markdown
    if len(runningConfig.encode('utf-8')) < 7434: #-6 becuase of ```config```
        response.markdown = "```" + runningConfig + "```" #format as code block
    else:
        #Respond to the user that we cant send over the chat and save file to running_config_<ip addr>_<timecode>.txt
        sender = bot.teams.people.get(incoming_msg.personId)
        response.markdown = "The running configuration is too big to send!\n"
        response.markdown += "Don't worry, I'll save the file for you, {}".format(sender.firstName)
        #Get epoch time
        dts = datetime.datetime.utcnow()
        epochtime = round(time.mktime(dts.timetuple()) + dts.microsecond/1e6)
        #Make and write file
        f = open("./runningConfigs/running_config_" + device_address + "_" + str(epochtime) + ".txt", "w")
        f.write(runningConfig)
    return response

### Genie Skill ###
def genie_skill(incoming_msg):
    response = Response()
    return response

# Create a function to respond to messages that lack any specific command
# The greeting will be friendly and suggest how folks can get started.
def greeting(incoming_msg):
    # Loopkup details about sender
    sender = bot.teams.people.get(incoming_msg.personId)
    # Create a Response object and craft a reply in Markdown.
    response = Response()
    response.markdown = "Hello {}, I am ready to slave away, how are you?".format(sender.firstName)
    response.markdown += "\n\nSee what I can do by asking for **/help**."
    return response

### Configure the Webex Teams Bot ###
# Set the bot greeting.
bot.set_greeting(greeting)
# Add Bot's Commmands
bot.add_command("interface state", "RESTCONF SKill: Get interface state infromation about Gig2.", restconf_skill)
bot.add_command("capture debug", "Ansible Skill: Save the debug information to a file on host.", ansible_skill)
bot.add_command("show run","Netmiko Skill: Return running configuration on the router", netmiko_skill)
# Every bot includes a default "/echo" command.  You can remove it, or any
bot.remove_command("/echo")

if __name__ == "__main__":
    # Run bot through ngrok on port 5000 (the ngrok server)
    bot.run(host="0.0.0.0", port=5000)