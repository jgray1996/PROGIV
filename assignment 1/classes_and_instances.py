class Atom:
    def __init__(self, symbol: str, atomic_number: int, neutrons: int) -> None:
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.neutrons = neutrons

    def __repr__(self):
        return f"{self.symbol}({self.atomic_number}, {self.neutrons})"

    def __lt__(self, other) -> bool:
        self._validate_comparison(other)
        return self.mass_number() < other.mass_number()

    def __eq__(self, other) -> bool:
        self._validate_comparison(other)
        return self.neutrons == other.neutrons

    def __gt__(self, other) -> bool:
        self._validate_comparison(other)
        return self.mass_number() > other.mass_number()

    def __ne__(self, other) -> bool:
        self._validate_comparison(other)
        return self.neutrons != other.neutrons

    def __le__(self, other) -> bool:
        self._validate_comparison(other)
        return self.mass_number() <= other.mass_number()

    def __ge__(self, other) -> bool:
        self._validate_comparison(other)
        return self.mass_number() >= other.mass_number()

    def proton_number(self) -> int:
        return self.atomic_number

    def mass_number(self) -> int:
        return self.atomic_number + self.neutrons

    def isotope(self, neutrons: int) -> None:
        self.neutrons = neutrons

    def _validate_comparison(self, other):
        if not isinstance(other, Atom):
            raise TypeError("Comparisons must be between Atom instances")
        if self.symbol != other.symbol:
            raise TypeError(
                "Comparisons must be between isotopes of the same element")


class Molecule:

    def __init__(self,
                 atoms: list) -> None:
        self.atoms = atoms
        self.name = self.render_molecule()

    def __add__(self, other) -> str:
        # This is incorrect
        # The add-method shoud return a new Molecule. In your realisation you
        # just return a string.
        return f"{self.render_molecule()}\
            {other.render_molecule()}"

    def __repr__(self) -> str:
        # why us a formatted string here? You are only formatting self.name,
        # which is already a string... 🤔
        return f"{self.name}"

    def render_molecule(self) -> str:
        molecule = ""
        for atom in self.atoms:
            molecule += atom[0].symbol
            if atom[1] > 1:
                molecule += str(atom[1])
        return molecule


class Chloroplast:

    water = 0
    co2 = 0

    def __repr__(self):
        return f"Chloroplast class containing {self.water} water molecules and {self.co2} CO2 molecules..."

    def add_molecule(self, molecule: Molecule) -> None:
        if molecule == None:
            return []
        try:
            if molecule.name == "CO2":
                self.co2 += 1
            elif molecule.name == "H2O":
                self.water += 1
            else:
                raise ValueError
        except ValueError:
            # Better to raise the error outside of the method, so that users of the method
            # know something is wrong with their input.
            return []

        if self.water >= 12 and \
                self.co2 >= 6:
            self.water -= 12
            self.co2 -= 6
            return (Molecule([(carbon, 6), (hydrogen, 12), (oxygen, 6)]),
                    Molecule([(oxygen, 6)]))
        else:
            return []


hydrogen = Atom('H', 1, 0)
carbon = Atom('C', 6, 6)
oxygen = Atom('O', 8, 8)

water = Molecule([(hydrogen, 2), (oxygen, 1)])
co2 = Molecule([(carbon, 1), (oxygen, 2)])
demo = Chloroplast()
els = [water, co2]

while (True):
    print('\nWhat molecule would you like to add?')
    print('[1] Water')
    print('[2] carbondioxyde')
    print('Please enter your choice: ', end='')
    try:
        choice = int(input())
        res = demo.add_molecule(els[choice-1])
        if (len(res) == 0):
            print(demo)
        else:
            print('\n=== Photosynthesis!')
            print(res)
            print(demo)

    except Exception:
        print('\n=== That is not a valid choice.')
