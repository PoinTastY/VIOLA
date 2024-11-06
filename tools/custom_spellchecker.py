# custom_spellchecker.py
from spellchecker import SpellChecker
from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from rasa.engine.storage.resource import Resource
from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.training_data import TrainingData
from rasa.shared.nlu.constants import TEXT
from typing import Dict, Text, Any

@DefaultV1Recipe.register([GraphComponent], is_trainable=True)
class SpellCheckerComponent(GraphComponent):
    def __init__(self, config: Dict[Text, Any]) -> None:
        super().__init__(config)
        self.spell = SpellChecker()

    def process(self, message: Message) -> Message:
        original_text = message.get(TEXT)
        corrected_text = " ".join([self.spell.correction(word) for word in original_text.split()])
        message.set(TEXT, corrected_text)
        return message

    def train(self, training_data: TrainingData) -> Resource:
        return Resource("spell_checker")
