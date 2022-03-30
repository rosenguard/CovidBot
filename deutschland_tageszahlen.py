import requests

class Deutschland:
    def wocheninzidenz(self):
        response = requests.get("https://api.corona-zahlen.org/germany")
        response_info = response.json()
        return round(response_info["weekIncidence"], 2)

    def rwert(self):
        response = requests.get("https://api.corona-zahlen.org/germany")
        response_info = response.json()
        btw = response_info["r"]["value"]
        btw = round(btw, 2)
        return btw

    def todesfaelle(self):
        response = requests.get("https://api.corona-zahlen.org/germany")
        response_info = response.json()
        return int(response_info["deaths"])

    def geimpft(self):
        response = requests.get("https://api.corona-zahlen.org/vaccinations")
        response_info = response.json()
        return response_info["data"]["vaccinated"]

    def vollgeimpft(self):
        response = requests.get("https://api.corona-zahlen.org/vaccinations")
        response_info = response.json()
        return response_info["data"]["secondVaccination"]["vaccinated"]

    def impfquote(self):
        response = requests.get("https://api.corona-zahlen.org/vaccinations")
        response_info = response.json()
        return round(response_info["data"]["secondVaccination"]["quote"], 2)

    def genesene(self):
        response = requests.get("https://api.corona-zahlen.org/germany")
        response_info = response.json()
        return response_info["recovered"]

    def allefaelle(self):
        response = requests.get("https://api.corona-zahlen.org/germany")
        response_info = response.json()
        return int(response_info["cases"])

class Bundeslaender:
    def wocheninzidenz(self,bd:str):
        response = requests.get("https://api.corona-zahlen.org/states")
        response_info = response.json()
        return round(response_info["data"]["{}".format(bd)]["weekIncidence"], 2)
    
    def genesen(self,bd:str):
        response = requests.get("https://api.corona-zahlen.org/states")
        response_info = response.json()
        return response_info["data"]["{}".format(bd)]["recovered"]

    def geimpft(self,bd:str):
        response = requests.get("https://api.corona-zahlen.org/vaccinations")
        response_info = response.json()
        return response_info["data"]["states"]["{}".format(bd)]["vaccinated"]
    
    def vollgeimpft(self,bd:str):
        response = requests.get("https://api.corona-zahlen.org/vaccinations")
        response_info = response.json()
        return response_info["data"]["states"]["{}".format(bd)]["secondVaccination"]["vaccinated"]

    def impfquote(self,bd:str):
        response = requests.get("https://api.corona-zahlen.org/vaccinations")
        response_info = response.json()
        return round(response_info["data"]["states"]["{}".format(bd)]["quote"], 2)   

    def todesfaelle(self,bd:str):
        response = requests.get("https://api.corona-zahlen.org/states")
        response_info = response.json()
        return response_info["data"]["administeredVaccinations"][f"{bd}"]["deaths"]

    def allefaelle(self,bd:str):
        response = requests.get("https://api.corona-zahlen.org/states")
        response_info = response.json()
        return response_info["data"][f"{bd}"]["cases"]


class Staedte:
    def wocheninzidenz(self, ct:str):
        response = requests.get("https://api.corona-zahlen.org/districts")
        response_info = response.json()
        save = None
        temp = None
        try:
            for ags in response_info["data"]:
                temp = response_info["data"][ags]
                if ct.capitalize() in temp["name"]:
                    save = temp["weekIncidence"]
                    break
            save = round(save, 2)
            return save
        except:
            print("error kek")
            return "error"
    
    def todesfaelle(self, ct:str):
        response = requests.get("https://api.corona-zahlen.org/districts")
        response_info = response.json()
        save = None
        temp = None
        try:
            for ags in response_info["data"]:
                temp = response_info["data"][ags]
                if ct in temp["name"]:
                    save = temp["deaths"]
            return save
        except:

            return "error"

    def allefaelle(self, ct:str):
        response = requests.get("https://api.corona-zahlen.org/districts")
        response_info = response.json()
        save = None
        temp = None
        try:
            for ags in response_info["data"]:
                temp = response_info["data"][ags]
                if ct in temp["name"]:
                    save = temp["cases"]
            return save
        except:
            return "error"


a = Staedte()

print(a.wocheninzidenz("Bochum"))