```
>>> from ncclient import manager
>>> eos=manager.connect(host="10.83.28.203", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)
>>> eos.connected
True
>>> eos.timeout
30
>>> eos.session_id
'872680990'
>>> assert("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring" in eos.server_capabilities), "NetConf server not compliant with https://tools.ietf.org/html/rfc6022"
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
>>> exit()
```
