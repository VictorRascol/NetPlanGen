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
                'set-name': 'eno1',
                'routes': [
                    {
                        'to': 'default',
                        'via': '',
                        'table': 200,
                    }
                ],
            }
        }
    }
}


#get ips
while True:
    print('Please enter each of the ip blocks (type \'done\' when complete):')
    x = input()
    try:
        block = ipaddress.ip_network(x)
        hosts = block.hosts()
        next(hosts, None)
        for ip in hosts:
            config['network']['ethernets']['eno1']['addresses'].append(str(ip)+'/'+str(block.prefixlen))
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
        config['network']['ethernets']['eno1']['routes'][0]['via'] = x
        config['network']['ethernets']['eno1']['gateway4'] = x
        break
    except ValueError:
        print('Not an ip address.')


print(yaml.dump(config))