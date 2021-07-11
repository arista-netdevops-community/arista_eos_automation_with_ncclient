```
s70515#sh version
Arista DCS-7050CX3-32S-F
Hardware version: 11.00
Serial number: JPE18501766
Hardware MAC address: 985d.82b4.ddf9
System MAC address: 985d.82b4.ddf9

Software image version: 4.26.1F
Architecture: i686
Internal build version: 4.26.1F-22602519.4261F
Internal build ID: 7715db93-0f94-4fec-b19f-3625f4e73eba
Image format version: 01.00

Uptime: 0 weeks, 0 days, 15 hours and 48 minutes
Total memory: 8099008 kB
Free memory: 6214560 kB
```
```
s70515#sh management api netconf
Enabled:                 Yes
Server:                  running on port 830, in default VRF
```
Start a NETCONF over SSH session
```
s70515#netconf start-client
```
Once the NETCONF session is open, the NETCONF server (EOS device) advertises its capabilities.

You must advertise the client capabilities. Example:
```
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <capabilities>
        <capability>urn:ietf:params:netconf:base:1.0</capability>
        <capability>urn:ietf:params:netconf:capability:candidate:1.0</capability>
        <capability>urn:ietf:params:netconf:capability:confimed-commit:1.0</capability>
        <capability>urn:ietf:params:netconf:capability:writable-running:1.0</capability>
        <capability>urn:ietf:params:netconf:capability:validate:1.0</capability>
    </capabilities>
</hello>
]]>]]>
```
Get all configuration and state data
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
  <get>
  </get>
</rpc>
]]>]]>
```
Get the operational status of an Interface
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="2">
  <get>
    <filter type="subtree">
        <interfaces>
            <interface>
                <name>Ethernet3</name>
                <state>
                    <oper-status>
                    </oper-status>
                </state>
            </interface>
        </interfaces>
    </filter>
  </get>
</rpc>
]]>]]>
```
Get the whole running configuration
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="3">
  <get-config>
    <source>
        <running/>
    </source>
  </get-config>
</rpc>
]]>]]>
```
Get the running configuration of an interface
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="4">
  <get-config>
    <source>
        <running/>
    </source>
    <filter>
        <interfaces>
            <interface>
                <name>Ethernet3</name>
            </interface>
        </interfaces>
    </filter>
  </get-config>
</rpc>
]]>]]>
```
Get the interface description from the running configuration
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="5">
  <get-config>
    <source>
        <running/>
    </source>
    <filter>
        <interfaces>
            <interface>
                <name>Ethernet3</name>
                <config>
                    <description>
                    </description>
                </config>
            </interface>
        </interfaces>
    </filter>
  </get-config>
</rpc>
]]>]]>
```
Lock the running configuration
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="6">
  <lock>
    <target>
      <running/>
    </target>
  </lock>
</rpc>
]]>]]>
```
Edit the running configuration using EOS native data model
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="7">
<edit-config>
    <target>
      <running/>
    </target>
    <default-operation>merge</default-operation>
    <commands>
       <command>vlan 198</command>
       <command>name test198</command>
       <command>interface ethernet6</command>
       <command>description test</command>
       <command>switchport access vlan 98</command>
    </commands>
</edit-config>
</rpc>
]]>]]>
```
Edit the running configuration using OpenConfig data model
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="8">
<edit-config>
    <target>
        <running/>
    </target>
    <default-operation>merge</default-operation>
    <config>
        <interfaces>
            <interface>
                <name>Ethernet4</name>
                <config>
                    <description>This is the best interface</description>
                </config>
            </interface>
        </interfaces>
     </config>
  </edit-config>
</rpc>
]]>]]>
```
Edit the running configuration to delete an existing existing data
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="9">
<edit-config>
    <target>
        <running/>
    </target>
    <default-operation>none</default-operation>
    <config>
        <system xmlns="http://arista.com/yang/openconfig/system/">
            <dns>
                <servers>
                    <server>
                        <address operation="delete">1.1.1.1</address>
                    </server>
                </servers>
            </dns>
        </system>
    </config>
</edit-config>
</rpc>
]]>]]>
```
Unlock the running configuration
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="10">
  <unlock>
    <target>
      <running/>
    </target>
  </unlock>
</rpc>
]]>]]>
```
Save running configuration on the flash
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="11">
  <copy-config>
    <target>
      <url>
        flash:/test.cfg
      </url>
    </target>
    <source>
      <running/>
    </source>
  </copy-config>
</rpc>
]]>]]>
```
Copy the running configuration datastore to the startup configuration datastore
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="12">
    <copy-config>
        <target>
            <startup/>
         </target>
         <source>
           <running/>
         </source>
    </copy-config>
</rpc>
]]>]]>
```
Lock the candidate configuration
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="13">
  <lock>
    <target>
      <candidate/>
    </target>
  </lock>
</rpc>
]]>]]>
```
Edit the candidate configuration
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="14">
<edit-config>
    <target>
        <candidate/>
    </target>
    <default-operation>merge</default-operation>
    <config>
        <interfaces>
            <interface>
                <name>Ethernet5/1</name>
                <config>
                    <description>This is the best interface</description>
                </config>
            </interface>
        </interfaces>
     </config>
  </edit-config>
</rpc>
]]>]]>
```
Commit the configuration change (from the candidate to the running configuration)
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="15">
    <commit/>
</rpc>
]]>]]>
```
Unlock the candidate configuration
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="20">
  <unlock>
    <target>
      <candidate/>
    </target>
  </unlock>
</rpc>
]]>]]>
```
Edit the candidate configuration
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="21">
<edit-config>
    <target>
        <candidate/>
    </target>
    <default-operation>merge</default-operation>
    <config>
        <system>
            <config>
                <hostname>test</hostname>
            </config>
        </system>
     </config>
  </edit-config>
</rpc>
]]>]]>
```
Get part of the candidate configuration
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="5">
  <get-config>
    <source>
        <candidate/>
    </source>
    <filter>
        <system>
            <config>
                <hostname></hostname>
            </config>
        </system>
    </filter>
  </get-config>
</rpc>
]]>]]>
```
If you decide to not commit the candidate configuration, you can revert the candidate configuration to the current running configuration
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="90">
  <discard-changes/>
</rpc>
]]>]]>
```
Close the session
```
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="100">
    <close-session>
    </close-session>
</rpc>
]]>]]>
```