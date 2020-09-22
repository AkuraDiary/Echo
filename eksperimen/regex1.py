import re
#template
bot_template = "BOT : {0}\n"
user_template = "USER : {0}"

keywords = {
    'greet' : ['hello', 'hey', 'hi'],
    'goodbye' : ['bye', 'farewell'],
    'thankyou' : ['thank', 'thx'],

}

responses = {
    'greet' : 'hello, how are you',
    'default' : 'yes'
}
patterns = {}

for intent, keys in keywords.items():
    patterns [intent] = re.compile('|'.join(keys))
#print (patterns)

# Define find_name()
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
            print(name)
    return name

def match_intent(message):
    #print(message)
    matched_intent = None
    
    for intent,pattern in patterns.items():
        if re.search(pattern,message):
            matched_intent=intent
    return matched_intent

def respond(message):
    name = find_name('message')
    intent=match_intent(message)
    
    key='default'
    
    if intent in responses:
      key = intent
    response = responses[key]

    # Find the name
    
    if name is not None:
        response = "Hello, {0}!".format(name)
        
    
    return response

def send_message(message):
    #print user_template & message
    print(user_template.format(message))

    responses = respond(message)
    
    #print BOT_template &responses
    print(bot_template.format(responses))

send_message('my name is Seta')
send_message('helo')
send_message("my name is David Copperfield")
print(find_name('my name is Seta'))
print(find_name("my name is David Copperfield"))