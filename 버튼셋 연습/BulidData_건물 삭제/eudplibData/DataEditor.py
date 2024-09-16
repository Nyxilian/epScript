from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x663898, Add, -6553600),# units:Mineral Cost  index:9    from 100 To 0
        SetMemory(0x65FD10, Add, -14745600),# units:Vespene Cost  index:9    from 225 To 0
        SetMemory(0x663CF0, Add, -1024),# units:Supply Required  index:9    from 4 To 0
    ])

