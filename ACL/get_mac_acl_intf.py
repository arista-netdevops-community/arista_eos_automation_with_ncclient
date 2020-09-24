from ncclient import manager
import xml.dom.minidom
eos=manager.connect(host="10.85.128.125", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

#########################################################################################
#                                                                                       #
#    This example will get the  MAC Access list        			                        #
#    configured on an L2 interface of the switch                                        #
#                                                                                       #
#########################################################################################

acls = '''
<acl xmlns="http://arista.com/yang/openconfig/acl">
    <interfaces>
        <interface>
                <id>Ethernet1/1</id>
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

output:

<?xml version="1.0" ?>
<rpc-reply message-id="urn:uuid:71cf4316-9cd2-4bf7-ad44-1a1d96fd32ee" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<data time-modified="2020-09-17T04:54:25.652913248Z">
		<acl xmlns="http://openconfig.net/yang/acl">
			<interfaces>
				<interface>
					<id>Ethernet1/1</id>
					<config>
						<id>Ethernet1/1</id>
					</config>
					<ingress-acl-sets>
						<ingress-acl-set>
							<set-name>MAC_ACL_NETCONF</set-name>
							<type>ACL_L2</type>
							<config>
								<set-name>MAC_ACL_NETCONF</set-name>
								<type>ACL_L2</type>
							</config>
						</ingress-acl-set>
					</ingress-acl-sets>
					<interface-ref>
						<config>
							<interface>Ethernet1/1</interface>
							<subinterface>0</subinterface>
						</config>
					</interface-ref>
				</interface>
			</interfaces>
		</acl>
	</data>
</rpc-reply>

'''