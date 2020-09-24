from ncclient import manager
eos=manager.connect(host="10.81.117.80", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

#######################################################################################
#                                                                                     #
#    This example will configure the following ipv4 prefix lists                      #
#                                                                                     #
#      ip prefix-list CUST1-ROUTE seq 10 permit 10.252.242.0/30 ge 30                 #
#      ip prefix-list CUST1-ROUTE seq 20 permit 17.160.72.0/25                        #
#                                                                                     #
#######################################################################################

ipv4_prefix = '''
<config>
    <routing-policy xmlns="http://openconfig.net/yang/routing-policy">
        <defined-sets>
            <prefix-sets>
                <prefix-set>
                    <name>CUST1-ROUTE</name>
                    <config>
                        <name>CUST1-ROUTE</name>
                    </config>
                    <prefixes>
                        <prefix>
                            <ip-prefix>10.252.242.0/30</ip-prefix>
                            <masklength-range>30..32</masklength-range>
                            <config>
                                <ip-prefix>10.252.242.0/30</ip-prefix>
                                <masklength-range>30..32</masklength-range>
                            </config>
                        </prefix>
                        <prefix>
                            <ip-prefix>17.160.72.0/25</ip-prefix>
                            <masklength-range>25..25</masklength-range>
                            <config>
                                <ip-prefix>17.160.72.0/25</ip-prefix>
                                <masklength-range>25..25</masklength-range>
                            </config>
                        </prefix>
                    </prefixes>
                </prefix-set>
            </prefix-sets>
        </defined-sets>
    </routing-policy>
</config>
'''

#######################################################################################
#                                                                                     #
#    This example will configure the following route-map                              #
#                                                                                     #
#      route-map DC1-CUST1-MAP1 statement 10 permit 10                                #
#        match ip address prefix-list CUST1-ROUTE                                     #
#        set as-path prepend 397269 397269                                            #
#                                                                                     #
#######################################################################################

route_map = '''
<config>
    <routing-policy xmlns="http://openconfig.net/yang/routing-policy">
        <policy-definitions>
            <policy-definition>
                <name>DC1-CUST1-MAP1</name>
                <config>
                    <name>DC1-CUST1-MAP1</name>
                </config>
                <statements>
                    <statement>
                        <name>10</name>
                        <actions>
                            <bgp-actions xmlns="http://openconfig.net/yang/bgp-policy">
                                <set-as-path-prepend>
                                    <config>
                                        <asn>397269</asn>
                                        <repeat-n>2</repeat-n>
                                    </config>
                                </set-as-path-prepend>
                            </bgp-actions>
                            <config>
                                <policy-result>ACCEPT_ROUTE</policy-result>
                            </config>
                        </actions>
                        <conditions>
                            <match-prefix-set>
                                <config>
                                    <match-set-options>ANY</match-set-options>
                                    <prefix-set>CUST1-ROUTE</prefix-set>
                                </config>
                            </match-prefix-set>
                        </conditions>
                        <config>
                            <name>10</name>
                        </config>
                    </statement>
                </statements>
            </policy-definition>
        </policy-definitions>
    </routing-policy>
</config>
'''

#######################################################################################
#                                                                                     #
#    This example will configure the following QoS policy map                         #
#                                                                                     #
#       ip access-list ACL-IT-VOIP                                                    #
#          10 permit ip 198.19.1.0/24 any                                             #
#          20 permit ip 198.19.2.0/24 any                                             #
#          30 permit ip 198.19.3.0/24 any                                             #
#       !                                                                             #
#       class-map type qos match-any CLASS-IT-VOIP                                    #
#          match ip access-group ACL-IT-VOIP                                          #
#       !                                                                             #
#       policy-map type quality-of-service PMAP-IT-VOIP                               #
#          class CLASS-IT-VOIP                                                        #
#               police cir 18000 bps bc 300 bytes                                     #
#          !                                                                          #
#          class class-default                                                        #
#                                                                                     #
#######################################################################################

arista_qos = '''
<config>
    <acl xmlns="http://openconfig.net/yang/acl">
        <acl-sets>
            <acl-set>
                <name>ACL-IT-VOIP</name>
                <type>ACL_IPV4</type>
                <acl-entries>
                    <acl-entry>
                        <sequence-id>10</sequence-id>
                        <actions>
                            <config>
                                <forwarding-action>ACCEPT</forwarding-action>
                                <log-action>LOG_NONE</log-action>
                            </config>
                        </actions>
                        <config>
                            <sequence-id>10</sequence-id>
                        </config>
                        <ipv4>
                            <config>
                                <destination-address>0.0.0.0/0</destination-address>
                                <source-address>198.19.1.0/24</source-address>
                            </config>
                        </ipv4>
                    </acl-entry>
                    <acl-entry>
                        <sequence-id>20</sequence-id>
                        <actions>
                            <config>
                                <forwarding-action>ACCEPT</forwarding-action>
                                <log-action>LOG_NONE</log-action>
                            </config>
                        </actions>
                        <config>
                            <sequence-id>20</sequence-id>
                        </config>
                        <ipv4>
                            <config>
                                <destination-address>0.0.0.0/0</destination-address>
                                <source-address>198.19.2.0/24</source-address>
                            </config>
                        </ipv4>
                    </acl-entry>
                    <acl-entry>
                        <sequence-id>30</sequence-id>
                        <actions>
                            <config>
                                <forwarding-action>ACCEPT</forwarding-action>
                                <log-action>LOG_NONE</log-action>
                            </config>
                        </actions>
                        <config>
                            <sequence-id>30</sequence-id>
                        </config>
                        <ipv4>
                            <config>
                                <destination-address>0.0.0.0/0</destination-address>
                                <source-address>198.19.3.0/24</source-address>
                            </config>
                        </ipv4>
                    </acl-entry>
                </acl-entries>
                <config>
                    <name>ACL-IT-VOIP</name>
                    <type>ACL_IPV4</type>
                </config>
            </acl-set>
        </acl-sets>
    </acl>

    <arista xmlns="http://arista.com/yang/experimental/eos">
        <eos>
            <qos xmlns="http://arista.com/yang/experimental/eos/qos">
                <acl xmlns="http://arista.com/yang/experimental/eos/qos/acl">
                    <input>
                        <cli>
                            <cmapType>
                                <type>mapQos</type>
                                <cmap>
                                    <name>CLASS-IT-VOIP</name>
                                    <match>
                                        <option>matchIpAccessGroup</option>
                                        <strValue>ACL-IT-VOIP</strValue>
                                    </match>
                                    <matchCondition>matchConditionAny</matchCondition>
                                </cmap>
                            </cmapType>
                        </cli>
                    </input>
                </acl>
            </qos>
        </eos>
    </arista>

    <arista xmlns="http://arista.com/yang/experimental/eos">
        <eos>
            <qos xmlns="http://arista.com/yang/experimental/eos/qos">
                <acl xmlns="http://arista.com/yang/experimental/eos/qos/acl">
                    <input>
                        <cli>
                            <pmapType>
                                <type>mapQos</type>
                                <pmap>
                                    <name>PMAP-IT-VOIP</name>
                                    <classAction>
                                        <name>CLASS-IT-VOIP</name>
                                        <policer>
                                            <bc>300</bc>
                                            <bcUnit>burstUnitBytes</bcUnit>
                                            <cir>18000</cir>
                                            <cirUnit>rateUnitbps</cirUnit>
                                            <redActions>
                                                <actionType>actionSetDrop</actionType>
                                            </redActions>
                                        </policer>
                                    </classAction>
                                </pmap>
                            </pmapType>
                        </cli>
                    </input>
                </acl>
            </qos>
        </eos>
    </arista>
</config>
'''

configuration = eos.edit_config(target = "running", config = arista_qos, default_operation="merge")
print(configuration)

eos.close_session()
