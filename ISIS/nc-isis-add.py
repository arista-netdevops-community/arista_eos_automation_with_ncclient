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
      <enabled>
       true
      </enabled>
      <identifier>
       oc-pol-types:ISIS
      </identifier>
      <name>
       SUPERCORE
      </name>
     </config>
     <isis>
      <global>
        <config>
          <instance>SUPERCORE</instance>
        </config>
      </global>
      <interfaces>
       <interface>
        <interface-id>
         Ethernet4/1
        </interface-id>
        <config>
         <circuit-type>
          POINT_TO_POINT
         </circuit-type>
         <enabled>
          true
         </enabled>
         <hello-padding>
          STRICT
         </hello-padding>
         <interface-id>
          Ethernet4/1
         </interface-id>
         <passive>
          false
         </passive>
        </config>
        <interface-ref>
         <config>
          <interface>
           Ethernet4/1
          </interface>
         </config>
        </interface-ref>
        <levels>
         <level>
          <level-number>
           1
          </level-number>
          <afi-safi>
           <af>
            <afi-name>
             oc-isis-types:IPV4
            </afi-name>
            <safi-name>
             oc-isis-types:UNICAST
            </safi-name>
            <config>
             <afi-name>
              oc-isis-types:IPV4
             </afi-name>
             <metric>
              10
             </metric>
             <safi-name>
              oc-isis-types:UNICAST
             </safi-name>
            </config>
           </af>
           <af>
            <afi-name>
             oc-isis-types:IPV6
            </afi-name>
            <safi-name>
             oc-isis-types:UNICAST
            </safi-name>
            <config>
             <afi-name>
              oc-isis-types:IPV6
             </afi-name>
             <metric>
              GLOBAL_METRIC
             </metric>
             <safi-name>
              oc-isis-types:UNICAST
             </safi-name>
            </config>
           </af>
          </afi-safi>
          <config>
           <enabled>
            false
           </enabled>
           <level-number>
            1
           </level-number>
           <priority>
            64
           </priority>
          </config>
          <hello-authentication>
           <config>
            <hello-authentication>
             false
            </hello-authentication>
           </config>
           <key>
            <config/>
           </key>
          </hello-authentication>
          <packet-counters>
           <csnp/>
           <iih/>
           <lsp/>
           <psnp/>
          </packet-counters>
          <timers>
           <config>
            <hello-interval>
             10
            </hello-interval>
            <hello-multiplier>
             3
            </hello-multiplier>
           </config>
          </timers>
         </level>
         <level>
          <level-number>
           2
          </level-number>
          <afi-safi>
           <af>
            <afi-name>
             oc-isis-types:IPV4
            </afi-name>
            <safi-name>
             oc-isis-types:UNICAST
            </safi-name>
            <config>
             <afi-name>
              oc-isis-types:IPV4
             </afi-name>
             <metric>
              10
             </metric>
             <safi-name>
              oc-isis-types:UNICAST
             </safi-name>
            </config>
           </af>
           <af>
            <afi-name>
             oc-isis-types:IPV6
            </afi-name>
            <safi-name>
             oc-isis-types:UNICAST
            </safi-name>
            <config>
             <afi-name>
              oc-isis-types:IPV6
             </afi-name>
             <metric>
              GLOBAL_METRIC
             </metric>
             <safi-name>
              oc-isis-types:UNICAST
             </safi-name>
            </config>
           </af>
          </afi-safi>
          <config>
           <enabled>
            true
           </enabled>
           <level-number>
            2
           </level-number>
           <priority>
            64
           </priority>
          </config>
          <hello-authentication>
           <config>
            <hello-authentication>
             false
            </hello-authentication>
           </config>
           <key>
            <config/>
           </key>
          </hello-authentication>
          <packet-counters>
           <csnp/>
           <iih/>
           <lsp/>
           <psnp/>
          </packet-counters>
          <timers>
           <config>
            <hello-interval>
             10
            </hello-interval>
            <hello-multiplier>
             3
            </hello-multiplier>
           </config>
          </timers>
         </level>
        </levels>
       </interface>
      </interfaces>
     </isis>
    </protocol>
   </protocols>
  </network-instance>
 </network-instances>
</config>
"""

configuration = eos.edit_config(target="running", config=isis, default_operation="merge")
print(configuration)

eos.close_session()
