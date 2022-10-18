import os
from dotenv import load_dotenv

import requests

load_dotenv()

def recoverAllPlayer() :
  player_list = ['DUPONT', 'HOUNKPATIN', 'YAN', 'LANDU']

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

def start_royaltiz_player() :
  all_player = recoverAllPlayer()
  all_player_price_list = getAllPrice(all_player)

  return all_player_price_list
