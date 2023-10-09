import json

def pega_info():
        
    with open('./bots.json', 'r') as arq:

        robo = json.load(arq)
    
    return(robo)

def salva_info(robo: dict):

    with open('./bots.json', 'w') as arq:
    
        json.dump(robo, arq, indent=2)