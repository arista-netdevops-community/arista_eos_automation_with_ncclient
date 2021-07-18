- [About this repository](#about-this-repository)
- [About ncclient](#about-ncclient)
- [About NETCONF](#about-netconf)
- [Requirements](#requirements)
- [ncclient demo](#ncclient-demo)
- [NETCONF over SSH demo](#netconf-over-ssh-demo)
- [Credits](#credits)
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
ncclient==0.6.12
```

Requirements on the EOS device:
```
switch1#show running-config section netconf
management api netconf
   transport ssh test
      vrf MGMT
```
```
switch1#sh management api netconf
Enabled:            Yes
Server:             running on port 830, in MGMT VRF
```
# ncclient demo

```
>>> from ncclient import manager
>>> eos=manager.connect(host="10.83.28.221", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)
>>>
>>> eos.connected
True
>>> eos.timeout
30
>>> eos.session_id
'1292406600'
>>>
>>> assert("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring" in eos.server_capabilities), "NetConf server not compliant with https://tools.ietf.org/html/rfc6022"
>>>
>>> conf = '''
... <config>
...     <system xmlns="http://openconfig.net/yang/system">
...         <config>
...             <domain-name>abc.xyz</domain-name>
...         </config>
...     </system>
... </config>
... '''
>>>
>>> eos.edit_config(target = "running", config = conf, default_operation="merge")
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:33ca18d3-43b5-4277-a6ce-9a751f74cada"><ok></ok></rpc-reply>
>>>
>>> domain_name='''
... <system xmlns="http://openconfig.net/yang/system">
...     <config>
...         <domain-name>
...         </domain-name>
...     </config>
... </system>
... '''
>>>
>>> domain_name_conf = eos.get_config(source="running", filter=("subtree", domain_name))
>>> print (domain_name_conf)
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:a43cfae5-3215-4f99-97ce-ff61ca1e285c"><data time-modified="2021-07-11T12:29:49.133333939Z"><system xmlns="http://openconfig.net/yang/system"><config><domain-name>abc.xyz</domain-name></config></system></data></rpc-reply>
>>>
>>> eos.close_session()
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:1841896a-9c97-467d-aef8-9a405b51d298"><ok></ok></rpc-reply>
>>>
>>> eos.connected
False
>>>
>>> exit()
```
```
>>> from lxml import etree
>>>
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
>>> eos=manager.connect(host="10.83.28.221", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)
>>> eos.connected
True
>>>
>>> print(eos.get_config(source="running", filter=("subtree", system_e)))
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:ab16e734-04df-4d4f-8efe-27963ece586c"><data time-modified="2021-07-11T12:29:49.138275819Z"><system xmlns="http://openconfig.net/yang/system"><dns><servers><server><address>8.8.8.8</address><config><address>8.8.8.8</address></config></server></servers></dns></system></data></rpc-reply>
>>>
>>> eos.close_session()
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:2eed88ee-106b-44d1-b196-f79611512b25"><ok></ok></rpc-reply>
>>>
>>> exit()
```

There are many other python scripts using ncclient in this repository

- [print_client_capabilities.py](print_client_capabilities.py) prints the NETCONF client capabilities.
- [print_server_capabilities.py](print_server_capabilities.py) prints the NETCONF server capabilities.
- [get.py](get.py) uses the `get` operation to retrieve the configuration and state data. It uses a filter to specify the portion of the configuration and state data to retrieve.
- [get_config.py](get_config.py) uses the `get-config` operation with a filter to retrieve part of the configuration.
- [parse_xml_output.py](parse_xml_output.py) uses the `get` operation to retrieve data from the device and then parse this data.
- [edit_config_merge.py](edit_config_merge.py) uses the `edit-config` operation with the `merge` operation (which is the default operation for `edit-config`)
- [edit_config_replace.py](edit_config_replace.py) uses the `edit-config` operation with the `replace` operation
- [edit_config_delete.py](edit_config_delete.py) uses the `edit-config` operation with the `delete` operation
- [EOS_commands_with_NETCONF.py](EOS_commands_with_NETCONF.py) configures a device using the `edit-config` operation and EOS data model
- [candidate_configuration_commit.py](candidate_configuration_commit.py) uses the `edit-config` operation with the `candidate` configuration datastore. It uses a `lock` operation and `commit` operation.
- [candidate_configuration_discard_changes.py](candidate_configuration_discard_changes.py). uses the `edit-config` operation with the `candidate` configuration datastore. It uses a `lock` operation and `discard_change` operation to revert the candidate configuration to the current running configuration (insteaf of commiting the candidate configuration).
- [rpc.py](rpc.py) sends RPCs to configure EOS devices.

To execute one of these scripts, run as example this command:

```
python3 print_server_capabilities.py
```

# NETCONF over SSH demo

- NETCONF is defined in the RFC 6241.
- NETCONF over SSH is discussed in a separate RFC (6242).

In order to open a NETCONF session inside an SSH connection, there are two options:
- we can invoke the NETCONF subsystem using the following SSH command `ssh username@device -s netconf`
- we can establish an SSH connection to an EOS device (NETCONF server), and then run the EOS command `netconf start-client`

There is NETCONF over SSH demo in [this file](NETCONF_over_SSH_demo.md): 
- It uses `lock`, `unlock`, `edit-config`, `commit`, `discard_change`, `get`, `get-config`, `copy-config` operations. 
- It also uses filters. 
- It edits both the `candidate` and `running` configuration datastore.

# Credits

Thank you to  John Allen for writing this blog https://eos.arista.com/ncclient-example-with-eos/
It provided the basis for this example.

