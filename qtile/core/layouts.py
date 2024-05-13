from libqtile import layout
from libqtile.config import Match

from utils import color

# ---- Tiling ---------------------------- #
config = {
  'border_focus': color['polar_night_3'],
  'border_normal': color['polar_night_0'],
  'border_width': 1,
  'margin': 5,
  'single_border_width': 2,
  'single_margin': 10,
}

layouts = [
  layout.MonadTall(
    **config,
    change_ratio = 0.02,
    min_ratio = 0.30,
    max_ratio = 0.70,
  ),
  layout.Max(**config),
  layout.Matrix(**config),
]

# ---- Floating -------------------------- #
floating_layout = layout.Floating(
  border_focus = color['polar_night_3'],
  border_normal = color['polar_night_0'],
  border_width = 0,
  fullscreen_border_width = 0,

  float_rules = [
    *layout.Floating.default_float_rules,
    Match(wm_class = [
      'confirmreset',
      'gnome-screenshot',
      'lxappearance',
      'makebranch',
      'maketag',
      'psterm',
      'ssh-askpass',
      'thunar',
      'Xephyr',
      'xfce4-about',
      'wm',
    ]), # type: ignore

    Match(title = [
      'branchdialog',
      'File Operation Progress',
      'minecraft-launcher',
      'Open File',
      'pinentry',
      'wm',
      'Java',
      'java',
    ]), # type: ignore
  ],
)
