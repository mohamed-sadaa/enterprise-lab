# VyOS Router Configuration

## Network Layout
- WAN: eth0 (DHCP from NAT)
- VLAN 10: 192.168.10.0/24 — IT Department
- VLAN 20: 192.168.20.0/24 — HR Department
- VLAN 30: 192.168.30.0/24 — Finance Department

## Key Commands
# Enter config mode
configure

# Show interfaces
show interfaces

# Show firewall rules
show firewall

## Firewall Rules
- HR (VLAN 20) blocked from Finance (VLAN 30)
- All VLANs reach internet via NAT masquerade
