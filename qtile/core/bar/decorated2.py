from libqtile.bar import CALCULATED
from libqtile.lazy import lazy

from core.bar.utils import base, decoration, iconFont, powerline
from extras import Clock, GroupBox, modify, TextBox, Volume, widget
from utils import color

tags = [
  '', '', '', '', '', '', '󰓇',  'ﭮ',  '󰖳', 
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
   
def allWidgets(bg: str, fg: str) -> list:
  return [
    # widget.CurrentScreen(
    #   **base(bg, fg),
    #   # **decoration('right'),
    #   active_text = '',
    #   active_color = fg,
    #   inactive_text = '',
    #   inactive_color = fg,
    # ),
    widget.Net(
      **base(bg, color['aurora_cyan']),
      **decoration('left'),
      padding = 2,
      interface='eno1',
      format=' 󰈀 {down}   {up}   ',
    ),
    modify(
      TextBox,
      **base(bg, color['aurora_pink']),
      **decoration('right'),
      **iconFont(),
      offset = 2,
      text = '',
      x = 4,
    ),
    modify(
      Clock,
      **base(bg, color['aurora_pink']),
      format = '%A - %I:%M %p ',
      long_format = '%B %-d, %Y ',
      padding = 6,
    ),
  ]

def clock(bg: str, fg: str) -> list:
  return [
  ]


widgets = [
  widget.Spacer(length = 2),
  logo(color['frost_3'], color['obg']),
  sep(color['black'], offset = 4, padding = 4),
  groups(color['obg']),
  sep(color['black'], offset = 4, padding = 4),

  widget.Spacer(),
  window_name(None, color['aurora_cyan']),
  widget.Spacer(),

  *allWidgets(color['kbg'], color['bg']),
  # *clock(color['magenta'], color['bg']),
  widget.Spacer(length = 2),
]

