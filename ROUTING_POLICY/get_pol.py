from ncclient import manager
import xml.dom.minidom

eos=manager.connect(host="10.81.108.236", port="22", timeout=30, username="cvpadmin", password="arastra", hostkey_verify=False)

###################################################################################################
#                                                                                                 #
#    This example will get the specificed prefix-list and route-map configured on the switch      #
#                                                                                                 #
###################################################################################################

prefix = '''
<routing-policy xmlns="http://openconfig.net/yang/routing-policy">
    <defined-sets>
        <prefix-sets>
            <prefix-set>
                <name>CUST1-ROUTE</name>
            </prefix-set>
        </prefix-sets>
    </defined-sets>
</routing-policy>
'''

route_map = '''
<routing-policy xmlns="http://openconfig.net/yang/routing-policy">
    <policy-definitions>
        <policy-definition>
            <name>DC1-CUST1-MAP1</name>
        </policy-definition>
    </policy-definitions>
</routing-policy>
'''

get_class_map = '''
<arista>
    <eos>
        <qos>
            <acl>
                <input>
                    <cli>
                        <cmapType>
                            <type>mapQos</type>
                            <cmap>
                                <name>CLASS-IT-VOIP</name>
                            </cmap>
                        </cmapType>
                    </cli>
                </input>
            </acl>
        </qos>
    </eos>
</arista>
'''

get_policy_map = '''
<arista>
    <eos>
        <qos>
            <acl>
                <input>
                    <cli>
                        <pmapType>
                            <type>mapQos</type>
                            <pmap>
                                <name>PMAP-IT-VOIP</name>
                            </pmap>
                        </pmapType>
                    </cli>
                </input>
            </acl>
        </qos>
    </eos>
</arista>
'''

resp = eos.get_config(source="running", filter=("subtree", get_policy_map))

xml = xml.dom.minidom.parseString(str(resp))

xml_pretty_str = xml.toprettyxml()

print xml_pretty_str

eos.close_session()