class langClass:
    def __init__(self,language: str,bits: int):
        self.language = language
        self.bits = bits
    def __str__(self):
        return f"{self.language}: {self.bits}"
    def makeStr(self,dat):
        return strType(self,dat)

class strType(langClass):
    def __init__(self, parent, dat):
        super().__init__(parent.language, parent.bits)
        self.__dat=dat
    def __str__(self):
        return super().__str__()+". "+self.__dat
    def knowSelf(self):
        print(f"self: {self.__dict__}")
        print(f"self type: {type(self)}")

def main():
    py = langClass("Python",1625)
    mystr=py.makeStr("wow")
    print(py)
    mystr.knowSelf()


if __name__ == "__main__": main()