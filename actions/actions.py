# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSuggestRecipes(Action):
    def name(self):
        return "action_suggest_recipes"
    
    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, domain: dict) -> list:
        ingredientes = tracker.get_slot("ingredients")


        if ingredientes is None or not ingredientes:
            dispatcher.utter_message("No tengo recetas para esos ingredientes.")
            return []

        dispatcher.utter_message(f"Buscando recetas con los ingredientes: {', '.join(ingredientes)}")

        if "maruchan" in ingredientes and "frijoles" in ingredientes:
            dispatcher.utter_message("Te recomiendo una maruchan con frijoles bien insana.")
        else:
            dispatcher.utter_message("No tengo recetas para esos ingredientes :c.")
        return []
