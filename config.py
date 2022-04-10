# -*- coding: utf-8 -*-
# http://docs.qtile.org/en/latest/index.html
from libqtile.dgroups import simple_key_binder
import os
import random
import subprocess
import socket
from libqtile import qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen  # , KeyChord
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal
from typing import List  # noqa: F401from typing import List  # noqa: F401
from libqtile.log_utils import logger
from libqtile.widget import base

mod = "mod4"  # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"  # My terminal of choice
myBrowser = "google-chrome"  # My browser of choice
myEditor = "code" # My code editor of choice

groups = [Group(i, layout="monadtall") for i in "123456789"]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group

dgroups_key_binder = simple_key_binder("mod4")

widget_background_color_schemes = {
    "pastel": [
        "#fbf8cc",
        "#fde4cf",
        "#ffcfd2",
        "#f1c0e8",
        "#cfbaf0",
        "#a3c4f3",
        "#90dbf4",
        "#8eecf5",
        "#98f5e1",
        "#b9fbc0",
    ],
    "spacedust": [
        "#fefff1",
        "#f1c0e8",
        "#ffc878",
        "#ff8a3a",
        "#c9d9c2",
        "#aecab8",
        "#67a0ce",
        "#83a7b4",
        "#ecf0c1",
        "#fbf8cc",
    ],
    "spacedust2": [
        "#f0f1ce",
        "#e3cd7b",
        "#e35b00",
        "#5cab96",
        "#06afc7",
        "#67a0ce",
        "#9b7f64",
        "#e35b00",
    ],
    "spacedust3": [
        "#9b7f64",
        "#ff8a3a",
        "#5cab96",
        "#e3cd7b",
        "#67a0ce",
        "#f0f1ce",
        "#06afc7",
        "#e35b00",
    ],
    "bold": [
        "#ffffff",
        "#ff0000",
        "#00ff00",
        "#ff8800",
        "#ff00ff",
        "#00ffff",
        "#ffff00",
        "#00ff88",
        "#0000ff",
        "#000000",
    ],
    "solarized": [
        "#FDF6E3",
        "#839496",
        "#657B83",
        "#D87979",
        "#D33682",
        "#88CF76",
        "#43B8C3",
        "#2699FF",
        "#657B83",
        "#FDF6E3",
    ],
    "purple_gradient": [
        "#f9f5ff",
        "#e6e6ff",
        "#ccccff",
        "#cfbaf0",
        "#b3b3ff",
        "#9999ff",
        "#8080ff",
        "#6666ff",
        "#4d4dff",
        "#3333ff",
    ],
    "purple_alternating": [
        "#cfbaf0",
        "#b3b3ff",
        "#9999ff",
        "#cfbaf0",
        "#b3b3ff",
        "#9999ff",
        "#cfbaf0",
        "#b3b3ff",
        "#9999ff",
        "#cfbaf0",
    ],
    "green_alternating": [
        "#88cf76",
        "#33bb33",
        "#88cf76",
        "#33bb33",
        "#88cf76",
        "#33bb33",
        "#88cf76",
        "#33bb33",
        "#88cf76",
        "#33bb33",
    ],
    "pink_fluffy_unicorns": [
        "#EC89CB",
        "#F9D0D9",
        "#Ec89CB",
        "#F9D0D9",
        "#Ec89CB",
        "#F9D0D9",
        "#Ec89CB",
        "#F9D0D9",
        "#Ec89CB",
    ],
    "red": [
        "#ff4444",
        "#dd4444",
        "#ff4444",
        "#dd4444",
        "#ff4444",
        "#dd4444",
        "#ff4444",
        "#dd4444",
    ],
}

colors = {
    "theme_accent": "#e1acff", # make sure to add an icon in the same color
    "dark_accent": "#884488",
    "bar_background": "#282c34",
    "white": "#ffffff",
    "gray": "#888888",
    "groupbox_active_highlight": "#434758",
    "groupbox_border": "#74438f", # I don't know where this appears
    "widget_background": "spacedust3",
    # "widget_background": random.choice(list(widget_background_color_schemes.keys())),
}

colors.update(
    {str(i): v for i, v in enumerate(
        widget_background_color_schemes[
            colors["widget_background"]
        ]
    )}
)

layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": colors["theme_accent"],
    "border_normal": colors["dark_accent"],
}

layouts = [
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Max(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.Floating(**layout_theme)
]

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = {
    "font": "Ubuntu Mono",
    "fontsize": 12,
    "padding": 2,
    "background": colors["bar_background"],
    "foreground": colors["bar_background"]
}
extension_defaults = widget_defaults.copy()

def widget_input(**overrides):
  return widget_defaults | overrides

widgets_list = [
    widget.Sep(
        **widget_input(
            linewidth=0,
            padding=6,
        )
    ),
    widget.Image(
        **widget_input(
            filename=os.path.expanduser("~/.config/qtile/icons/purple_circle.png"),
            scale="False",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(myTerm)}
        )
    ),
    widget.Sep(
        **widget_input(
            linewidth=0,
            padding=6,
        )
    ),
    widget.GroupBox(
        **widget_input(
            font="Ubuntu Bold",
            fontsize=9,
            padding=1,
            highlight_method="line",
            rounded=False,
            active=colors["white"],
            inactive=colors["gray"],
            highlight_color=colors["groupbox_active_highlight"],
            this_current_screen_border=colors["theme_accent"],
            this_screen_border=colors["groupbox_border"],
            other_current_screen_border=colors["theme_accent"],
            other_screen_border=colors["groupbox_border"],
            foreground=colors["white"],
        )
    ),
    widget.Sep(
        **widget_input(
            linewidth=0,
            padding=6,
            foreground=colors["bar_background"],
        )
    ),
    widget.WindowTabs(
        **widget_input(
            foreground=colors["theme_accent"],
            padding=0
        )
    ),
    widget.Sep(
        **widget_input(
            linewidth=0,
            padding=6,
            foreground=colors["bar_background"],
        )
    ),
    widget.Systray(
        **widget_input()
    ),
    widget.TextBox(
        **widget_input(
            text=" Volume:",
            background=colors["0"],
            padding=0,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("amixer -q -D pulse sset Master toggle")}
        )
    ),
    widget.Volume(
        **widget_input(
            background=colors["0"],
            padding=5,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("amixer -q -D pulse sset Master toggle")}
        )
    ),
    widget.TextBox(
        **widget_input(
            text=" Wifi:",
            background=colors["1"],
            padding=0,
        )
    ),
    widget.Wlan(
        **widget_input(
            interface="wlp2s0",
            background=colors["1"],
            padding=5
        )
    ),
    widget.TextBox(
        **widget_input(
            text=" Tp-Link:",
            background=colors["2"],
            padding=0,
        )
    ),
    widget.Wlan(
        **widget_input(
            interface="wlx9848274aa03a",
            background=colors["2"],
            padding=5
        )
    ),
    widget.TextBox(
        **widget_input(
            text=" Battery:",
            background=colors["3"],
            padding=0,
        )
    ),
    widget.Battery(
        **widget_input(
            padding=5,
            charge_char='🔺' or '^',
            discharge_char="🔻" or 'v',
            format='{char} {percent:2.0%} {hour:d}:{min:02d}',
            update_interval=5,
            background=colors["3"]
        )
    ),
    widget.CPU(
        **widget_input(
            format='CPU: {freq_current}GHz {load_percent}%',
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(f'{myTerm} -e htop')
            },
            background=colors["4"],
        )
    ),
    widget.ThermalSensor(
        **widget_input(
            background=colors["4"],
            threshold=90,
            padding=5,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(f'{myTerm} -e htop')
            },
        )
    ),
    widget.TextBox(
        **widget_input(
            text=" Layout:",
            background=colors["5"],
            padding=0,
            mouse_callbacks={
                'Button1': qtile.cmd_next_layout,
                'Button2': qtile.cmd_prev_layout
            }
        )
    ),
    widget.CurrentLayout(
        **widget_input(
            background=colors["5"],
            padding=5
        )
    ),
    widget.Clock(
        **widget_input(
            background=colors["6"],
            format=" %A, %B %d | %I:%M:%S ",
            mouse_callbacks={'Button1': lazy.reload_config()}
        )
    ),
]

screens = [
    Screen(
        top=bar.Bar(
            widgets=widgets_list,
            opacity=0.85,
            size=20,
            wallpaper="/home/mecaneer23/.config/qtile/wallpapers/online1.jpg"
        )
    )
]

mouse = [
    Drag([mod],
         "Button1",
         lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod],
         "Button3",
         lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

keys = [
    # The essentials
    Key([mod], "Return", lazy.spawn(myTerm), desc='Launches My Terminal'),
    Key([mod, "shift"],
        "Return",
        lazy.spawn("dmenu_run -p 'Run: '"),
        desc='Run Launcher'),
    Key([mod], "b", lazy.spawn(myBrowser), desc='Browser'),
    Key([mod], "e", lazy.spawn(myEditor), desc='Editor'),
    Key([mod], "c", lazy.spawn(f"{myTerm} -e cmatrix"), desc='Spawn cmx window'),
    Key([mod], "r", lazy.spawn(f"run-prompt"), desc='Spawn run-prompt'),
    Key([mod], "Tab", lazy.next_layout(), desc='Toggle through layouts'),
    Key([mod, "shift"], "c", lazy.window.kill(), desc='Kill active window'),
    Key([mod, "shift"], "r", lazy.restart(), desc='Restart Qtile'),
    Key([mod, "shift"], "q", lazy.shutdown(), desc='Shutdown Qtile'),
    # Window controls
    Key([mod],
        "j",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'),
    Key([mod],
        "k",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'),
    Key([mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc='Move windows down in current stack'),
    Key([mod, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc='Move windows up in current stack'),
    Key([mod],
        "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
        ),
    Key([mod],
        "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
        ),
    Key([mod],
        "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'),
    Key([mod],
        "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'),
    Key([mod, "shift"],
        "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc='toggle fullscreen'),
    # Stack controls
    Key([mod, "shift"],
        "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
        ),
    Key([mod],
        "space",
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'
        ),
    Key([mod, "shift"],
        "space",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'
        ),
    Key(
        [mod],
        "Right",
        lazy.screen.next_group(),
        desc='Move to next group'
    ),
    Key(
        [mod],
        "Left",
        lazy.screen.prev_group(),
        desc='Move to previous group'
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("amixer -c 0 -q set Master 2dB+"),
        desc="Increase the volume"
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("amixer -c 0 -q set Master 2dB-"),
        desc="Decrease the volume"
    ),
    Key(
        [],
        "XF86AudioMute",
        # lazy.spawn("amixer -c 0 -q set Master toggle"),
        lazy.spawn("amixer -q -D pulse sset Master toggle"),
        desc="Mute toggle"
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 10%-"), 
        desc="Decrease the brightness"
    ),
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set 10%+"),
        desc="Increase the brightness"
    ),
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),  # tastyworks exit box
    Match(title='Qalculate!'),  # qalculate-gtk
    Match(wm_class='kdenlive'),  # kdenlive
    Match(wm_class='pinentry-gtk-2'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
subprocess.Popen(['/home/mecaneer23/.config/qtile/autostart.sh'])
wmname = "LG3D"
