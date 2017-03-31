import logging as log
import unittest

from sparkBot.handlers.numbers import Numbers

from utils.logging_utils import Utils


class testNumbers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(testNumbers, cls).setUpClass()
        log.getLogger("testNumbers")
        with open("test_logs/numbers_test.log", 'w') as test_file:
            test_file.truncate()
        log.basicConfig(filename='test_logs/numbers_test.log', level=log.DEBUG,
                        format='[%(asctime)s]:%(levelname)s: %(message)s')
        cls.utils = Utils()

    def setUp(self):
        super(testNumbers, self).setUp()
        self.numbers = Numbers()

    def test_100_numbers_no_options(self):
        """
            Simple test to check numbers works and returns a no game due to no options supplied.
        """
        self.utils.banner("Starting Test 100 numbers command no options")

        response = self.numbers.handle_message("{}".format("numbers"), "test_email@email.mail",
                                               username="Testa")

        expected_response = "**Cancelling numbers game**<br>No options supplied."

        self.assertEqual(response, expected_response,
                         "ERROR, response \"%s\" did not match expected \"%s\"."
                         % (response, expected_response))

        self.utils.end_banner("Finished Test 100")

    def test_101_numbers_with_correct_options(self):
        """
            Simple test to check numbers works and returns a game.
        """
        self.utils.banner("Starting Test 101 numbers command with correct options")

        response = self.numbers.handle_message("{}".format("numbers s:2 l:4"), "test_email@email.mail",
                                               username="Testa")

        expected_response = "**Numbers Game**<br>**Target:** %d<br>" \
                            "**Numbers:** %d, %d, %d, %d, %d, %d" \
                            % (self.numbers.target, self.numbers.numbers[0], self.numbers.numbers[1],
                               self.numbers.numbers[2], self.numbers.numbers[3], self.numbers.numbers[4],
                               self.numbers.numbers[5])

        self.assertEqual(response, expected_response,
                         "ERROR, response \"%s\" did not match expected \"%s\"."
                         % (response, expected_response))

        self.utils.end_banner("Finished Test 101")

    def test_102_numbers_with_large_option_too_high(self):
        """
            Simple test to check numbers works and returns no game due to large option too high.
        """
        self.utils.banner("Starting Test 102 numbers command with options too high.")

        response = self.numbers.handle_message("{}".format("numbers s:0 l:7"), "test_email@email.mail",
                                               username="Testa")

        expected_response = "**Cancelling numbers game**<br>Large number is too big 7."

        self.assertEqual(response, expected_response,
                         "ERROR, response \"%s\" did not match expected \"%s\"."
                         % (response, expected_response))

        self.utils.end_banner("Finished Test 102")

    def test_103_numbers_with_small_option_too_high(self):
        """
            Simple test to check numbers works and returns no game due to small option too high.
        """
        self.utils.banner("Starting Test 103 numbers command with small too high.")

        response = self.numbers.handle_message("{}".format("numbers s:7 l:0"), "test_email@email.mail",
                                               username="Testa")

        expected_response = "**Cancelling numbers game**<br>Small number is too big 7."

        self.assertEqual(response, expected_response,
                         "ERROR, response \"%s\" did not match expected \"%s\"."
                         % (response, expected_response))

        self.utils.end_banner("Finished Test 103")

    def test_104_numbers_with_options_less_than_six(self):
        """
            Simple test to check numbers works and returns no game due to options less than six.
        """
        self.utils.banner("Starting Test 104 numbers command with options less then six.")

        response = self.numbers.handle_message("{}".format("numbers s:4 l:1"), "test_email@email.mail",
                                               username="Testa")

        expected_response = "**Cancelling numbers game**<br>Combined numbers were less than six<br>" \
                            "s:4 + l:1 < 6"

        self.assertEqual(response, expected_response,
                         "ERROR, response \"%s\" did not match expected \"%s\"."
                         % (response, expected_response))

        self.utils.end_banner("Finished Test 104")

    def test_105_numbers_with_options_greater_than_six(self):
        """
            Simple test to check numbers works and returns no game due to options greater than six.
        """
        self.utils.banner("Starting Test 104 numbers command with options gerater then six.")

        response = self.numbers.handle_message("{}".format("numbers s:5 l:2"), "test_email@email.mail",
                                               username="Testa")

        expected_response = "**Cancelling numbers game**<br>Combined numbers can't be greater than six<br>" \
                            "s:5 + l:2 > 6"

        self.assertEqual(response, expected_response,
                         "ERROR, response \"%s\" did not match expected \"%s\"."
                         % (response, expected_response))

        self.utils.end_banner("Finished Test 105")

    @classmethod
    def tearDownClass(cls):
        super(testNumbers, cls).tearDownClass()

    def tearDown(self):
        super(testNumbers, self).tearDownClass()
        self.numbers = None

if __name__ == '__main__':
    unittest.main()
