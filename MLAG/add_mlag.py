from ncclient import manager
import xml.dom.minidom
eos=manager.connect(host="10.85.128.81", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

#########################################################################################
#                                                                                       #
#    This example will configure following example MLAG                                 #
#                                                                                       #     
#       mlag configuration                                                              #
#           domain-id MLAG-POD1                                                         #
#           local-interface Vlan4094                                                    #
#           peer-address 10.149.70.33                                                   #
#           peer-link Port-Channel1000                                                  #
#           dual-primary detection delay 120 action errdisable all-interfaces           #
#           reload-delay 200                                                            #
#           reload-delay non-mlag 200                                                   #    
#           reload-delay mode lacp standby              			                    #
#                                                                                       #
#########################################################################################

conf='''
<config>
    <arista xmlns="http://arista.com/yang/experimental/eos">
        <eos>
            <mlag xmlns="urn:aristanetworks:yang:experimental:eos">
                <config>
                    <domain-id>MLAG-POD1</domain-id>
                    <dual-primary-action/>
                    <dual-primary-detection-delay>120</dual-primary-detection-delay>
                    <heartbeat-interval>4000</heartbeat-interval>
                    <heartbeat-peer-address>
                        <address>0.0.0.0</address>
                        <vrf/>
                    </heartbeat-peer-address>
                    <lacp-standby>true</lacp-standby>
                    <local-intf>Vlan4094</local-intf>
                    <peer-address>10.149.70.33</peer-address>
                    <peer-link-intf>Port-Channel1000</peer-link-intf>
                    <reload-delay>200</reload-delay>
                    <reload-delay-non-mlag>200</reload-delay-non-mlag>
                    <enabled>true</enabled>
                </config>
            </mlag>
        </eos>
    </arista>
</config>
'''

configuration = eos.edit_config(target = "running", config = conf, default_operation="merge")

print(configuration)

eos.close_session()
