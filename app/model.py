import spacy


class Model:
    def __init__(self):
        self.model = spacy.load("en_core_web_sm")

    def recognize_entities(self, text):
        text_entities = self.model(text)
        return [(word.text, word.label_) for word in text_entities.ents]
