import random
import time
import re 
import json
import urllib.request

#leuk kattten feitje.
#De api's die we vonden werkten niet dus we hebben deze maar gebruikt. deze wou ook niet als je het aanvroeg hem geven dus krijg je hem gewoon aan het begin
url = 'https://meowfacts.herokuapp.com/'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
cat_fact = result["data"]
random_fact = result["data"]
random_fact = random_fact[0]
print(result)



#alle mogelijke antwoorden.
responses = {"Hi":["Hallo., hoe gaat het?","Hoe voelt u zich?","Hallo.","Hoi."],
  "Goed jij": ["Met mij gaat het goed.","Prima.","Slecht."],
  "Goed": ["Met mij ook.","Met mij gaat het prima."],
  "Slecht": ["Naar om te horen.","Wat jammer, met mij gaat het goed.","Wat jammer, met mij gaat het slecht.","Wat jammer, met mij gaat het prima."],
  "Prima":["Dat is goed.","Met mij gaat het goed.","Met mij gaat het slecht.","Met mij gaat het prima."],
  "Hallo": ["Hallo hoe gaat het?","Hoi."],
  "Help":["Wat is er."],
  "Ik heb een vraag" : ["Wat is uw vraag?","Wat is er?"],
  "Wat is er in de aanbieding" : ["Vandaag (Wo 20 nov) zijn broccoli, blauwe bessen, Ben en Jerry's of hertog mini's en de HAK producten in de aanbieding."],
  "Wanneer opent de jumbo" : ["De jumbo open iedere dag om 8:00 uur en sluit om 21:00 uur en is op zondag van 10 tot 20 open."],
  "Wanneer sluit de jumbo" : ["De jumbo sluit iedere dag om 21:00 uur."],
  "Wie is de gast van de jumbo reclame" : ["Frank Lammers"],
  "Wie is de eigenaar van de jumbo" : ["De eigenaar van de jumbo is Karel van Eerd."],
  "Mag ik een feitje over de jumbo" : ["ja hoor, de grootste jumbo van Nederland staat in Gent.","De eigenaren willen een naam en logo dat krachtiger overkomt dan de stier van de concurrerende supermarkt Torro, en zo wordt olifant Jumbo geboren","Het hoofdkantoor van de jumbo staat in Veghel wat in Noord-Brabant ligt."],
  "Wanneer eindigd de actie" : ["De actie's die nu bezig zijn (Wo 20 nov) eindigen op di 26 nov."],
  "Wanneer is de eerste jumbo ontstaan" : ["De eerste jumbo is ontstaan op 18 okt 1979 in Tilburg."],
  "Hoeveel jumbo winkels zijn er" : ["Er zijn in totaal 725 jumbo winkels."],
  "Hoe kan ik werken bij de jumbo" : ["Als je naar uw dichtst bijzijnde jumbo gaat kunt u daar vragen of u mag soliciteren."],
}



def construct_dialogue():
  message = input()
  patterns = "Wat kost (.*)"
  match = re.search(patterns,message) 
  if message in responses:
    time.sleep(random.randint(1,3))
    print (random.choice(responses[message]))
  else:
    if match: 
      random_getal = random.randint(3,50)
      print ("BOT: " + match.group(1) + " kost: ",random_getal," euro.")
    else: 
      print("Ik hoorde je je zei",message)

print("Dit was een leuk kattenfeitje want wij van de jumbo houden heel erg van alle soorten dieren. Hallo, dit is de chatbot van de jumbo. Dit is nog een beta variant dus kan de bot mogenlijk niet alle vragen (goed) beantwoorden. Gebruik alstublieft een hoofdletter aan het begin van een vraag en geen leestekens in de vraag, dan krijgt u het beste antwoord.")
while True:
  construct_dialogue()









