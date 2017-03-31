"""
    Sup.
"""
import logging as log
import os

class Utils(object):

    def __init__(self):
        log.getLogger("testVote")
        log.basicConfig(filename='test_logs/vote_test.log', level=log.DEBUG,
                        format='[%(asctime)s]:%(levelname)s: %(message)s')

    def banner(self, message):
        count = len(message)
        log.info("*"*(count+6))
        log.info("** %s **" % message)
        log.info("*"*(count+6))

    def end_banner(self, msg=""):
        count = len(msg)
        if count is 0:
            count = 20
        log.info("*" * (count + 6))
        log.info("** %s **" % msg)
        log.info(("*" * (count + 6)) + "\n")

    def log(self, msg):
        log.info(msg)

