from botCore import botCore

import json


config = json.load(open('./config.json'))
bot = botCore(config['bot_token'])
print "Booting skynet."


def remove_mention(msg):
    if msg.find(config["bot_name"]) > -1:
        try:
            return msg.split(' ', 1)[1]
        except IndexError:
            return "No Command"
    else:
        return msg


def get_room_id(activity):
    return activity.target.id


def run():
    while True:
        activity = bot.get_next_post()
        conversation_id = get_room_id(activity)
        raw_msg = remove_mention(activity.object.displayName)
        name = bot.get_user_display_name(bot, email=activity.actor.emailAddress)
        responses = bot.process_message(raw_msg, user_email=activity.actor.emailAddress, username=name)
        count = 0
        for value in responses:
            if value is not False and bot.response_string == " " and value is not None:
                bot.response_string = str(value)
            elif value is not False:
                bot.response_string += "<br>" + str(value)
            else:
                count += 1
        if count >= bot.len_handlers:
            bot.response_string = "I'm sorry, I don't know how to handle: {}".format(raw_msg)
        bot.post_msg_to_conversation(conversation_id, markdown=bot.response_string)
        bot.response_string = " "


if __name__ == '__main__':
    run()
