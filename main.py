"""Divvy Bikes is a bike sharing facility provided by the city of Chicago for its residents. As
this is a popular service, the city provides bike sharing data open to developers for
continuous innovation, system planning etc. They generally share the data adhering to
the specification listed here.
Among other things, the following are two JSON feeds that are quite useful.
station_status (info about the bike docking stations)
- https://gbfs.divvybikes.com/gbfs/en/station_status.json
free_bike_status (info about each individual bik)
- https://gbfs.divvybikes.com/gbfs/en/free_bike_status.json

Assignment:
Please build a REST API wrapper on the top of both of these API which when pinged gives
the following info as a json response

1. Total Docks Avl (use station url)
2. Total Bikes Avl (use station url)
3. Total Station Active (use station url)
4. Total Bikes that is reserved (use free bike url)
Once done, please share the API link as well as code github link (which should have
open access) at vivek.kumar@intrcity.com.
For any question - contact with subject line - "Doubt - hiring assignment"."""

import requests
from flask import Flask, jsonify, request


class ebike:
    def Total_Docks_Avl():
        url = "https://gbfs.divvybikes.com/gbfs/en/station_status.json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()
        Docks_Avl = 0
        for i in data['data']['stations']:
            Docks_Avl += i['num_docks_available']
        return Docks_Avl

    def Total_Bikes_Avl():
        url = "https://gbfs.divvybikes.com/gbfs/en/station_status.json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()
        Bikes_Avl = 0
        for i in data['data']['stations']:
            Bikes_Avl += i['num_bikes_available']
        return Bikes_Avl

    def Total_Station_Active():
        url = "https://gbfs.divvybikes.com/gbfs/en/station_status.json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()
        Station_Active = 0
        for i in data['data']['stations']:
            if i['station_status'] == "active":
                Station_Active += 1
        return Station_Active

    def Total_Reserved_Bikes():
        url = "https://gbfs.divvybikes.com/gbfs/en/free_bike_status.json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()
        is_reserved = 0
        for i in data["data"]['bikes']:
            is_reserved += i["is_reserved"]
        return is_reserved


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # type_ = request.form['type']
        # print(type_)
        # if type_ == "Total_Docks_Avl":
        #     return jsonify({type_: ebike.Total_Docks_Avl()})
        # if type_ == "Total_Bikes_Avl":
        #     return jsonify({type_: ebike.Total_Bikes_Avl()})
        # if type_ == "Total_Station_Active":
        #     return jsonify({type_: ebike.Total_Station_Active()})
        # if type_ == "Total_Reserved_Bikes":
        #     return jsonify({type_: ebike.Total_Reserved_Bikes()})
        return jsonify({"Total_Docks_Avl": ebike.Total_Reserved_Bikes(),
                        "Total_Bikes_Avl": ebike.Total_Bikes_Avl(),
                        "Total_Station_Active": ebike.Total_Station_Active(),
                        "Total_Reserved_Bikes": ebike.Total_Reserved_Bikes()
                        })
        # return jsonify({"MSG": "INVALID"})


# driver function
if __name__ == '__main__':
    app.run(debug=True)


# http://127.0.0.1:5000/