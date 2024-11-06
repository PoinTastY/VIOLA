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

class ActionRecommendComponents(Action):

    def name(self):
        return "action_recommend_components"

    def run(self, dispatcher, tracker, domain):
        # Obtiene la carrera del usuario
        career = tracker.get_slot("Career") if tracker.get_slot("Career") else ""

        # Envía un mensaje general sobre la recomendación
        dispatcher.utter_message(text=f"Para la carrera de {career}, recomiendo una computadora con las siguientes especificaciones...")

        # Convierte la carrera a minúsculas y la actualiza en la ranura
        career_lower = career.lower()

        # Genera una respuesta específica basada en la carrera del usuario
        if career_lower == "ingenieria de sistemas":
            response = "Un procesador i7 o Ryzen 7 y al menos 16 GB de RAM."
        elif career_lower == "diseño grafico":
            response = "Es ideal una tarjeta gráfica potente y una pantalla de alta resolución."
        elif career_lower == "ingenieria en computacion":
            response = "Un procesador i5 o Ryzen 5 y al menos 16 GB de RAM."

        elif career_lower == "cine":
            response = "Un procesador i5 (intel), o ryzen 5 (amd), minimo 16 gb de ram, y una tarjeta grafica RTX 3060."
        else:
            response = """No encontre esa carrera en mi base de conocimientos, sin embargo, la composicion mas Todo Terreno, 
seria un procesador superior a Intel Core I3, o Ryzen 3 para amd, 8 GB de ram, y un disco duro ssd con al menos 240 gb :) """ 

        # Envía la recomendación específica
        dispatcher.utter_message(text=response)

        return []
