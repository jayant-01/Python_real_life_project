import geocoder
import json
import turtle
import urllib.request
import time
import webbrowser


def main():
    print("welcome to nasa project with python")
    # free API
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    print("result = ", result)
    location = result["iss_position"]
    lat = location["latitude"]
    lon = location["longitude"]
    print("latitude = ", lat)
    print("longitude = ", lon)
    # map
    map = "https://www.google.com/maps/place/" + lat + "," + lon
    print("map = ", map)
    webbrowser.open(map)
    # turtle
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic("map.gif")
    screen.register_shape("iss.gif")
    iss = turtle.Turtle()
    iss.shape("iss.gif")
    iss.setheading(90)
    iss.penup()
    iss.goto(float(lon), float(lat))
    # pass
    url = "http://api.open-notify.org/iss-pass.json"
    url = url + "?lat=" + str(37.78) + "&lon=" + str(-122.41)
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    print(result)
    over = result["response"][1]["risetime"]
    style = ('Arial', 6, 'bold')
    # turtle
    location = turtle.Turtle()
    location.hideturtle()
    location.penup()
    location.goto(-180, 90)
    location.color("white")
    location.write(time.ctime(over), font=style)
    # pass
    url = "http://api.open-notify.org/astros.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    print(result)
    print("People in space: ", result["number"])
    people = result["people"]
    print(people)
    for p in people:
        print(p["name"], " in ", p["craft"])
        # turtle
        location.goto(-180, 80)
        location.write(p["name"] + " in " + p["craft"], font=style)
        # pass
        url = "http://api.open-notify.org/iss-pass.json"
        url = url + "?lat=" + str(37.78) + "&lon=" + str(-122.41)
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
        print(result)
        over = result["response"][1]["risetime"]
        style = ('Arial', 6, 'bold')
        # turtle
        location = turtle.Turtle()
        location.hideturtle()
        location.penup()
        location.goto(-180, 90)
        location.color("white")
        location.write(time.ctime(over), font=style)
        # pass
        url = "http://api.open-notify.org/astros.json"
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
        print(result)
        print("People in space: ", result["number"])
        people = result["people"]
        print(people)
        for p in people:
            
main()
