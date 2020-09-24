from ncclient import manager
eos=manager.connect(host="10.81.108.236", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

#########################################################################################
#                                                                                       #
#    This example will delete a specified IPv4 static route                             #
#                                                                                       #
#    no ip route 11.11.11.11/32 10.85.128.1                                             #
#                                                                                       #
#########################################################################################

del_prefix_default_VRF = '''
<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
    <network-instances xmlns="http://openconfig.net/yang/network-instance">
        <network-instance>
            <name>default</name>
            <protocols>
               <protocol>
                    <identifier>STATIC</identifier>
                    <name>STATIC</name>
                    <static-routes>
                        <static xc:operation="delete">
                            <prefix>11.11.11.11/32</prefix>
                        </static>
                    </static-routes>
               </protocol> 
            </protocols>
        </network-instance>
    </network-instances>
</config>
'''

#########################################################################################
#                                                                                       #
#    This example will delete a specified IPv4 static route                             #
#                                                                                       #
#    no ip route vrf management 11.11.11.11/32 10.85.128.1                              #
#                                                                                       #
#########################################################################################

del_prefix_non_default_VRF = '''
<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
    <network-instances xmlns="http://openconfig.net/yang/network-instance">
        <network-instance>
            <name>management</name>
            <protocols>
               <protocol>
                    <identifier>STATIC</identifier>
                    <name>STATIC</name>
                    <static-routes>
                        <static xc:operation="delete">
                            <prefix>11.11.11.11/32</prefix>
                        </static>
                    </static-routes>
               </protocol> 
            </protocols>
        </network-instance>
    </network-instances>
</config>
'''

configuration = eos.edit_config(target = "running", config = del_prefix_non_default_VRF, default_operation="merge")
print(configuration)

eos.close_session()