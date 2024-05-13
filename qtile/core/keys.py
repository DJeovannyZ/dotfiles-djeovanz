from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from extras import float_to_front
from utils import config

keys, mod, alt = [ ], 'mod4', 'mod1'
terminal = config['terminal'].copy()

if not terminal['main']:
  terminal['main'] = guess_terminal()

for key in [
    
    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "x", lazy.next_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "m", lazy.spawn("/home/djeovanz/.config/rofi/launchers/type-5/launcher.sh")),
    ([mod, "control"], "m", lazy.spawn("/home/djeovanz/.config/rofi/applets/bin/quicklinks.sh")),
    ([mod, "control"], "l", lazy.spawn("/home/djeovanz/.config/rofi/applets/bin/powermenu.sh")),

    # Window Nav

    # Browser
    ([mod], "b", lazy.spawn("brave")),

    # File Explorer
    ([mod], "e", lazy.spawn("dolphin")),

    # Terminal
    ([mod], "Return", lazy.spawn("kitty")),
    ([mod], "i", lazy.spawn("setxkbmap us")),
    ([mod], "o", lazy.spawn("setxkbmap -layout es -variant winkeys")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 4000")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

     # Screenshot
    ([mod], "s", lazy.spawn("/home/djeovanz/.config/rofi/applets/bin/screenshot.sh")),

    ([mod], "c", lazy.spawn("code")),
    ([mod], "v", lazy.spawn("/home/djeovanz/.config/rofi/applets/bin/clipboard.sh")),
    ([mod], "p", lazy.spawn("skanlite")),
    ([mod], "u", lazy.spawn("discord")),
    # ------------ Hardware Configs ------------



  # # Switch between windows
  # ([mod], 'h', lazy.layout.left()),
  # ([mod], 'l', lazy.layout.right()),
  # ([mod], 'j', lazy.layout.down()),
  # ([mod], 'k', lazy.layout.up()),

  # # Move windows between columns
  # ([mod, 'shift'], 'h', lazy.layout.shuffle_left()),
  # ([mod, 'shift'], 'l', lazy.layout.shuffle_right()),
  # ([mod, 'shift'], 'j', lazy.layout.shuffle_down()),
  # ([mod, 'shift'], 'k', lazy.layout.shuffle_up()),

  # # Increase/decrease window size
  # ([mod], 'i', lazy.layout.grow()),
  # ([mod], 'm', lazy.layout.shrink()),

  # # Window management
  # ([mod, 'shift'], 'space', lazy.layout.flip()),
  # ([mod], 'o', lazy.layout.maximize()),
  # ([mod], 'n', lazy.layout.normalize()),
  # ([mod], 'a', lazy.window.kill()),
  # ([ ], 'F11', lazy.window.toggle_fullscreen()),

  # # Floating window management
  # ([mod], 'space', lazy.window.toggle_floating()),
  # ([mod], 'c', lazy.window.center()),
  # ([mod], 'f', lazy.function(float_to_front)),

  # # Toggle between layouts
  # ([mod], 'Tab', lazy.next_layout()),

  # # Qtile management
  ([mod, 'control'], 'b', lazy.hide_show_bar()),
  # ([mod, 'control'], 's', lazy.shutdown()),
  # ([mod, 'control'], 'r', lazy.reload_config()),
  # ([mod, alt], 'r', lazy.restart()),

  # # Kill X11 session
  # ([mod, alt], 's', lazy.spawn('kill -9 -1')),

  # # Terminal
  # ([mod], 'Return', lazy.spawn(terminal['main'])),
  # ([mod, 'shift'], 'Return', lazy.spawn(terminal['floating'])),

  # # Application Launcher
  # ([mod, 'shift'], 'r', lazy.spawn('rofi -show window')),
  # ([mod], 'r', lazy.spawn('rofi -show drun')),

  # # Web Browser
  # ([mod], 'b', lazy.spawn(config['browser'])),

  # # Screenshot Tool
  # ([ ], 'Print', lazy.spawn('gnome-screenshot -i')),

  # # Backlight
  # ([mod], 'XF86AudioLowerVolume', lazy.spawn('brightnessctl set 5%-')),
  # ([mod], 'XF86AudioRaiseVolume', lazy.spawn('brightnessctl set +5%')),

  # Volume
  ([ ], 'XF86AudioMute', lazy.spawn('pamixer --toggle-mute')),
  ([ ], 'XF86AudioLowerVolume', lazy.spawn('pamixer --decrease 5')),
  ([ ], 'XF86AudioRaiseVolume', lazy.spawn('pamixer --increase 5')),

  # Player
  ([ ], 'XF86AudioPlay', lazy.spawn('playerctl play-pause')),
  ([ ], 'XF86AudioPrev', lazy.spawn('playerctl previous')),
  ([ ], 'XF86AudioNext', lazy.spawn('playerctl next')),
]: keys.append(Key(*key)) # type: ignore
