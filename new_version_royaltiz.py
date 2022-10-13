import os
from dotenv import load_dotenv

import requests

load_dotenv()
all_player_price = []

def recoverAllPlayer() :
  player_list = ['DUPONT', 'HOUNKPATIN', 'TANGA', 'LANDU']

  return player_list

def getAllPrice(player_list) :
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

def start() :
  all_player = recoverAllPlayer()
  all_player_price_list = getAllPrice(all_player)

  print(all_player_price_list)
