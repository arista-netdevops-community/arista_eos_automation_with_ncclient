from ncclient import manager
eos=manager.connect(host="10.83.28.203", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)

# Get running configuration:
eos.get_config(source = "running")

# Using filters

hostname='''
<system>
    <config>
        <hostname>
        </hostname>
    </config>
</system>
'''
print (eos.get_config(source="running", filter=("subtree", hostname)))

domain_name='''
<system>
    <config>
        <domain-name>
        </domain-name>
    </config>
</system>
'''
print (eos.get_config(source="running", filter=("subtree", domain_name)))

dns_servers='''
<system>
    <dns>
        <servers>
        </servers>
    </dns>
</system>
'''
print (eos.get_config(source="running", filter=("subtree", dns_servers)))

dns_8888='''
<system>
    <dns>
        <servers>
            <server>
                <address>8.8.8.8</address>
                <config>
                </config>
            </server>
        </servers>
    </dns>
</system>
'''
print (eos.get_config(source="running", filter=("subtree", dns_8888)))

Interface_Ethernet3='''
<interfaces>
    <interface>
        <name>Ethernet3</name>
    </interface>
</interfaces>
'''
print(eos.get_config(source="running", filter=("subtree", Interface_Ethernet3)))

Interface_Ethernet3_description='''
<interfaces>
    <interface>
        <name>Ethernet3</name>
    <config>
        <description>
        </description>
    </config>
    </interface>
</interfaces>
'''
print(eos.get_config(source="running", filter=("subtree", Interface_Ethernet3_description)))

eos.close_session()
