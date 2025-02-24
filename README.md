i# Cafe and Wifi Website

## Goal

<u>Build a website that lists cafes with wifi and power for remote working</u>

* Use the provided database to create a website that displays the cafes and 
allows users to add and delete cafes.

## TODOS

- Make boolean fields of cafe submission not text input. Use button or something.
- When users submit a cafe, it sends an email to the admin.
- Create a "pending" database of user submitted cafes that can be approved by admin.
    * All the same things that are in the cafe table, but also:
        * submitted by (username / email?)
        * submitted on (date)
- When a pending cafe is accepted, remove it from the db
- Add users/auth
- Let users add cafes
- Let users remove cafes
- Nav bar
- Line up /cafe columns, with properties on the left and their values on the right

1. When you click a link on the index page, it should bring you to the /cafe page
for the cafe you clicked, with details about that cafe.
    * Use cafe id in URL
]
## Table Structure:
### Cafe
```
0|id|INTEGER|0||1
1|name|VARCHAR (250)|1||0
2|map_url|VARCHAR (500)|1||0
3|img_url|VARCHAR (500)|1||0
4|location|VARCHAR (250)|1||0
5|has_sockets|BOOLEAN|1||0
6|has_toilet|BOOLEAN|1||0
7|has_wifi|BOOLEAN|1||0
8|can_take_calls|BOOLEAN|1||0
9|seats|VARCHAR (250)|0||0
10|coffee_price|VARCHAR (250)|0||0
11|submitted_by_id|INTEGER|1|0
```
"id", "name", "map_url", "img_url", "location", "has_sockets", "has_toilet",
"has_wifi", "can_take_calls", "seats","coffee_price" 

### User
```
0|id|INTEGER|0||1
1|username|TEXT|1||0
2|pw_hash|TEXT|1||0
```
* find user's submissions:
`SELECT * FROM cafe WHERE submitted_by_id = <user_id>`

### Submissions
```
0|id|INTEGER|0||1
1|name|VARCHAR (250)|1||0
2|map_url|VARCHAR (500)|1||0
3|img_url|VARCHAR (500)|1||0
4|location|VARCHAR (250)|1||0
5|has_sockets|BOOLEAN|1||0
6|has_toilet|BOOLEAN|1||0
7|has_wifi|BOOLEAN|1||0
8|can_take_calls|BOOLEAN|1||0
9|seats|VARCHAR (250)|0||0
10|coffee_price|VARCHAR (250)|0||0
111|submitted_by_id|INTEGER|1|0
```

## Protip for finding the gmail app password setting:
https://myaccount.google.com/apppasswords

## Go from string representation of dictionary back to dictionary
```
>>> dict_str =  "{'name': 'wake forest coffee', 'map_url': 'n/a', 'img_url': 'n/a', 'location': 'wake forest nc', 'has_sockets': 'Y', 'has_toilet': 'Y', 'has_wifi': 'Y', 'can_take_calls': 'Y', 'seats': '24', 'coffee_price': '$4'}"
>>> dict(dict_str)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> dict_str.split(",").strip("{}")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'strip'
>>> dict_str.strip("{}").split(",")
["'name': 'wake forest coffee'", " 'map_url': 'n/a'", " 'img_url': 'n/a'", " 'location': 'wake forest nc'", " 'has_sockets': 'Y'", " 'has_toilet': 'Y'", " 'has_wifi': 'Y'", " 'can_take_calls': 'Y'", " 'seats': '24'", " 'coffee_price': '$4'"]
>>> kv_pairs = dict_str.strip("{}").split(",")
>>> kv_pairs = [tuple(_.split(":")) for _ in kv_pairs]
>>> kv_pairs
[("'name'", " 'wake forest coffee'"), (" 'map_url'", " 'n/a'"), (" 'img_url'", " 'n/a'"), (" 'location'", " 'wake forest nc'"), (" 'has_sockets'", " 'Y'"), (" 'has_toilet'", " 'Y'"), (" 'has_wifi'", " 'Y'"), (" 'can_take_calls'", " 'Y'"), (" 'seats'", " '24'"), (" 'coffee_price'", " '$4'")]
>>> new_dict = {k:v for (k,v) in kv_pairs}
>>> new_dict
{"'name'": " 'wake forest coffee'", " 'map_url'": " 'n/a'", " 'img_url'": " 'n/a'", " 'location'": " 'wake forest nc'", " 'has_sockets'": " 'Y'", " 'has_toilet'": " 'Y'", " 'has_wifi'": " 'Y'", " 'can_take_calls'": " 'Y'", " 'seats'": " '24'", " 'coffee_price'": " '$4'"}
>>>
```

## Methods and properties of RadioField
['_Option', '__call__', '__class__', '__delattr__', '__dict__', '__dir__',
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__getstate__', '__gt__', '__hash__', '__html__', '__init__',
'__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__',
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', '__weakref__',
'_choices_generator', '_formfield', '_run_validation_chain', '_translations',
'check_validators', 'choices', 'coerce', 'data', 'default', 'description',
'do_not_call_in_templates', 'errors', 'filters', 'flags', 'gettext',
'has_groups', 'id', 'iter_choices', 'iter_groups', 'label', 'meta', 'name',
'ngettext', 'object_data', 'option_widget', 'populate_obj', 'post_validate',
'pre_validate', 'process', 'process_data', 'process_errors',
'process_formdata', 'raw_data', 'render_kw', 'short_name', 'type', 'validate',
'validate_choice', 'validators', 'widget'] Decision:
 How do I tell which cafe is being referenced when I send a POST request submitting
 the radio form?
