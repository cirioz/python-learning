
#! Nesting

capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
    "Italy": "Rome"
}



#! Nesting a list

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

#! Dictionary in a dictionary
visits = 0
friends = 0

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": visits, "friends_met": friends}
}


#! Nesting a dictionary in a list

travel_log = [
    {
     "country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"], 
     "total_visits": 12
     }
    ,
    {
     "country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": visits, "friends_met": friends
     },
    ]

