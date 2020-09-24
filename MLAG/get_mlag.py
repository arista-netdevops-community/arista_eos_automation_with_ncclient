from ncclient import manager
import xml.dom.minidom
eos=manager.connect(host="10.85.128.81", port="22", timeout=30, username="cvpadmin", password="arista", hostkey_verify=False)

#########################################################################################
#                                                                                       #
#    This example will get the  MLAG configuration        			                    #
#                                                                                       #
#########################################################################################

mlag = '''
<arista xmlns="http://arista.com/yang/experimental/eos">
    <eos>
        <mlag></mlag>
    </eos>
</arista> 
'''

resp = eos.get_config(source="running", filter=("subtree", mlag))

xml = xml.dom.minidom.parseString(str(resp))

xml_pretty_str = xml.toprettyxml()

print xml_pretty_str

eos.close_session()