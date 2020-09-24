from ncclient import manager
import xml.dom.minidom
eos=manager.connect(host="10.85.128.125", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

###################################################################################
#                                                                                 #
#    This example will assign and ingress ipv6 ACL to an L3 interface             #
#                                                                                 #
###################################################################################

conf = '''
<config>
    <acl xmlns="http://arista.com/yang/openconfig/acl">
        <interfaces>
            <interface>
                <id>Ethernet2/1</id>
                <config>
                    <id>Ethernet2/1</id>
                </config>
                <interface-ref>
                    <config>
                        <interface>Ethernet2/1</interface>
                        <subinterface>0</subinterface>
                    </config>
                </interface-ref>
                <egress-acl-sets/>
                <ingress-acl-sets>
                    <ingress-acl-set>
                        <set-name>IPv6_ACL_NETCONF</set-name>
                        <type>ACL_IPV6</type>
                        <config>
                            <set-name>IPv6_ACL_NETCONF</set-name>
                            <type>ACL_IPV6</type>
                        </config>
                    </ingress-acl-set>
                </ingress-acl-sets>
            </interface>
        </interfaces>
    </acl>
</config>
'''

configuration = eos.edit_config(target = "running", config = conf, default_operation="merge")

print(configuration)

eos.close_session()
