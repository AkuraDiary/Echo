import time
import re
import random
time.sleep(0.5)

#template
bot_template = "BOT : {0}\n"
user_template = "USER : {0}"

###kumpulan respon (dictionary)###

#kata kunci intent
keywords = {
    'greet' : ['hello', 'hey', 'hi'],
    'goodbye' : ['bye', 'farewell'],
    'thankyou' : ['thank', 'thx'],
    'sgreet':['hello there'],
    'ask name':['your name', 'name?', 'name'],
    'remember':['do you remember','remember'],
}

#untuk meng anu patterns
patterns = {}

for intent, keys in keywords.items():
    patterns [intent] = re.compile('|'.join(keys))

#respon dari kata kunci
responses = {
    "greet" : ["hello", 'hello, how are you'],

    'default':[
        'Please rephrase...', 
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
        ],

    'ask name' : [
        "yes", 
        "sure","My name is EchoBot", 
        "they call me echo bot", 
        "Echo BOT",
        "my name is ECHO BOT"
        ],

    'goodbye': ['farewell then','nice to meet you'],

    'thankyou':["your welcome"],

    'sgreet':['general kenobi'],

    'remember': [
        'Did you think I would forget {0}',
        "Why haven't you been able to forget {0}",
        'What about {0}',
        'Yes .. and?',
        "yes... why?"
        ]
    }



#jangan dihapus (dipakai jarang, dibuang sayang)
'''
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

    'hi|hey|heyy|halo':['HI','hello','hello there','halo'],

    '(.*) name (.*)':[
        "yes", 
        "sure","My name is EchoBot", 
        "they call me echo bot", 
        "Echo BOT",
        "my name is ECHO BOT" ],

    'hello there':["General Kenobi"],



     }
    


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


### program ###

def match_intent(message):
    #print(message)
    matched_intent = None
    
    for intent,pattern in patterns.items():
        if re.search(pattern,message):
            matched_intent=intent
    return matched_intent

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

    

#respon pesan
def respond(message):
    #call match_intent
    intent=match_intent(message)
    
    key='default'
    #phrase = message
    
    if intent in responses:
      key = intent

    response = random.choice(responses[key])

    #Jngan dihapus
    #call match_rule
    phrase = message
    if "{0}" in response:
        #response, phrase = match_rule(response, message)
        match = re.search(patterns[intent], phrase) #"""pokoknya disekitaran sini lah, saya juga kurang tahu"""
        phrase = re.sub(str(match.group()), "", phrase)
        # # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase) #  '''atau disini '''
        # Include the phrase in the response 
        response = response.format(phrase) #  '''error nya disekitar sini'''
    #print(response)

    return response

##jangan dihapus, dipakai jarang dibuang sayang##
'''
def match_rule(response, message):
    #response, phrase = None, None
    # Iterate over the rules dictionary
    for pattern, response in patterns.items():
        # Create a match object
        #match = re.search(responses[response], message)
        #if match is not None:
            # Choose a random response
            #response = random.choice(responses[key])
        if '{0}' in response:
            match = re.search(responses[key], message)
            phrase = match.group(1)
            phrase = replace_pronouns(phrase)
    # Return the response and phrase
    return response, phrase#format(phrase)
''' 
#pengirim pesan
def send_message(message):
    #print user_template & message
    print(user_template.format(message))

    responses = respond(message)
    
    #print BOT_template &responses
    print(bot_template.format(responses))

#testing
#send_message("halo")
#send_message("hi")
#send_message("hey there ")
#send_message("hello there")
#end_message("bye")    
#send_message("you have any name ? ")
send_message("hello there")    
send_message("what's your name ?")
#send_message("how are you?")
send_message("your book")
send_message("do you remember your last birthday?")
