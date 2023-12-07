from getpass import getpass
from netmiko import ConnectHandler

username = 'prne'
password = getpass('Enter your password:')

with open('commands_file.txt') as f:
    commands_list = f.read().splitlines()

with open('devices_file.txt') as f:
    devices_list = f.read().splitlines()

for ip_address_of_device in devices_list:
    print('Connecting to the device: ' + ip_address_of_device)
    
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': username,
        'password': password,
        'secret': password,  # Assuming the enable password is the same as the login password
        'fast_cli': True,   # Enables fast_cli mode for quicker execution
    }
    
    try:
        net_connect = ConnectHandler(**ios_device)
        net_connect.enable()  # Enter enable mode
        output = net_connect.send_config_set(commands_list)
        print(output)
    except Exception as e:
        print(f"Failed to connect to {ip_address_of_device}: {str(e)}")
    
    #finally:
      # net_connect.disconnect()