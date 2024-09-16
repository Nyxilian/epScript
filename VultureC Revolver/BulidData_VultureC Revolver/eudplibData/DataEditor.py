from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x663160, Add, 134217728),# units:Elevation Level  index:19    from 4 To 12
        SetMemory(0x664260, Add, 536870910),# units:Special Ability Flags  index:120    from 1140850691 To 1677721601
        SetMemory(0x656EB8, Add, -1900544),# weapons:Damage Amount  index:5    from 30 To 1
        SetMemory(0x656FBC, Add, -5632),# weapons:Weapon Cooldown  index:5    from 22 To 0
        SetMemory(0x6CA058, Add, -854),# flingy:Speed  index:88    from 1707 To 853
        SetMemory(0x6C9D28, Add, -71),# flingy:Acceleration  index:88    from 100 To 29
        SetMemory(0x6C9A90, Add, 14569),# flingy:Halt Distance  index:88    from 14569 To 29138
        SetMemory(0x6C9E78, Add, -7),# flingy:Turn Radius  index:88    from 40 To 33
        SetMemory(0x655760, Add, -6553600),# upgrades:Mineral Cost Base  index:17    from 100 To 0
        SetMemory(0x655860, Add, -6553600),# upgrades:Vespene Cost Base  index:17    from 100 To 0
        SetMemory(0x655BA0, Add, -98304000),# upgrades:Research Time Base  index:17    from 1500 To 0
    ])

