from ncclient import manager
eos=manager.connect(host="10.83.28.203", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)

conf = '''
<config>
    <system>
        <config>
            <domain-name>abc.xyz</domain-name>
            <hostname>switch1</hostname>
        </config>
        <dns>
            <config>
                <network-instance xmlns="http://arista.com/yang/openconfig/system/augments">default</network-instance>
            </config>
                <servers>
                    <server>
                        <address>8.8.8.8</address>
                        <config>
                            <address>8.8.8.8</address>
                            <port>53</port>
                         </config>
                    </server>
                    <server>
                        <address>10.83.28.52</address>
                        <config>
                            <address>10.83.28.52</address>
                            <port>53</port>
                        </config>
                    </server>
                </servers>
        </dns>
    </system>
</config>
'''

configuration = eos.edit_config(target = "running", config = conf)
print(configuration)


dns_servers='''
<system>
    <dns>
        <servers>
        </servers>
    </dns>
</system>
'''

dns_servers_conf = eos.get_config(source="running", filter=("subtree", dns_servers))
print (dns_servers_conf)

eos.close_session()
