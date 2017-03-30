import json
import logging as log
import unittest

from sparkBot.handlers.vote import Vote

from utils.logging_utils import Utils

path = "testing_files/votes_test.json"


class testVote(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(testVote, cls).setUpClass()
        log.getLogger("testVote")
        with open("test_logs/vote_test.log", 'w') as file:
            file.truncate()
        log.basicConfig(filename='test_logs/vote_test.log', level=log.DEBUG,
                        format='[%(asctime)s]:%(levelname)s: %(message)s')
        cls.utils = Utils()

    def setUp(self):
        super(testVote, self).setUp()
        self.vote = Vote(path_to_file=path)

    #####################################
    ## start_vote command test 100-103 ##
    #####################################

    def test_100_start_vote(self):
        """
            Simple test to check start_vote works and creates default vote options.
        """
        self.utils.banner("Starting Test 100 start_vote command")
        self.assert_start_vote()

        log.info("Asserting the json")
        self.assert_json()

        self.utils.end_banner("Finished Test 100")

    def test_101_start_vote_camelcase(self):
        """
            Simple test to check start_vote works with camelCase and creates default vote options.
        """
        self.utils.banner("Starting Test 101 start_vote camelcase")
        self.assert_start_vote(start_vote="sTaRt_vOte", test="101")

        log.info("Asserting the json")
        self.assert_json()

        self.utils.end_banner("Finished Test 101")

    def test_102_start_vote_options(self):
        """
            Simple test to check start_vote works and creates specified vote options.
        """
        self.utils.banner("Starting Test 102 start_vote with options")
        options_string = "test1, test2, test3"
        self.assert_start_vote(test="102", options=options_string,
                               expected_response=("**Starting Vote, options:**<br>%s" % options_string))

        log.info("Asserting the json in the test file matches the expected json")
        json_data = {"options": ["test1", "test2", "test3"]}
        self.assert_json(expected_json=json_data)

        self.utils.end_banner("Finished Test 102")

    def test_103_start_vote_one_option(self):
        """
            Simple test to check start_vote cancels due to a invalid number of vote options.
        """
        self.utils.banner("Starting Test 103 start_vote with one option.")
        option = "test1"
        expected_response = "**Cancelling vote:**<br>There was only one option: %s" % option
        self.assert_start_vote(expected_response=expected_response, options=option, test="103")

        log.info("Asserting the json in the test file matches the expected json")
        data = {"options": []}
        self.assert_json(expected_json=data)

        self.utils.end_banner("Finished Test 103")


    ###############################
    ## vote command test 104-110 ##
    ###############################

    def test_104_vote_with_no_option(self):
        """
            Test to check vote is no logged due to no option specifed.
            start_vote -> default options -> vote (no option) -> no vote logged.
        """
        self.utils.banner("Starting Test 104 vote command with no vote cast.")
        self.assert_start_vote(test="104")

        log.info("Asserting the json in the test file matches the expected json")
        self.assert_json()

        log.info("Cast a vote with no option present. Asserting the blank vote")
        self.assert_vote()

        log.info("Asserting the json in the test file matches the expected json")
        self.assert_json()

        self.utils.end_banner("Finished Test 104")

    def test_105_vote_with_correct_option(self):
        """
            Test to check vote is logged due to correct option specified.
            start_vote -> default options -> vote option -> vote logged.
        """
        self.utils.banner("Starting Test 105 vote command with a vote cast.")
        self.assert_start_vote(test="105")

        log.info("Asserting the json in the test file matches the expected json")
        self.assert_json()

        log.info("Cast a vote with no option present. Asserting the blank vote")
        self.assert_vote(cast="yes", expected_response="Your vote has been logged.", test="105")

        log.info("Asserting the json in the test file matches the expected json")
        data = {'options': ['yes', 'no'], 'test_email@email.mail': 'yes'}
        self.assert_json(expected_json=data)

        self.utils.end_banner("Finished Test 105")

    def test_106_vote_with_incorrect_option(self):
        """
            Test to check vote is not logged due to incorrect option specified.
            start_vote -> default options -> vote incorrect option -> return error.
        """
        self.utils.banner("Starting Test 106 vote command with a vote cast.")
        self.assert_start_vote(test="106")

        log.info("Asserting the json in the test file matches the expected json")
        self.assert_json()

        log.info("Cast a vote with correct option present. Asserting the vote.")
        self.assert_vote(cast="wrong", expected_response="Not a valid vote: \"wrong\"", test="106")

        log.info("Asserting the json in the test file matches the expected json")
        data = {'options': ['yes', 'no']}
        self.assert_json(expected_json=data)

        self.utils.end_banner("Finished Test 106")

    def test_107_vote_with_user_twice(self):
        """
            Test to check vote is not logged due to same user voting again.
            start_vote -> default options -> vote incorrect option -> return error.
        """
        self.utils.banner("Starting Test 107 vote command with a vote cast.")
        self.assert_start_vote(test="107")

        log.info("Asserting the json in the test file matches the expected json")
        self.assert_json()

        log.info("Cast a vote with correct option present. Asserting the vote.")
        self.assert_vote(cast="yes", expected_response="Your vote has been logged.", test="107")

        log.info("Asserting the json in the test file matches the expected json")
        data = {'options': ['yes', 'no'], 'test_email@email.mail': 'yes'}
        self.assert_json(expected_json=data)

        log.info("Cast a vote from the same user. Asserting the vote is not logged.")
        self.assert_vote(cast="yes", expected_response="You have already voted.", test="107")

        log.info("Asserting the json in the test file matches the expected json")
        data = {'options': ['yes', 'no'], 'test_email@email.mail': 'yes'}
        self.assert_json(expected_json=data)

        self.utils.end_banner("Finished Test 107")

    def test_108_vote_with_camelcase(self):
        """
            Test to check vote is logged due to correct option specified.
            Vote and option are camel case.
            start_vote -> default options -> vote option -> vote logged.
        """
        self.utils.banner("Starting Test 108 vote command with a vote cast.")
        self.assert_start_vote(test="108")

        log.info("Asserting the json in the test file matches the expected json")
        self.assert_json()

        log.info("Cast a vote with no option present. Asserting the blank vote")
        self.assert_vote(vote="vOtE", cast="yEs", expected_response="Your vote has been logged.",
                         test="108")

        log.info("Asserting the json in the test file matches the expected json")
        data = {'options': ['yes', 'no'], 'test_email@email.mail': 'yes'}
        self.assert_json(expected_json=data)

        self.utils.end_banner("Finished Test 108")

    def test_109_vote_with_two_different_users(self):
        """
            Test to check votes are logged due to correct options specified.
            start_vote -> default options -> vote option user 1 -> vote logged
            -> vote option user 2 -> vote logged.
        """
        self.utils.banner("Starting Test 109 vote command with a vote cast.")
        self.vote_x_times_different_users()

        self.utils.end_banner("Finished Test 109")

    def test_110_vote_with_two_different_users_one_the_same(self):
        """
            Test to check votes are logged due to correct options specified.
            start_vote -> default options -> vote option user 1 -> vote logged
            -> vote option user 2 -> vote logged -> user1 votes again
            -> not logged.
        """
        self.utils.banner("Starting Test 110 vote command with a vote cast.")
        data = self.vote_x_times_different_users(test="110")

        log.info("Cast a vote with a user that has already voted. Asserting the vote is not logged.")
        self.assert_vote(vote="vote", cast="no", expected_response="You have already voted.",
                         test_mail="test_email1@email.mail", test="110")
        self.assert_json(expected_json=data)

        self.utils.end_banner("Finished Test 110")

    ###################################
    ## end_vote command test 111-110 ##
    ###################################

    def test_111_end_vote_with_no_votes(self):
        """
            Test to check end_vote returns expected response.
            start_vote -> default options -> end_vote -> assert response.
        """
        self.utils.banner("Starting Test 111 end_vote command with no votes cast.")
        self.assert_start_vote(test="111")

        response = self.vote.handle_message("end_vote", user_email="test_email@email.mail", username="Testa")
        expected_response = "**No Votes Cast**<br>Ending vote."
        #"**Votes are in!**<br>yes: 0<br>no: 0<br>**The winner is**<br>"
        self.assertTrue(response == expected_response,
                        "Failed, expect response to end_vote was %s. Actual response is %s"
                        % (expected_response, response))

        self.utils.end_banner("Finished Test 111")

    def test_112_end_vote_camel_case_with_no_votes(self):
        """
            Test to check end_vote in camelcase returns expected response.
            start_vote -> default options -> end_vote -> assert response.
        """
        self.utils.banner("Starting Test 112 end_vote command with camelcase.")
        self.assert_start_vote(test="112")

        response = self.vote.handle_message("eNd_VoTe", user_email="test_email@email.mail", username="Testa")
        expected_response = "**No Votes Cast**<br>Ending vote."
        self.assertTrue(response == expected_response,
                        "Failed, expect response to end_vote was %s. Actual response is %s."
                        % (expected_response, response))

        self.utils.end_banner("Finished Test 112")

    def test_113_end_vote_with_a_vote_cast(self):
        """
            Test to check end_vote returns expected response with a vote cast.
            start_vote -> default options -> user votes -> logged -> end_vote
            -> assert response.
        """
        self.utils.banner("Starting Test 113 end_vote command with a vote cast.")

        self.vote_x_times_different_users(test="113")

        response = self.vote.handle_message("end_vote", user_email="test_email@email.mail", username="Testa")
        expected_response = "**Votes are in!**<br>yes: 2<br>no: 0<br>**The winner is**<br>yes"
        self.assertTrue(response == expected_response,
                        "Failed, expect response to end_vote was %s. Actual response is %s."
                        % (expected_response, response))

        self.utils.end_banner("Finished Test 113")

    def vote_x_times_different_users(self, x=2, test="109"):
        self.assert_start_vote(test=test)

        log.info("Asserting the json in the test file matches the expected json")
        self.assert_json()

        data = {'options': ['yes', 'no']}
        for i in range(0, x):
            email = "test_email%d@email.mail" % i
            log.info("Cast a vote with user%d's option. Asserting the vote logged." % i)
            self.assert_vote(cast="yes", expected_response="Your vote has been logged.", test=test,
                             test_mail=email)

            log.info("Asserting the json in the test file matches the expected json")
            data[email] = 'yes'
            self.assert_json(expected_json=data)
        return data

    def assert_vote(self, vote="vote", expected_response="**No Vote**<br>Please cast a vote!",
                    cast="", test="104", test_mail="test_email@email.mail"):
        response = self.vote.handle_message("{} {}".format(vote, cast), test_mail, username="Testa")
        log.info("Asserting vote as \"{} {}\" has return expected results".format(
            vote, cast))

        self.assertTrue(expected_response == response,
                        "ERROR vote %s failed: Expected %s, Actual %s"
                        % (test, expected_response, response))

    def assert_start_vote(self, start_vote="start_vote", expected_response="**Starting Vote, options:**<br>Yes or No",
                          options=None, test="100", test_mail="test_email@email.mail"):
        if options is None:
            response = self.vote.handle_message("{}".format(start_vote), test_mail, username="Testa")
            log.info("Asserting start_vote as \"{}\" has return expected results".format(
                start_vote))
        else:
            response = self.vote.handle_message("{} {}".format(start_vote, options), test_mail, username="Testa")
            log.info("Asserting start_vote as \"{} {}\" has return expected results".format(
                start_vote, options))

        self.assertTrue(expected_response == response,
                        "ERROR start_vote %s failed: Expected \"%s\", Actual \"%s\""
                        % (test, expected_response, response))

    def assert_json(self, expected_json=None):
        if expected_json is None:
            expected_json = {"options": ["yes", "no"]}

        actual_json = self.get_vote_file_json()

        self.assertTrue(actual_json == expected_json,
                        "ERROR json was incorrect failed: Expected: \"%s\", Actual: \"%s\""
                        % (expected_json, actual_json))

    def get_vote_file_json(self):
        with open(path) as json_data:
            input_data = json.load(json_data)
            return input_data

    def clear_vote_file(self):
        with open(path, 'w') as output:
            json.dump({"options": []}, output)

    @classmethod
    def tearDownClass(cls):
        super(testVote, cls).tearDownClass()

    def tearDown(self):
        super(testVote, self).tearDownClass()
        self.clear_vote_file()
        self.vote = None

if __name__ == '__main__':
    unittest.main()
