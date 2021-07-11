from ncclient import manager
eos=manager.connect(host="10.83.28.203", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)

# Get configuration and state data
eos.get()

# Get configuration and state data using a filter

# Get configuration and state data for interface Ethernet 3
get_int_eth3 = eos.get(filter=("subtree", "<interfaces><interface><name>Ethernet3</name></interface></interfaces>"))
print (get_int_eth3.ok)
print (get_int_eth3)

int_eth3 = '''
<interfaces>
    <interface>
        <name>Ethernet3</name>
    </interface>
</interfaces>
'''
get_int_eth3 = eos.get(filter=("subtree", int_eth3))
print (get_int_eth3)

# Get interface description configured on interface Ethernet 3
int_eth3_description = '''
<interfaces>
    <interface>
        <name>
            Ethernet3
        </name>
        <config>
            <description>
            </description>
        </config>
    </interface>
</interfaces>
'''
get_int_eth3_description = eos.get(filter=("subtree", int_eth3_description))
print (get_int_eth3_description)

# Get interface Ethernet 3 operational status
int_eth3_op_status = '''
<interfaces>
    <interface>
        <name>
            Ethernet3
        </name>
        <state>
            <oper-status>
            </oper-status>
        </state>
    </interface>
</interfaces>
'''
get_int_eth3_op_status = eos.get(filter=("subtree", int_eth3_op_status))
print (get_int_eth3_op_status)

# Other examples
eos.get(filter=("subtree", "<system><aaa><authentication><users><user><username></username></user></users></authentication></aaa></system>"))
eos.get(filter=("subtree", "<system><aaa><authentication><users><user><username>arista</username></user></users></authentication></aaa></system>"))
