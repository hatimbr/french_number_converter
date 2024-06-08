class FrenchConverter:
    def __init__(self):
        self._units = {
            0: "zéro",
            1: "un",
            2: "deux",
            3: "trois",
            4: "quatre",
            5: "cinq",
            6: "six",
            7: "sept",
            8: "huit",
            9: "neuf",
            10: "dix",
            11: "onze",
            12: "douze",
            13: "treize",
            14: "quatorze",
            15: "quinze",
            16: "seize",
        }
        self._tens = {
            1: "dix",
            2: "vingt",
            3: "trente",
            4: "quarante",
            5: "cinquante",
            6: "soixante",
            7: "soixante-dix",
            8: "quatre-vingts",
            9: "quatre-vingt-dix",
        }

        self._correction_units = {
            "dix-et-un": "onze",
            "dix-deux": "douze",
            "dix-trois": "treize",
            "dix-quatre": "quatorze",
            "dix-cinq": "quinze",
            "dix-six": "seize",
            "soixante-onze": "soixante-et-onze",
            "quatre-vingt-et-un": "quatre-vingt-un",
            "ts-": "t-",
            "es-": "e-",
        }

    def _correct_units(self, result: str) -> str:
        for key, value in self._correction_units.items():
            if key in result:
                result = result.replace(key, value)

        return result

    def _to_sixteen(self, number: int) -> str:
        return self._units.get(number)
    
    def _to_hundred(self, number: int) -> str:
        if number % 10 == 0:
            return self._tens.get(number // 10)
        elif number % 10 == 1:
            result = self._tens.get(number // 10) + "-et-un"
        else:
            result = self._tens.get(number // 10) + "-" + self._units.get(number % 10)

        return result
    
    def _to_thousand(self, number: int) -> str:
        if number // 100 == 1:
            result = "cent"
        else:
            result = self._units.get(number // 100) + "-cents"
        
        if number % 100 == 0:
            if number // 100 == 8:
                result + "s"
            return result
        else:
            return result + "-" + self.convert(number % 100)
        
    def _to_million(self, number: int) -> str:
        if number // 1000 == 1:
            result = "mille"
        else:
            result = self.convert(number // 1000) + "-milles"
        
        if number % 1000 == 0:
            return result
        else:
            return result + "-" + self.convert(number % 1000)
    
    
    def convert(self, number: int) -> str:
        if number < 17:
            result = self._to_sixteen(number)
        elif number < 100:
            result =  self._to_hundred(number)
        elif number < 1000:
            result =  self._to_thousand(number)
        elif number < 1000000:
            result =  self._to_million(number)
        
        return self._correct_units(result)
