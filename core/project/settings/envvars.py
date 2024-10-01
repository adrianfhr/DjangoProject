from core.core.utils.collections import deep_update
from core.core.utils.settings import get_settings_from_environment

"""
This takes env vars with matching prefix, strips out the prefix, and add it to globals()

for example, if you have the following env vars:
export CORESETTINGS_IN_DOCKER=true (env var)

Could then be referenced as a global variable:
IN_DOCKER (where the value would be True)
"""

# globals() is a dict of global variables in the current module
deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))  # type: ignore # noqa : F821