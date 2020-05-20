# About this repository 

This repo has python scripts using ncclient to interact with Arista EOS devices

# About ncclient  

ncclient is a python library. It is a NETCONF client implementation in Python.    
Code https://github.com/ncclient/ncclient  
Documentation https://ncclient.readthedocs.io/en/latest/  
PyPI (Python Package Index) https://pypi.python.org/pypi/ncclient  

# About NETCONF

NETCONF is a protocol defined in the [RFC 6241](https://tools.ietf.org/html/rfc6241)   
ncclient is a NETCONF client  

# Requirements 

Requirements on your laptop: 
```
pip freeze | grep ncclient
ncclient==0.6.7
```

Requirements on the EOS device: 
```
s7152#show running-config section netconf
management api netconf
   transport ssh def
```

# ncclient demo

```
>>> from ncclient import manager
>>> 
>>> eos=manager.connect(host="10.83.28.203", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)
>>> eos.connected
True
>>> eos.timeout
30
>>> eos.session_id
'872680990'
>>> 
>>> assert("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring" in eos.server_capabilities), "NetConf server not compliant with https://tools.ietf.org/html/rfc6022"
>>> 
>>> domain_name='''
... <system>
...     <config>
...         <domain-name>
...         </domain-name>
...     </config>
... </system>
... '''
>>> domain_name_conf = eos.get_config(source="running", filter=("subtree", domain_name))
>>> print (domain_name_conf)
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:e41791b2-72ef-41ce-9d2a-8d2286cbbfef"><data time-modified="2020-05-20T17:39:58.332197444Z"><system xmlns="http://openconfig.net/yang/system"><config><domain-name>lab.local</domain-name></config></system></data></rpc-reply>
>>> 
>>> eos.close_session()
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:bbc401ee-21ef-480e-947c-10d8d5f998b3"><ok></ok></rpc-reply>
>>> eos.connected
False
>>> 
>>> exit()
```

# Credits

Thank you to  John Allen for writing this blog https://eos.arista.com/ncclient-example-with-eos/  
It provided the basis for this example.

