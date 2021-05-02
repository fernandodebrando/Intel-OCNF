from osmclient import client
from osmclient.common.exceptions import ClientException
from osmclient.common.exceptions import NotFound
import yaml
from prettytable import PrettyTable
from dotenv import dotenv_values

# hostname = "127.0.0.1"
# user = 'admin'
# password = 'admin'
# project = 'admin'
# kwargs = {}
# if user is not None:
#     kwargs['user'] = user
# if password is not None:
#     kwargs['password'] = password
# if project is not None:
#     kwargs['project'] = project
# myclient = client.Client(host=hostname, sol005=True, **kwargs)
# resp = myclient.vnfd.list()
# print(yaml.safe_dump(resp, indent=4, default_flow_style=False))

def auth():
    config = dotenv_values(".env")
    kwargs = {}
    if config["USER_OSM"] is not None:
        kwargs['user'] = config["USER_OSM"] 
    if config["PASSWORD_OSM"]  is not None:
        kwargs['password'] = config["PASSWORD_OSM"] 
    if config["PROJECT_OSM"]  is not None:
        kwargs['project'] = config["PROJECT_OSM"] 
    myclient = client.Client(host=config["HOSTNAME_OSM"], sol005=True, **kwargs)
    return myclient

def GetNSDescriptor(name):
    client_osm = auth()
    try:
        nsd = client_osm.nsd.get(name)
    except NotFound as ve:
        nsd = ve
    return nsd

def CreatesNSInstance(nsd_name, nsr_name, account, description):
    client_osm = auth()
    ns = ''
    try:
        client_osm.ns.create(nsd_name, nsr_name, account, description=description)
    except NotFound as e:
        ns = e
    except ClientException as e:
        ns = e
    return ns

def NSLCManagement():
    """ create(instantiate)(ns), scale(ns), delete(terminate)(ns), get_monitoring(
    """
    client_osm = auth()
    # client_osm.ns.s
    return ""
    



nsd = GetNSDescriptor('pingpong')
print(nsd)
# if nsd['name']:
#     ns = CreatesNSInstance(nsd['name'], nsd['name'], 'emu-vim', nsd['description'])
#     print(ns)


# client_osm = auth()
# print(client_osm.vim.list())

