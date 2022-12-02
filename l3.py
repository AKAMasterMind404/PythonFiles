# %%
"""
## `NAME`: Atharv Karbhari
## `PRN`: 20190802003
"""

# %%
"""
### `AIM`: To perform segmentation and Feature Engineering on Text data.
"""

# %%
"""
**Importing nessary libraries**
"""

# %%
import PyPDF2 as pdf
import re

# %%
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# %%
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# %%
"""
**Extracting data from Pdf**
"""


# %%
def readPDF(fileName):
    pdfFile = pdf.PdfFileReader(fileName)

    return pdfFile.getPage(0).extractText()


# %%
"""
## Feature Engineering on the Data
"""

# %%
"""
**Extracting feature in our case: `ABSTRACT` from the pdf Data**
"""


# %%
def extractAbstract(pdfData, start, end):
    pdfDataArray = pdfData.split("\n")
    # Extracting Abstract from the data
    abstractDatapdf = "".join(pdfDataArray[start:end])

    lower_abstract_datapdf = abstractDatapdf.lower()

    return lower_abstract_datapdf


# %%
"""
**Tokenize the data that is diving the strings into substring**
"""


# %%
def tokenizeData(pdfData):
    tokenized_datapdf = nltk.sent_tokenize(pdfData)
    return tokenized_datapdf


# %%
"""
**Removing any special characters from the data that does not help in the training process**
"""


# %%
def removeSpecialChar(pdfData):
    for index, i in enumerate(pdfData):
        pdfData[index] = re.sub(r"[^a-zA-Z0-9 ]", "", i)

    return pdfData


# %%
"""
**Remove any kind of stop words from the data given**
"""


# %%
def removeStopWords(pdfData):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize("".join(pdfData))

    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

    filtered_words = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_words.append(w)

    return filtered_words


# %%
"""
**Applying stemming to the sentence that is fetching root form of each word in the sentence**
"""


# %%
def stemming(pdfData):
    ps = PorterStemmer()
    for index, i in enumerate(pdfData):
        pdfData[index] = ps.stem(i)

    return pdfData


# %%
"""
**Applying lemmatize on the sentence**
"""


# %%
def lemmatize(pdfData):
    lemmatizer = WordNetLemmatizer()

    for index, i in enumerate(pdfData):
        pdfData[index] = lemmatizer.lemmatize(i)

    return pdfData


# %%
"""
## Feature Counting for a better understanding of the frequency of the words appearing in the sentence and encouraging better results in the training process.
"""


# %%
def countFeatures(pdfData):
    vectorizer = CountVectorizer()
    vectorizer.fit(pdfData)

    return vectorizer.vocabulary_


# %%
def tfidfFeatures(pdfData):
    vectorizer = TfidfVectorizer()
    vectorizer.fit(pdfData)

    return vectorizer.vocabulary_


# %%
"""
### Applying the above methods on each pdf Data
"""

# %%
"""
## `PDF 1`
"""

# %%
pdf1 = readPDF("pdf1.pdf")

# %%
abstractData = extractAbstract(pdf1, 8, 26)

# %%
import nltk

nltk.download('punkt')

# %%
abstractData

# %%
pdf1TokenizedData = tokenizeData(abstractData)

# %%
pdf1TokenizedData

# %%
pdf1AbstractData = removeSpecialChar(pdf1TokenizedData)
import nltk

nltk.download('stopwords')

# %%
filtered_words = removeStopWords(pdf1AbstractData)

# %%
filtered_words[:10]

# %%
stemmedData = stemming(filtered_words)

# %%
stemmedData[:10]

# %%
import nltk

nltk.download('wordnet')
import nltk

nltk.download('omw-1.4')
lemmatizeData = lemmatize(stemmedData)

# %%
lemmatizeData[:10]

# %%
countFeatures1 = countFeatures(lemmatizeData)

# %%
"""
**For example let's consider `Present`**
"""

# %%
countFeatures1["present"]

# %%
tfidfFeatures1 = tfidfFeatures(lemmatizeData)

# %%
tfidfFeatures1["present"]

# %%
"""
## `PDF 2`
"""

# %%
pdf2 = readPDF("pdf2.pdf")

# %%
abstractData = extractAbstract(pdf2, 7, 17)

# %%
abstractData

# %%
pdf2TokenizedData = tokenizeData(abstractData)

# %%
pdf2TokenizedData

# %%
pdf2AbstractData = removeSpecialChar(pdf2TokenizedData)

# %%
filtered_words = removeStopWords(pdf2AbstractData)

# %%
filtered_words[:10]

# %%
stemmedData = stemming(filtered_words)

# %%
stemmedData[:10]

# %%
lemmatizeData = lemmatize(stemmedData)

# %%
lemmatizeData[:10]

# %%
countFeatures2 = countFeatures(lemmatizeData)

# %%
"""
**For example let's consider `Vision`**
"""

# %%
countFeatures2["vision"]

# %%
tfidfFeatures2 = tfidfFeatures(lemmatizeData)

# %%
tfidfFeatures2["task"]

# %%
"""
## `PDF 3`
"""

# %%
pdf3 = readPDF("pdf3.pdf")

# %%
abstractData = extractAbstract(pdf3, 7, 20)

# %%
abstractData

# %%
pdf3TokenizedData = tokenizeData(abstractData)

# %%
pdf3TokenizedData

# %%
pdf3AbstractData = removeSpecialChar(pdf3TokenizedData)

# %%
filtered_words = removeStopWords(pdf3AbstractData)

# %%
filtered_words[:10]

# %%
stemmedData = stemming(filtered_words)

# %%
stemmedData[:10]

# %%
lemmatizeData = lemmatize(stemmedData)

# %%
lemmatizeData[:10]

# %%
countFeatures3 = countFeatures(lemmatizeData)

# %%
"""
**For example let's consider `Algorithm`**
"""

# %%
countFeatures3["algorithm"]

# %%
tfidfFeatures3 = tfidfFeatures(lemmatizeData)

# %%
tfidfFeatures3["object"]

# %%
"""
### `CONCLUSION`: Hence, we have successfully implemented and observed some of the features and preprocessing required on the data set for the training process. We have also done the required feature engineering on the `Abstract` data from the research papers.
"""

# %%
