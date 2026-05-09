# ELK Stack — Centralized Logging (SIEM)

## Server Details
- OS: Ubuntu Server 22.04
- Hostname: elk.company.local
- IP: 192.168.10.30

## Components
| Service | Port | Purpose |
|---------|------|---------|
| Elasticsearch | 9200 | Log storage |
| Logstash | 5044 | Log processing |
| Kibana | 5601 | Dashboard |
| Filebeat | - | Log shipper |

## Log Sources
- Samba: /var/log/auth.log, /var/log/syslog
- FreeIPA: /var/log/krb5kdc.log

## Access
Kibana: http://192.168.10.30:5601

## Key Commands
sudo systemctl status elasticsearch kibana logstash
curl http://localhost:9200
