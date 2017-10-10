import os

from api.server import App
import config

current_config = config.Local
env = os.environ.get('ENV', 'Development')
print('env = ', env)
if hasattr(config, env):
    current_config = getattr(config, env)

api = App(current_config)
