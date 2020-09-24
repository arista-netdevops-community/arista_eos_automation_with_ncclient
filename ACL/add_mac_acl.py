from ncclient import manager
import xml.dom.minidom
eos=manager.connect(host="10.81.108.236", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

#####################################################################################################
#                                                                                                   #
#    This example will create a  MAC access-list similar to following on EOS                        #
#                                                                                                   #
#    mac access-list MAC_ACL_NETCONF                                                                #
#      10 permit 00:1c:73:7a:40:d2 00:00:00:00:00:00 00:1c:73:7a:40:91 00:00:00:00:00:00 arp log    #                            #                                            #
#                                                                                                   #
#                                                                                                   #
#####################################################################################################

conf = '''
<config>
    <acl xmlns="http://arista.com/yang/openconfig/acl">
        <acl-sets>
            <acl-set>
                <name>MAC_ACL_NETCONF</name>
                <type>ACL_L2</type>
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
                        <l2>
                            <config>
                                <destination-mac>00:1c:73:7a:40:91</destination-mac>
                                <destination-mac-mask>ff:ff:ff:ff:ff:ff</destination-mac-mask>
                                <ethertype>2054</ethertype>
                                <source-mac>00:1c:73:7a:40:d2</source-mac>
                                <source-mac-mask>ff:ff:ff:ff:ff:ff</source-mac-mask>
                            </config>
                        </l2>
                    </acl-entry>
                </acl-entries>
                <config>
                    <name>MAC_ACL_NETCONF</name>
                    <type>ACL_L2</type>
                </config>
            </acl-set>
        </acl-sets>
    </acl>
</config>
'''

configuration = eos.edit_config(target = "running", config = conf, default_operation="merge")

print(configuration)

eos.close_session()
