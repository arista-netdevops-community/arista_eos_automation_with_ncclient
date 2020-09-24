from ncclient import manager
eos=manager.connect(host="10.81.108.236", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

###########################################################################################
#                                                                                         #
#    This example will create an IPv6 static route similar to following on EOS            #
#                                                                                         #
#    ipv6 route 2001::/64 Ethernet2/1 2002::2 10                                          #
#                                                                                         #
###########################################################################################

default_VRF_conf = '''
<config>
    <network-instances xmlns="http://openconfig.net/yang/network-instance">
        <network-instance>
            <name>default</name>
            <protocols>
               <protocol>
                    <identifier>STATIC</identifier>
                    <name>STATIC</name>
                    <config>
                        <identifier>STATIC</identifier>
                        <name>STATIC</name>
                    </config>
                    <static-routes>
                        <static>
                            <prefix>2001::/64</prefix>
                            <config>
                                <prefix>2001::/64</prefix>
                            </config>
                            <next-hops>
                                <next-hop>
                                    <index>AUTO_1_2002--2_Ethernet2_1</index>
                                    <config>
                                        <index>AUTO_1_2002--2_Ethernet2_1</index>
                                        <metric>10</metric>
                                        <next-hop>2002::2</next-hop>
                                    </config>
                                    <interface-ref>
                                        <config>
                                            <interface>Ethernet2/1</interface>
                                        </config>
                                    </interface-ref>
                                </next-hop>
                            </next-hops>
                        </static>
                    </static-routes>
               </protocol> 
            </protocols>
        </network-instance>
    </network-instances>
</config>
'''

###########################################################################################
#                                                                                         #
#    This example will create an IPv6 static route similar to following on EOS            #
#                                                                                         #
#    ipv6 route vrf management ::/0 2607:f140:ffff:fe00::2 10                             #
#                                                                                         #
###########################################################################################

non_default_VRF_conf = '''
<config>
    <network-instances xmlns="http://openconfig.net/yang/network-instance">
        <network-instance>
            <name>management</name>
            <protocols>
               <protocol>
                    <identifier>STATIC</identifier>
                    <name>STATIC</name>
                    <config>
                        <identifier>STATIC</identifier>
                        <name>STATIC</name>
                    </config>
                    <static-routes>
                        <static>
                            <prefix>::/0</prefix>
                            <config>
                                <prefix>::/0</prefix>
                            </config>
                            <next-hops>
                                <next-hop>
                                    <index>AUTO_1_2607-f140-ffff-fe00--2</index>
                                    <config>
                                        <index>AUTO_1_2607-f140-ffff-fe00--2</index>
                                        <metric>10</metric>
                                        <next-hop>2607:f140:ffff:fe00::2</next-hop>
                                    </config>
                                </next-hop>
                            </next-hops>
                        </static>
                    </static-routes>
               </protocol> 
            </protocols>
        </network-instance>
    </network-instances>
</config>
'''

###########################################################################################
#                                                                                         #
#    This example will create an IPv6 static route similar to following on EOS            #
#                                                                                         #
#    ipv6 route 112:112:112::112/128 Null0                                                #
#                                                                                         #
###########################################################################################

null0_route = '''
<config>
    <network-instances xmlns="http://openconfig.net/yang/network-instance">
        <network-instance>
            <name>default</name>
            <protocols>
               <protocol>
                    <identifier>STATIC</identifier>
                    <name>STATIC</name>
                    <config>
                        <identifier>STATIC</identifier>
                        <name>STATIC</name>
                    </config>
                    <static-routes>
                        <static>
                            <prefix>112:112:112::112/128</prefix>
                            <config>
                                <prefix>112:112:112::112/128</prefix>
                            </config>
                            <next-hops>
                                <next-hop>
                                    <index>AUTO_DROP_ROUTE</index>
                                    <config>
                                        <index>AUTO_DROP_ROUTE</index>
                                        <metric>1</metric>
                                        <next-hop>DROP</next-hop>
                                    </config>
                                </next-hop>
                            </next-hops>
                        </static>
                    </static-routes>
               </protocol> 
            </protocols>
        </network-instance>
    </network-instances>
</config>
'''
configuration = eos.edit_config(target = "running", config = null0_route, default_operation="merge")
print(configuration)

eos.close_session()