
from pyscript import document


# Book Club Member Lookup

def get_fullname(e):
    book_club = {
        ('isabella', 'allas'): 'Isabella Esguerra',
        ('lindsay', 'esguerra'): 'Lindsay Esguerra',
        ('athena', 'alfaro'): 'Athena Alfaro'
    }

    namef = document.getElementById('fname').value.lower().strip()
    namel = document.getElementById('lname').value.lower().strip()

    result = document.getElementById('div1')

    message = book_club.get((namef, namel), 'Sorry, your name is not in the list.')

    result.innerHTML = message + (' is in the book club!' if (namef, namel) in book_club else '')


# Add Club Members

gradeten = {'Athena Alfaro', 'Bela Allas', 'Lindsay Esguerra'}

gradenine = {'Katniss Everdeen', 'Jude Duarte', 'Evangeline Fox'}

gradeeight = {'Daisy Maria', 'Lara Jean Covey', 'Clementine West'}

gradeseven = {'Cecilia Lisbon', 'Susanna Kaysen', 'Esther Greenwood'}

superset = gradeten | gradenine | gradeeight | gradeseven


def getname(event):
    firstname = document.getElementById('fname').value.title().strip()
    lastname = document.getElementById('lname').value.title().strip()

    full_name = firstname + ' ' + lastname

    superset.add(full_name)

    output = document.getElementById('output')
    output.innerHTML = '<h3>Club Members</h3>'

    for name in sorted(superset):
        output.innerHTML += f'<p>{name}</p>'

    output.innerHTML += f'<p>Total students: {len(superset)}</p>'


# Non-Metal Element Checker

Elements = {
    'H': {
        'name': 'Hydrogen',
        'atomic_number': 1,
        'atomic_mass': 1.008
    },
    'He': {
        'name': 'Helium',
        'atomic_number': 2,
        'atomic_mass': 4.0026
    },
    'C': {
        'name': 'Carbon',
        'atomic_number': 6,
        'atomic_mass': 12.011
    },
    'N': {
        'name': 'Nitrogen',
        'atomic_number': 7,
        'atomic_mass': 14.007
    },
    'O': {
        'name': 'Oxygen',
        'atomic_number': 8,
        'atomic_mass': 15.999
    },
    'F': {
        'name': 'Fluorine',
        'atomic_number': 9,
        'atomic_mass': 18.998
    },
    'Ne': {
        'name': 'Neon',
        'atomic_number': 10,
        'atomic_mass': 20.180
    },
    'P': {
        'name': 'Phosphorus',
        'atomic_number': 15,
        'atomic_mass': 30.974
    },
    'S': {
        'name': 'Sulfur',
        'atomic_number': 16,
        'atomic_mass': 32.06
    },
    'Cl': {
        'name': 'Chlorine',
        'atomic_number': 17,
        'atomic_mass': 35.45
    },
    'Ar': {
        'name': 'Argon',
        'atomic_number': 18,
        'atomic_mass': 39.948
    },
    'Se': {
        'name': 'Selenium',
        'atomic_number': 34,
        'atomic_mass': 78.971
    },
    'Br': {
        'name': 'Bromine',
        'atomic_number': 35,
        'atomic_mass': 79.904
    },
    'Kr': {
        'name': 'Krypton',
        'atomic_number': 36,
        'atomic_mass': 83.798
    },
    'I': {
        'name': 'Iodine',
        'atomic_number': 53,
        'atomic_mass': 126.904
    },
    'Xe': {
        'name': 'Xenon',
        'atomic_number': 54,
        'atomic_mass': 131.293
    },
    'Rn': {
        'name': 'Radon',
        'atomic_number': 86,
        'atomic_mass': 222
    }
}


def get_element(e):
    symbol = document.getElementById('Elements').value.strip().capitalize()

    result = document.getElementById('result')
    element = Elements.get(symbol)

    message = element and f"""
        <h3>{symbol} - {element['name']}</h3>
        <p><strong>Element Symbol:</strong> {symbol}</p>
        <p><strong>Element Name:</strong> {element['name']}</p>
        <p><strong>Atomic Number:</strong> {element['atomic_number']}</p>
        <p><strong>Atomic Mass:</strong> {element['atomic_mass']}</p>
    """ or 'This element does not exist in the non-metals list.'

    result.innerHTML = message
