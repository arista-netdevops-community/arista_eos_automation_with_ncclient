from ncclient import manager
import xml.dom.minidom

eos=manager.connect(host="10.85.128.125", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

#########################################################################################
#                                                                                       #
#    This example will get the specificed MAC Access list configured on the switch      #
#                                                                                       #
#########################################################################################

acls = '''
<acl xmlns="http://openconfig.net/yang/acl">
	<acl-sets>
		<acl-set>
			<name>MAC_ACL_NETCONF</name>
		</acl-set>
	</acl-sets>
</acl>'''

resp = eos.get_config(source="running", filter=("subtree", acls))

xml = xml.dom.minidom.parseString(str(resp))

xml_pretty_str = xml.toprettyxml()

print xml_pretty_str

eos.close_session()

'''
<?xml version="1.0" ?>
<rpc-reply message-id="urn:uuid:cceb3b29-0f05-4076-b220-0d74b53c4a56" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<data time-modified="2020-09-17T04:44:57.491545531Z">
		<acl xmlns="http://openconfig.net/yang/acl">
			<acl-sets>
				<acl-set>
					<name>MAC_ACL_NETCONF</name>
					<type>ACL_L2</type>
					<acl-entries>
						<acl-entry>
							<sequence-id>10</sequence-id>
							<actions>
								<config>
									<forwarding-action>ACCEPT</forwarding-action>
									<log-action>LOG_SYSLOG</log-action>
								</config>
							</actions>
							<config>
								<sequence-id>10</sequence-id>
							</config>
							<l2>
								<config>
									<destination-mac>00:1c:73:7a:40:91</destination-mac>
									<destination-mac-mask>ff:ff:ff:ff:ff:ff</destination-mac-mask>
									<ethertype>2054</ethertype>
									<source-mac>00:1c:73:7a:40:d2</source-mac>
									<source-mac-mask>ff:ff:ff:ff:ff:ff</source-mac-mask>
								</config>
							</l2>
						</acl-entry>
					</acl-entries>
					<config>
						<name>MAC_ACL_NETCONF</name>
						<type>ACL_L2</type>
					</config>
				</acl-set>
			</acl-sets>
		</acl>
	</data>
</rpc-reply>
'''