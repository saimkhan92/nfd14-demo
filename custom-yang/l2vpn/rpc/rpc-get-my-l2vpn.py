from jnpr.junos import Device

def main():
  l_dev = Device(host='custom-yang-pe-a', user='user-name-for-this-dev', password='password', gather_facts=False)
  l_dev.open()

  l_rsp = l_dev.rpc.get_l2vpn_connection_information()

  print "<my-l2vpn>"

  for inst in l_rsp.iter("instance"):
    l_inst_name = inst.findtext("instance-name")
    for l_cid in inst.iter("connection"):
      r_pe = l_cid.findtext("remote-pe")
      l_con_id = l_cid.findtext("connection-id")
      l_con_type = l_cid.findtext("connection-type")
      l_con_status = l_cid.findtext("connection-status")
      l_i_label = l_cid.findtext("inbound-label")
      l_o_label = l_cid.findtext("outbound-label")

      r_dev = Device(host=r_pe, user='user-name-for-remote-dev', password='password', gather_facts=False)
      r_dev.open()

      r_rsp = r_dev.rpc.get_l2vpn_connection_information()
      for r_inst in r_rsp.iter("instance"):
        r_inst_name = r_inst.findtext("instance-name")
        if (l_inst_name == r_inst_name):
          for r_cid in r_inst.iter("connection"):
            r_con_id = r_cid.findtext("connection-id")
            r_con_type = r_cid.findtext("connection-type")
            r_con_status = r_cid.findtext("connection-status")
            r_i_label = r_cid.findtext("inbound-label")
            r_o_label = r_cid.findtext("outbound-label")

           
            print ("<instance-name>" + l_inst_name + "</instance-name>")  
            print ("<local-connection-id>" + l_con_id + "</local-connection-id>")
            print ("<remote-connection-id>" + r_con_id + "</remote-connection-id>")

            print ("<local-connection-type>" + l_con_type + "</local-connection-type>")
            print ("<remote-connection-type>" + r_con_type + "</remote-connection-type>")

            print ("<local-connection-status>" + l_con_status + "</local-connection-status>")
            print ("<remote-connection-status>" + r_con_status + "</remote-connection-status>")

            print ("<local-inbound-label>" + l_i_label + "</local-inbound-label>")
            print ("<remote-inbound-label>" + r_i_label + "</remote-inbound-label>")

            print ("<local-outbound-label>" + l_o_label + "</local-outbound-label>")
            print ("<remote-outbound-label>" + r_o_label + "</remote-outbound-label>")
        
      r_dev.close()
  l_dev.close()
  print "</my-l2vpn>"

if __name__ == '__main__':
  main()
