from ncclient import manager

eos = manager.connect(host="10.83.28.190", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)

# list all schemas supported on the netconf server using the get operation (RFC 6022)
subtree='''
<netconf-state>
        <schemas>
        </schemas>
</netconf-state>
'''
subtree='''
<netconf-state xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring">
    <schemas>
    </schemas>
</netconf-state>
'''
get_reply = eos.get(filter=("subtree", subtree))
print(get_reply.ok)
# print(get_reply)

# retrieve a schema from the NETCONF server via get_schema operation (RFC 6022)
get_schema_reply = eos.get_schema(identifier = "arista-vlan-deviations", version = "2019-11-13", format = 'yang')
print(get_schema_reply.ok)
# print(get_schema_reply)

# retrieve the data model defined here https://datatracker.ietf.org/doc/html/rfc6022#section-5
get_schema_reply = eos.get_schema(identifier = "ietf-netconf-monitoring", version = "2010-10-04", format = 'yang')
print(get_schema_reply.ok)
# print(get_schema_reply)

# rfc6022 - list of datastores supported on this device
subtree='''
<netconf-state>
    <datastores>
    </datastores>
</netconf-state>
'''
get_reply = eos.get(filter=("subtree", subtree))
print(get_reply.ok)
# print(get_reply)


