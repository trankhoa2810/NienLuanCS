# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

import requests
from datetime import date, timedelta

class ActionCoronaTrackerVietNam(Action):

    def name(self) -> Text:
        return "action_corona_tracker_viet_nam"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        today = date.today()
        # yesterday = today - timedelta(days = 1)

        # url = f"https://api.covid19api.com/live/country/vietnam/status/confirmed/date/{yesterday}"
        url = "https://api.coronatracker.com/v3/stats/worldometer/country?countryCode=VN"

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload).json()
        response = response[0]
        new_day = today.strftime("%d/%m/%Y")
        str = f"Tình hình covid ở Việt Nam ngày {new_day}:<br>\
                - Số ca mới hôm nay: {response['dailyConfirmed']:,}<br>\
                - Số ca tử vong hôm nay: {response['dailyDeaths']:,}<br>\
                - Tổng số ca nhiễm: {response['totalConfirmed']:,}<br>\
                - Tổng số ca tử vong: {response['totalDeaths']:,}<br>\
                - Tổng số ca đã hồi phục: {response['totalRecovered']:,}."
        dispatcher.utter_message(text=str)

        return []


class ActionCoronaTrackerWorld(Action):

    def name(self) -> Text:
        return "action_corona_tracker_on_the_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        today = date.today()

        # url = "https://api.covid19api.com/world/total"
        url = "https://api.coronatracker.com/v3/stats/worldometer/global"

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload).json()
        today = today.strftime("%d/%m/%Y")
        str = f"Tình hình covid trên Thế Giới ngày {today}:<br>\
                - Số ca mới hôm nay: {response['totalNewCases']:,}<br>\
                - Số ca tử vong hôm nay: {response['totalNewDeaths']:,}<br>\
                - Tổng số ca nhiễm: {response['totalConfirmed']:,}<br>\
                - Tổng số ca tử vong: {response['totalDeaths']:,}<br>\
                - Tổng số ca đã hồi phục: {response['totalRecovered']:,}."
        dispatcher.utter_message(text=str)

        return []
