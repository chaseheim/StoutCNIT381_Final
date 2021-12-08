from netmiko import Netmiko

#Netmiko skill function that gets called by the Webex bot's skill 'show run'
def showRun(host, username, password):
    #Open a connection to the CSR that is passed into the function
    connection = Netmiko(host=host, port='22' ,username=username, password=password, device_type='cisco_ios')
    #Send the 'show run' command to the CSR and save in output, then return output
    output = connection.send_command('show run')
    connection.disconnect()
    return output