class Gato:
    color="default"
    def hablar (self):
        print(f"Miau, soy un gato {self.color}")

Atigrado=Gato()
Atigrado.color='cafe'
Atigrado.hablar()

Gris=Gato()
Gris.color='gris'
Gris.hablar()