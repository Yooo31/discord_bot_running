import requests

url = 'https://7l3ovtpgbzgkzg4abhmlgskfji.appsync-api.eu-west-1.amazonaws.com/graphql'

headers = {
  "x-api-key" : "da2-njdlg6jenjekzgczrzjuoxuqw4"
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
        "id": "DUPONT"
    }

r = requests.post(url, json={'query':query ,'variables':variables}, headers=headers)
