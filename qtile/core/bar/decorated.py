from libqtile.bar import CALCULATED
from libqtile.lazy import lazy

from core.bar.utils import base, decoration, iconFont, powerline
from extras import Clock, GroupBox, modify, TextBox, Volume, widget
from utils import color

tags = [
  '', '', '', '', '', '', '󰓇',  'ﭮ',  '󰖳', 
]

bar = {
  'background': color['obg'],
  'border_color': color['obg'],
  'border_width': 6,
  'margin': [10, 10, 0, 10],
  'opacity': 0.8,
  'size': 28,
}

def sep(fg: str, offset = 0, padding = 8) -> TextBox:
  return TextBox(
    **base(None, fg),
    **iconFont(),
    offset = offset,
    padding = padding,
    text = '󰇙',
  )

def logo(bg: str, fg: str) -> TextBox:
  return modify(
    TextBox,
    **base(bg, fg),
    **decoration(),
    **iconFont(),
    mouse_callbacks = { 'Button1': lazy.restart() },
    offset = 4,
    padding = 17,
    text = '',
  )

def groups(bg: str) -> GroupBox:
  return GroupBox(
    **iconFont(),
    background = bg,
    borderwidth = 1,
    rounded = True,
    # highlight_color = color['polar_night_3'],
    highlight_color = bg, 
    colors = [
      color['aurora_red'], color['aurora_orange'], color['aurora_yellow'],
      color['aurora_green'], color['aurora_cyan'], color['aurora_pink'],
      color['aurora_blue'], color['aurora_purple'], color['aurora_red'],
    ],
    # highlight_color = ['000000', '282828'],
    highlight_method = 'line',
    inactive = color['inactive'],
    invert = True,
    padding = 5,
    rainbow = True,
  )

def window_name(bg: str, fg: str) -> object:
  return widget.WindowName(
    **base(bg, fg),
    format = ' {name}',
    max_chars = 60,
    width = CALCULATED,
  )
def systrai(bg: str, fg: str) -> object:
  return widget.Systray(
    **base(bg, fg),
    padding = 5,
  )

def allWidgets(bg: str, fg: str) -> list:
  return [
    modify(
      TextBox,
      **base(bg, color['aurora_red']),
      **decoration('left'),
      **iconFont(),
      text = '',
      x = 4,
    ),
    modify(
      Volume,
      **base(bg, color['aurora_red']),
      **powerline('arrow_right'),
      commands = {
        'decrease': 'pamixer --decrease 5',
        'increase': 'pamixer --increase 5',
        'get': 'pamixer --get-volume-human',
        'mute': 'pamixer --toggle-mute',
      },
      update_interval = 0.1,
    ),
    TextBox(
      **base(bg, color['aurora_green']),
      **iconFont(),
      offset = -1,
      text = '󰏕',
      x = -5,
    ),
    widget.CheckUpdates(
      **base(bg, color['aurora_green']),
      # **decoration('right'),
      colour_have_updates = color['aurora_green'],
      colour_no_updates = color['aurora_green'],
      display_format = '{updates} updates  ',
      distro = 'Arch_checkupdates',
      initial_text = 'Up To Date ',
      no_update_string = 'Up To Date ',
      padding = 0,
      update_interval = 3600,
    ),
    # widget.CurrentScreen(
    #   **base(bg, fg),
    #   # **decoration('right'),
    #   active_text = '',
    #   active_color = fg,
    #   inactive_text = '',
    #   inactive_color = fg,
    # ),
    TextBox(
      **base(bg, color['aurora_yellow']),
      **iconFont(),
      offset = -2,
      padding = 5,
      text = '﬙',
      x = -2,
    ),
    widget.Memory(
      **base(bg, color['aurora_yellow']),
      # **powerline('arrow_right'),
      format = '{MemUsed: .0f}{mm} ',
      padding = -1,
    ),
    modify(
      TextBox,
      **base(bg, color['aurora_cyan']),
      # **decoration('left'),
      **iconFont(),
      offset = 3,
      text = '',
      x = 5,
    ),
    widget.CPU(
      **base(bg, color['aurora_cyan']),
      **powerline('arrow_right'),
      format = '{load_percent:.0f}%',
    ),
    TextBox(
      **base(bg, color['aurora_purple']),
      **iconFont(),
      offset = -1,
      text = '󰋊',
      x = -5,
    ),
    widget.DF(
      **base(bg, color['aurora_purple']),
      # **decoration('right'),
      format = '{f} GB',
      padding = 0,
      partition = '/',
      visible_on_warn = False,
      warn_color = fg,
    ),
    widget.CurrentLayoutIcon(
      **base(bg, color['aurora_orange']),
      **decoration('right'),
      padding = 10,
      scale = 0.5,
    ),
  ]

def clock(bg: str, fg: str) -> list:
  return [
    modify(
      TextBox,
      **base(bg, fg),
      **decoration('left'),
      **iconFont(),
      offset = 2,
      text = '',
      x = 4,
    ),
    modify(
      Clock,
      **base(bg, fg),
      **decoration('right'),
      format = '%A - %I:%M %p ',
      long_format = '%B %-d, %Y ',
      padding = 6,
    ),
  ]


widgets = [
  widget.Spacer(length = 2),
  logo(color['frost_3'], color['obg']),
  sep(color['kbg'], offset = -8),
  groups(color['obg']),
  sep(color['kbg'], offset = 4, padding = 4),

  widget.Spacer(),
  window_name(None, color['aurora_cyan']),
  widget.Spacer(),

  *allWidgets(color['kbg'], color['bg']),
  sep(color['kbg']),
  systrai(None, color['fg']),
  # *clock(color['magenta'], color['bg']),
  widget.Spacer(length = 2),
]

