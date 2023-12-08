from getpass import getpass
from netmiko import ConnectHandler

username = 'prne'
password = getpass('Enter your password:')
# Define the parameters for Router 1
router1_params = {
    'dvice_type': 'cisco_ios',
    'ip': 'Router1_ip_address',
    'username': 'prne',
    'password': 'cisco123!',

}

#Define the parameters for Router 2
router2_params = {
    'device_type': 'cisco_ios',
    'ip': 'Router2_ip_address',
    'usrname': 'prne',
    'password': 'cisco123!',

}

# Establish SSH connection to Router 1
#router1_connection = ConnectHandler(**router1_params)

# Establish SSH connection to Router 2
#router2_connection = ConnectHandler(**router2_params)

# Now, you can interact with Router 1 and Router 2 using these connections
# For example, you can send configuration commands

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
    
    # Close the connection when done
    #router1_connection.disconnect()
    #router2_connection.disconnect()
    #finally:
      # net_connect.disconnect()