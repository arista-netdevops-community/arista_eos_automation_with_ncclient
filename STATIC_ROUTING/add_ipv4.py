from ncclient import manager
eos=manager.connect(host="10.81.108.236", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

###################################################################################
#                                                                                 #
#    This example will create an IPv4 static route similar to following on EOS    #
#                                                                                 #
#    ip route 11.11.11.11/32 10.81.108.193                                        #
#                                                                                 #
###################################################################################

default_VRF_conf = '''
<config>
    <network-instances>
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
                            <prefix>11.11.11.11/32</prefix>
                            <config>
                                <prefix>11.11.11.11/32</prefix>
                            </config>
                            <next-hops>
                                <next-hop>
                                    <index>AUTO_1_10-81-108-193</index>
                                    <config>
                                        <index>AUTO_1_10-81-108-193</index>
                                        <metric>1</metric>
                                        <next-hop>10.81.108.193</next-hop>
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

###################################################################################
#                                                                                 #
#    This example will create an IPv4 static route similar to following on EOS    #
#                                                                                 #
#    ip route vrf management 11.11.11.11/32 10.85.128.1                           #
#                                                                                 #
###################################################################################

non_default_VRF_conf = '''
<config>
    <network-instances>
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
                            <prefix>11.11.11.11/32</prefix>
                            <config>
                                <prefix>11.11.11.11/32</prefix>
                            </config>
                            <next-hops>
                                <next-hop>
                                    <index>AUTO_1_11.11.11.11</index>
                                    <config>
                                        <index>AUTO_1_11.11.11.11</index>
                                        <metric>1</metric>
                                        <next-hop>10.85.128.1</next-hop>
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

###################################################################################
#                                                                                 #
#    This example will create an IPv4 static route similar to following on EOS    #
#                                                                                 #
#    ip route vrf management 11.11.11.11/32 Null0                                 #
#                                                                                 #
###################################################################################

null0_route = '''
<config>
    <network-instances>
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
                            <prefix>11.11.11.11/32</prefix>
                            <config>
                                <prefix>11.11.11.11/32</prefix>
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