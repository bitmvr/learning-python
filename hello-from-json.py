#!/usr/bin/env python3

import json

person = open('./resources/person.json', 'r');
dictionary_of_person = json.load(person);
print(dictionary_of_person['first_name']);
person.close();

