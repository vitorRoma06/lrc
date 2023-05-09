from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # Add links
        self.addLink(h1, s1, bw=10, delay='1ms', loss=0)
        self.addLink(h3, s1, bw=10, delay='1ms', loss=0)
        self.addLink(h2, s2, bw=10, delay='1ms', loss=0)
        self.addLink(h4, s2, bw=10, delay='1ms', loss=0)
        self.addLink(s1, s2, bw=10, delay='1ms', loss=0)

if __name__ == '__main__':
    topo = MyTopo()
    net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink)
    net.start()
    net.pingAll()
    net.stop()
