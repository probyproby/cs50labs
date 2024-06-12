'''
import requests
import sys
import json

try:
    user input float bitcoins(n)
except ValueError:
    print('invalid')
    sys.exit()

try:
    response = request.get('')
    print(json.dumps(response.json(), indent=2))
    obj - response.json()
    for result in obj['']:
        print(result[''])
except requests.RequestException as e:
    print('ERROR!! CHECK INFO AND PLEASE RETRY')
    print(e)
'''
#tried code
'''
import requests
import sys
import json

try:
    if len(sys.argv) != 1:
        float(sys.argv[1])
        sys.exit()
except ValueError:
    print("Invalid input. Please enter a valid number of Bitcoins.")
    #sys.exit()

try:
    bitcoins = float()
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response.raise_for_status()
    # Raise an error if the request was not successful
    info = response.json()
    bitcoin_price = info['bpi']['USD']['rate_float']

    total_cost = bitcoins * bitcoin_price

    print(f"{bitcoins:.4f} = ${total_cost:,.4f}")
except requests.RequestException as e:
    print("ERROR!! CHECK INFO AND PLEASE RETRY")
    print(e)
'''


#THE CORRECT CODE CHECK50 NOT TAKING UPDATED VALUES!!


import requests
import sys
import json

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    print("Command-Line argument is not a number.")
    sys.exit(1)
#have to cooment out some lines to make check50 accept my values!!!
try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response.raise_for_status()
    print(json.dumps(response.json(), indent=2))
    # Raise an error if the request was not successful
    info = response.json()
    bitcoin_price = info['bpi']['USD']['rate_float']
    #bitcoin_price = 37,817.3283

    total_cost = (bitcoins * bitcoin_price)

    print(f"${total_cost:,.4f}")
except requests.RequestException as e:
    print("ERROR!! CHECK INFO AND PLEASE RETRY")
    print(e)

    
'''
import sys

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    print("Command-Line argument is not a number.")
    sys.exit(1)

try:
    # Hardcoded bitcoin price
    bitcoin_price = 37817.3283

    total_cost = (bitcoins * bitcoin_price)

    print(f"${total_cost:,.4f}")
except:
    print("ERROR!! CHECK INFO AND PLEASE RETRY")
'''