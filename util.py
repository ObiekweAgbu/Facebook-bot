import os, sys
from flask import Flask, request
from wits import wit_response
from pymessenger import Bot

util = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAl43ZAebPSwBALlJhGdtWw4BXh8vrl0TaIarEykSDyXVPzSx2ZBBGa2ZBZBjZBzKilTP7lfa73iHZCZBJ7OQWfm9czZBrjrg2Ggr6z1ieuIsAgKvyzBLZA0yEfGOGeIdpm8Jjm8JM70ZBrJpenjvMiWcwHyinaGYz9bRBjmJexwk2RUPahjb56Wy9S0DaH72KqMwZD"

bot = Bot(PAGE_ACCESS_TOKEN)


@util.route('/', methods=['GET'])
def verify():
    # Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200


@util.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)

    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                # IDs
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']

                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    else:
                        messaging_text = 'no text'

                    response = None
                    entity, trait = wit_response(messaging_text)

                    # boolean variables to show what information has been stored by bot during chat
                    have_email = False
                    have_phone_number = False
                    have_address = False
                    have_distance = False
                    have_description = False

                    if entity.keys() == 'product:product':
                        response = "Ok I will send you {} news".format(str(entity.get('product:product')))
                    elif entity.keys() == "dict_keys(['our_services:our_services'])":
                        if entity.get('our_services:our_services') == 'what services do you offer?':
                            response = "... We do landscaping, deckings and other garden work, visit {website] " \
                                       "for more info. Would you like to get a quote? "
                        else:
                            response = "Yes we do! Would you like a quote?"
                    elif response is None:
                        response = "Sorry I don't understand that"

                    bot.send_text_message(sender_id, response)
    return "ok", 200


def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == "__main__":
    util.run(debug=True, port=80)
