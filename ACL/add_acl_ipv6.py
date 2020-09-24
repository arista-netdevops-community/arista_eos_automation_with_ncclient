from ncclient import manager
eos=manager.connect(host="10.85.128.125", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

###################################################################################
#                                                                                 #
#    This example will create an IPv6 access-list similar to following on EOS     #
#                                                                                 #
#    ipv6 access-list IPv6_ACL_NETCONF                                            #
#      10 permit icmpv6 any any log                                               #
#      20 deny ipv6 any 2001:a18::/29                                             # 
#                                                                                 #
###################################################################################

conf = '''
<config>
    <acl xmlns="http://arista.com/yang/openconfig/acl">
        <acl-sets>
            <acl-set>
                <name>IPv6_ACL_NETCONF</name>
                <type>ACL_IPV6</type>
                <acl-entries>
                    <acl-entry>
                        <sequence-id>10</sequence-id>
                        <actions>
                            <config>
                                <forwarding-action>ACCEPT</forwarding-action>
                                <log-action>LOG_SYSLOG</log-action>
                            </config>
                        </actions>
                        <config>
                            <sequence-id>10</sequence-id>
                        </config>
                        <ipv6>
                            <config>
                                <destination-address>::/0</destination-address>
                                <protocol>58</protocol>
                                <source-address>::/0</source-address>
                            </config>
                        </ipv6>
                    </acl-entry>
                    <acl-entry>
                        <sequence-id>20</sequence-id>
                        <actions>
                            <config>
                                <forwarding-action>DROP</forwarding-action>
                                <log-action>LOG_NONE</log-action>
                            </config>
                        </actions>
                        <config>
                            <sequence-id>20</sequence-id>
                        </config>
                        <ipv6>
                            <config>
                                <destination-address>2001:a18::/29</destination-address>
                                <source-address>::/0</source-address>
                            </config>
                        </ipv6>
                    </acl-entry>
                </acl-entries>
                <config>
                    <name>IPv6_ACL_NETCONF</name>
                    <type>ACL_IPV6</type>
                </config>
            </acl-set>
        </acl-sets>
    </acl>
</config>
'''

configuration = eos.edit_config(target = "running", config = conf, default_operation="merge")
print(configuration)

eos.close_session()
