from ncclient import manager

eos=manager.connect(host="hostname", port="22", timeout=30, username="admin", password="", hostkey_verify=False)

isis = """
<config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
   <network-instances xmlns="http://openconfig.net/yang/network-instance"
      xmlns:oc-pol-types="http://openconfig.net/yang/policy-types"
      xmlns:oc-isis-types="http://openconfig.net/yang/isis-types"
      >
  <network-instance>
   <name>
    default
   </name>
   <protocols>
    <protocol>
     <identifier>
      oc-pol-types:ISIS
     </identifier>
     <name>
      SUPERCORE
     </name>
     <config>
     <identifier>
       oc-pol-types:ISIS
      </identifier>
      <name>
       SUPERCORE
      </name>
     </config>
     <isis>
      <interfaces>
      <interface nc:operation="delete">
        <interface-id>
         Ethernet4/1
        </interface-id>
        <config>
         <interface-id>
          Ethernet4/1
         </interface-id>
        </config>
       </interface>
      </interfaces>
     </isis>
    </protocol>
   </protocols>
  </network-instance>
 </network-instances>
</config>
"""

configuration = eos.edit_config(target="running", config=isis, default_operation="none")
print(configuration)

eos.close_session()
