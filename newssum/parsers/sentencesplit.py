from .parser import BaseParser
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
from sumy.utils import get_stop_words


class SentenceSplittedParser(BaseParser):
    """
    Parse text from a list of strings: text = ["text sentence 1", "text sentence 2", ...]
    """

    def __init__(self, text, pos_tagger=pos_tag, keep_only_n_and_adj=True, remove_stopwords=True,
                 stemming_mode="stemming"):
        #text is a list of sentences
        self.body = " ".join(text)
        self.sents = text
        super().__init__(word_tokenize, get_stop_words("english"), pos_tagger, keep_only_n_and_adj, remove_stopwords,
                         stemming_mode)
