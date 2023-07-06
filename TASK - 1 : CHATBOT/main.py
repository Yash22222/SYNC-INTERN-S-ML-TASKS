# Yash Shirsath :- TE AIDS ACPCE'25
# SYNC INTERN'S
# CHATBOT AKA SIDBOT

import re
import respo as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hello!', ['hello', 'hi', 'hey', 'hola'], single_response=True)
    response('Sayo Nara!', ['bye', 'goodbye'], single_response=True)
    response('Jay Shree Ram!', ['jay', 'Shri', 'siya', 'Shree'], single_response=True)
    response('Hare Krishna!', ['hare', 'krishna', 'krisna'], single_response=True)
    response('Yes..!', ['ferroequinologist', 'railfan', 'you'], required_words=['railfan', 'ferroequinologist'])
    response('I\'m fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('ok!', ['i', 'love', 'you'], required_words=['love'])
    response('No!', ['single', 'you', 'nalla'], required_words=['single'])
    response('Talking With You!', ['doing', 'you', 'what'], required_words=['doing'])

    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_TRAIN, ['train', 'your', 'favourite'], required_words=['favourite'])
    response(long.R_MARRIED, ['are', 'you', 'married'], required_words=['married'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_ASKING, ['who', 'is', 'dhiraj'], required_words=['dhiraj'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


while True:
    print('SidBot: ' + get_response(input('Yash: ')))
