#!/usr/bin/python
#
# NETCAP - Traffic Analysis Framework
# Copyright (c) 2017 Philipp Mieden <dreadl0ck [at] protonmail [dot] ch>
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

import netcap_pb2 as netcap

types = {
    netcap.Header.__name__: netcap.Header(),
    netcap.Batch.__name__: netcap.Batch(),
    netcap.Flow.__name__: netcap.Flow(),
    netcap.Connection.__name__: netcap.Connection(),
    netcap.LinkFlow.__name__: netcap.LinkFlow(),
    netcap.NetworkFlow.__name__: netcap.NetworkFlow(),
    netcap.TransportFlow.__name__: netcap.TransportFlow(),
    netcap.Ethernet.__name__: netcap.Ethernet(),
    netcap.ARP.__name__: netcap.ARP(),
    netcap.Dot1Q.__name__: netcap.Dot1Q(),
    netcap.Dot11.__name__: netcap.Dot11(),
    netcap.Dot11QOS.__name__: netcap.Dot11QOS(),
    netcap.Dot11HTControl.__name__: netcap.Dot11HTControl(),
    netcap.Dot11HTControlVHT.__name__: netcap.Dot11HTControlVHT(),
    netcap.Dot11HTControlHT.__name__: netcap.Dot11HTControlHT(),
    netcap.Dot11HTControlMFB.__name__: netcap.Dot11HTControlMFB(),
    netcap.Dot11LinkAdapationControl.__name__: netcap.Dot11LinkAdapationControl(),
    netcap.Dot11ASEL.__name__: netcap.Dot11ASEL(),
    netcap.LinkLayerDiscovery.__name__: netcap.LinkLayerDiscovery(),
    netcap.LLDPChassisID.__name__: netcap.LLDPChassisID(),
    netcap.LLDPPortID.__name__: netcap.LLDPPortID(),
    netcap.LinkLayerDiscoveryValue.__name__: netcap.LinkLayerDiscoveryValue(),
    netcap.EthernetCTP.__name__: netcap.EthernetCTP(),
    netcap.EthernetCTPReply.__name__: netcap.EthernetCTPReply(),
    netcap.LinkLayerDiscoveryInfo.__name__: netcap.LinkLayerDiscoveryInfo(),
    netcap.LLDPSysCapabilities.__name__: netcap.LLDPSysCapabilities(),
    netcap.LLDPCapabilities.__name__: netcap.LLDPCapabilities(),
    netcap.LLDPMgmtAddress.__name__: netcap.LLDPMgmtAddress(),
    netcap.LLDPOrgSpecificTLV.__name__: netcap.LLDPOrgSpecificTLV(),
    netcap.IPv4.__name__: netcap.IPv4(),
    netcap.IPv4Option.__name__: netcap.IPv4Option(),
    netcap.IPv6.__name__: netcap.IPv6(),
    netcap.ICMPv4.__name__: netcap.ICMPv4(),
    netcap.ICMPv6.__name__: netcap.ICMPv6(),
    netcap.ICMPv6NeighborAdvertisement.__name__: netcap.ICMPv6NeighborAdvertisement(),
    netcap.ICMPv6RouterAdvertisement.__name__: netcap.ICMPv6RouterAdvertisement(),
    netcap.ICMPv6Option.__name__: netcap.ICMPv6Option(),
    netcap.UDP.__name__: netcap.UDP(),
    netcap.TCP.__name__: netcap.TCP(),
    netcap.TCPOption.__name__: netcap.TCPOption(),
    netcap.SCTP.__name__: netcap.SCTP(),
    netcap.DNS.__name__: netcap.DNS(),
    netcap.DNSResourceRecord.__name__: netcap.DNSResourceRecord(),
    netcap.DNSSOA.__name__: netcap.DNSSOA(),
    netcap.DNSSRV.__name__: netcap.DNSSRV(),
    netcap.DNSMX.__name__: netcap.DNSMX(),
    netcap.DNSQuestion.__name__: netcap.DNSQuestion(),
    netcap.DHCPv4.__name__: netcap.DHCPv4(),
    netcap.DHCPOption.__name__: netcap.DHCPOption(),
    netcap.DHCPv6.__name__: netcap.DHCPv6(),
    netcap.DHCPv6Option.__name__: netcap.DHCPv6Option(),
    netcap.LLC.__name__: netcap.LLC(),
    netcap.NTP.__name__: netcap.NTP(),
    netcap.SIP.__name__: netcap.SIP(),
    netcap.IGMP.__name__: netcap.IGMP(),
    netcap.IGMPv3GroupRecord.__name__: netcap.IGMPv3GroupRecord(),
    netcap.IPv6HopByHop.__name__: netcap.IPv6HopByHop(),
    netcap.IPv6HopByHopOption.__name__: netcap.IPv6HopByHopOption(),
    netcap.IPv6HopByHopOptionAlignment.__name__: netcap.IPv6HopByHopOptionAlignment(),
    netcap.SNAP.__name__: netcap.SNAP(),
    netcap.ICMPv6Echo.__name__: netcap.ICMPv6Echo(),
    netcap.ICMPv6NeighborSolicitation.__name__: netcap.ICMPv6NeighborSolicitation(),
    netcap.ICMPv6RouterSolicitation.__name__: netcap.ICMPv6RouterSolicitation(),
    netcap.HTTP.__name__: netcap.HTTP(),
    netcap.TLSClientHello.__name__: netcap.TLSClientHello(),
    netcap.IPSecAH.__name__: netcap.IPSecAH(),
    netcap.IPSecESP.__name__: netcap.IPSecESP(),
    netcap.Geneve.__name__: netcap.Geneve(),
    netcap.IPv6Fragment.__name__: netcap.IPv6Fragment(),
    netcap.VXLAN.__name__: netcap.VXLAN(),
    netcap.USB.__name__: netcap.USB(),
    netcap.LCM.__name__: netcap.LCM(),
    netcap.MPLS.__name__: netcap.MPLS(),
    netcap.ModbusTCP.__name__: netcap.ModbusTCP(),
    netcap.OSPFv2.__name__: netcap.OSPFv2(),
    netcap.OSPFv3.__name__: netcap.OSPFv3(),
    netcap.BFD.__name__: netcap.BFD(),
    netcap.GRE.__name__: netcap.GRE(),
    netcap.FDDI.__name__: netcap.FDDI(),
    netcap.EAP.__name__: netcap.EAP(),
    netcap.VRRPv2.__name__: netcap.VRRPv2(),
    netcap.EAPOL.__name__: netcap.EAPOL(),
    netcap.EAPOLKey.__name__: netcap.EAPOLKey(),
    netcap.CiscoDiscovery.__name__: netcap.CiscoDiscovery(),
    netcap.CiscoDiscoveryInfo.__name__: netcap.CiscoDiscoveryInfo(),
    netcap.USBRequestBlockSetup.__name__: netcap.USBRequestBlockSetup(),
    netcap.NortelDiscovery.__name__: netcap.NortelDiscovery(),
}