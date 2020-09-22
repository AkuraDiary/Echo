import time
import re
import random
time.sleep(0.5)

#template
bot_template = "BOT : {0}\n"
user_template = "USER : {0}"

#kumpulan respon (dictionary)
rules = {
   'I want (.*)': [
        'What would it mean if you got {0}',
        'Why do you want {0}',
        "What's stopping you from getting {0}"
        ],
   'do you remember (.*)': [
       'Did you think I would forget {0}',
       "Why haven't you been able to forget {0}",
       'What about {0}',
       'Yes .. and?',
       "yes... why?"
       ],
     
   'do you think (.*)': ['if {0}? Absolutely.', 'No chance'],

   'if (.*)': [
       "Do you really think it's likely that {0}",
       'Do you wish that {0}',
       'What do you think about {0}',
       'Really--if {0}'
       ],

    'hi (.*)':['HI','hello','hello there','halo'],

    '(.*) name (.*)':[
        "yes", 
        "sure","My name is EchoBot", 
        "they call me echo bot", 
        "Echo BOT",
        "my name is ECHO BOT" ],

    'hello there':["General Kenobi"],



     }

#jangan dihapus
default_responses = {"default" :
    [
    "Very interesting",
    "I am not sure I understand you fully",
    "What does that suggest to you?",
    "Please continue",
    "Go on",
    "Do you feel strongly about discussing such things?",
    "i dont get it",
    "i still dont understand",
    "i still dont get it",
    "could you explain",
    "explain yourself please",
    "do you have the slightest idea how little that narrows it down?",
    "I can’t get my head around it",
    "I have no clue"
    ]
    }
'''
responses = {
    "what's your name?" : ["My name is EchoBot", "they call me echo bot", "Echo BOt"],
    "how are you?" : ["fine","Great!!!"],
    "statement" : ["wow", "yess"],
    
    "sapaan" : ["ya?", "halo"],
    
    "question" : ["I Dont Know", "saya kurang tahu", "IDK"]
    }
'''

### program ###

def replace_pronouns(message):
    message = message.lower()
    if 'I' in message:
        return re.sub('I', 'you', message)
    if 'my' in message:
        return re.sub('my', 'your', message)
    if 'your' in message:
        return re.sub('your', 'my', message)
    if 'me' in message:
        return re.sub('me', 'you', message)
    if 'you' in message:
        return re.sub('me', 'you', message)

    return message
def match_rule(rules, message):
    response, phrase = random.choice(default_responses["default"]), None
    
    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
                #phrase = replace_pronouns(phrase)
    # Return the response and phrase
    return response, phrase #format(phrase)

#respon pesan
def respond(message):
    #call match_rule
    response, phrase = match_rule(rules, message)
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase)
        # Include the phrase in the response
        response = response.format(phrase)
    return response

#pengirim pesan
def send_message(message):
    #print user_template & message
    print(user_template.format(message))

    responses = respond(message)
    
    #print BOT_template &responses
    print(bot_template.format(responses))

#testing
send_message("you have any name ? ")
send_message("hello there")    
send_message("what's your name ?")
send_message("how are you?")
send_message("do you remember your last birthday")
send_message("your book")