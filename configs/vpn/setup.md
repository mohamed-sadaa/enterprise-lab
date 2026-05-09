# WireGuard VPN Gateway

## Deployed On: Samba VM (192.168.10.20)
## VPN Subnet: 10.0.0.0/24
## Server IP: 10.0.0.1
## Client IP: 10.0.0.2
## Port: 51820 UDP

## What it does
Creates an encrypted tunnel giving remote clients
full access to the internal 192.168.10.0/24 network.

## Commands
sudo wg show              # check VPN status
sudo wg-quick up wg0      # connect
sudo wg-quick down wg0    # disconnect
