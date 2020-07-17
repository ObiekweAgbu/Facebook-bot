from wit import Wit

access_token = "4WHEQTWZ2BLJHROJJGGRKGW2QAXEGQTX"

client = Wit(access_token=access_token)


def wit_response(message_text):
    resp = client.message(message_text)
    entity = None
    value = None
    intent = None
    try:
        entity = list(resp['entities'])[0]
        value = resp['entities'][entity][0]['value']
        intent = list(resp['intents'])[0]['name']
    except:
        pass
    return (entity, value, intent)


print(wit_response("I want sports news"))
