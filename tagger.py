from rasa.nlu import load_data
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.model import Trainer

from tag import Tag

class Tagger:
    def __init__(self, languages):
        pipeline = [{"name": "WhitespaceTokenizer"},
                    {"name": "CRFEntityExtractor"},
                    {"name": "EntitySynonymMapper"},
                    {"name": "CountVectorsFeaturizer"},
                    {"name": "EmbeddingIntentClassifier"}]

        self.interpreters = {}
        for lang in languages:
            training_data = load_data(f'data/nlu_{lang}.md')
            trainer = Trainer(RasaNLUModelConfig({"pipeline": pipeline}))
            self.interpreters[lang] = trainer.train(training_data)

    @staticmethod
    def detect_language(message):
        return "en"

    @staticmethod
    def convert_confidences_to_tags(confidences):
        print(confidences)
        return []

    def tag(self, message):
        returned_tags = []

        lang = self.detect_language(message)
        returned_tags.append(Tag("Lang", lang))

        returned_tags += self.convert_confidences_to_tags(self.interpreters[lang].parse(message))

        return returned_tags

