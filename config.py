# config.py
import appdirs
from appdirs import AppDirs


APP_CONFIG = {
    'APP_NAME': 'dpgTemplate',
    'APP_DESCRIPTION': 'dpgTemplate is a simple application that does nothing.',
    'APP_AUTHOR': 'Phillip Jerome Yosief',
    'APP_AUTHOR_EMAIL': '',
    'APP_PORTABLE': False,
    'GITHUB_URL': 'phillipyosief/dpgTemplate',
    'LOCAL-PATH': ''
}

WINDOW_CONFIG = {
    'WINDOW_WIDTH': 800,
    'WINDOW_HEIGHT': 600,
    'WINDOW_MIN_WIDTH': 250,
    'WINDOW_MIN_HEIGHT': 250,
    'WINDOW_MAX_WIDTH': 10000,
    'WINDOW_MAX_HEIGHT': 10000,
    'WINDOW_X_POS': 100,
    'WINDOW_Y_POS': 100,
    'WINDOW_VSYNC': True,
    'WINDOW_ALWAYS_ON_TOP': False,
    'WINDOW_DECORATED': True,
    'WINDOW_CLEAR_COLOR': (0, 0, 0, 255),
    'WINDOW_DISABLE_CLOSE': False,
    'WINDOW_RESIZABLE': True,
    'WINDOW_GLOBAL_FONT_SCALE': 1.0,
    'WINDOW_TITLE': APP_CONFIG['APP_NAME']
}

FONT_CONFIG = {
    'FONT_SCALE': None,
}

MENUBAR_CONFIG = {}

UPDATE_CONFIG = {
    'METHOD': 'GITHUB',  # GITHUB or LOCAL-PATH: Just getting the latest release from a network drive
    'GITHUB': {
        'REPO': APP_CONFIG['GITHUB_URL']
    },
    'LOCAL-PATH': {
        'PATH': APP_CONFIG['LOCAL-PATH']
    },
    'AUTO-UPDATE': True
}

app_dirs = AppDirs(APP_CONFIG['APP_NAME'], APP_CONFIG['APP_AUTHOR'])

RESOURCES_CONFIG = {
    'ICONS': {
        'WINDOWS': {
            '16x16': app_dirs.user_data_dir + '/resources/icons/generated/ico/icon_16x16.ico',
            '32x32': app_dirs.user_data_dir + '/resources/icons/generated/ico/icon_32x32.ico',
            '64x64': app_dirs.user_data_dir + '/resources/icons/generated/ico/icon_64x64.ico',
            '128x128': app_dirs.user_data_dir + '/resources/icons/generated/ico/icon_128x128.ico',
            '256x256': app_dirs.user_data_dir + '/resources/icons/generated/ico/icon_256x256.ico',
        },
        'LINUX': {
            '16x16': app_dirs.user_data_dir + '/resources/icons/generated/gif/icon_16x16.gif',
            '32x32': app_dirs.user_data_dir + '/resources/icons/generated/gif/icon_32x32.gif',
            '64x64': app_dirs.user_data_dir + '/resources/icons/generated/gif/icon_64x64.gif',
            '128x128': app_dirs.user_data_dir + '/resources/icons/generated/gif/icon_128x128.gif',
            '256x256': app_dirs.user_data_dir + '/resources/icons/generated/gif/icon_256x256.gif',
        },
        'MACOS': {
            '16x16': app_dirs.user_data_dir + '/resources/icons/generated/icns/icon_16x16.icns',
            '32x32': app_dirs.user_data_dir + '/resources/icons/generated/icns/icon_32x32.icns',
            '128x128': app_dirs.user_data_dir + '/resources/icons/generated/icns/icon_128x128.icns',
            '256x256': app_dirs.user_data_dir + '/resources/icons/generated/icns/icon_256x256.icns',
        }
    }
}
