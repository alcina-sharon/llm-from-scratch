import re

class Tokenizer:
    def __init__(self, vocab):
        self.token_id = vocab
        self.id_token = {i:j for j,i in self.token_id.items()}

    def encode(self, text):
        result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        inputStrList = [i.strip() for i in result if i.strip()]
        cleanedInputStrList = [
            word if word in self.token_id else "<|unknown|>" for word in inputStrList
        ]
        return [self.token_id[i] for i in cleanedInputStrList]
    
    def decode(self, inputIdList):
        listOfIds = [self.id_token[i] for i in inputIdList]
        sentence = " ".join(listOfIds)
        final = re.sub(r'\s+([,.?!"()\'])', r'\1', sentence) # if space & punctuation generated, then replace it with punctuation alone.
        #\1 means group one; 0th group is space and punctuation; 1st is (punctuations)
        return final