from wit import Wit

access_token = "GAYQO3AHCHCTWLSBT6JNWYMOWUFU4SEP"

client = Wit(access_token=access_token)


def wit_response(message_text):
    resp = client.message(message_text)
    entity = None
    trait = None
    try:
        if len(list(resp['entities'])) <= 1:
            entity = {list(resp['entities'])[0]: resp['entities'][list(resp['entities'])[0]][0]['value']}
            if len(list(resp['traits'])) > 0:
                trait = {list(resp['traits'])[0]: resp['traits'][list(resp['traits'])[0]][0]['value']}
            elif len(list(resp['traits'])) > 1:
                trait = {list(resp['traits'])[0]: resp['traits'][list(resp['traits'])[0]][0]['value'],
                         list(resp['traits'])[1]: resp['traits'][list(resp['traits'])[1]][0]['value']}

        elif len(list(resp['entities'])) == 2:
            entity = {list(resp['entities'])[0]: resp['entities'][list(resp['entities'])[0]][0]['value'],
                      list(resp['entities'])[1]: resp['entities'][list(resp['entities'])[1]][0]['value']}
            if len(list(resp['traits'])) > 0:
                trait = {list(resp['traits'])[0]: resp['traits'][list(resp['traits'])[0]][0]['value']}
            elif len(list(resp['traits'])) > 1:
                trait = {list(resp['traits'])[0]: resp['traits'][list(resp['traits'])[0]][0]['value'],
                         list(resp['traits'])[1]: resp['traits'][list(resp['traits'])[1]][0]['value']}


        elif len(list(resp['entities'])) == 3:
            entity = {list(resp['entities'])[0]: resp['entities'][list(resp['entities'])[0]][0]['value'],
                      list(resp['entities'])[1]: resp['entities'][list(resp['entities'])[1]][0]['value'],
                      list(resp['entities'])[2]: resp['entities'][list(resp['entities'])[2]][0]['value']}
            if len(list(resp['traits'])) > 0:
                trait = {list(resp['traits'])[0]: resp['traits'][list(resp['traits'])[0]][0]['value']}
            elif len(list(resp['traits'])) > 1:
                trait = {list(resp['traits'])[0]: resp['traits'][list(resp['traits'])[0]][0]['value'],
                         list(resp['traits'])[1]: resp['traits'][list(resp['traits'])[1]][0]['value']}

    except:
        pass

    return(entity, trait)


print(wit_response("How much would it cost for a hedge trim"))


#print(wit_response("I want sports news"))

