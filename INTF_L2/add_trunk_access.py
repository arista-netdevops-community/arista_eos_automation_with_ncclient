from ncclient import manager
eos=manager.connect(host="10.81.117.80", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

#######################################################################################
#                                                                                     #
#    This example will configure an L2 ethernet intf as follows                       #
#       interface Ethernet1                                                           #
#          description Uplink to Spine                                                #
#          switchport trunk native vlan 10                                            #
#          switchport trunk allowed vlan 1-10                                         #
#          switchport mode trunk                                                      #
#######################################################################################

ethernet_trunk = '''
<config>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
            <name>Ethernet1</name>
            <config>
                <description>Uplink to Spine</description>
                <name>Ethernet1</name>
                <enabled>true</enabled>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
            </config>
            <ethernet xmlns="http://openconfig.net/yang/interfaces/ethernet">
                <switched-vlan xmlns="http://openconfig.net/yang/vlan">
                    <config>
                        <interface-mode>TRUNK</interface-mode>
                        <native-vlan>10</native-vlan>
                        <trunk-vlans>1..10</trunk-vlans>
                    </config>
                </switched-vlan>
            </ethernet>
        </interface>
    </interfaces>
</config>
'''

#######################################################################################
#                                                                                     #
#    This example will configure an L2 port-channel  as follows                       #
#       interface Port-Channel1000                                                    #
#          description NFS-2                                                          #
#          switchport access vlan 4094                                                #
#######################################################################################

port_channel_access = '''
<config>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
            <name>Port-Channel1000</name>
            <config>
                <description>NFS-2</description>
                <name>Port-Channel1000</name>
                <enabled>true</enabled>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ieee8023adLag</type>
            </config>
            <aggregation xmlns="http://openconfig.net/yang/interfaces/aggregate">
                <config>
                    <lag-type>LACP</lag-type>
                </config>
                <switched-vlan xmlns="http://openconfig.net/yang/vlan">
                    <config>
                        <interface-mode>ACCESS</interface-mode>
                        <access-vlan>4094</access-vlan>
                    </config>
                </switched-vlan>
            </aggregation>
        </interface>
    </interfaces>
</config>
'''

#######################################################################################
#                                                                                     #
#    This example will configure  L2 intf as part of port-channel                     #
#    Then configure port-channel as trunk and mlag interface                          #
#    interface Ethernet3                                                              #
#      description MLAG Port-Channel to NFS-1-standby                                 #
#      channel-group 1000 mode active                                                 #
#                                                                                     #
#    interface Ethernet5                                                              #
#      description MLAG Port-Channel to NFS-1-active                                  #
#      channel-group 1000 mode active                                                 #
#                                                                                     #
#    interface Port-Channel1000                                                       #
#      description MLAG NFS-1                                                         #
#      switchport trunk allowed vlan 1214                                             #
#      switchport mode trunk                                                          #
#      mlag 2                                                                         #
#                                                                                     #
#######################################################################################

mlag_intf = '''
<config>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
            <name>Ethernet5</name>
            <config>
                <name>Ethernet5</name>
                <enabled>true</enabled>
                <description>MLAG Port-Channel to NFS-1-active</description>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
            </config>
            <ethernet xmlns="http://openconfig.net/yang/interfaces/ethernet">
                <config>
                    <aggregate-id xmlns="http://openconfig.net/yang/interfaces/aggregate">Port-Channel1000</aggregate-id>
                </config>
            </ethernet>
        </interface>
        <interface>
            <name>Ethernet3</name>
            <config>
                <name>Ethernet3</name>
                <enabled>true</enabled>
                <description>MLAG Port-Channel to NFS-1-standby</description>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
            </config>
            <ethernet xmlns="http://openconfig.net/yang/interfaces/ethernet">
                <config>
                    <aggregate-id xmlns="http://openconfig.net/yang/interfaces/aggregate">Port-Channel1000</aggregate-id>
                </config>
            </ethernet>
        </interface>
        <interface>
            <name>Port-Channel1000</name>
            <config>
                <description>MLAG NFS-1</description>
                <name>Port-Channel1000</name>
                <enabled>true</enabled>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ieee8023adLag</type>
            </config>
            <aggregation xmlns="http://openconfig.net/yang/interfaces/aggregate">
                <config>
                    <lag-type>LACP</lag-type>
                    <mlag xmlns="http://arista.com/yang/openconfig/interfaces/augments">2</mlag>
                </config>
                <switched-vlan xmlns="http://openconfig.net/yang/vlan">
                    <config>
                        <interface-mode>TRUNK</interface-mode>
                        <trunk-vlans>1214</trunk-vlans>
                    </config>
                </switched-vlan>
            </aggregation>
        </interface>
    </interfaces>
</config>
'''


configuration = eos.edit_config(target = "running", config = mlag_intf, default_operation="merge")
print(configuration)

eos.close_session()