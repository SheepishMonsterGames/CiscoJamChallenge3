import logging as log
import unittest

from sparkBot.handlers.meaningoflife import MeaningOfLife

from utils.logging_utils import Utils


class testMeaningOfLife(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(testMeaningOfLife, cls).setUpClass()
        log.getLogger("testMeaningOfLife")
        with open("test_logs/meaningoflife_test.log", 'w') as test_file:
            test_file.truncate()
        log.basicConfig(filename='test_logs/meaningoflife_test.log', level=log.DEBUG,
                        format='[%(asctime)s]:%(levelname)s: %(message)s')
        cls.utils = Utils()

    def setUp(self):
        super(testMeaningOfLife, self).setUp()
        self.meaningoflife = MeaningOfLife()

    def test_100_meaning_of_life(self):
        """
            Simple test to check meaning of life works and returns "42 <username>".
        """
        self.utils.banner("Starting Test 100 meaning of life command")

        response = self.meaningoflife.handle_message("{}".format("meaning of life"),
                                                     "test_email@email.mail",
                                                     username="Testa")

        expected = "42 Testa"

        self.assertEquals(response, expected,
                          "ERROR, response \"%s\" was not the same as expected response %s."
                          % (response, expected))

        self.utils.end_banner("Finished Test 100")

    def test_101_meaning_of_life_different_user(self):
        """
            Simple test to check meaning of life works and returns "42 <username>".
        """
        self.utils.banner("Starting Test 101 meaning of life command different user")

        response = self.meaningoflife.handle_message("{}".format("meaning of life"),
                                                     "im_different@email.mail",
                                                     username="different_user")

        expected = "42 different_user"

        self.assertEquals(response, expected,
                          "ERROR, response \"%s\" was not the same as expected response %s."
                          % (response, expected))

        self.utils.end_banner("Finished Test 101")

    @classmethod
    def tearDownClass(cls):
        super(testMeaningOfLife, cls).tearDownClass()

    def tearDown(self):
        super(testMeaningOfLife, self).tearDownClass()
        self.meaningoflife = None

if __name__ == '__main__':
    unittest.main()
