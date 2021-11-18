import yaml
import ipaddress

config = {
    'network': {
        'version': 2,
        'ethernets': {
            'eno1': {
                'addresses': [],
                'mtu': 1500,
                'gateway4': '',
                'nameservers': {
                    'addresses': [
                        '8.8.8.8',
                        '1.1.1.1',
                        '8.8.4.4',
                    ],
                    'search': []
                },
                'routes': [
                    {
                        'to': '0.0.0.0/0',
                        'via': '',
                        'table': 200,
                    }
                ],
            }
        }
    }
}
interface_name = ''
print('Please enter interface name (e.x. eno1): ')

interface_name = input()
config['network']['ethernets'][interface_name] = config['network']['ethernets'].pop('eno1')


#get ips
while True:
    print('Please enter each of the ip blocks (type \'done\' when complete):')
    x = input()
    try:
        block = ipaddress.ip_network(x)
        hosts = block.hosts()
        next(hosts, None)
        for ip in hosts:
            config['network']['ethernets'][interface_name]['addresses'].append(str(ip)+'/'+str(block.prefixlen))
    except ValueError:
        if x == 'done':
            break
        else:
            print('Not an ip block.')

while True:
    print('Please enter the main gateway: ')
    x = input()
    try:
        ip = ipaddress.ip_address(x)
        config['network']['ethernets'][interface_name]['routes'][0]['via'] = x
        config['network']['ethernets'][interface_name]['gateway4'] = x
        break
    except ValueError:
        print('Not an ip address.')


print(yaml.dump(config))