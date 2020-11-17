import spacy

class ParsingSpacy:

    # Constructor
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        self.nlp.Defaults.stop_words.add('rt')

    # Extraction des StopWords
    def extractionStopWords(self, dico, arrayStopWord = {}):
        for key, value in dico.items():
            about_doc = self.nlp(value)
            string = ""
            for token in about_doc:
                if not token.is_stop:
                    string = string + " " + token.text
            arrayStopWord[key] = string
        return arrayStopWord
