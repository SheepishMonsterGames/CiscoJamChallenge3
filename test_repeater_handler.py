import logging as log
import unittest

from sparkBot.handlers.repeater import Repeater

from utils.logging_utils import Utils


class testRepeater(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(testRepeater, cls).setUpClass()
        log.getLogger("testRepeater")
        with open("test_logs/repeater_test.log", 'w') as test_file:
            test_file.truncate()
        log.basicConfig(filename='test_logs/repeater_test.log', level=log.DEBUG,
                        format='[%(asctime)s]:%(levelname)s: %(message)s')
        cls.utils = Utils()

    def setUp(self):
        super(testRepeater, self).setUp()
        self.repeater = Repeater()

    def test_100_repeater(self):
        """
            Simple test to check repeater works and returns text repeated.
        """
        self.utils.banner("Starting Test 100 repeater_message command.")

        expected = "**All I do is repeat:**  Get Rekt."
        response = self.repeater.handle_message("repeat message Get Rekt.", "test_email@email.mail",
                                                username="Testa")

        self.assertEqual(response, expected,
                        "ERROR, response \"%s\" was not the same as actual %s."
                        % (expected, response))

        self.utils.end_banner("Finished Test 100")

    def test_101_repeater_camel_case(self):
        """
            Simple test to check repeater works in camelcase and returns text repeated.
        """
        self.utils.banner("Starting Test 101 repeater_message camelcase command.")

        expected = "**All I do is repeat:**  Get Rekt"
        response = self.repeater.handle_message("RePeAt MeSsAgE Get Rekt", "test_email@email.mail",
                                                username="Testa")

        self.assertEqual(response, expected,
                         "ERROR, response \"%s\" was not the same as actual %s."
                         % (expected, response))

        self.utils.end_banner("Finished Test 101")

    def test_102_repeater_backwards(self):
        """
            Simple test to check repeater works in camelcase and returns text repeated.
        """
        self.utils.banner("Starting Test 100 repeater_message command.")

        expected = "**Repeating your message backwards:** tkeR teG"
        response = self.repeater.handle_message("repeat backwards Get Rekt", "test_email@email.mail",
                                                username="Testa")

        self.assertEqual(response, expected,
                         "ERROR, response \"%s\" was not the same as actual %s."
                         % (expected, response))

        self.utils.end_banner("Finished Test 100")

    def test_104_repeater_backwards_camel_case(self):
        """
            Simple test to check repeater works in camelcase and returns text repeated.
        """
        self.utils.banner("Starting Test 100 repeater_backwards camelcase command.")

        expected = "**Repeating your message backwards:** tkeR teG"
        response = self.repeater.handle_message("RePeAt BackwarDS Get Rekt", "test_email@email.mail",
                                                username="Testa")

        self.assertEqual(response, expected,
                         "ERROR, response \"%s\" was not the same as actual %s."
                         % (expected, response))

        self.utils.end_banner("Finished Test 100")

    @classmethod
    def tearDownClass(cls):
        super(testRepeater, cls).tearDownClass()

    def tearDown(self):
        super(testRepeater, self).tearDownClass()
        self.repeater = None

if __name__ == '__main__':
    unittest.main()
