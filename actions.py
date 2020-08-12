from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import subprocess
import random

class ActionReplyAction(Action):
    def name(self) -> Text:
        return "action_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message["entities"]
        entity = ""
        for i in range(0, len(entities)-1):
            v = entities[i]
            if v["entity"] == "app_name":
                entity = v["value"]
                break
        if entity == "" :
            dispatcher.utter_message(text="Tôi không thể tìm thấy ứng dụng bạn muốn tương tác !")
        else :
            if entity.strip().__contains__(" "):
                entity = entity.strip().replace(" ","-")
            try :
                dispatcher.utter_custom_message(text="Đang mở " + entity)
                subprocess.call(entity)
            except :
                dispatcher.utter_message(text="Tôi không thể tìm thấy ứng dụng bạn muốn tương tác !")

        return []


class ActionReplyGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        m = str(tracker.latest_message["text"])
        n = random.random()
        if m.__contains__("daxua"):
            dispatcher.utter_message("Tao lại sợ mày quá")
        elif m.__contains__("dcm"):
            dispatcher.utter_message("cl")
        elif m.__contains__("ai tạo ra mày"):
            dispatcher.utter_message("He's D")
        elif m.__contains__("mày là ai") | m.__contains__("tên là gì?"):
            dispatcher.utter_message("Hi, I am Winston :)")
        elif m.lower().__eq__("sủa") |  m.lower().__eq__("sủa lên") | m.lower().__eq__("mày lại sủa"):
            if n%2 == 0:
                dispatcher.utter_message("sủa")
            else:
                dispatcher.utter_message("sủa cl")
        elif m.lower().__contains__("hay sủa"):
            dispatcher.utter_message("Đương nhiên là thằng SƠN VŨ")
        elif m.__contains__("chất"):
            dispatcher.utter_message("SƠN VŨ CHẤT NHẤT")
        elif n%2==0:
            dispatcher.utter_message("Hi :)")
        else:
            dispatcher.utter_message("Chào bạn, tôi có thể giúp gì cho bạn?")
        return []


class ActionReplyGoodbye(Action):
    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        n = random.random()
        if n%3==0:
            dispatcher.utter_message("Byeee")
        elif n%3==1:
            dispatcher.utter_message("Chào bạn, hẹn gặp lại")
        else:
            dispatcher.utter_message("Tạm biệt")
        return []

