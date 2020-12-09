from ncclient import manager

eos=manager.connect(host="hostname", port="22", timeout=30, username="admin", password="", hostkey_verify=False)

config = """
<config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="http://openconfig.net/yang/interfaces">
    <interface>
      <name>Ethernet4/1</name>
        <subinterfaces>
          <subinterface>
            <index>0</index>
            <ipv4 xmlns="http://openconfig.net/yang/interfaces/ip">
              <addresses>
              <address nc:operation="delete">
                <ip>172.168.14.2</ip>
              </address>
              </addresses>
            </ipv4>
          </subinterface>
        </subinterfaces>
    </interface>
  </interfaces>
</config>
"""

configuration = eos.edit_config(target="running", config=config, default_operation="none")
print(configuration)

eos.close_session()
