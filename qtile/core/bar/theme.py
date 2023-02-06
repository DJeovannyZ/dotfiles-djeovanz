from importlib import import_module
from libqtile.bar import Bar

from utils import config

themes = [
  'decorated'
]

if config['bar'] in themes:
  module = import_module(f"core.bar.{config['bar']}")
  module2 = import_module(f"core.bar.{config['secondBar']}")
  module.bar.update(
    { 'widgets': module.widgets }
  )
  module2.bar.update(
    { 'widgets': module2.widgets }
  )

  bar: tuple[Bar | None,Bar | None, list] = (
    Bar(**module.bar),
    Bar(**module2.bar),
    module.tags,
  )
else:
  bar = ( None, None, [None] * 10 )
