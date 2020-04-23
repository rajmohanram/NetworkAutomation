import yaml
from pprint import pprint

with open("inventory.yml", 'r') as f:
    hosts = yaml.load(f, Loader=yaml.FullLoader)
pprint(hosts)

for key, value in hosts.items():
    print("Hostname:", key)
    print("IP Address:", value['ipaddress'])
