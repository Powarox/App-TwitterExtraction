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



# Fréquence des mots ----------------------

# complete_doc = nlp(complete_text)
#
# # Remove stop words and punctuation symbols
# words = [token.text for token in complete_doc if not token.is_stop and not token.is_punct]
# word_freq = Counter(words)
#
# # 5 commonly occurring words with their frequencies
# common_words = word_freq.most_common(5)
# print (common_words)
#
# # Unique words
# unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
# print (unique_words)
