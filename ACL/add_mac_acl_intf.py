from ncclient import manager
import xml.dom.minidom
eos=manager.connect(host="10.81.108.236", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

###################################################################################
#                                                                                 #
#    This example will assign an ingress MAC ACL to an L2 interface               #
#                                                                                 #
#          interface Ethernet1/1                                                  #
#            mac access-group MAC_ACL_NETCONF in                                  #                                       #
#                                                                                 #
#                                                                                 #
###################################################################################

conf = '''
<config>
    <acl xmlns="http://arista.com/yang/openconfig/acl">
        <interfaces>
            <interface>
                <id>Ethernet1/1</id>
                <config>
                    <id>Ethernet1/1</id>
                </config>
                <interface-ref>
                    <config>
                        <interface>Ethernet1/1</interface>
                        <subinterface>0</subinterface>
                    </config>
                </interface-ref>
                <ingress-acl-sets>
                    <ingress-acl-set>
                        <set-name>MAC_ACL_NETCONF</set-name>
                        <type>ACL_L2</type>
                        <config>
                            <set-name>MAC_ACL_NETCONF</set-name>
                            <type>ACL_L2</type>
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
