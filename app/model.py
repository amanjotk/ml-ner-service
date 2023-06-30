import spacy


class Model:
    def __init__(self):
        self.model = spacy.load("en_core_web_sm")

    def recognize_human_names(self, text):
        text_entities = self.model(text)

        return [word.text for word in text_entities.ents
                if word.label_ == "PERSON"]
