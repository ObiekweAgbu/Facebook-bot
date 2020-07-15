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
                    entity, value = wit_response(messaging_text)

                    if entity == 'news':
                        response = "Ok I will snd you {} news".format(str(value))
                    elif entity == "location":
                        response = "You live in {0}. I will send you top headlines from {0}".format(str(value))

                    if response == None:
                        response = "Sorry I don't understand that"
                    bot.send_text_message(sender_id, response)
    return "ok", 200


def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == "__main__":
    util.run(debug=True, port=80)
