# config.py
from appdirs import AppDirs

APP_CONFIG = {
    'APP_NAME': 'MyApp',
    'APP_VERSION': '1.0.0',
    'APP_DESCRIPTION': 'MyApp is a simple application that does nothing.',
    'APP_AUTHOR': '',
    'APP_AUTHOR_EMAIL': '',
    'APP_PORTABLE': False
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

MENUBAR_CONFIG = {

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
            '16x16': app_dirs.user_data_dir + '/resources/icons/generated/png/icon_16x16.png',
            '32x32': app_dirs.user_data_dir + '/resources/icons/generated/png/icon_32x32.png',
            '128x128': app_dirs.user_data_dir + '/resources/icons/generated/png/icon_128x128.png',
            '256x256': app_dirs.user_data_dir + '/resources/icons/generated/png/icon_256x256.png',
        }
    }
}


