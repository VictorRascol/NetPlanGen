# NetPlanGen
Generate Netplan Template Based On User Input
requirements: python 3+ and pip
#install required packages
pip install pyyaml ipaddress 
#run script
python generate_netplan.py
follow prompts
copy past output into /etc/netplan/00-installer-config.yaml
sudo netplan apply