import random

R_EATING = "I Not Eating , I am Chatbot!"
R_ADVICE = "I am not free here to giving advice you, ask google!"
R_MARRIED = "Yes I am Married With Alexa..!"
R_TRAIN = 'My Favourite train is 22221 Mumbai CSMT - H.Nizamuddin Rajdhani Express'
R_ASKING = 'Dhiraj is Nalla Electrician..LOL!'


def unknown():
    response = ["Could you please Ask Again? ",
                "...",
                "Please Speak Again.",
                "What does that mean?"][
        random.randrange(4)]
    return response


#                                          THANK YOU....!
