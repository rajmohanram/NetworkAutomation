# using netmiko
from netmiko import ConnectHandler


# return connection
def netConnect(deviceParams):
    device_params = {
        'device_type': deviceParams.nos,
        'host': deviceParams.ip,
        'username': deviceParams.username,
        'password': deviceParams.password,
        'timeout': 3
    }
    try:
        net_connect = ConnectHandler(**device_params)
        return net_connect
    except:
        print("Connection error:", deviceParams.host, "continuing with next device...")
        return -1