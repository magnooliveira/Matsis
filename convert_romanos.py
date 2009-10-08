class Romano(object):

    def __init__(self):
        self.DIC_CONVERSION = {'I':1,
                               'V':5,
                               'X':10,
                               'L':50,
                               'C':100,
                               'D':500,
                               'M':1000}

    def convert_Romano(self,numero_romano):

        result = 0
        for number in range(len(numero_romano)):
            if number+1 < len(numero_romano) and self.DIC_CONVERSION[numero_romano[number]]<self.DIC_CONVERSION[numero_romano[number+1]]:
                result-=self.DIC_CONVERSION[numero_romano[number]]
            else:
                result+=self.DIC_CONVERSION[numero_romano[number]]
        return result
