from ncclient import manager
eos=manager.connect(host="10.81.117.80", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

#######################################################################################
#                                                                                     #
#    This example will configure an IPv6 SVI as follows                               #
#                                                                                     #
#######################################################################################

svi = '''
<config>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
            <name>Vlan200</name>
            <config>
                <name>Vlan200</name>
                <tpid xmlns="http://openconfig.net/yang/vlan" xmlns:oc-vlan-types="http://openconfig.net/yang/vlan-types">oc-vlan-types:TPID_0X8100</tpid>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:l3ipvlan</type>
            </config>
            <routed-vlan xmlns="http://openconfig.net/yang/vlan">
                <config>
                    <vlan>Vlan200</vlan>
                </config>
                <ipv6 xmlns="http://openconfig.net/yang/interfaces/ip">
                    <addresses>
                        <address>
                            <ip>10:23:31::1:32:93</ip>
                            <config>
                                <ip>10:23:31::1:32:93</ip>
                                <prefix-length>64</prefix-length>
                            </config>
                        </address>
                    </addresses>
                    <config>
                        <enabled>true</enabled>
                    </config>
                </ipv6>
            </routed-vlan>
        </interface>
    </interfaces>
</config>
'''


#######################################################################################
#                                                                                     #
#    This example will configure an IPv6 intf as follows                              #
#    interface Ethernet5                                                              #
#      ipv6 enable                                                                    #
#      ipv6 address 2039::415/64                                                      #
#                                                                                     #
#######################################################################################

l3_intf = '''
<config>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
            <name>Ethernet5</name>
            <config>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
            </config>
            <subinterfaces>
                <subinterface>
                    <index>0</index>
                    <ipv6 xmlns="http://openconfig.net/yang/interfaces/ip">
                        <addresses>
                            <address>
                                <ip>2039::415</ip>
                                <config>
                                    <ip>2039::415</ip>
                                    <prefix-length>64</prefix-length>
                                </config>
                            </address>
                        </addresses>
                        <config>
                            <enabled>true</enabled>
                        </config>
                    </ipv6>
                </subinterface>
            </subinterfaces>
        </interface>
    </interfaces>
</config>
'''

#######################################################################################
#                                                                                     #
#    This example will configure an IPv6 loopback as follows                          #
#    interface Loopback100                                                            #
#      ipv6 enable                                                                    #
#      ipv6 address 2002:415::415/128                                                 #
#                                                                                     #
#######################################################################################

loopback = '''
<config>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
            <name>Loopback100</name>
            <config>
                <enabled>true</enabled>
                <name>Loopback100</name>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
            </config>
            <subinterfaces>
                <subinterface>
                    <index>0</index>
                    <ipv6 xmlns="http://openconfig.net/yang/interfaces/ip">
                       <addresses>
                            <address>
                                <ip>2002:415::415</ip>
                                <config>
                                    <ip>2002:415::415</ip>
                                    <prefix-length>128</prefix-length>
                                </config>
                            </address>
                       </addresses> 
                       <config>
                            <enabled>true</enabled>
                        </config>
                    </ipv6>
                </subinterface>
            </subinterfaces>
        </interface>
    </interfaces>
</config>
'''

#######################################################################################
#                                                                                     #
#    This example will configure an IPv6 subinterface as follows                      #
#    interface Ethernet10.100                                                         #
#      description sub-interface-et10_100                                             #
#      ipv6 enable                                                                    #
#      ipv6 address 2001:1516::416/64                                                 #
#                                                                                     #
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
                        <index>100</index>
                        <enabled>true</enabled>
                        <description>sub-interface-et10_100</description>
                    </config>
                    <ipv4 xmlns="http://openconfig.net/yang/interfaces/ip">
                        <config><enabled>true</enabled></config>
                    </ipv4>
                    <ipv6 xmlns="http://openconfig.net/yang/interfaces/ip">
                        <addresses>
                            <address>
                                <ip>2001:1516::416</ip>
                                <config>
                                    <ip>2001:1516::416</ip>
                                    <prefix-length>64</prefix-length>
                                </config>
                            </address>
                        </addresses>
                        <config>
                            <enabled>true</enabled>
                        </config>
                    </ipv6>
                </subinterface>
            </subinterfaces>
        </interface>
    </interfaces>
</config>
'''

configuration = eos.edit_config(target = "running", config = loopback, default_operation="merge")
print(configuration)

eos.close_session()