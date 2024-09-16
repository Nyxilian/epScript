from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x6647B0, Add, 1),# units:Shield Enable  index:0    from 0 To 1
        SetMemory(0x6647BC, Add, 16777216),# units:Shield Enable  index:15    from 0 To 1
        SetMemory(0x6647D0, Add, 65536),# units:Shield Enable  index:34    from 0 To 1
        SetMemory(0x6647D4, Add, 1),# units:Shield Enable  index:36    from 0 To 1
        SetMemory(0x6647E4, Add, 65536),# units:Shield Enable  index:54    from 0 To 1
        SetMemory(0x6647E8, Add, 65536),# units:Shield Enable  index:58    from 0 To 1
        SetMemory(0x664810, Add, 1),# units:Shield Enable  index:96    from 0 To 1
        SetMemory(0x664810, Add, 16777216),# units:Shield Enable  index:99    from 0 To 1
        SetMemory(0x660E00, Add, 10000),# units:Shield Amount  index:0    from 0 To 10000
        SetMemory(0x660E1C, Add, 655360000),# units:Shield Amount  index:15    from 0 To 10000
        SetMemory(0x660E44, Add, 10000),# units:Shield Amount  index:34    from 0 To 10000
        SetMemory(0x660E48, Add, 10000),# units:Shield Amount  index:36    from 0 To 10000
        SetMemory(0x660E74, Add, 10000),# units:Shield Amount  index:58    from 0 To 10000
        SetMemory(0x660E78, Add, 652738560),# units:Shield Amount  index:61    from 40 To 10000
        SetMemory(0x660E84, Add, 9920),# units:Shield Amount  index:66    from 80 To 10000
        SetMemory(0x660E98, Add, 9200),# units:Shield Amount  index:76    from 800 To 10000
        SetMemory(0x660E98, Add, 639631360),# units:Shield Amount  index:77    from 240 To 10000
        SetMemory(0x660EA4, Add, 650117120),# units:Shield Amount  index:83    from 80 To 10000
        SetMemory(0x662350, Add, 2549760),# units:Hit Points  index:0    from 10240 To 2560000
        SetMemory(0x66238C, Add, 2549760),# units:Hit Points  index:15    from 10240 To 2560000
        SetMemory(0x6623D8, Add, 2544640),# units:Hit Points  index:34    from 15360 To 2560000
        SetMemory(0x6623E0, Add, 2508800),# units:Hit Points  index:36    from 51200 To 2560000
        SetMemory(0x662428, Add, 2529280),# units:Hit Points  index:54    from 30720 To 2560000
        SetMemory(0x662438, Add, 2508800),# units:Hit Points  index:58    from 51200 To 2560000
        SetMemory(0x662444, Add, 2539520),# units:Hit Points  index:61    from 20480 To 2560000
        SetMemory(0x662458, Add, 2534400),# units:Hit Points  index:66    from 25600 To 2560000
        SetMemory(0x662460, Add, 2557440),# units:Hit Points  index:68    from 2560 To 2560000
        SetMemory(0x662480, Add, 2534400),# units:Hit Points  index:76    from 25600 To 2560000
        SetMemory(0x662484, Add, 2498560),# units:Hit Points  index:77    from 61440 To 2560000
        SetMemory(0x66249C, Add, 2534400),# units:Hit Points  index:83    from 25600 To 2560000
        SetMemory(0x6624B0, Add, 2496000),# units:Hit Points  index:88    from 64000 To 2560000
        SetMemory(0x6624D0, Add, 2544640),# units:Hit Points  index:96    from 15360 To 2560000
        SetMemory(0x6624DC, Add, 2508800),# units:Hit Points  index:99    from 51200 To 2560000
        SetMemory(0x6640BC, Add, 4),# units:Special Ability Flags  index:15    from 402718720 To 402718724
        SetMemory(0x664108, Add, 4),# units:Special Ability Flags  index:34    from 404815872 To 404815876
        SetMemory(0x664158, Add, 536870912),# units:Special Ability Flags  index:54    from 403768512 To 940639424
        SetMemory(0x664174, Add, -4194304),# units:Special Ability Flags  index:61    from 406913024 To 402718720
        SetMemory(0x664190, Add, 536870912),# units:Special Ability Flags  index:68    from 469762304 To 1006633216
        SetMemory(0x6641E0, Add, 536870912),# units:Special Ability Flags  index:88    from 1509949508 To 2046820420
        SetMemory(0x664200, Add, 536870912),# units:Special Ability Flags  index:96    from 402718720 To 939589632
        SetMemory(0x66420C, Add, 536870912),# units:Special Ability Flags  index:99    from 404816448 To 941687360
        SetMemory(0x664338, Add, 536870912),# units:Special Ability Flags  index:174    from 67108865 To 603979777
        SetMemory(0x66433C, Add, 536870912),# units:Special Ability Flags  index:175    from 67108865 To 603979777
        SetMemory(0x664374, Add, 536870912),# units:Special Ability Flags  index:189    from 1140850689 To 1677721601
        SetMemory(0x665D04, Add, -256),# sprites:Is Visible  index:189    from 1 To 0
        SetMemory(0x669EAC, Add, 655360),# images:Draw Function  index:134    from 0 To 10
    ])

