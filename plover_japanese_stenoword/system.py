from plover.system import english_stenotype

KEYS = (
    'P-', 'T-', 'H-', 'K-', 'S-',
    'L-', 'M-',
    '*',
    '-N', '-R',
    '-U', '-A', '-I',
    '-O', '-E'
)

IMPLICIT_HYPHEN_KEYS = KEYS

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = '*'

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Keyboard': {
        'P-': 'a',
        'T-': 's',
        'H-': 'd',
        'K-': 'f',
        'S-': 'g',
        'L-': 'c',
        'M-': 'v',
        '*': 'b',
        '-N': 'n',
        '-R': 'm',
        '-U': 'h',
        '-A': 'j',
        '-O': 'k',
        '-I': 'l',
        '-E': 'p',
        'arpeggiate': 'space',
    },
}

DICTIONARIES_ROOT = 'asset:plover_japanese_stenoword:dictionaries'
DEFAULT_DICTIONARIES = ('StenoWord.json', 'commands.json', 'users.json')
