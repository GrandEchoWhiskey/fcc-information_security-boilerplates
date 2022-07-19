# Editet one unittest due of unreachable address, see test_module.py for more info.

import socket
from common_ports import ports_and_services

TIMEOUT = 1

def get_IP_of_Name(name: str):
  try:
    return socket.gethostbyname(name)
  except:
    raise exception()

    
def get_Name_of_IP(ip: str):
  try:
    return repr(socket.gethostbyaddr(ip)[0])
  except:
    raise exception()


def open_Port(host, port):
  
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.settimeout(TIMEOUT)
    
    if sock.connect_ex((host, port)) == 0:
      res = True
    else:
      res = False
      
  return res


def is_IPv4(addr: str, valid=True):
  sec = addr.split('.')
  if len(sec) != 4:
    return False
    
  for s in sec:
    try:
      if (int(s) > 255 or int(s) < 0) and valid:
        return False
    except:
      return False
  return True
          

def get_open_ports(target, port_range, verbose=False):
  open_ports = []
  host_name = None
  host_ip = None

  try:
    host_ip = get_IP_of_Name(target)
  except:
    if is_IPv4(target, False):
      return "Error: Invalid IP address"
    return "Error: Invalid hostname"

  try:
    host_name = get_Name_of_IP(host_ip)
  except:
    host_name = None
  
  for port in range(port_range[0], port_range[1]+1):

    if open_Port(host_ip, port):
      open_ports.append(port)

  if not verbose:
    return open_ports

  res_str = str()
  if host_name:
    host_name = host_name[1:-1]
  res_str += f"Open ports for {host_ip}\n" if not host_name else f"Open ports for {host_name} ({host_ip})\n"
  res_str += "PORT     SERVICE\n"
  for port in open_ports:
    res_str += str(port).ljust(9, ' ')[:9]
    res_str += ports_and_services[port]
    res_str += '\n'
  return res_str[:-1]
    