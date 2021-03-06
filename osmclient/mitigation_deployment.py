from osmclient import client
from osmclient.common.exceptions import ClientException
from osmclient.common.exceptions import NotFound
from dotenv import dotenv_values

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

def GetNSDescriptors():
    client_osm = auth()
    nsd = client_osm.nsd.list()
    return nsd

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

def NSLCManagement_instantiante(nsd_name, nsr_name, account, description):
    return CreatesNSInstance(nsd_name, nsr_name, account, description)

def NSLCManagement_scale(ns_name, vnf_name, scaling_group, scale_in, scale_out):
    client_osm = auth()
    ns = ''
    try:
        client_osm.ns.scale_vnf(ns_name, vnf_name, scaling_group, scale_in, scale_out)
    except NotFound as e:
        ns = e
    except ClientException as e:
        ns = e
    return ns

def NSLCManagement_update(ns_name):
    return ''

def NSLCManagement_heal(ns_name):
    return ''

def NSLCManagement_terminate(ns_name):
    client_osm = auth()
    ns = ''
    try:
        client_osm.ns.delete(ns_name)
    except NotFound as e:
        ns = e
    except ClientException as e:
        ns = e
    return ns



    






