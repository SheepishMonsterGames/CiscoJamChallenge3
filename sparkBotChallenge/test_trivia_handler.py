import logging as log
import unittest
import json
import re

from sparkBot.handlers.trivia import Trivia
from utils.logging_utils import Utils


class testTrivia(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(testTrivia, cls).setUpClass()
        log.getLogger("testTrivia")

        # Regex expression, matches parts of your output exactly and the rest loosely.
        cls.question_pattern = ">\*Category: .*<br><br>>\*Question: .*\*"

        with open("test_logs/trivia_test.log", 'w') as test_file:
            test_file.truncate()
        log.basicConfig(filename='test_logs/trivia_test.log', level=log.DEBUG,
                        format='[%(asctime)s]:%(levelname)s: %(message)s')

        cls.path_to_file = "testing_files/trivia_test.json"  # test file location

        cls.utils = Utils()

        with open(cls.path_to_file, 'w') as json_file:
            json.dump({"text": ""}, json_file)

    def setUp(self):
        super(testTrivia, self).setUp()
        self.trivia = Trivia(path_to_file=self.path_to_file)

    def test_100_trivia_question_returned(self):
        """
            Simple test to check if Trivia works and returns a question string.
        """
        log.info("Starting Test 100 trivia question command")

        response = self.trivia.handle_message('trivia question', user_email="test_email@email.mail",
                                              username="Testa")

        pattern = re.compile(self.question_pattern)

        self.assertTrue(pattern.match(response),
                        "ERROR, received incorrect response data type. Response was %s,"
                        "expect to match pattern %s"
                        % (response, self.question_pattern))

        log.info("Finished Test 100")

    def test_101_trivia_question_fails_as_question_already_ask(self):
        """
            Test to check if Trivia works and returns a string asking the user
            to call the answer command.
        """
        log.info("Starting Test 101 trivia question returns trivia answer command")

        response = self.trivia.handle_message('trivia question', user_email="test_email@email.mail",
                                              username="Testa")

        expected_response = "**Trivia insession**<br>Please get the answer to the last question"

        self.assertEqual(response, expected_response,
                         "ERROR, received incorrect response from \"trivia question\""
                         ". Response was: \"%s\", expect_response: \"%s\""
                         % (response, expected_response))

        log.info("Finished Test 101")

    def test_102_trivia_answer_returned(self):
        """
            Simple test to check if Trivia works and returns an appropriate answer,
            and that the answer is stored in the json file.
        """
        log.info("Starting Test 102 trivia answer command")

        with open(self.path_to_file) as json_file:
            data = json.load(json_file)
            self.assertTrue(type(data) is dict,
                            "ERROR, data stored in %s is not json data. Got type %s"
                            % (self.path_to_file, type(data)))

        expected_response = data["text"]

        response = self.trivia.handle_message('trivia answer', user_email="test_email@email.mail",
                                              username="Testa")

        self.assertEqual(response, expected_response,
                         "ERROR, received incorrect response data type. Expected %s, received %s"
                         % (response, expected_response))

        log.info("Finished Test 102")

    def test_103_trivia_answer_command_fails_as_no_answer_available(self):
        """
            Simple test to check if the Trivia answer command called when no question
            is asked returns a prompt to the user to call the "trivia question" command.
        """
        log.info("Starting Test 103 trivia answer with no question asked")

        with open(self.path_to_file) as json_file:
            data = json.load(json_file)
            self.assertTrue(type(data) is dict,
                            "ERROR, data stored in %s is not json data. Got type %s"
                            % (self.path_to_file, type(data)))

        expected_data = {"text":""}
        self.assertEqual(data, expected_data,
                         "ERROR: expected response \"%s\" did not match actual \"%s\""
                         % (expected_data, data))

        expected_response = "**No Question**<br>Use \"trivia question\" to get a new question."
        response = self.trivia.handle_message("trivia answer", user_email="test_email@email.mail",
                                              username="Testa")

        self.assertEqual(response, expected_response,
                         "ERROR, response \"%s\" did not match expected response \"%s\""
                         % (response, expected_response))

        log.info("Finished Test 103")

    @classmethod
    def tearDownClass(cls):
        super(testTrivia, cls).tearDownClass()
        cls.trivia = None

    def tearDown(self):
        super(testTrivia, self).tearDownClass()

if __name__ == '__main__':
    unittest.main()
