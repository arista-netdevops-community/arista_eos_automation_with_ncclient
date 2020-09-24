from ncclient import manager
import xml.dom.minidom

eos=manager.connect(host="10.81.108.236", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

#########################################################################################
#                                                                                       #
#    This example will get the specificed IPv6 Access list configured on the switch     #
#                                                                                       #
#########################################################################################

acls = '''
<acl xmlns="http://openconfig.net/yang/acl">
	<acl-sets>
		<acl-set>
			<name>IPv6_ACL_NETCONF</name>
		</acl-set>
	</acl-sets>
</acl>'''

resp = eos.get_config(source="running", filter=("subtree", acls))

xml = xml.dom.minidom.parseString(str(resp))

xml_pretty_str = xml.toprettyxml()

print xml_pretty_str

eos.close_session()