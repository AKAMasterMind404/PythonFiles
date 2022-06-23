import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')
from spacy.lang.en import English
from nltk.corpus import wordnet as wn

nlp = English()
my_stopwords = ["she", "their", "under", "are", "by"]


def analyzeText(text):
    stop_words = []
    nouns = []
    verbs = []
    regular_words = []

    for word in text.split():
        if nlp.vocab[word].is_stop:
            stop_words.append(word)
        else:
            regular_words.append(word)

        result = wn.synsets(word)
        result = result[0].pos() if result != [] else None
        isVerb = result == 'v'
        isNoun = result == 'n'

        if isVerb:
            verbs.append(word)
        elif isNoun:
            nouns.append(word)

    print("STOP WORD LIST(15):")
    print(stop_words[:15])
    print("-----------------")
    print("NUMBER OF STOP WORDS:", len(stop_words))
    print("-----------------")
    print("NOUNS:")
    print(nouns)
    print("-----------------")
    print("VERBS:")
    print(verbs)
    print("-----------------")
    print("OUTPUT AFTER REMOVAL OF STOP WORDS:")
    print(" ".join(regular_words))
    print("-----------------")


if __name__ == '__main__':
    text = """Note from poster to Kubrick newsgroup:

    I found this on a bbs a while ago and I thought I'd pass it along to all 
    of you Kubrick freaks out there.

    02/23/89
    Transcriber's note:

    For all you Clarke/Kubrick/2001 fans,

    I found the original paper copy of this screenplay a while back and felt 
    compelled to transcribe it to disk and upload it to various bulletin 
    boards for the enjoyment of all.

    The final movie deviates from this screenplay in a number of interesting 
    ways. I've tried to maintain the format of the original document except 
    the number of lines per page of the original. In order to reduce the 
    length of this file I've used a bar of "------" to delimit the pages as 
    there was a lot of whitespace per original screenplay page."""

    analyzeText(text)

    text = " ".join(my_stopwords) + text

    print("RESULTS AFTER ADDING STOPWORDS:")
    print("-----------------")
    print("-----------------")
    analyzeText(text)
