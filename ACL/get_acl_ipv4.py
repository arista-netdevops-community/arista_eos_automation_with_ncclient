from ncclient import manager
import xml.dom.minidom

eos=manager.connect(host="10.85.128.125", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

#########################################################################################
#                                                                                       #
#    This example will get the specificed IPv4 Access list configured on the switch     #
#                                                                                       #
#########################################################################################

acls = '''
<acl xmlns="http://openconfig.net/yang/acl">
	<acl-sets>
		<acl-set>
			<name>IPv4_ACL_NETCONF</name>
		</acl-set>
	</acl-sets>
</acl>'''

resp = eos.get_config(source="running", filter=("subtree", acls))

xml = xml.dom.minidom.parseString(str(resp))

xml_pretty_str = xml.toprettyxml()

print xml_pretty_str

eos.close_session()


'''output example:

<?xml version="1.0" ?>
<rpc-reply message-id="urn:uuid:f9a169d1-c993-4a73-b768-fd3d9e50c033" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<data time-modified="2020-09-14T11:22:37.758981627Z">
		<acl xmlns="http://openconfig.net/yang/acl">
			<acl-sets>
				<acl-set>
					<name>IPv4_ACL_NETCONF</name>
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
									<hop-limit>5</hop-limit>
									<protocol>1</protocol>
									<source-address>10.10.10.2/32</source-address>
								</config>
							</ipv4>
							<transport>
								<config/>
							</transport>
						</acl-entry>
					</acl-entries>
					<config>
						<name>IPv4_ACL_NETCONF</name>
						<type>ACL_IPV4</type>
					</config>
				</acl-set>
			</acl-sets>
		</acl>
	</data>
</rpc-reply>
'''

