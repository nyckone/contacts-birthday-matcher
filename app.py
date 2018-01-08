from flask import Flask, request, abort
import json

from contacts import contacts

CONTACT_DICT = "contact_dict"
BIRTHDAY_DICT = "birthday_dict"

app = Flask(__name__)


@app.route('/get_contacts_with_birthday', methods=['POST'])
def get_contacts_with_birthday():
    if not request.json:
        abort(400)

    input_data = request.data
    input_data_dict = json.loads(input_data)
    contact_dict = input_data_dict[CONTACT_DICT]
    birthday_dict = input_data_dict[BIRTHDAY_DICT]
    updated_contact_dict = contacts.add_birthday_to_contacts(name_birthday_dict=birthday_dict, contact_dict=contact_dict)
    return json.dumps(updated_contact_dict)


if __name__ == '__main__':
    app.run()
