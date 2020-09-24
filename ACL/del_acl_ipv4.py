from ncclient import manager
eos=manager.connect(host="10.81.108.236", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

############################################################################################
#                                                                                          #
#    This example will delete the specificed IPv4 Access list configured on the switch     #
#                                                                                          #
############################################################################################

conf = '''
<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
    <acl xmlns="http://arista.com/yang/openconfig/acl">
        <acl-sets>
            <acl-set xc:operation="delete">
                <name>IPv4_ACL_NETCONF</name>
                <type>ACL_IPV4</type>
            </acl-set>
        </acl-sets>
    </acl>
</config>
'''

configuration = eos.edit_config(target = "running", config = conf, default_operation="merge")
print(configuration)

eos.close_session()
