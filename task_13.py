# Сеть задана IP-адресом 172.16.168.0 и маской сети 255.255.248.0. Сколько в этой сети IP-адресов, для которых количество единиц в двоичной записи IP-адреса не кратно 5?
# from ipaddress import *

# net = ip_network('172.16.168.0/255.255.248.0', 0)
# result = 0

# for ip in net:
#     ip_bin = f'{ip:b}'
#     if ip_bin.count('1') % 5 != 0:
#         result += 1

# print(result)



# 220)	(ЕГЭ-2024) Сеть задана IP-адресом 106.184.0.0 и маской сети 255.248.0.0. Сколько в этой сети IP-адресов, для которых сумма единиц в двоичной записи IP-адреса не кратна 2?
# from ipaddress import *
# net = ip_network('106.184.0.0/255.248.0.0', 0)
# res = 0
# for ip in net:
#     ip_bin = f'{ip:b}'
#     if ip_bin.count('1') % 2 !=0:
#         res += 1
# print(res)



# 222)	(ЕГЭ-2024) Сеть задана IP-адресом 112.160.0.0 и сетевой маской 255.240.0.0. Сколько в этой сети IP-адресов, для которых количество единиц в двоичной записи IP-адреса не кратно 3?
# from ipaddress import *
# net = ip_network('112.160.0.0/255.240.0.0', 0)
# res = 0
# for ip in net:
#     ip_bin = f'{ip:b}'
#     if ip_bin.count('1') % 3 != 0:
#         res += 1
# print(res)



# 223)	(ЕГЭ-2024) Сеть задана IP-адресом 112.160.0.0 и сетевой маской 255.240.0.0. Сколько в этой сети IP-адресов, для которых количество единиц в двоичной записи IP-адреса кратно 5? 
# from ipaddress import *
# net = ip_network('112.160.0.0/255.240.0.0', 0)
# res = 0
# for ip in net:
#     ip_bin = f'{ip:b}'
#     if ip_bin.count('1') % 5 == 0:
#         res += 1
# print(res)



# 224)	(ЕГЭ-2024) Сеть задана IP-адресом 115.198.0.0 и маской сети 255.254.0.0. Сколько в этой сети IP-адресов, для которых количество единиц в двоичной записи IP-адреса кратно 5?
# from ipaddress import *
# net = ip_network('115.198.0.0/255.254.0.0', 0)
# res = 0
# for ip in net:
#     ip_bin = f'{ip:b}'
#     if ip_bin.count('1') % 5 == 0:
#         res += 1
# print(res)



# 229)	(Демо-2025)  Сеть задана IP-адресом 172.16.168.0 и маской сети 255.255.248.0. Сколько в этой сети IP-адресов, для которых количество единиц в двоичной записи IP-адреса не кратно 5? 
# from ipaddress import *
# net = ip_network('172.16.168.0/255.255.248.0', 0)
# res = 0
# for ip in net:
#     ip_bin = f'{ip:b}'
#     if ip_bin.count('1') % 5 != 0:
#         res += 1
# print(res)



# from ipaddress import *
# net = ip_network('122.159.136.144/255.255.255.248', 0)
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:]
#     if ip_bin.count('1') % 4 != 0:
#         count += 1
# print(count)



# наибольший ip
# from ipaddress import *
# net = ip_network('218.194.82.148/255.255.255.192', 0)
# print(net[-2]) всегда предпоследний, т.к. последний служебный



# наименьший ip
from ipaddress import *
net = ip_network('158.214.121.40/255.255.255.224', 0)
for ip in net.hosts():
    print(ip) # можно сделать так, тут сразу пропускаются служебные