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
# from ipaddress import *
# net = ip_network('158.214.121.40/255.255.255.224', 0)
# # for ip in net.hosts():
# #     print(ip) # можно сделать так, тут сразу пропускаются служебные
# print(str(net[1]))



# из пробника
# from ipaddress import *
# net = ip_network('35.131.56.108/255.192.0.0', 0)
# print(str(net[-2]))



# 14648 составляем все возможные маски
# from ipaddress import ip_network
#
# for m in range(0, 33): # количество единиц в маске
#     net = ip_network(f'218.48.192.56/{m}', 0)
#     if str(net.network_address) == '218.48.192.0': # сверяю с адресом сети из условия
#         if len(list(net.hosts())) >= 500: # сверяю количество узлов
#             print(net.netmask) # вывожу все маски и смотрю все возможные третьи слева байты



# 14359
# from ipaddress import ip_network
#
# for m in range(0, 33):
#     net1 = ip_network(f'157.127.172.56/{m}', 0)
#     net2 = ip_network(f'157.127.191.78/{m}', 0)
#     if str(net1.network_address) != str(net2.network_address):
#         print(m)
#         break



# 14649
# from ipaddress import ip_network
#
# for A in range(1, 256):
#     net = ip_network(f'116.242.{A}.26/255.255.255.224', 0)
#     usl = [bin(int(ip))[2:].zfill(32)[:16].count('1') >= bin(int(ip))[2:].zfill(32)[16:].count('1') for ip in net]
#     if all(usl):
#         print(A)



# 14650
# from ipaddress import ip_network
#
# for m in range(0, 33):
#     net1 = ip_network(f'216.54.187.235/{m}', 0)
#     net2 = ip_network(f'216.54.174.128/{m}', 0)
#     if str(net1.network_address) != str(net2.network_address):
#         if '216.54.187.235' != str(net1.network_address) and '216.54.187.235' != str(net1.broadcast_address):
#             if '216.54.174.128' != str(net2.network_address) and '216.54.174.128' != str(net2.broadcast_address):
#                 print(m)



# 21412
# from ipaddress import *
# net = ip_network('143.168.72.213/255.255.255.240', 0)
# print(net[-2])



# 21899
# from ipaddress import *
# net = ip_network('98.81.154.195/255.252.0.0', 0)
# print(net[-2]) # 9883255254



# 21708
# from ipaddress import *
# net = ip_network('11.92.135.56/255.224.0.0', 0)
# print(net[-2]) # 1195255254



# 20902
# from ipaddress import *
# net = ip_network('172.16.80.0/255.255.248.0', 0)
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:]
#     if ip_bin.count('0') % 2 != 0:
#         count += 1
# print(count)



# 20807
# from ipaddress import *
# net = ip_network('172.16.192.0/255.255.192.0', 0)
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:]
#     if ip_bin.count('1') % 5 != 0:
#         count += 1
# print(count)



# 19245
from ipaddress import *
net = ip_network('218.194.82.148/255.255.255.192', 0)
print(net[-2]) # 21819482190



























