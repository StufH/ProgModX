class Bil:
    def __init__(self, merke: str, hestekrefter: int) -> None:
        self.merke = merke
        self.hestekrefter = hestekrefter

    def __str__(self) -> str:
        return f"{self.merke}, {self.hestekrefter}hk"

    def kjor(self) -> None:
        if self.hestekrefter < 250:
            print(f"{self.merke}en kjører sakte!")
        else:
            print(f"{self.merke}en kjører fort!")

    def hent_info(self) -> None:
        print(f"{self.merke}en har {self.hestekrefter} hestekrefter")

volvo: Bil = Bil("Volvo", 200)
bmw: Bil = Bil("BMW", 300)

volvo.kjor()
volvo.hent_info()

print("")

bmw.kjor()
bmw.hent_info()

print("")

print(volvo)
print(bmw)

