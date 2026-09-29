"""Resolve system fonts without personal absolute paths or bundled font files."""
import os
from pathlib import Path

def font_path(role):
    names={
        'serif':['times.ttf','Times New Roman.ttf','LiberationSerif-Regular.ttf','DejaVuSerif.ttf'],
        'serif_bold':['timesbd.ttf','Times New Roman Bold.ttf','LiberationSerif-Bold.ttf','DejaVuSerif-Bold.ttf'],
        'mono':['consola.ttf','Consolas.ttf','LiberationMono-Regular.ttf','DejaVuSansMono.ttf'],
    }[role]
    directories=[Path(os.environ['SURVEY_FONT_DIR'])] if os.environ.get('SURVEY_FONT_DIR') else []
    directories += [Path(os.environ.get('WINDIR','C:/Windows'))/'Fonts',
                    Path('/usr/share/fonts/truetype/msttcorefonts'),
                    Path('/usr/share/fonts/truetype/liberation2'),
                    Path('/usr/share/fonts/truetype/liberation'),
                    Path('/usr/share/fonts/truetype/dejavu'),
                    Path('/Library/Fonts'),Path('/System/Library/Fonts/Supplemental')]
    for filename in names:
        for directory in directories:
            candidate=directory/filename
            if candidate.is_file():return str(candidate)
    raise FileNotFoundError(f'No compatible {role} font found. Set SURVEY_FONT_DIR to a font directory.')
