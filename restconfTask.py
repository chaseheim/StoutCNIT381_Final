from typing import OrderedDict
import requests

#RESTCONF skill function that gets called by the Webex bot's skill 'interface state'
def get_int_state(url_base, headers, dev_user, dev_pass):
    url = url_base + "/data/ietf-interfaces:interfaces-state/interface=GigabitEthernet2"
    requests.packages.urllib3.disable_warnings()

    #Perform get for the information we want
    response = requests.get(url, auth=(dev_user, dev_pass), headers=headers, verify=False)

    #format and omit
    data = response.json()["ietf-interfaces:interface"]
    mac_addr = str(data["phys-address"])
    speed = int(data["speed"])
    discontinuity_time = str(data["statistics"]["discontinuity-time"])
    in_octets = int(data["statistics"]["in-octets"])
    in_uni_pkts = int(data["statistics"]["in-unicast-pkts"])
    in_broad_pkts = int(data["statistics"]["in-broadcast-pkts"])
    in_multi_pkts = int(data["statistics"]["in-multicast-pkts"])
    out_octets = int(data["statistics"]["out-octets"])
    out_uni_pkts = int(data["statistics"]["out-unicast-pkts"])

    #Send the info back to the bot to send to webex, in the form of a tuple
    #We send as a tuple becuase we want to send a bunch of different variables back
    #Sadly, python doesnt have pointers. It's a sad day to be a C++ programmer.
    returnData = (("Physical Address: {}".format(mac_addr)),
    ("Interface Speed: {}".format(speed)),
    ("Discontinuity Time: {}".format(discontinuity_time)),
    ("In Octets: {}".format(in_octets)),
    ("In Unicast Packets: {}".format(in_uni_pkts)),
    ("In Broadcast Packets: {}".format(in_broad_pkts)),
    ("In Multicast Packets: {}".format(in_multi_pkts)),
    ("Out Octets: {}".format(out_octets)),
    ("Out Unicast Packets: {}".format(out_uni_pkts)))
    return returnData