# This bot shows how to enable a debugger session to explore the objects
# IMPORTANT: timeouts need to be disabled, or you will not have time to use
# the debugger at all. Run a game with:
# pelita --no-timeout demo08_debugger.py demo01_stopping.py
#

TEAM_NAME = 'Debuggable Bot'

def move(turn, game):
    # in Python >= 3.7 this can be changed to simply
    # breakpoint()
    import pdb; pdb.set_trace()
    return (0,0)
