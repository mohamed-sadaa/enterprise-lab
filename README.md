# 🏢 Enterprise Network Infrastructure Lab

> A fully simulated enterprise network built from scratch on a single Ubuntu machine using VirtualBox. Demonstrates real-world IT infrastructure concepts used in production environments.

---

## 📸 What This Project Looks Like

| Flask Helpdesk Dashboard | Kibana Log Dashboard |
|--------------------------|----------------------|
| Server status, tickets, live logs | Centralized logs from all servers |

---

## 🏗️ Architecture

```
                    ┌─────────────────────┐
                    │    VyOS Router       │
                    │   192.168.10.1       │
                    │ VLAN 10 / 20 / 30    │
                    └──────┬──────┬───────┘
                           │      │
              ┌────────────┘      └────────────┐
              │                                │
    ┌─────────┴──────────┐        ┌────────────┴────────────┐
    │  VLAN 10 — IT       │        │  VLAN 20/30 — HR/Finance │
    │  192.168.10.0/24    │        │  192.168.20/30.0/24      │
    └─────────┬──────────┘        └─────────────────────────┘
              │
    ┌─────────┼──────────┬────────────────┐
    │         │          │                │
┌───┴────┐ ┌──┴────┐ ┌───┴────┐ ┌────────┴───┐
│FreeIPA │ │ Samba │ │  ELK   │ │ WireGuard  │
│.10.10  │ │.10.20 │ │.10.30  │ │  VPN       │
└────────┘ └───────┘ └────────┘ └────────────┘
```

---

## 🔧 Technologies Used

| Technology | Purpose | Version |
|-----------|---------|---------|
| VirtualBox | Virtualization platform | 6.x |
| VyOS | Enterprise router + firewall | Rolling |
| AlmaLinux 9 | RHEL-based OS for FreeIPA | 9.x |
| Ubuntu Server | OS for Samba + ELK | 22.04 LTS |
| FreeIPA | LDAP + Kerberos + DNS (like Active Directory) | 4.x |
| Samba | Windows-compatible file server | 4.x |
| Elasticsearch | Log storage and indexing | 8.x |
| Logstash | Log processing pipeline | 8.x |
| Kibana | Log visualization dashboard | 8.x |
| Filebeat | Log shipper | 8.x |
| WireGuard | Modern VPN gateway | 1.x |
| Flask | Python web framework for helpdesk | 3.x |
| SQLite | Lightweight ticket database | 3.x |

---

## 📋 Project Phases

### ✅ Phase 1 — Foundation
- Installed VirtualBox on Ubuntu host
- Set up Git and GitHub for version control
- Downloaded Ubuntu Server and AlmaLinux ISOs
- Created project structure

### ✅ Phase 2 — VyOS Router + VLAN Segmentation
- Deployed VyOS virtual router
- Created 3 VLANs (IT/HR/Finance departments)
- Configured NAT for internet access
- Added firewall rule blocking HR from Finance network

### ✅ Phase 3 — FreeIPA Authentication Server
- Deployed AlmaLinux 9 VM
- Installed and configured FreeIPA (LDAP + Kerberos + DNS)
- Created department users and groups:
  - `john.it` → IT team
  - `sara.hr` → HR team
  - `mike.finance` → Finance team
- Enabled web dashboard at `http://192.168.10.10/ipa/ui`

### ✅ Phase 4 — Samba File Server with Access Controls
- Deployed Ubuntu Server VM
- Installed and configured Samba
- Created department shares with group-based permissions:
  - `IT-Share` → it-team only
  - `HR-Share` → hr-team only
  - `Finance-Share` → finance-team only
- Verified access control (users denied access to other departments)

### ✅ Phase 5 — ELK Stack Centralized Logging (SIEM)
- Deployed Ubuntu Server VM with 3GB RAM
- Installed Elasticsearch, Logstash, Kibana (ELK Stack 8.x)
- Installed Filebeat on Samba and FreeIPA VMs
- Configured log shipping pipeline to central ELK server
- Kibana dashboard showing live logs from all servers

### ✅ Phase 6 — WireGuard VPN Gateway
- Installed WireGuard on Samba VM
- Generated server and client key pairs
- Configured encrypted VPN tunnel (10.0.0.0/24)
- Host machine connects to entire lab network through VPN

### ✅ Phase 7 — Flask Helpdesk Web Application
- Built Python/Flask web application
- Features:
  - Real-time server status dashboard (pings all VMs)
  - Ticket creation, assignment, and status tracking
  - Live log feed from ELK Elasticsearch API
  - Department user assignment
- Accessible at `http://192.168.10.20:5000`

---

## 🚀 How to Run This Lab

### Prerequisites
- Ubuntu Linux (host machine)
- VirtualBox 6.x+
- Minimum 16GB RAM
- 100GB free disk space

### Setup Order
```bash
# 1. Clone this repo
git clone https://github.com/YOUR_USERNAME/enterprise-lab.git
cd enterprise-lab

# 2. Follow phase guides in order
cat configs/vyos/setup.md
cat configs/freeipa/setup.md
cat configs/samba/setup.md
cat configs/elk/setup.md
cat configs/vpn/setup.md

# 3. Run the helpdesk app
cd helpdesk-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

---

## 🌐 Service Endpoints

| Service | URL | Description |
|---------|-----|-------------|
| Flask Helpdesk | `http://192.168.10.20:5000` | Main dashboard |
| Kibana | `http://192.168.10.30:5601` | Log analysis |
| FreeIPA | `http://192.168.10.10/ipa/ui` | User management |
| Elasticsearch | `http://192.168.10.30:9200` | Log API |

---

## 📁 Repository Structure

```
enterprise-lab/
├── README.md
├── configs/
│   ├── vyos/
│   │   └── setup.md          # VyOS router config guide
│   ├── freeipa/
│   │   └── setup.md          # FreeIPA installation guide
│   ├── samba/
│   │   └── setup.md          # Samba config guide
│   ├── elk/
│   │   └── setup.md          # ELK Stack setup guide
│   └── vpn/
│       └── setup.md          # WireGuard VPN guide
└── helpdesk-app/
    ├── app.py                 # Flask application
    ├── database.py            # SQLAlchemy models
    ├── templates/
    │   ├── base.html
    │   ├── dashboard.html
    │   ├── tickets.html
    │   └── new_ticket.html
    └── static/
```

---

## 💡 Key Concepts Demonstrated

- **Network segmentation** using VLANs and firewall rules
- **Centralized identity management** with LDAP and Kerberos (equivalent to Active Directory)
- **Role-based access control** on file shares
- **SIEM / centralized logging** with ELK Stack
- **VPN gateway** for encrypted remote access
- **Full-stack web development** with Python and Flask
- **Infrastructure as code** — all configs documented and version controlled

---

## 🏆 Skills Shown

`Linux` `Networking` `VLANs` `Firewall` `LDAP` `Kerberos` `Active Directory` `Samba` `File Permissions` `ELK Stack` `SIEM` `Log Management` `VPN` `WireGuard` `Python` `Flask` `SQLite` `Git` `VirtualBox` `AlmaLinux` `Ubuntu Server`

---

## 👨‍💻 Author

**Yasser Mohamed**
Aspiring IT Support / System Administrator
- GitHub: [@mohamed-sadaa](https://github.com/mohamed-sadaa)
- Email: mohameasser@gmail.com

---

> Built entirely with free and open source tools. No licenses required.
