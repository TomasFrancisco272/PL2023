class Distribuicao:
    def __init__(self, dict):
        for member in dict:
            setattr(self, member, 0)