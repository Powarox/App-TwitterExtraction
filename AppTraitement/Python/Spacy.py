# Stop word ----------------------------

for token in about_doc:
    if not token.is_stop:
        print (token)

import spacy

nlp = spacy.load("en_core_web_sm")

spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)

for stop_word in list(spacy_stopwords)[:10]:
     print(stop_word)

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
