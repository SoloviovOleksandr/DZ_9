class TextProcessor:
    def __init__(self):
        self._flag = False
    def get_clean_string(self,sentense):
        result = ""
        for i in sentense:
            if not self.__is_punctuation(i):
                result += i
        return result
    def __is_punctuation(self,letter):
        if letter.isalnum():
            self.__flag = False
        else:
            self.__flag = True
            return self.__flag
f = TextProcessor()
print(f.get_clean_string("kfkkfkfk,kffkfkf"))

class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = ""

    @property
    def clean_string(self):
            print("Printing clean string")
            return self.__clean_string

    def set_clean_text(self, text):
            self.__clean_string = self.__text_processor.get_clean_string(text)

loader = TextLoader()
loader.set_clean_text('jfksjfkkdgjkdjgk,,,,d;d;sfjkj')
print(loader.clean_string)

class DataInterface:
    def __init__(self):
        self._text_loader = TextLoader()

    def process_text(self, list_strings: list):
     for sentense in list_strings:
        self._text_loader.set_clean_text(sentense)
        print(self._text_loader.clean_string)
data = DataInterface()
data.process_text(["***!!!kolfof","**,,,,b9lboblfn","ko/p//" ])
