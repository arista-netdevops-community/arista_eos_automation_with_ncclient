![GitHub](https://img.shields.io/github/license/ksator/arista_eos_automation_with_ncclient)   

# About this repository 

This repository has python scripts using ncclient to interact with Arista EOS devices

# About ncclient  

ncclient is a python library.  
It is a NETCONF client implementation in Python.    
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
>>> conf = '''
... <config>
...     <system>
...         <config>
...             <domain-name>abc.xyz</domain-name>
...         </config>
...     </system>
... </config>
... '''
>>> eos.edit_config(target = "running", config = conf)
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:45df179a-4dfd-441b-80b7-b7076068efb1"><ok></ok></rpc-reply>
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
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:7d60e55e-4eaf-45cc-ba3e-1e834e93d382"><data time-modified="2020-05-20T23:40:20.013989594Z"><system xmlns="http://openconfig.net/yang/system"><config><domain-name>abc.xyz</domain-name></config></system></data></rpc-reply>
>>> 
>>> eos.close_session()
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:bbc401ee-21ef-480e-947c-10d8d5f998b3"><ok></ok></rpc-reply>
>>> eos.connected
False
>>> 
>>> exit()
```
```
>>> from lxml import etree
>>> system_e = etree.Element("system")
>>> dns_e = etree.SubElement(system_e, "dns")
>>> servers_e = etree.SubElement(dns_e, "servers")
>>> server_e = etree.SubElement(servers_e, "server")
>>> address_e = etree.SubElement(server_e, "address")
>>> config_e = etree.SubElement(server_e, "config")
>>> address_e.text = "8.8.8.8"
>>> 
>>> address_e.text
'8.8.8.8'
>>> 
>>> etree.tostring(system_e)
b'<system><dns><servers><server><address>8.8.8.8</address><config/></server></servers></dns></system>'
>>> 
>>> etree.tostring(system_e, pretty_print = True)
b'<system>\n  <dns>\n    <servers>\n      <server>\n        <address>8.8.8.8</address>\n        <config/>\n      </server>\n    </servers>\n  </dns>\n</system>\n'
>>> 
>>> etree.dump(system_e)
<system>
  <dns>
    <servers>
      <server>
        <address>8.8.8.8</address>
        <config/>
      </server>
    </servers>
  </dns>
</system>
>>> 
>>> from ncclient import manager
>>> eos=manager.connect(host="10.83.28.203", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)
>>> eos.connected
True
>>> 
>>> print(eos.get_config(source="running", filter=("subtree", system_e)))
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:852573e7-7f0b-44eb-bd89-a3ecc4393596"><data time-modified="2020-05-20T23:40:20.065542759Z"><system xmlns="http://openconfig.net/yang/system"><dns><servers><server><address>8.8.8.8</address><config><address>8.8.8.8</address><port>53</port></config></server></servers></dns></system></data></rpc-reply>
>>> 
>>> eos.close_session()
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:b1d2afcb-90f2-4ea2-afed-3641339016f1"><ok></ok></rpc-reply>
>>> exit()
```
# Credits

Thank you to  John Allen for writing this blog https://eos.arista.com/ncclient-example-with-eos/  
It provided the basis for this example.

