# print server capabilities 

from ncclient import manager

eos=manager.connect(host="10.83.28.203", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)

for item in eos.server_capabilities: 
    print (item)

# check if the server advertised some NetConf capabilities
assert("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring" in eos.server_capabilities), "NetConf server not compliant with https://tools.ietf.org/html/rfc6022"

eos.close_session()


 <rpc message-id="101"
          xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
       <get>
         <filter type="subtree">
           <top xmlns="http://example.com/schema/1.2/stats">
             <interfaces>
               <interface>
                 <ifName>eth0</ifName>
               </interface>
             </interfaces>
           </top>
         </filter>
       </get>
     </rpc>
     