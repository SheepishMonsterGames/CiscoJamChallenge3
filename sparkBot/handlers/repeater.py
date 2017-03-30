from handler_base import MessageHandler
"""
    This is an example class for you to understand how the handlers work.
    Each new handler must extend MessageHandler class, override the handle_message
    and the help message.
"""


class Repeater(MessageHandler):
    def __init__(self):
        pass

    def handle_message(self, raw_msg, user_email, username):
        """
            Repeats the message based on the command,
            The raw_msg should remove the command before it replies.

            all handle_message should return false if they can't be handled by this class.
        """
        if "repeat message" in raw_msg.lower():
            return "**All I do is repeat:** " + raw_msg[14::]
        if "repeat backwards" in raw_msg.lower():
            return "**Repeating your message backwards:** " + (raw_msg[::-1])[:-16].strip()
        if "repeat help" in raw_msg.lower():
            return self.help()
        return False

    def help(self):
        return "**repeat message** - Repeats whatever message is sent.<br>" \
               "**repeat backwards** - Repeats the message backwards."
