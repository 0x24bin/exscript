import sys, unittest, re, os.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from TransportTest      import TransportTest
from Exscript.protocols import Telnet

class TelnetTest(TransportTest):
    CORRELATE = Telnet

    def createTransport(self):
        self.transport = Telnet(echo = 0)

    def testConstructor(self):
        self.assert_(isinstance(self.transport, Telnet))

def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TelnetTest)
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity = 2).run(suite())
