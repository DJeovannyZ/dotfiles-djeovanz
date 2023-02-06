from libqtile.config import Screen

from core.bar import bar, bar1
from utils import config

screens = [
  Screen(
    wallpaper = config['wallpaper'],
    wallpaper_mode = 'fill',
    top = bar,
  ),

  Screen(
    wallpaper = config['wallpaper'],
    wallpaper_mode = 'fill',
    top = bar1,
  ),
]
