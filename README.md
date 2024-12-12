i# Cafe and Wifi Website

## Goal

<u>Build a website that lists cafes with wifi and power for remote working</u>

* Use the provided database to create a website that displays the cafes and 
allows users to add and delete cafes.

## TODOS

1. Add users/auth
2. Let users add cafes
3. Let users remove cafes
4. Nav bar
1. Line up /cafe columns, with properties on the left and their values on the right

1. When you click a link on the index page, it should bring you to the /cafe page
for the cafe you clicked, with details about that cafe.
    * Use cafe id in URL
]
## Table Structure:

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
```
"id", "name", "map_url", "img_url", "location", "has_sockets", "has_toilet", "has_wifi", "can_take_calls", "seats","coffee_price" 

