# NetPlanGen
## Generate Netplan Template Based On User Input
Requirements: 
- python 3+ 
- pip
```
#install required packages
pip install pyyaml ipaddress
```
1. run script
```
python generate_netplan.py
```
2. follow prompts
3. copy paste output into /etc/netplan/00-installer-config.yaml
```
sudo netplan apply
```