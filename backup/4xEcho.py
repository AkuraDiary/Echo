import time
import re
import random
#time.sleep(0.5)

#template
bot_template = "BOT : {0}\n"
user_template = "USER : {0}"

###kumpulan respon (dictionary)###

#kata kunci intent
keywords = {
    'greet' : ['hello', 'hey', 'hi', 'halo','helo','wassup', 'whats up', 'bruh'], #1
    'introduce' : ['who are you', 'introduce yourself', 'am i know you?', 'what are you'], #2
    'goodbye' : ['bye', 'farewell', 'nice to meet you','see ya'], #3
    'thankyou' : ['thank', 'thx'], #4
    'sgreet':['hello there'], #5
    'ask name':['your name', 'name?', 'name'], #6
    'remember':['do you remember','remember'], #7
    'want':['i want', 'wanna', 'want', 'can i', 'may i'], #8
    'question' : ['do you mind','what do you', 'what can you do','can you'], #9
    'AYcircum' : ['how are you', 'how do you do', 'how\'s life','how\'s going', 'what\'s wrong with you'], #10
    'beat' : ['by the way', 'btw', 'you know what','\.....','um','hm'], #11
    'callyou' : ['echo bot','oi', 'hei echo', 'echo', 'bot'], #12
    'old' : ['how old','how old are you?', 'old', 'your birthday'], #13
    'think' : ['what do you think','what do you thing about', 'have you ever think', 'think', 'thinking about'],#14
    '+Uanswer' : ['yes', 'sure', 'why not', 'yes iam','interesting', 'really','great'],#15
    '-Uanswer' :['nope', 'dunno', 'well, no', 'no','dont','don\'t'],#16
    'gender' : ['gender', 'what is your gender', 'you have any gender?', 'are you male or female', 'male', 'female'],#17
    'comand' : ['\@','\$','\>','\/',],#18

}

#untuk meng membuat sebuah patterns
patterns = {}

for intent, keys in keywords.items():
    patterns [intent] = re.compile('|'.join(keys))

#respon dari kata kunci
responses = {
    "introduce":[
        'hello, my name is EchoBOT, and who are you?', 
        'Iam Echo BOt, a simple chat bot',
        'let me introduce myself, my name is echo Bot',
        'hey, iam ECHO BOT, a simple chat bot made in python, by Asthi21, do you know him?',
        'hello, my name is Echo Bot nice to meet you',
        'iam just a few hundreds lines of code'
    ],

    'old' : ['dunno man', 'I have no idea about it','Bruh... you know i am a bot...'],

    "greet" : ["hello", 'hello, how are you', 'hello there', 'Bruh...', 'Yo, wassup'],

    'AYcircum' : [
        'iam fine, thanks','iam great', 'great, what about you?', 'iam fine',
        'nothing happens','not good, what about you?', 'Daijoubou desu....'
    ],

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
        "I can’t get my head around it. Wait, i didnt had any head :D",
        "I have no clue"
        ],

    'ask name' : [
        "yes", 
        "sure","My name is EchoBot, and you?", 
        "they call me echo bot, what about you?", 
        "Echo BOT",
        "my name is ECHO BOT",
        'you can call me ECHO BOT'
        ],

    'goodbye': [
        'farewell then',
        'nice to meet you',
        'see ya',
        'see you next time',
        'bye bye'
        ],

    'thankyou':[
        "your welcome",
        'no problem',
        'okay',
        'dont mind it'
        ],

    'sgreet':['general kenobi'],

    'remember': [
        'Did you think I would forget{0}',
        "Why haven't you been able to forget{0}",
        'What about{0}',
        'Yes .. and?',
        "yes... why?"
        ],

    'want' : [
        'What would it mean if you got{0}',
        'Why do you want to {0}',
        "What's stopping you from getting{0}",
        'no, you can\'t{0}',
        'yes, you can'
        ],

    'question' : [
        'yes... yes iam',
        'yes i can{0}',
        'if {0}? Absolutely.',
        'No chance',
        'just {0}? Sure',
        'yes',
        'yes..... just kidding, i cant do anything :D',
    ],

    'beat' : ['yes?', 'what?', 'go on...', 'take your time', '...?','yes?'],

    'callyou' : ['yes?', 'can i help you?', 'what?','....?','iam here', 'whats wrong?','yes? can i help you?', 'did you just called me?'],

    'think' : ['i am thingking about you <(U-w-U)>', 'yeah i think {0} is a great idea','its great','nothing','NOPE, dont worrry, i cant think', 'What do you think about {0}'],

    '+Uanswer' : ['yes','good', 'great', 'wow, really?', 'thats great', 'NICE', 'cool','ok','okay'],
    '-Uanswer' : ['okay then', 'well, its okay'],

    'gender' : ['Dunno', 'Dunno man...', 'i have no idea','i dont think i have it','well yes, but actually no','I dont know','idk'],
    'comand' : [
        '-_-', 'do you think i have some comand? haha, unfortunately i dont',
        'i dont have any comand',':D','my creator didnt smart enough to give me a command key bruh'
        ],
    'usrname' : ['Hello, {0}!', 'hey {0}, iam echo bot', 'nice to meet you {0}', '{0}? thats a great name!'],

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


#################### ini programnya ####################

def match_intent(message):
    #print(message)
    matched_intent = None
    
    for intent,pattern in patterns.items():
        if re.search(pattern,message):
            matched_intent=intent
    return matched_intent

def find_name(message):
    name = None
    # Create a pattern for checking if the keywords occur
    name_keyword = re.compile('name|call')
    # Create a pattern for finding capitalized words
    name_pattern = re.compile('[A-Z]{1}[a-z]*')
    if name_keyword.search(message):
        # Get the matching words in the string
        name_words = name_pattern.findall(message)
        if len(name_words) > 0:
            # Return the name if the keywords are present
            name = ' '.join(name_words)
            #print(name)
    return name

def replace_pronouns(message):
    message = message.lower()
    if ' I ' in message:
        return re.sub('I', 'you', message)
    if ' my ' in message:
        return re.sub('my', 'your', message)
    if ' your ' in message:
        return re.sub('your', 'my', message)
    if ' me ' in message:
        return re.sub('me', 'you', message)
    if ' you ' in message:
        return re.sub('you', 'me', message)

    return message

    

#respon pesan
def respond(message):
    #call match_intent
    intent=match_intent(message.lower())
    name = find_name(message)

    key='default'
    #phrase = message
    
    if intent in responses:
      key = intent

    response = random.choice(responses[key])
    #Jngan dihapus

    #mencari jika ada {0}
    phrase = message
    if "{0}" in response:
        #response, phrase = match_rule(response, message)
        #membuat match objek
        match = re.search(patterns[intent], phrase) 
        #menggabungkan dengan pesan
        phrase = re.sub(str(match.group()), "", phrase)
        # # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase) 
        # Include the phrase in the response 
        response = response.format(phrase) 
    #print(response)

    if name is not None:
        response = random.choice(responses['usrname']).format(name)

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
    time.sleep(0.5)
    #print BOT_template &responses
    print(bot_template.format(responses))

#testing
'''
'Helo'
"hi"
"hey there "
"hello there"
"bye"
"you have any name ? "
"Hello There"    
"what's your name ?"
"how are you?")
"your book"
"can you do something for me?"
"Who are you?"
'do you remember about movie we watched last night?'
'yes'
'what are you thinking about?'
"btw"'''
send_message('hello, my name is Seta')

pesan = {'item' :['Helo','can you be honest to me ',
"hi",
"hey there ",
"hello there",
"bye",
"you have any name ? ",
"Hello There",    
"what's your name ?",
"how are you?",
"your book",
"can you do something for me ?",
"Who are you?",
'do you remember about movie we watched last night?',
'yes',
'what are you thinking about?',
"btw"
]
}
#send_message(random.choice(pesan['item']))