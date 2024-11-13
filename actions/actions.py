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

from actions.infrastructure.repos.career_components_repo import CareerComponentsRepo
from actions.domain.entities.carrera_pc_componentes import CarreraPcComponentes
from actions.domain.entities.carrera_universitaria import CarreraUniversitaria

class ActionRecommendComponents(Action):
    #create repository instance on builder
    def __init__(self):
        #call the parent constructor
        super().__init__()

        #create a new instance of the CareerComponentsRepo
        self.career_components_repo = CareerComponentsRepo()
        

    def name(self):
        return "action_recommend_components"

    def run(self, dispatcher, tracker, domain):
        # Obtiene la carrera del usuario
        career_from_user = tracker.get_slot("career") if tracker.get_slot("career") else ""

        carrera_universitaria_name = self.career_components_repo.search_synonym(career_from_user)

        # Envía un mensaje general sobre la recomendación
        dispatcher.utter_message(text=f"Dame un momento para buscar las recomendaciones para la carrera: {carrera_universitaria_name}...")

        # Convierte la carrera a minúsculas y la actualiza en la ranura
        carrera_universitaria : CarreraUniversitaria = self.career_components_repo.get_carrera_universitaria_by_name(carrera_universitaria_name)
        if carrera_universitaria is None:
            response = """No encontre esa carrera en mi base de conocimientos, sin embargo, la composicion mas Todo Terreno,
seria un procesador superior a Intel Core I3, o Ryzen 3 para amd, 8 GB de ram, y un disco duro ssd con al menos 240 gb :) """ 

        else:
            carrera_pc_componentes : CarreraPcComponentes = self.career_components_repo.get_carrera_pc_componentes(carrera_universitaria.id)
            if carrera_pc_componentes is None:
                response = """No encontre esa carrera en mi base de conocimientos, sin embargo, la composicion mas Todo Terreno,
seria un procesador superior a Intel Core I3, o Ryzen 3 para amd, 8 GB de ram, y un disco duro ssd con al menos 240 gb :) """ 

            else:
                response = f"""Para la carrera de {carrera_universitaria.nombre} se RECOMIENDA:
- Procesador: {carrera_pc_componentes.rec_cpu}
- RAM: {carrera_pc_componentes.rec_ram}
- Tarjeta gráfica minima: {carrera_pc_componentes.rec_gpu if carrera_pc_componentes.rec_gpu != "" else "No se requiere"}
- Almacenamiento minimo: {carrera_pc_componentes.rec_storage}

Como MINIMO, se recomienda:
- Procesador: {carrera_pc_componentes.min_cpu}
- RAM: {carrera_pc_componentes.min_ram}
- Tarjeta gráfica recomendada: {carrera_pc_componentes.min_gpu if carrera_pc_componentes.min_gpu != "" else "No se requiere"}
- Almacenamiento recomendado: {carrera_pc_componentes.min_storage}

{carrera_pc_componentes.recomendacion_extra if carrera_pc_componentes.recomendacion_extra != "" else ""}
"""

        # Envía la recomendación específica
        dispatcher.utter_message(text=response)

        return []
