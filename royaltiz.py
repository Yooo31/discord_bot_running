import os
from dotenv import load_dotenv

import requests

load_dotenv()

global allObjectivPrice
allObjectivPrice = {"DUPONT": 12, "HOUNKPATIN": 100, "YAN": 5, "LANDU": 5}

def recoverAllPlayer(player) :
  if (player == "") :
    player_list = ['DUPONT', 'HOUNKPATIN', 'YAN', 'LANDU']
  else :
    player_list = [player]

  return player_list

def getAllPrice(player_list) :
  all_player_price = []

  for player in player_list :
    print('Get ' + player + ' price !')

    player_price = getPlayerPrice(player)
    all_player_price.append(player + ': ' + player_price)

  return all_player_price

def getPlayerPrice(player) :
  url = 'https://7l3ovtpgbzgkzg4abhmlgskfji.appsync-api.eu-west-1.amazonaws.com/graphql'

  headers = {
    "x-api-key" : os.getenv("ROYALTIZ-KEY")
  }

  query = """
    query TalentGet($id: ID!) {
        talentGet(id: $id) {
          id
          valuationPrice
          fullName
        }
    }
  """

  variables = {
    "id": player
  }

  response = requests.post(url, json={'query':query ,'variables':variables}, headers=headers)
  player_price_extracted = extractJsonPlayerPrice(response.json())

  return str(player_price_extracted) + '€'

def extractJsonPlayerPrice(jsonPlayerPrice) :
  price = jsonPlayerPrice['data']['talentGet']['valuationPrice']

  return price/100

def start_royaltiz_player(player="") :
  all_player = recoverAllPlayer(player)
  all_player_price_list = getAllPrice(all_player)

  return all_player_price_list

def convertElement(element) :
  element.replace(" ", "")
  element = element.replace("€", "")
  element = element.split(":")

  return element

def asAugmentation(element) :
  objectivPrice = allObjectivPrice[element[0]]

  if (objectivPrice <= float(element[1])) :
    return(element[0] + " dépasse l'objectif (" + str(objectivPrice) + "€) avec un prix de " + element[1] + "€ !!!")
  else :
    return ""

def filterTheResult(unfilteredResult) :
  result = []

  for element in unfilteredResult :
    element = convertElement(element)
    element = asAugmentation(element)

    if (element != "") :
      result.append(element)

  return result