# Samba File Server

## Server Details
- OS: Ubuntu Server 22.04
- Hostname: samba.company.local
- IP: 192.168.10.20
- Mode: Standalone (security = user)

## Department Shares
| Share | Path | Access |
|-------|------|--------|
| IT-Share | /srv/shares/it | it-team only |
| HR-Share | /srv/shares/hr | hr-team only |
| Finance-Share | /srv/shares/finance | finance-team only |

## Key Commands
sudo testparm                                    # test config
sudo systemctl restart smbd nmbd                 # restart samba
smbclient //localhost/IT-Share -U john.it        # test access
