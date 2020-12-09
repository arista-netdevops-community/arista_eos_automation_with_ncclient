from ncclient import manager

eos=manager.connect(host="hostname", port="22", timeout=30, username="admin", password="", hostkey_verify=False)

ethernet_trunk = '''
<config>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
            <name>Ethernet3/1</name>
            <config>
                <name>Ethernet3/1</name>
            </config>
            <ethernet xmlns="http://openconfig.net/yang/interfaces/ethernet">
                <switched-vlan xmlns="http://openconfig.net/yang/vlan"
                               nc:operation="delete">
                </switched-vlan>
            </ethernet>
        </interface>
    </interfaces>
</config>
'''

configuration = eos.edit_config(target="running", config=ethernet_trunk, default_operation="merge")
print(configuration)

eos.close_session()
