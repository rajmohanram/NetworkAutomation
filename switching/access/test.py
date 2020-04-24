import yaml
from pprint import pprint
from utils.dictx import DictX
from utils.netmiko_utils import netConnect

argument_user = "ospf"

# load inventory yaml to python object
with open("inventory.yml", 'r') as f:
    hosts = yaml.load(f, Loader=yaml.FullLoader)

# load commands yaml to python object
with open("operational_commands.yml", 'r') as f:
    commands = yaml.load(f, Loader=yaml.FullLoader)
print(commands)

# Convert python dict to DictX objects - to access dict elements by dot
inv_obj_list = list()
for item in hosts:
    inv_object = DictX(item)
    inv_obj_list.append(inv_object)

# connect to devices and execute commands
for obj in inv_obj_list:
    command = commands[argument_user][obj.nos]
    print(command)
    conn = netConnect(obj)
    if conn != -1:
        output = conn.send_command(command)
    else:
        continue
