import langdetect
from rasa.nlu import load_data
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.model import Trainer

from pkg_resources import resource_filename

from chatbot_demo.tag import TAGS

CONFIDENCE_THRESHOLD = 0.1
COMPANY_STRUCTURES = ['ltd', 'plc']


class Tagger:
    def __init__(self, languages=None):

        if languages is None:
            languages = ['en', 'de']

        pipeline = [{"name": "WhitespaceTokenizer"},
                    {"name": "CRFEntityExtractor"},
                    {"name": "EntitySynonymMapper"},
                    {"name": "CountVectorsFeaturizer"},
                    {"name": "EmbeddingIntentClassifier"}]

        self.interpreters = {}
        for lang in languages:
            filepath = resource_filename(__name__, f'nlu_{lang}.md')
            training_data = load_data(filepath)
            trainer = Trainer(RasaNLUModelConfig({"pipeline": pipeline}))
            self.interpreters[lang] = trainer.train(training_data)

    @staticmethod
    def detect_language(message):
        return langdetect.detect(message)

    @staticmethod
    def convert_confidences_to_tags(confidences):
        tags = []
        for intent in confidences['intent_ranking']:
            if intent['confidence'] > CONFIDENCE_THRESHOLD:
                tags.append(TAGS[intent['name']])

        return tags

    def tag(self, message):
        detected_tags = []

        lang = self.detect_language(message)
        detected_tags.append(TAGS[lang])

        detected_tags += self.convert_confidences_to_tags(self.interpreters[lang].parse(message))

        return set([x.id for x in detected_tags])
