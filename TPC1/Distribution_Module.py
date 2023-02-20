class Distribuicao:
    def _init_(self, dict):
        for member in dict:
            setattr(self, member, 0)