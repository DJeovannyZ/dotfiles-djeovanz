import json

from utils import dir
from utils.settings import config

colorschemes = [
  'catppuccin',
  'nord',
]

if config['colorscheme'] in colorschemes:
  colorscheme = f"{config['colorscheme']}.json"
else:
  colorscheme = 'nord.json'

path = f'{dir.get()}/utils/colorscheme/{colorscheme}'

with open(path, 'r') as file:
  color = json.load(file)
