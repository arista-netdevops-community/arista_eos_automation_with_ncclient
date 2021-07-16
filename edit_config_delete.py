from ncclient import manager
eos=manager.connect(host="10.83.28.221", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)

# Edit the running configuration with delete operation
# Get first the running configuration to be sure to then delete existing configuration data

conf = '''
<system xmlns="http://arista.com/yang/openconfig/system/">
    <config>
        <domain-name>
        </domain-name>
    </config>
    <dns>
        <servers>
            <server>
            </server>
        </servers>
    </dns>
    <aaa>
        <authentication>
            <users>
                <user>
                    <username>
                    </username>
                </user>
            </users>
        </authentication>
    </aaa>
</system>
'''
eos.get_config(source="running", filter=("subtree", conf))

conf = '''
<config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    <system xmlns="http://arista.com/yang/openconfig/system/">
        <config>
            <domain-name operation="delete">abc.xyz</domain-name>
         </config>
        <dns>
            <servers>
                <server>
                    <address operation="delete">1.1.1.1</address>
                </server>
            </servers>
        </dns>
    </system>
</config>
'''
reply = eos.edit_config(target = "running", config = conf, default_operation="none")

conf = '''
<config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    <system xmlns="http://arista.com/yang/openconfig/system/">
        <aaa>
            <authentication>
                <users>
                    <user>
                        <username operation="delete">gnmi</username>
                    </user>
                </users>
            </authentication>
        </aaa>
    </system>
</config>
'''
reply = eos.edit_config(target = "running", config = conf, default_operation="none")

eos.close_session()