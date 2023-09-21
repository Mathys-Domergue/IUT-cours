import dns.resolver

mon_ipaddr='80.227.199.194.in-addr.arpa'

fqdn=dns.resolver.resolve(mon_ipaddr,'ptr')
for data in fqdn:
    print('Le nom du serveur est', data)