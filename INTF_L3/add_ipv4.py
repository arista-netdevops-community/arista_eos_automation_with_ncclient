from ncclient import manager
eos=manager.connect(host="10.81.117.80", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

#######################################################################################
#                                                                                     #
#    This example will configure an SVI as follows                                    #
#                                                                                     #
#    interface Vlan100                                                                #
#      ip address 100.1.10.2/24                                                       #
#######################################################################################

svi = '''
<config>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
            <name>Vlan100</name>
            <config>
                <name>Vlan100</name>
                <enabled>true</enabled>
                <tpid xmlns="http://openconfig.net/yang/vlan" xmlns:oc-vlan-types="http://openconfig.net/yang/vlan-types">oc-vlan-types:TPID_0X8100</tpid>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:l3ipvlan</type>
            </config>
            <routed-vlan xmlns="http://openconfig.net/yang/vlan">
                <config>
                    <vlan>Vlan100</vlan>
                </config>
                <ipv4 xmlns="http://openconfig.net/yang/interfaces/ip">
                    <addresses>
                        <address>
                            <ip>100.1.10.2</ip>
                            <config>
                                <addr-type xmlns="http://arista.com/yang/openconfig/interfaces/augments">PRIMARY</addr-type>
                                <ip>100.1.10.2</ip>
                                <prefix-length>24</prefix-length>
                            </config>
                        </address>
                    </addresses>
                </ipv4>
            </routed-vlan>
        </interface>
    </interfaces>
</config>
'''

#######################################################################################
#                                                                                     #
#    This example will configure an L3 intf as follows                                #
#                                                                                     #
#    interface Ethernet10                                                             #
#      description Uplink to spine1                                                   #
#      ip address 172.168.14.2/30                                                     #
#######################################################################################

l3_intf = '''
<config>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
            <name>Ethernet10</name>
            <config>
                <description>Uplink to spine1</description>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
            </config>
            <subinterfaces>
                <subinterface>
                    <index>0</index>
                    <ipv4 xmlns="http://openconfig.net/yang/interfaces/ip">
                        <addresses>
                            <address>
                                <ip>172.168.14.2</ip>
                                <config>
                                    <ip>172.168.14.2</ip>
                                    <addr-type xmlns="http://arista.com/yang/openconfig/interfaces/augments">PRIMARY</addr-type>
                                    <prefix-length>30</prefix-length>
                                </config>
                            </address>
                        </addresses>
                    </ipv4>
                </subinterface>
            </subinterfaces>
        </interface>
    </interfaces>
</config>
'''

#######################################################################################
#                                                                                     #
#    This example will configure an L3 sub-intf as follows                            #
#                                                                                     #
#    interface Ethernet10.100                                                         #
#      description sub-interface-et10_100                                             #
#      ip address 172.168.100.1/30                                                    #
#######################################################################################

sub_intf = '''
<config>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
            <name>Ethernet10</name>
            <config>
                <name>Ethernet10</name>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
            </config>
            <subinterfaces>
                <subinterface>
                    <index>100</index>
                    <config>
                        <enabled>true</enabled>
                        <index>100</index>
                        <description>sub-interface-et10_100</description>
                    </config>
                    <ipv4 xmlns="http://openconfig.net/yang/interfaces/ip">
                        <addresses>
                            <address>
                                <ip>172.168.100.1</ip>
                                <config>
                                    <addr-type xmlns="http://arista.com/yang/openconfig/interfaces/augments">PRIMARY</addr-type>
                                    <ip>172.168.100.1</ip>
                                    <prefix-length>30</prefix-length>
                                </config>
                            </address>
                        </addresses>
                        <config>
                            <enabled>true</enabled>
                        </config>
                    </ipv4>
                    <vlan xmlns="http://openconfig.net/yang/vlan">
                        <config>
                            <vlan-id>100</vlan-id>
                        </config>
                    </vlan>
                </subinterface>
            </subinterfaces>
        </interface>
    </interfaces>
</config>
'''

#######################################################################################
#                                                                                     #
#    This example will configure a loopback as follows                                #
#                                                                                     #
#    interface Loopback1                                                              #
#      description EVPN_OVERLAY                                                       #
#      ip address 1.1.1.1/32                                                          #
#######################################################################################

loopback = '''
<config>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
            <name>Loopback1</name>
            <config>
                <description>EVPN_OVERLAY</description>
                <name>Loopback1</name>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
            </config>
            <subinterfaces>
                <subinterface>
                    <index>0</index>
                    <ipv4 xmlns="http://openconfig.net/yang/interfaces/ip">
                        <addresses>
                            <address>
                                <ip>1.1.1.1</ip>
                                <config>
                                    <ip>1.1.1.1</ip>
                                    <addr-type xmlns="http://arista.com/yang/openconfig/interfaces/augments">PRIMARY</addr-type>
                                    <prefix-length>32</prefix-length>
                                </config>
                            </address>
                        </addresses>
                    </ipv4>
                </subinterface>
            </subinterfaces>
        </interface>
    </interfaces>
</config>
'''


configuration = eos.edit_config(target = "running", config = loopback, default_operation="merge")
print(configuration)

eos.close_session()
