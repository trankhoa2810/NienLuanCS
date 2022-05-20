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
        yesterday = today - timedelta(days = 1)

        url = f"https://api.covid19api.com/live/country/vietnam/status/confirmed/date/{yesterday}"

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload).json()
        response = response[0]
        new_day = today.strftime("%d/%m/%Y")
        str = f"Số ca nhiễm covid ở Việt Nam tính đến ngày {new_day}:<br>\
                - Tổng số ca nhiễm: {response['Confirmed']:,}<br>\
                - Tổng số ca tử vong: {response['Deaths']:,}."
        dispatcher.utter_message(text=str)

        return []


class ActionCoronaTrackerWorld(Action):

    def name(self) -> Text:
        return "action_corona_tracker_on_the_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        today = date.today()

        url = "https://api.covid19api.com/world/total"

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload).json()
        today = today.strftime("%d/%m/%Y")
        str = f"Số ca nhiễm covid trên toàn thế giới tính đến ngày {today}:<br>\
                - Tổng số ca nhiễm: {response['TotalConfirmed']:,}<br>\
                - Tổng số ca tử vong: {response['TotalDeaths']:,}."
        dispatcher.utter_message(text=str)

        return []
