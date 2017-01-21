#!/usr/bin/python

import jcs

from lxml import etree
from junos import Junos_Configuration

ns = {
        'l2vpn': 'http://yang.juniper.net/yang/demo/l2vpn',
}

def main():
    root = Junos_Configuration

    change = ''

    local_site = root.xpath('l2vpn:l2vpn/l2vpn:global/l2vpn:local-site-identifier', namespaces=ns)[0].text
    rd_prefix = root.xpath('l2vpn:l2vpn/l2vpn:global/l2vpn:rd-prefix', namespaces=ns)[0].text
    rt_prefix = root.xpath('l2vpn:l2vpn/l2vpn:global/l2vpn:rt-prefix', namespaces=ns)[0].text
    interface = root.xpath('l2vpn:l2vpn/l2vpn:global/l2vpn:physical-interface', namespaces=ns)[0].text
    if root.find('l2vpn:l2vpn', namespaces=ns):
        change += '''
        <interfaces>
          <interface>
            <name>%s</name>
            <flexible-vlan-tagging/>
            <encapsulation>flexible-ethernet-services</encapsulation>
            <description>L2VPN interface</description>
          </interface>
        </interfaces>''' % (interface)

        for elem in root.xpath('l2vpn:l2vpn/l2vpn:customer', namespaces=ns):
            name = elem.xpath('./l2vpn:name', namespaces=ns)[0].text
            remote_site_id = elem.xpath('./l2vpn:remote-site-identifier', namespaces=ns)[0].text
            vlan_id = elem.xpath('./l2vpn:vlan-id', namespaces=ns)[0].text
            change += '''
            <interfaces>
              <interface>
                <name>%s</name>
                <unit>
                  <name>%s</name>
                  <description>%s</description>
                  <vlan-id>%s</vlan-id>
                  <encapsulation>vlan-ccc</encapsulation>
                  <family>
                    <ccc/>
                  </family>
                </unit>
              </interface>
            </interfaces>
            <routing-instances>
              <instance>
                <name>%s</name>
                <instance-type>l2vpn</instance-type>
                <interface>
                  <name>%s.%s</name>
                </interface>
                <route-distinguisher>
                  <rd-type>%s:%s</rd-type>
                </route-distinguisher>
                <vrf-target>
                  <community>target:%s:%s</community>
                </vrf-target>
                <protocols>
                  <l2vpn>
                    <encapsulation-type>ethernet-vlan</encapsulation-type>
                    <no-control-word/>
                    <site>
                      <name>l2vpn-site-%s</name>
                      <site-identifier>%s</site-identifier>
                      <interface>
                        <name>%s.%s</name>
                        <remote-site-id>%s</remote-site-id>
                      </interface>
                    </site>
                  </l2vpn>
                </protocols>
              </instance>
            </routing-instances>''' % (interface, vlan_id, name, vlan_id, name,
                    interface, vlan_id, rd_prefix, vlan_id,
                    rt_prefix, vlan_id, vlan_id, local_site,
                    interface, vlan_id, remote_site_id)

    jcs.emit_warning('Custom L2VPN YANG model processing')
    jcs.emit_change(change, 'transient-change', 'xml')

if __name__ == '__main__':
    main()
