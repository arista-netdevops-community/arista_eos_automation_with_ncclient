from ncclient import manager
eos=manager.connect(host="10.81.117.80", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

###################################################################################
#                                                                                 #
#    This example will create an IPv4 access-list similar to following on EOS     #
#                                                                                 #
#    ip access-list IPv4_ACL_NETCONF                                              #
#       10 permit icmp host 10.10.10.2 any ttl eq 5                               #
#                                                                                 #
###################################################################################

conf = '''
<config>
    <acl xmlns="http://arista.com/yang/openconfig/acl">
        <acl-sets>
            <acl-set>
                <name>IPv4_ACL_NETCONF</name>
                <type>ACL_IPV4</type>
                <acl-entries>
                    <acl-entry>
                        <sequence-id>10</sequence-id>
                        <actions>
                            <config>
                                <forwarding-action>ACCEPT</forwarding-action>
                                <log-action>LOG_NONE</log-action>
                            </config>
                        </actions>
                        <config>
                            <sequence-id>10</sequence-id>
                        </config>
                        <ipv4>
                            <config>
                                <destination-address>0.0.0.0/0</destination-address>
                                <protocol>1</protocol>
                                <source-address>10.10.10.2/32</source-address>
                                <hop-limit>5</hop-limit>
                            </config>
                        </ipv4>
                    </acl-entry>
                </acl-entries>
                <config>
                    <name>IPv4_ACL_NETCONF</name>
                    <type>ACL_IPV4</type>
                </config>
            </acl-set>
        </acl-sets>
    </acl>
</config>
'''

configuration = eos.edit_config(target = "running", config = conf, default_operation="merge")
print(configuration)

eos.close_session()
