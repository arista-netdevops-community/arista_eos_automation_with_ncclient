from ncclient import manager
eos=manager.connect(host="10.83.28.221", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)

# Edit the running configuration with merge operation
# Small examples

cfg_domain_name = '''
<config>
    <system xmlns="http://openconfig.net/yang/system">
        <config>
            <domain-name>abc.xyz</domain-name>
        </config>
    </system>
</config>
'''
reply = eos.edit_config(target = "running", config = cfg_domain_name, default_operation="merge")

cfg_login_banner = '''
<config>
    <system xmlns="http://openconfig.net/yang/system">
        <config>
            <login-banner>Access to this swicth is stricly restticted to authorized persons only. Every activity on this system is monitored. </login-banner>
        </config>
    </system>
</config>
'''
reply = eos.edit_config(target = "running", config = cfg_login_banner, default_operation="merge")

cfg_hostname = '''
<config>
    <system xmlns="http://openconfig.net/yang/system">
        <config>
            <hostname>switch1</hostname>
        </config>
    </system>
</config>'''
reply = eos.edit_config(target = "running", config = cfg_hostname, default_operation="merge")

cfg_username = '''
<config>
  <system xmlns="http://openconfig.net/yang/system">
    <aaa>
      <authentication>
        <users>
          <user>
          <username>gnmi</username>
            <config>
              <username>gnmi</username>
              <password>gnmi123</password>
              <role>network-admin</role>
            </config>
          </user>
        </users>
      </authentication>
    </aaa>
  </system>
</config>
'''
reply = eos.edit_config(target = "running", config = cfg_username, default_operation="merge")

cfg_username = '''
<config>
  <system xmlns="http://openconfig.net/yang/system">
    <aaa>
      <authentication>
        <users>
          <user>
          <username>netconf</username>
            <config>
              <username>netconf</username>
              <password-hashed>$6$AqpRA4JEgazppO2A$M9Yg7bXVTvuWN/ht0Uf3j08rFsXLJPjEuE8kr.H85Mb1D9I7YMgUcEJoDDrGPtYC4yHOdC9il32MtPI8R916f1</password-hashed>
              <role>network-admin</role>
            </config>
          </user>
        </users>
      </authentication>
    </aaa>
  </system>
</config>
'''
reply = eos.edit_config(target = "running", config = cfg_username, default_operation="merge")

cfg_interface_ethernet3_description = '''
<config>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
            <name>Ethernet3</name>
            <config>
                <description>This is the best</description>
            </config>
        </interface>
    </interfaces>
</config>
'''
reply = eos.edit_config(target="running", config=cfg_interface_ethernet3_description, default_operation="merge")
reply = eos.edit_config(target="running", config=cfg_interface_ethernet3_description)

# Edit the running configuration with merge operation
# Larger example

cfg_system = '''
<config>
    <system xmlns="http://openconfig.net/yang/system">
        <config>
            <domain-name>abc.xyz</domain-name>
            <hostname>switch1</hostname>
        </config>
        <dns>
            <servers>
                <server>
                    <address>
                        8.8.8.8
                    </address>
                    <config>
                        <address>8.8.8.8</address>
                        <port>53</port>
                    </config>
                </server>
                <server>
                    <address>10.83.28.52</address>
                    <config>
                        <address>10.83.28.52</address>
                        <port>53</port>
                    </config>
                </server>
            </servers>
        </dns>
    </system>
</config>
'''
configuration = eos.edit_config(target = "running", config = cfg_system, default_operation="merge")
print(configuration)
print(configuration.ok)

system = '''
<system xmlns="http://openconfig.net/yang/system">
    <dns>
        <servers>
        </servers>
    </dns>
    <config>
        <domain-name>
        </domain-name>
        <hostname>
        </hostname>
    </config>
</system>
'''
system_conf = eos.get_config(source="running", filter=("subtree", system))
print (system_conf)

# Edit the running configuration with replace operation

cfg_interface_ethernet3_description = '''
<config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
            <name>Ethernet3/1</name>
            <config>
                <description nc:operation="replace">This is the new interface description</description>
            </config>
        </interface>
    </interfaces>
</config>
'''
reply = eos.edit_config(target="running", config=cfg_interface_ethernet3_description, default_operation="none")

# Edit the running configuration with delete operation
# Get first the running configuration to be sure to then delete existing configuration data

conf = '''
<system xmlns="http://arista.com/yang/openconfig/system/">
    <config>
        <domain-name>
        </domain-name>
    </config>
    <dns>
        <servers>
            <server>
            </server>
        </servers>
    </dns>
    <aaa>
        <authentication>
            <users>
                <user>
                    <username>
                    </username>
                </user>
            </users>
        </authentication>
    </aaa>
</system>
'''
eos.get_config(source="running", filter=("subtree", conf))

conf = '''
<config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    <system xmlns="http://arista.com/yang/openconfig/system/">
        <config>
            <domain-name operation="delete">abc.xyz</domain-name>
         </config>
        <dns>
            <servers>
                <server>
                    <address operation="delete">1.1.1.1</address>
                </server>
            </servers>
        </dns>
    </system>
</config>
'''
reply = eos.edit_config(target = "running", config = conf, default_operation="none")

conf = '''
<config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    <system xmlns="http://arista.com/yang/openconfig/system/">
        <aaa>
            <authentication>
                <users>
                    <user>
                        <username operation="delete">gnmi</username>
                    </user>
                </users>
            </authentication>
        </aaa>
    </system>
</config>
'''
reply = eos.edit_config(target = "running", config = conf, default_operation="none")
