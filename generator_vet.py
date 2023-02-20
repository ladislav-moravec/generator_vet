import random


class GeneratorVet:
    # Třída reprezentuje generátor náhodných vět

    privlastky = ["modrý", "velký", "hubený", "nejlepší", "automatizovaný"]
    podmety = ["jednorožec", "programátor", "manažer", "hroch", "T-rex"]
    prislovce = ["rychle", "s oblibou", "hodně", "málo", "se zpožděním"]
    slovesa = ["spal", "ležel", "vařil", "uklízel", "derivoval"]
    pum = ["pod stolem", "v lese", "u babičky", "v práci", "na stole"]

    # Vrátí náhodné slovo z listu
    def nahodne_slovo(self, pole):
        slovo = random.choice(pole)
        return slovo

    # Vrátí náhodnou větu
    def generuj(self):

        return "{0} {1} {2} {3} {4}".format(
            self.nahodne_slovo(self.privlastky),
            self.nahodne_slovo(self.podmety),
            self.nahodne_slovo(self.prislovce),
            self.nahodne_slovo(self.slovesa),
            self.nahodne_slovo(self.pum)
        )
