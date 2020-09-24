from ncclient import manager
import xml.dom.minidom
eos=manager.connect(host="10.85.128.125", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

#########################################################################################
#                                                                                       #
#    This example will get the  IPv6 Access list                                        #
#    configured on an L3 interface of the switch                                        #
#                                                                                       #
#########################################################################################

acls = '''
<acl xmlns="http://arista.com/yang/openconfig/acl">
    <interfaces>
        <interface>
                <id>Ethernet2/1</id>
        </interface>
    </interfaces>
</acl>
'''

resp = eos.get_config(source="running", filter=("subtree", acls))

xml = xml.dom.minidom.parseString(str(resp))

xml_pretty_str = xml.toprettyxml()

print xml_pretty_str

eos.close_session()
