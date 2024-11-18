class Bil:
    def __init__(self, merke: str, hestekrefter: int) -> None:
        self.merke = merke
        self.hestekrefter = hestekrefter

    def kjør(self) -> None:
        if self.hestekrefter < 250:
            print(f"{self.merke}en kjører sakte!")
        else:
            print(f"{self.merke}en kjører fort!")

    def hent_info(self) -> None:
        print(f"{self.merke}en har {self.hestekrefter} hestekrefter")

volvo: Bil = Bil("volvo", 200)
BMW: Bil = Bil("BMW", 300)
volvo.kjør()
volvo.hent_info()
print("")
BMW.kjør()
BMW.hent_info()
