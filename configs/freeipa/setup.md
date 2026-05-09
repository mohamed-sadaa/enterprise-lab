# FreeIPA Authentication Server

## Server Details
- OS: AlmaLinux 9
- Hostname: freeipa.company.local
- IP: 192.168.10.10
- Realm: COMPANY.LOCAL

## Services
- LDAP (389-ds): central user directory
- Kerberos (KDC): authentication tickets
- DNS: internal hostname resolution
- Web UI: http://192.168.10.10/ipa/ui

## Users & Groups
| User | Group | Department |
|------|-------|-----------|
| john.it | it-team | IT |
| sara.hr | hr-team | HR |
| mike.finance | finance-team | Finance |

## Key Commands
kinit admin              # get Kerberos ticket
ipa user-find            # list all users
ipa group-find           # list all groups
ipa user-add username    # add new user
ipactl status            # check all services
