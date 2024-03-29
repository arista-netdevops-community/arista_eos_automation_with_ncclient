from ncclient import manager
eos=manager.connect(host="10.73.1.105", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)

# Configure an interface description
Interface_Ethernet3_description='''
    <config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces xmlns="http://openconfig.net/yang/interfaces">
            <interface>
                <name>Ethernet3</name>
                <config>
                    <description nc:operation="replace">This is the best interface</description>
                </config>
            </interface>
        </interfaces>
    </config>
'''
reply = eos.edit_config(target="running", config=Interface_Ethernet3_description, default_operation="none")

# Get interface state and configuration data
Interface_Ethernet3='''
    <interfaces>
        <interface>
            <name>Ethernet3</name>
        </interface>
    </interfaces>
'''
get_interface_ethernet3 = eos.get(filter=("subtree", Interface_Ethernet3))
print (get_interface_ethernet3)

# Parse the XML output

ns = {None: 'http://openconfig.net/yang/interfaces'}

description = get_interface_ethernet3.data.find(".//interfaces/interface/config/description", namespaces=ns)
print(description.text)

operStatus = get_interface_ethernet3.data.find(".//interfaces/interface/state/oper-status", namespaces=ns)
print(operStatus.text)

# Get interface configuration and parse the XML output

get_interface_ethernet3 = eos.get_config(source="running", filter=("subtree", Interface_Ethernet3))
print (get_interface_ethernet3)

ns = {None: 'http://openconfig.net/yang/interfaces'}
description = get_interface_ethernet3.data.find(".//interfaces/interface/config/description", namespaces=ns)
print(description.text)
