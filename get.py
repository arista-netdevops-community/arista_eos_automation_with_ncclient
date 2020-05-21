from ncclient import manager
eos=manager.connect(host="10.83.28.203", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)

Interface_Ethernet3='''
<interfaces>
    <interface>
        <name>Ethernet3</name>
    </interface>
</interfaces>
'''

get_interface_ethernet3 = eos.get(filter=("subtree", Interface_Ethernet3))

print (get_interface_ethernet3.ok)

print (get_interface_ethernet3)


