from enum import Enum

class Formacao(str, Enum): 
    mestre = "MESTRE"
    doutor = "DOUTOR"
    phd = "PHD"