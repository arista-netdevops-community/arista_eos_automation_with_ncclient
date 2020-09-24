from ncclient import manager
import xml.dom.minidom
eos=manager.connect(host="10.85.128.125", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

#########################################################################################
#                                                                                       #
#    This example will get the IPv4 Access list       			                        #
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


'''
output sample:

<?xml version="1.0" ?>
<rpc-reply message-id="urn:uuid:fe3a88c9-f3ac-441f-b1a6-8d38a62d19f8" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<data time-modified="2020-09-17T04:21:40.249639256Z">
		<acl xmlns="http://openconfig.net/yang/acl">
			<interfaces>
				<interface>
					<id>Ethernet2/1</id>
					<config>
						<id>Ethernet2/1</id>
					</config>
					<egress-acl-sets>
						<egress-acl-set>
							<set-name>IPv4_ACL_NETCONF_EGRESS</set-name>
							<type>ACL_IPV4</type>
							<config>
								<set-name>IPv4_ACL_NETCONF_EGRESS</set-name>
								<type>ACL_IPV4</type>
							</config>
						</egress-acl-set>
					</egress-acl-sets>
					<ingress-acl-sets>
						<ingress-acl-set>
							<set-name>IPv4_ACL_NETCONF_INGRESS</set-name>
							<type>ACL_IPV4</type>
							<config>
								<set-name>IPv4_ACL_NETCONF_INGRESS</set-name>
								<type>ACL_IPV4</type>
							</config>
						</ingress-acl-set>
					</ingress-acl-sets>
					<interface-ref>
						<config>
							<interface>Ethernet2/1</interface>
							<subinterface>0</subinterface>
						</config>
					</interface-ref>
				</interface>
			</interfaces>
		</acl>
	</data>
</rpc-reply>

'''
