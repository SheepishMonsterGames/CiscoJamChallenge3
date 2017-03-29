import logging as log
import unittest

from sparkBot.handlers.futurama import Futurama

from utils.logging_utils import Utils


class testFuturama(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(testFuturama, cls).setUpClass()
        log.getLogger("testFuturama")
        with open("test_logs/futurama_test.log", 'w') as test_file:
            test_file.truncate()
        log.basicConfig(filename='test_logs/futurama_test.log', level=log.DEBUG,
                        format='[%(asctime)s]:%(levelname)s: %(message)s')
        cls.utils = Utils()

    def setUp(self):
        super(testFuturama, self).setUp()
        self.futurama = Futurama()

    def test_100_futurama_quote(self):
        """
            Simple test to check futurama works and returns a quote.
        """
        self.utils.banner("Starting Test 100 futurama command")

        response = self.futurama.handle_message("{}".format("futurama"), "test_email@email.mail",
                                                username="Testa")

        self.assertTrue(response in self.futurama.quotes,
                        "ERROR, response \"%s\" was not in the list of quotes."
                        % response)

        self.utils.end_banner("Finished Test 100")

    @classmethod
    def tearDownClass(cls):
        super(testFuturama, cls).tearDownClass()

    def tearDown(self):
        super(testFuturama, self).tearDownClass()
        self.futurama = None

if __name__ == '__main__':
    unittest.main()
