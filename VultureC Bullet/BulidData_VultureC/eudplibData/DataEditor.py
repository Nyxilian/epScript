from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x664528, Add, -10),# units:Graphics  index:48    from 14 To 4
        SetMemory(0x6645B8, Add, 1572864),# units:Graphics  index:194    from 122 To 146
        SetMemory(0x6645B8, Add, 671088640),# units:Graphics  index:195    from 123 To 163
        SetMemory(0x6645BC, Add, 32),# units:Graphics  index:196    from 124 To 156
        SetMemory(0x6645BC, Add, -18944),# units:Graphics  index:197    from 122 To 48
        SetMemory(0x6645BC, Add, -2752512),# units:Graphics  index:198    from 123 To 81
        SetMemory(0x6645BC, Add, 1006632960),# units:Graphics  index:199    from 124 To 184
        SetMemory(0x661170, Add, -37),# units:Construction Animation  index:48    from 52 To 15
        SetMemory(0x660620, Add, 18),# units:Unit Direction  index:48    from 14 To 32
        SetMemory(0x6606B4, Add, 0),# units:Unit Direction  index:197    from 0 To 0
        SetMemory(0x6647B8, Add, 65536),# units:Shield Enable  index:10    from 0 To 1
        SetMemory(0x6647BC, Add, 0),# units:Shield Enable  index:15    from 0 To 0
        SetMemory(0x6647C0, Add, 16777216),# units:Shield Enable  index:19    from 0 To 1
        SetMemory(0x6647DC, Add, 65536),# units:Shield Enable  index:46    from 0 To 1
        SetMemory(0x6647E0, Add, 0),# units:Shield Enable  index:48    from 0 To 0
        SetMemory(0x6647F4, Add, -1),# units:Shield Enable  index:68    from 1 To 0
        SetMemory(0x6647FC, Add, -16777216),# units:Shield Enable  index:79    from 1 To 0
        SetMemory(0x660E1C, Add, -3932160),# units:Shield Amount  index:15    from 100 To 40
        SetMemory(0x660E24, Add, 0),# units:Shield Amount  index:19    from 100 To 100
        SetMemory(0x660E88, Add, -150),# units:Shield Amount  index:68    from 350 To 200
        SetMemory(0x662354, Add, 14080),# units:Hit Points  index:1    from 11520 To 25600
        SetMemory(0x66238C, Add, 15360),# units:Hit Points  index:15    from 10240 To 25600
        SetMemory(0x662390, Add, -25600),# units:Hit Points  index:16    from 64000 To 38400
        SetMemory(0x66239C, Add, -38400),# units:Hit Points  index:19    from 76800 To 38400
        SetMemory(0x662410, Add, -153600),# units:Hit Points  index:48    from 204800 To 51200
        SetMemory(0x66241C, Add, -12800),# units:Hit Points  index:51    from 102400 To 89600
        SetMemory(0x662438, Add, 12800),# units:Hit Points  index:58    from 51200 To 64000
        SetMemory(0x662460, Add, 74240),# units:Hit Points  index:68    from 2560 To 76800
        SetMemory(0x66248C, Add, 69120),# units:Hit Points  index:79    from 20480 To 89600
        SetMemory(0x66315C, Add, -1024),# units:Elevation Level  index:13    from 4 To 0
        SetMemory(0x663160, Add, 0),# units:Elevation Level  index:16    from 4 To 4
        SetMemory(0x663160, Add, 251658240),# units:Elevation Level  index:19    from 4 To 19
        SetMemory(0x663180, Add, 0),# units:Elevation Level  index:48    from 4 To 4
        SetMemory(0x663188, Add, -1048576),# units:Elevation Level  index:58    from 16 To 0
        SetMemory(0x6631B4, Add, 201326592),# units:Elevation Level  index:103    from 4 To 16
        SetMemory(0x663210, Add, 851968),# units:Elevation Level  index:194    from 0 To 13
        SetMemory(0x663210, Add, 251658240),# units:Elevation Level  index:195    from 0 To 15
        SetMemory(0x663214, Add, 15),# units:Elevation Level  index:196    from 0 To 15
        SetMemory(0x663214, Add, 3584),# units:Elevation Level  index:197    from 0 To 14
        SetMemory(0x663214, Add, 1048576),# units:Elevation Level  index:198    from 0 To 16
        SetMemory(0x663214, Add, 218103808),# units:Elevation Level  index:199    from 0 To 13
        SetMemory(0x663E14, Add, -9),# units:Rank/Sublabel  index:68    from 9 To 0
        SetMemory(0x662EAC, Add, -512),# units:Comp AI Idle  index:13    from 20 To 18
        SetMemory(0x662EAC, Add, 268435456),# units:Comp AI Idle  index:15    from 2 To 18
        SetMemory(0x662EB0, Add, 16),# units:Comp AI Idle  index:16    from 2 To 18
        SetMemory(0x662ECC, Add, 1048576),# units:Comp AI Idle  index:46    from 2 To 18
        SetMemory(0x662ED0, Add, 16),# units:Comp AI Idle  index:48    from 2 To 18
        SetMemory(0x662ED0, Add, 268435456),# units:Comp AI Idle  index:51    from 2 To 18
        SetMemory(0x662ED8, Add, 1048576),# units:Comp AI Idle  index:58    from 2 To 18
        SetMemory(0x662EE4, Add, 16),# units:Comp AI Idle  index:68    from 2 To 18
        SetMemory(0x662EEC, Add, 268435456),# units:Comp AI Idle  index:79    from 2 To 18
        SetMemory(0x662F60, Add, -1376256),# units:Comp AI Idle  index:194    from 23 To 2
        SetMemory(0x662F60, Add, -352321536),# units:Comp AI Idle  index:195    from 23 To 2
        SetMemory(0x662F64, Add, -21),# units:Comp AI Idle  index:196    from 23 To 2
        SetMemory(0x662F64, Add, -38656),# units:Comp AI Idle  index:197    from 153 To 2
        SetMemory(0x662F64, Add, -9895936),# units:Comp AI Idle  index:198    from 153 To 2
        SetMemory(0x662F64, Add, -2533359616),# units:Comp AI Idle  index:199    from 153 To 2
        SetMemory(0x662274, Add, -512),# units:Human AI Idle  index:13    from 20 To 18
        SetMemory(0x662274, Add, 268435456),# units:Human AI Idle  index:15    from 2 To 18
        SetMemory(0x662278, Add, 16),# units:Human AI Idle  index:16    from 2 To 18
        SetMemory(0x662294, Add, 1048576),# units:Human AI Idle  index:46    from 2 To 18
        SetMemory(0x662298, Add, 16),# units:Human AI Idle  index:48    from 2 To 18
        SetMemory(0x662298, Add, 268435456),# units:Human AI Idle  index:51    from 2 To 18
        SetMemory(0x6622A0, Add, 1048576),# units:Human AI Idle  index:58    from 2 To 18
        SetMemory(0x6622AC, Add, 16),# units:Human AI Idle  index:68    from 2 To 18
        SetMemory(0x6622B4, Add, 268435456),# units:Human AI Idle  index:79    from 2 To 18
        SetMemory(0x662328, Add, -1376256),# units:Human AI Idle  index:194    from 23 To 2
        SetMemory(0x662328, Add, -352321536),# units:Human AI Idle  index:195    from 23 To 2
        SetMemory(0x66232C, Add, -21),# units:Human AI Idle  index:196    from 23 To 2
        SetMemory(0x66232C, Add, -38656),# units:Human AI Idle  index:197    from 153 To 2
        SetMemory(0x66232C, Add, -9895936),# units:Human AI Idle  index:198    from 153 To 2
        SetMemory(0x66232C, Add, -2533359616),# units:Human AI Idle  index:199    from 153 To 2
        SetMemory(0x6648A4, Add, -512),# units:Return to Idle  index:13    from 20 To 18
        SetMemory(0x6648A4, Add, 268435456),# units:Return to Idle  index:15    from 2 To 18
        SetMemory(0x6648A8, Add, 16),# units:Return to Idle  index:16    from 2 To 18
        SetMemory(0x6648C4, Add, 1048576),# units:Return to Idle  index:46    from 2 To 18
        SetMemory(0x6648C8, Add, 16),# units:Return to Idle  index:48    from 2 To 18
        SetMemory(0x6648C8, Add, 268435456),# units:Return to Idle  index:51    from 2 To 18
        SetMemory(0x6648D0, Add, 1048576),# units:Return to Idle  index:58    from 2 To 18
        SetMemory(0x6648DC, Add, 16),# units:Return to Idle  index:68    from 2 To 18
        SetMemory(0x6648E4, Add, 268435456),# units:Return to Idle  index:79    from 2 To 18
        SetMemory(0x664958, Add, -1376256),# units:Return to Idle  index:194    from 23 To 2
        SetMemory(0x664958, Add, -352321536),# units:Return to Idle  index:195    from 23 To 2
        SetMemory(0x66495C, Add, -21),# units:Return to Idle  index:196    from 23 To 2
        SetMemory(0x66495C, Add, -5376),# units:Return to Idle  index:197    from 23 To 2
        SetMemory(0x66495C, Add, -1376256),# units:Return to Idle  index:198    from 23 To 2
        SetMemory(0x66495C, Add, -352321536),# units:Return to Idle  index:199    from 23 To 2
        SetMemory(0x66332C, Add, -256),# units:Attack Unit  index:13    from 20 To 19
        SetMemory(0x66332C, Add, -33554432),# units:Attack Unit  index:15    from 21 To 19
        SetMemory(0x663330, Add, 9),# units:Attack Unit  index:16    from 10 To 19
        SetMemory(0x66334C, Add, 589824),# units:Attack Unit  index:46    from 10 To 19
        SetMemory(0x663350, Add, 9),# units:Attack Unit  index:48    from 10 To 19
        SetMemory(0x663350, Add, 150994944),# units:Attack Unit  index:51    from 10 To 19
        SetMemory(0x663358, Add, 589824),# units:Attack Unit  index:58    from 10 To 19
        SetMemory(0x663364, Add, 9),# units:Attack Unit  index:68    from 10 To 19
        SetMemory(0x66336C, Add, 150994944),# units:Attack Unit  index:79    from 10 To 19
        SetMemory(0x6633E0, Add, -131072),# units:Attack Unit  index:194    from 23 To 21
        SetMemory(0x6633E0, Add, -352321536),# units:Attack Unit  index:195    from 23 To 2
        SetMemory(0x6633E4, Add, -21),# units:Attack Unit  index:196    from 23 To 2
        SetMemory(0x6633E4, Add, -5376),# units:Attack Unit  index:197    from 23 To 2
        SetMemory(0x6633E4, Add, -1376256),# units:Attack Unit  index:198    from 23 To 2
        SetMemory(0x6633E4, Add, -352321536),# units:Attack Unit  index:199    from 23 To 2
        SetMemory(0x663A5C, Add, -42240),# units:Attack Move  index:13    from 188 To 23
        SetMemory(0x663A5C, Add, 352321536),# units:Attack Move  index:15    from 2 To 23
        SetMemory(0x663A60, Add, 21),# units:Attack Move  index:16    from 2 To 23
        SetMemory(0x663A7C, Add, 1376256),# units:Attack Move  index:46    from 2 To 23
        SetMemory(0x663A80, Add, 21),# units:Attack Move  index:48    from 2 To 23
        SetMemory(0x663A80, Add, 352321536),# units:Attack Move  index:51    from 2 To 23
        SetMemory(0x663A88, Add, 1376256),# units:Attack Move  index:58    from 2 To 23
        SetMemory(0x663A94, Add, 21),# units:Attack Move  index:68    from 2 To 23
        SetMemory(0x663A9C, Add, 352321536),# units:Attack Move  index:79    from 2 To 23
        SetMemory(0x663B10, Add, -1376256),# units:Attack Move  index:194    from 23 To 2
        SetMemory(0x663B10, Add, -352321536),# units:Attack Move  index:195    from 23 To 2
        SetMemory(0x663B14, Add, -21),# units:Attack Move  index:196    from 23 To 2
        SetMemory(0x663B14, Add, -5376),# units:Attack Move  index:197    from 23 To 2
        SetMemory(0x663B14, Add, -1376256),# units:Attack Move  index:198    from 23 To 2
        SetMemory(0x663B14, Add, -352321536),# units:Attack Move  index:199    from 23 To 2
        SetMemory(0x6636C4, Add, 31744),# units:Ground Weapon  index:13    from 6 To 130
        SetMemory(0x6636E4, Add, -5242880),# units:Ground Weapon  index:46    from 130 To 50
        SetMemory(0x6636E8, Add, 9),# units:Ground Weapon  index:48    from 41 To 50
        SetMemory(0x6636F0, Add, -1769472),# units:Ground Weapon  index:58    from 130 To 103
        SetMemory(0x6645F0, Add, 0),# units:Max Ground Hits  index:19    from 1 To 1
        SetMemory(0x664618, Add, 65536),# units:Max Ground Hits  index:58    from 0 To 1
        SetMemory(0x66170C, Add, -5242880),# units:Air Weapon  index:46    from 130 To 50
        SetMemory(0x6601B0, Add, 196608),# units:AI Internal  index:58    from 0 To 3
        SetMemory(0x6601BC, Add, 3),# units:AI Internal  index:68    from 0 To 3
        SetMemory(0x6640A8, Add, -134217728),# units:Special Ability Flags  index:10    from 402718784 To 268501056
        SetMemory(0x6640B4, Add, 134217728),# units:Special Ability Flags  index:13    from 402653184 To 536870912
        SetMemory(0x6640BC, Add, 0),# units:Special Ability Flags  index:15    from 402718720 To 402718720
        SetMemory(0x6640C0, Add, -2097664),# units:Special Ability Flags  index:16    from 404816448 To 402718784
        SetMemory(0x664138, Add, -36765824),# units:Special Ability Flags  index:46    from 439419008 To 402653184
        SetMemory(0x664140, Add, -67174592),# units:Special Ability Flags  index:48    from 469827776 To 402653184
        SetMemory(0x66414C, Add, -2163264),# units:Special Ability Flags  index:51    from 404816576 To 402653312
        SetMemory(0x664168, Add, -1107296132),# units:Special Ability Flags  index:58    from 1509949444 To 402653312
        SetMemory(0x664190, Add, -67108736),# units:Special Ability Flags  index:68    from 469762304 To 402653568
        SetMemory(0x6641BC, Add, -2162368),# units:Special Ability Flags  index:79    from 404815936 To 402653568
        SetMemory(0x6641E0, Add, 268435456),# units:Special Ability Flags  index:88    from 1509949508 To 1778384964
        SetMemory(0x664260, Add, 536870910),# units:Special Ability Flags  index:120    from 1140850691 To 1677721601
        SetMemory(0x664388, Add, 134217727),# units:Special Ability Flags  index:194    from 536870913 To 671088640
        SetMemory(0x66438C, Add, 134217727),# units:Special Ability Flags  index:195    from 536870913 To 671088640
        SetMemory(0x664390, Add, 134217727),# units:Special Ability Flags  index:196    from 536870913 To 671088640
        SetMemory(0x664394, Add, 134217727),# units:Special Ability Flags  index:197    from 536870913 To 671088640
        SetMemory(0x664398, Add, 134217727),# units:Special Ability Flags  index:198    from 536870913 To 671088640
        SetMemory(0x66439C, Add, 134217727),# units:Special Ability Flags  index:199    from 536870913 To 671088640
        SetMemory(0x662DB8, Add, -1536),# units:Target Acquisition Range  index:1    from 7 To 1
        SetMemory(0x662DC0, Add, 720896),# units:Target Acquisition Range  index:10    from 3 To 14
        SetMemory(0x662DC8, Add, 8),# units:Target Acquisition Range  index:16    from 6 To 14
        SetMemory(0x662DE8, Add, 11),# units:Target Acquisition Range  index:48    from 3 To 14
        SetMemory(0x662DE8, Add, 285212672),# units:Target Acquisition Range  index:51    from 3 To 20
        SetMemory(0x662DF0, Add, 524288),# units:Target Acquisition Range  index:58    from 6 To 14
        SetMemory(0x662DFC, Add, 11),# units:Target Acquisition Range  index:68    from 3 To 14
        SetMemory(0x662E04, Add, 184549376),# units:Target Acquisition Range  index:79    from 3 To 14
        SetMemory(0x663270, Add, 196608),# units:Sight Range  index:58    from 8 To 11
        SetMemory(0x6635E0, Add, -16777216),# units:Armor Upgrade  index:19    from 1 To 0
        SetMemory(0x663600, Add, -3),# units:Armor Upgrade  index:48    from 3 To 0
        SetMemory(0x663600, Add, -50331648),# units:Armor Upgrade  index:51    from 3 To 0
        SetMemory(0x663608, Add, -131072),# units:Armor Upgrade  index:58    from 2 To 0
        SetMemory(0x663614, Add, -5),# units:Armor Upgrade  index:68    from 5 To 0
        SetMemory(0x66361C, Add, -83886080),# units:Armor Upgrade  index:79    from 5 To 0
        SetMemory(0x6620A4, Add, 768),# units:Right-click Action  index:13    from 0 To 3
        SetMemory(0x6620A4, Add, 16777216),# units:Right-click Action  index:15    from 2 To 3
        SetMemory(0x6620A8, Add, 2),# units:Right-click Action  index:16    from 1 To 3
        SetMemory(0x6620C4, Add, 65536),# units:Right-click Action  index:46    from 2 To 3
        SetMemory(0x6620C8, Add, 2),# units:Right-click Action  index:48    from 1 To 3
        SetMemory(0x6620C8, Add, 33554432),# units:Right-click Action  index:51    from 1 To 3
        SetMemory(0x6620D0, Add, 131072),# units:Right-click Action  index:58    from 1 To 3
        SetMemory(0x6620DC, Add, 2),# units:Right-click Action  index:68    from 1 To 3
        SetMemory(0x6620E4, Add, 33554432),# units:Right-click Action  index:79    from 1 To 3
        SetMemory(0x662158, Add, 131072),# units:Right-click Action  index:194    from 0 To 2
        SetMemory(0x662158, Add, 33554432),# units:Right-click Action  index:195    from 0 To 2
        SetMemory(0x66215C, Add, 2),# units:Right-click Action  index:196    from 0 To 2
        SetMemory(0x66215C, Add, 512),# units:Right-click Action  index:197    from 0 To 2
        SetMemory(0x66215C, Add, 131072),# units:Right-click Action  index:198    from 0 To 2
        SetMemory(0x66215C, Add, 33554432),# units:Right-click Action  index:199    from 0 To 2
        SetMemory(0x662880, Add, -37),# units:StarEdit Placement Box Width  index:8    from 38 To 1
        SetMemory(0x662894, Add, -15),# units:StarEdit Placement Box Width  index:13    from 16 To 1
        SetMemory(0x66289C, Add, -16),# units:StarEdit Placement Box Width  index:15    from 17 To 1
        SetMemory(0x6628A0, Add, -14),# units:StarEdit Placement Box Width  index:16    from 15 To 1
        SetMemory(0x6628B4, Add, -37),# units:StarEdit Placement Box Width  index:21    from 38 To 1
        SetMemory(0x662918, Add, -26),# units:StarEdit Placement Box Width  index:46    from 27 To 1
        SetMemory(0x662920, Add, -37),# units:StarEdit Placement Box Width  index:48    from 38 To 1
        SetMemory(0x66292C, Add, -14),# units:StarEdit Placement Box Width  index:51    from 15 To 1
        SetMemory(0x662948, Add, -49),# units:StarEdit Placement Box Width  index:58    from 50 To 1
        SetMemory(0x662970, Add, -31),# units:StarEdit Placement Box Width  index:68    from 32 To 1
        SetMemory(0x66299C, Add, -23),# units:StarEdit Placement Box Width  index:79    from 24 To 1
        SetMemory(0x6629C0, Add, -35),# units:StarEdit Placement Box Width  index:88    from 36 To 1
        SetMemory(0x6629C8, Add, -31),# units:StarEdit Placement Box Width  index:90    from 32 To 1
        SetMemory(0x6629FC, Add, -31),# units:StarEdit Placement Box Width  index:103    from 32 To 1
        SetMemory(0x662B68, Add, -95),# units:StarEdit Placement Box Width  index:194    from 96 To 1
        SetMemory(0x662B6C, Add, -95),# units:StarEdit Placement Box Width  index:195    from 96 To 1
        SetMemory(0x662B70, Add, -95),# units:StarEdit Placement Box Width  index:196    from 96 To 1
        SetMemory(0x662B74, Add, -95),# units:StarEdit Placement Box Width  index:197    from 96 To 1
        SetMemory(0x662B78, Add, -95),# units:StarEdit Placement Box Width  index:198    from 96 To 1
        SetMemory(0x662B7C, Add, -95),# units:StarEdit Placement Box Width  index:199    from 96 To 1
        SetMemory(0x662880, Add, -1900544),# units:StarEdit Placement Box Height  index:8    from 30 To 1
        SetMemory(0x662894, Add, -983040),# units:StarEdit Placement Box Height  index:13    from 16 To 1
        SetMemory(0x66289C, Add, -1245184),# units:StarEdit Placement Box Height  index:15    from 20 To 1
        SetMemory(0x6628A0, Add, -1376256),# units:StarEdit Placement Box Height  index:16    from 22 To 1
        SetMemory(0x6628B4, Add, -1900544),# units:StarEdit Placement Box Height  index:21    from 30 To 1
        SetMemory(0x662918, Add, -1572864),# units:StarEdit Placement Box Height  index:46    from 25 To 1
        SetMemory(0x662920, Add, -2031616),# units:StarEdit Placement Box Height  index:48    from 32 To 1
        SetMemory(0x66292C, Add, -1376256),# units:StarEdit Placement Box Height  index:51    from 22 To 1
        SetMemory(0x662948, Add, -3211264),# units:StarEdit Placement Box Height  index:58    from 50 To 1
        SetMemory(0x662970, Add, -2031616),# units:StarEdit Placement Box Height  index:68    from 32 To 1
        SetMemory(0x66299C, Add, -1769472),# units:StarEdit Placement Box Height  index:79    from 28 To 1
        SetMemory(0x6629C0, Add, -2031616),# units:StarEdit Placement Box Height  index:88    from 32 To 1
        SetMemory(0x6629C8, Add, -2031616),# units:StarEdit Placement Box Height  index:90    from 32 To 1
        SetMemory(0x6629FC, Add, -2031616),# units:StarEdit Placement Box Height  index:103    from 32 To 1
        SetMemory(0x662B68, Add, -4128768),# units:StarEdit Placement Box Height  index:194    from 64 To 1
        SetMemory(0x662B6C, Add, -4128768),# units:StarEdit Placement Box Height  index:195    from 64 To 1
        SetMemory(0x662B70, Add, -4128768),# units:StarEdit Placement Box Height  index:196    from 64 To 1
        SetMemory(0x662B74, Add, -4128768),# units:StarEdit Placement Box Height  index:197    from 64 To 1
        SetMemory(0x662B78, Add, -4128768),# units:StarEdit Placement Box Height  index:198    from 64 To 1
        SetMemory(0x662B7C, Add, -4128768),# units:StarEdit Placement Box Height  index:199    from 64 To 1
        SetMemory(0x661830, Add, -6),# units:Unit Size Left  index:13    from 7 To 1
        SetMemory(0x661860, Add, -10),# units:Unit Size Left  index:19    from 16 To 6
        SetMemory(0x661870, Add, -18),# units:Unit Size Left  index:21    from 19 To 1
        SetMemory(0x661A88, Add, -14),# units:Unit Size Left  index:88    from 18 To 4
        SetMemory(0x661A98, Add, -8),# units:Unit Size Left  index:90    from 16 To 8
        SetMemory(0x661B00, Add, -14),# units:Unit Size Left  index:103    from 15 To 1
        SetMemory(0x661DD8, Add, -44),# units:Unit Size Left  index:194    from 48 To 4
        SetMemory(0x661DE0, Add, -44),# units:Unit Size Left  index:195    from 48 To 4
        SetMemory(0x661DE8, Add, -44),# units:Unit Size Left  index:196    from 48 To 4
        SetMemory(0x661DF0, Add, -44),# units:Unit Size Left  index:197    from 48 To 4
        SetMemory(0x661DF8, Add, -44),# units:Unit Size Left  index:198    from 48 To 4
        SetMemory(0x661E00, Add, -44),# units:Unit Size Left  index:199    from 48 To 4
        SetMemory(0x661830, Add, -393216),# units:Unit Size Up  index:13    from 7 To 1
        SetMemory(0x661860, Add, -655360),# units:Unit Size Up  index:19    from 16 To 6
        SetMemory(0x661870, Add, -917504),# units:Unit Size Up  index:21    from 15 To 1
        SetMemory(0x661A88, Add, -655360),# units:Unit Size Up  index:88    from 16 To 6
        SetMemory(0x661A98, Add, -524288),# units:Unit Size Up  index:90    from 16 To 8
        SetMemory(0x661B00, Add, -917504),# units:Unit Size Up  index:103    from 15 To 1
        SetMemory(0x661DD8, Add, -1835008),# units:Unit Size Up  index:194    from 32 To 4
        SetMemory(0x661DE0, Add, -1835008),# units:Unit Size Up  index:195    from 32 To 4
        SetMemory(0x661DE8, Add, -1835008),# units:Unit Size Up  index:196    from 32 To 4
        SetMemory(0x661DF0, Add, -1835008),# units:Unit Size Up  index:197    from 32 To 4
        SetMemory(0x661DF8, Add, -1835008),# units:Unit Size Up  index:198    from 32 To 4
        SetMemory(0x661E00, Add, -1835008),# units:Unit Size Up  index:199    from 32 To 4
        SetMemory(0x661834, Add, -6),# units:Unit Size Right  index:13    from 7 To 1
        SetMemory(0x661864, Add, -9),# units:Unit Size Right  index:19    from 15 To 6
        SetMemory(0x661874, Add, -17),# units:Unit Size Right  index:21    from 18 To 1
        SetMemory(0x661A8C, Add, -13),# units:Unit Size Right  index:88    from 17 To 4
        SetMemory(0x661A9C, Add, -7),# units:Unit Size Right  index:90    from 15 To 8
        SetMemory(0x661B04, Add, -15),# units:Unit Size Right  index:103    from 16 To 1
        SetMemory(0x661DDC, Add, -43),# units:Unit Size Right  index:194    from 47 To 4
        SetMemory(0x661DE4, Add, -43),# units:Unit Size Right  index:195    from 47 To 4
        SetMemory(0x661DEC, Add, -43),# units:Unit Size Right  index:196    from 47 To 4
        SetMemory(0x661DF4, Add, -43),# units:Unit Size Right  index:197    from 47 To 4
        SetMemory(0x661DFC, Add, -43),# units:Unit Size Right  index:198    from 47 To 4
        SetMemory(0x661E04, Add, -43),# units:Unit Size Right  index:199    from 47 To 4
        SetMemory(0x661834, Add, -393216),# units:Unit Size Down  index:13    from 7 To 1
        SetMemory(0x661864, Add, -589824),# units:Unit Size Down  index:19    from 15 To 6
        SetMemory(0x661874, Add, -851968),# units:Unit Size Down  index:21    from 14 To 1
        SetMemory(0x661A8C, Add, -589824),# units:Unit Size Down  index:88    from 15 To 6
        SetMemory(0x661A9C, Add, -458752),# units:Unit Size Down  index:90    from 15 To 8
        SetMemory(0x661B04, Add, -983040),# units:Unit Size Down  index:103    from 16 To 1
        SetMemory(0x661DDC, Add, -1769472),# units:Unit Size Down  index:194    from 31 To 4
        SetMemory(0x661DE4, Add, -1769472),# units:Unit Size Down  index:195    from 31 To 4
        SetMemory(0x661DEC, Add, -1769472),# units:Unit Size Down  index:196    from 31 To 4
        SetMemory(0x661DF4, Add, -1769472),# units:Unit Size Down  index:197    from 31 To 4
        SetMemory(0x661DFC, Add, -1769472),# units:Unit Size Down  index:198    from 31 To 4
        SetMemory(0x661E04, Add, -1769472),# units:Unit Size Down  index:199    from 31 To 4
        SetMemory(0x662FE8, Add, 7),# units:Portrait  index:48    from 22 To 29
        SetMemory(0x663938, Add, -65536),# units:Mineral Cost  index:89    from 1 To 0
        SetMemory(0x65FDB0, Add, -65536),# units:Vespene Cost  index:89    from 1 To 0
        SetMemory(0x6604D8, Add, -65536),# units:Build Time  index:89    from 1 To 0
        SetMemory(0x6637AC, Add, -8),# units:Staredit Group Flags  index:12    from 10 To 2
        SetMemory(0x6637F8, Add, 8),# units:Staredit Group Flags  index:88    from 12 To 20
        SetMemory(0x663860, Add, 983040),# units:Staredit Group Flags  index:194    from 1 To 16
        SetMemory(0x663860, Add, 234881024),# units:Staredit Group Flags  index:195    from 2 To 16
        SetMemory(0x663864, Add, 12),# units:Staredit Group Flags  index:196    from 4 To 16
        SetMemory(0x663864, Add, 3840),# units:Staredit Group Flags  index:197    from 1 To 16
        SetMemory(0x663864, Add, 917504),# units:Staredit Group Flags  index:198    from 2 To 16
        SetMemory(0x663864, Add, 201326592),# units:Staredit Group Flags  index:199    from 4 To 16
        SetMemory(0x657368, Add, 1638400),# weapons:Label  index:69    from 289 To 314
        SetMemory(0x656CB4, Add, 10),# weapons:Graphics  index:3    from 143 To 153
        SetMemory(0x656D70, Add, -9),# weapons:Graphics  index:50    from 162 To 153
        SetMemory(0x656DBC, Add, 10),# weapons:Graphics  index:69    from 143 To 153
        SetMemory(0x656DC0, Add, -3),# weapons:Graphics  index:70    from 156 To 153
        SetMemory(0x656E44, Add, -49),# weapons:Graphics  index:103    from 202 To 153
        SetMemory(0x6579A0, Add, 65536),# weapons:Target Flags  index:5    from 2 To 3
        SetMemory(0x657A64, Add, 131072),# weapons:Target Flags  index:103    from 1 To 3
        SetMemory(0x657484, Add, 16),# weapons:Maximum Range  index:5    from 160 To 176
        SetMemory(0x6574F0, Add, -96),# weapons:Maximum Range  index:32    from 256 To 160
        SetMemory(0x657504, Add, 241),# weapons:Maximum Range  index:37    from 15 To 256
        SetMemory(0x657538, Add, 64),# weapons:Maximum Range  index:50    from 128 To 192
        SetMemory(0x657584, Add, 64),# weapons:Maximum Range  index:69    from 96 To 160
        SetMemory(0x657588, Add, 160),# weapons:Maximum Range  index:70    from 64 To 224
        SetMemory(0x65760C, Add, 32),# weapons:Maximum Range  index:103    from 192 To 224
        SetMemory(0x657258, Add, 33554432),# weapons:Weapon Type  index:3    from 2 To 4
        SetMemory(0x65725C, Add, 512),# weapons:Weapon Type  index:5    from 2 To 4
        SetMemory(0x657270, Add, 131072),# weapons:Weapon Type  index:26    from 2 To 4
        SetMemory(0x657288, Add, 131072),# weapons:Weapon Type  index:50    from 2 To 4
        SetMemory(0x65729C, Add, 65536),# weapons:Weapon Type  index:70    from 3 To 4
        SetMemory(0x6572BC, Add, 50331648),# weapons:Weapon Type  index:103    from 1 To 4
        SetMemory(0x6566A0, Add, 131072),# weapons:Weapon Behavior  index:50    from 0 To 2
        SetMemory(0x6566B4, Add, 0),# weapons:Weapon Behavior  index:69    from 2 To 2
        SetMemory(0x6566D4, Add, -100663296),# weapons:Weapon Behavior  index:103    from 8 To 2
        SetMemory(0x657084, Add, 0),# weapons:Remove After  index:69    from 255 To 255
        SetMemory(0x65673C, Add, 768),# weapons:Explosion Type  index:69    from 1 To 4
        SetMemory(0x65673C, Add, -196608),# weapons:Explosion Type  index:70    from 3 To 0
        SetMemory(0x65675C, Add, -402653184),# weapons:Explosion Type  index:103    from 24 To 0
        SetMemory(0x656EB4, Add, 90),# weapons:Damage Amount  index:2    from 10 To 100
        SetMemory(0x656EB4, Add, -1966080),# weapons:Damage Amount  index:3    from 30 To 0
        SetMemory(0x656EB8, Add, -1310720),# weapons:Damage Amount  index:5    from 30 To 10
        SetMemory(0x656EE4, Add, -16),# weapons:Damage Amount  index:26    from 16 To 0
        SetMemory(0x656EF8, Add, -2555904),# weapons:Damage Amount  index:37    from 50 To 11
        SetMemory(0x656F14, Add, -5),# weapons:Damage Amount  index:50    from 5 To 0
        SetMemory(0x656F38, Add, -1310720),# weapons:Damage Amount  index:69    from 20 To 0
        SetMemory(0x656F3C, Add, -30),# weapons:Damage Amount  index:70    from 30 To 0
        SetMemory(0x656F7C, Add, -393216),# weapons:Damage Amount  index:103    from 6 To 0
        SetMemory(0x656FB8, Add, 369098752),# weapons:Weapon Cooldown  index:3    from 22 To 44
        SetMemory(0x656FBC, Add, 0),# weapons:Weapon Cooldown  index:5    from 22 To 22
        SetMemory(0x656FD8, Add, 239),# weapons:Weapon Cooldown  index:32    from 1 To 240
        SetMemory(0x656FDC, Add, 57600),# weapons:Weapon Cooldown  index:37    from 15 To 240
        SetMemory(0x656FE8, Add, 4915200),# weapons:Weapon Cooldown  index:50    from 22 To 97
        SetMemory(0x656FFC, Add, 55808),# weapons:Weapon Cooldown  index:69    from 22 To 240
        SetMemory(0x656FFC, Add, 11272192),# weapons:Weapon Cooldown  index:70    from 20 To 192
        SetMemory(0x65701C, Add, 939524096),# weapons:Weapon Cooldown  index:103    from 64 To 120
        SetMemory(0x6564E0, Add, -16777216),# weapons:Damage Factor  index:3    from 1 To 0
        SetMemory(0x6564E4, Add, 0),# weapons:Damage Factor  index:5    from 1 To 1
        SetMemory(0x656510, Add, 0),# weapons:Damage Factor  index:50    from 1 To 1
        SetMemory(0x656808, Add, -7536640),# weapons:Icon  index:69    from 355 To 240
        SetMemory(0x6CA378, Add, 173),# flingy:Sprite  index:48    from 200 To 373
        SetMemory(0x6CA3B8, Add, 7667712),# flingy:Sprite  index:81    from 239 To 356
        SetMemory(0x6CA40C, Add, 90),# flingy:Sprite  index:122    from 283 To 373
        SetMemory(0x6CA40C, Add, 4718592),# flingy:Sprite  index:123    from 284 To 356
        SetMemory(0x6CA410, Add, 81),# flingy:Sprite  index:124    from 285 To 366
        SetMemory(0x6CA488, Add, -143),# flingy:Sprite  index:184    from 481 To 338
        SetMemory(0x6C9F08, Add, -1),# flingy:Speed  index:4    from 1 To 0
        SetMemory(0x6C9FA4, Add, 20),# flingy:Speed  index:43    from 1280 To 1300
        SetMemory(0x6C9FB8, Add, 999),# flingy:Speed  index:48    from 1 To 1000
        SetMemory(0x6CA02C, Add, -1),# flingy:Speed  index:77    from 1 To 0
        SetMemory(0x6CA03C, Add, 220),# flingy:Speed  index:81    from 1280 To 1500
        SetMemory(0x6CA058, Add, -854),# flingy:Speed  index:88    from 1707 To 853
        SetMemory(0x6CA0E0, Add, 1000),# flingy:Speed  index:122    from 0 To 1000
        SetMemory(0x6CA0E4, Add, 1500),# flingy:Speed  index:123    from 0 To 1500
        SetMemory(0x6CA0E8, Add, 1500),# flingy:Speed  index:124    from 0 To 1500
        SetMemory(0x6CA140, Add, -7533),# flingy:Speed  index:146    from 8533 To 1000
        SetMemory(0x6CA148, Add, -24600),# flingy:Speed  index:148    from 25600 To 1000
        SetMemory(0x6CA168, Add, 1500),# flingy:Speed  index:156    from 0 To 1500
        SetMemory(0x6CA178, Add, -15867),# flingy:Speed  index:160    from 17067 To 1200
        SetMemory(0x6CA180, Add, -7033),# flingy:Speed  index:162    from 8533 To 1500
        SetMemory(0x6CA184, Add, -7533),# flingy:Speed  index:163    from 8533 To 1000
        SetMemory(0x6CA1D8, Add, 900),# flingy:Speed  index:184    from 0 To 900
        SetMemory(0x6C9C80, Add, -1),# flingy:Acceleration  index:4    from 1 To 0
        SetMemory(0x6C9CCC, Add, 3407872),# flingy:Acceleration  index:43    from 48 To 100
        SetMemory(0x6C9CD8, Add, 999),# flingy:Acceleration  index:48    from 1 To 1000
        SetMemory(0x6C9D10, Add, -65536),# flingy:Acceleration  index:77    from 1 To 0
        SetMemory(0x6C9D18, Add, 93913088),# flingy:Acceleration  index:81    from 67 To 1500
        SetMemory(0x6C9D28, Add, -71),# flingy:Acceleration  index:88    from 100 To 29
        SetMemory(0x6C9D6C, Add, 1000),# flingy:Acceleration  index:122    from 0 To 1000
        SetMemory(0x6C9D6C, Add, 65536000),# flingy:Acceleration  index:123    from 0 To 1000
        SetMemory(0x6C9D70, Add, 1500),# flingy:Acceleration  index:124    from 0 To 1500
        SetMemory(0x6C9D9C, Add, -167),# flingy:Acceleration  index:146    from 267 To 100
        SetMemory(0x6C9DA0, Add, -8433),# flingy:Acceleration  index:148    from 8533 To 100
        SetMemory(0x6C9DB0, Add, 1500),# flingy:Acceleration  index:156    from 0 To 1500
        SetMemory(0x6C9DB8, Add, 350),# flingy:Acceleration  index:160    from 850 To 1200
        SetMemory(0x6C9DBC, Add, 833),# flingy:Acceleration  index:162    from 667 To 1500
        SetMemory(0x6C9DBC, Add, -37158912),# flingy:Acceleration  index:163    from 667 To 100
        SetMemory(0x6C9DE8, Add, 900),# flingy:Acceleration  index:184    from 0 To 900
        SetMemory(0x6C9940, Add, -1),# flingy:Halt Distance  index:4    from 1 To 0
        SetMemory(0x6C99DC, Add, -16967),# flingy:Halt Distance  index:43    from 17067 To 100
        SetMemory(0x6C99F0, Add, 99),# flingy:Halt Distance  index:48    from 1 To 100
        SetMemory(0x6C9A64, Add, -1),# flingy:Halt Distance  index:77    from 1 To 0
        SetMemory(0x6C9A74, Add, -12127),# flingy:Halt Distance  index:81    from 12227 To 100
        SetMemory(0x6C9A90, Add, 14569),# flingy:Halt Distance  index:88    from 14569 To 29138
        SetMemory(0x6C9B18, Add, 100),# flingy:Halt Distance  index:122    from 0 To 100
        SetMemory(0x6C9B1C, Add, 100),# flingy:Halt Distance  index:123    from 0 To 100
        SetMemory(0x6C9B20, Add, 100),# flingy:Halt Distance  index:124    from 0 To 100
        SetMemory(0x6C9B78, Add, -136252),# flingy:Halt Distance  index:146    from 136352 To 100
        SetMemory(0x6C9B80, Add, -38302),# flingy:Halt Distance  index:148    from 38402 To 100
        SetMemory(0x6C9BA0, Add, 100),# flingy:Halt Distance  index:156    from 0 To 100
        SetMemory(0x6C9BB0, Add, -171243),# flingy:Halt Distance  index:160    from 171343 To 100
        SetMemory(0x6C9BB8, Add, -54482),# flingy:Halt Distance  index:162    from 54582 To 100
        SetMemory(0x6C9BBC, Add, -54482),# flingy:Halt Distance  index:163    from 54582 To 100
        SetMemory(0x6C9C10, Add, 100),# flingy:Halt Distance  index:184    from 0 To 100
        SetMemory(0x6C9E48, Add, 1174405120),# flingy:Turn Radius  index:43    from 30 To 100
        SetMemory(0x6C9E50, Add, -27),# flingy:Turn Radius  index:48    from 27 To 0
        SetMemory(0x6C9E70, Add, -10240),# flingy:Turn Radius  index:81    from 40 To 0
        SetMemory(0x6C9E78, Add, -7),# flingy:Turn Radius  index:88    from 40 To 33
        SetMemory(0x6C9EB0, Add, 5701632),# flingy:Turn Radius  index:146    from 13 To 100
        SetMemory(0x6C9EB4, Add, -127),# flingy:Turn Radius  index:148    from 127 To 0
        SetMemory(0x6C9EBC, Add, 100),# flingy:Turn Radius  index:156    from 0 To 100
        SetMemory(0x6C9EC0, Add, -27),# flingy:Turn Radius  index:160    from 127 To 100
        SetMemory(0x6C9EC0, Add, -2621440),# flingy:Turn Radius  index:162    from 40 To 0
        SetMemory(0x6C9EC0, Add, 1006632960),# flingy:Turn Radius  index:163    from 40 To 100
        SetMemory(0x6C9ED8, Add, 100),# flingy:Turn Radius  index:184    from 0 To 100
        SetMemory(0x6C9888, Add, -2),# flingy:Movement Control  index:48    from 2 To 0
        SetMemory(0x6C98D0, Add, -131072),# flingy:Movement Control  index:122    from 2 To 0
        SetMemory(0x6C98D0, Add, -33554432),# flingy:Movement Control  index:123    from 2 To 0
        SetMemory(0x6C98D4, Add, -2),# flingy:Movement Control  index:124    from 2 To 0
        SetMemory(0x6C98E8, Add, -65536),# flingy:Movement Control  index:146    from 1 To 0
        SetMemory(0x6C98EC, Add, -1),# flingy:Movement Control  index:148    from 1 To 0
        SetMemory(0x6C98F4, Add, -2),# flingy:Movement Control  index:156    from 2 To 0
        SetMemory(0x6C98F8, Add, -1),# flingy:Movement Control  index:160    from 1 To 0
        SetMemory(0x6C98F8, Add, -65536),# flingy:Movement Control  index:162    from 1 To 0
        SetMemory(0x6C98F8, Add, -16777216),# flingy:Movement Control  index:163    from 1 To 0
        SetMemory(0x6C9910, Add, -2),# flingy:Movement Control  index:184    from 2 To 0
        SetMemory(0x666348, Add, 6488064),# sprites:Image File  index:245    from 258 To 357
        SetMemory(0x66638C, Add, 110),# sprites:Image File  index:278    from 342 To 452
        SetMemory(0x66C1DC, Add, -1),# images:Clickable  index:140    from 1 To 0
        SetMemory(0x66C1E0, Add, -16777216),# images:Clickable  index:147    from 1 To 0
        SetMemory(0x66C2B4, Add, -256),# images:Clickable  index:357    from 1 To 0
        SetMemory(0x66D6D4, Add, -256),# images:Use Full Iscript  index:509    from 1 To 0
        SetMemory(0x669EA4, Add, 655360),# images:Draw Function  index:126    from 0 To 10
        SetMemory(0x669EAC, Add, 655360),# images:Draw Function  index:134    from 0 To 10
        SetMemory(0x669F1C, Add, -8),# images:Draw Function  index:244    from 10 To 2
        SetMemory(0x66A030, Add, 3),# images:Draw Function  index:520    from 9 To 12
        SetMemory(0x66A034, Add, 0),# images:Draw Function  index:524    from 9 To 9
        SetMemory(0x66EE94, Add, -71),# images:Iscript ID  index:147    from 160 To 89
        SetMemory(0x66F1D0, Add, -122),# images:Iscript ID  index:354    from 211 To 89
        SetMemory(0x66F1FC, Add, -61),# images:Iscript ID  index:365    from 306 To 245
        SetMemory(0x66F200, Add, -61),# images:Iscript ID  index:366    from 306 To 245
        SetMemory(0x66F204, Add, -217),# images:Iscript ID  index:367    from 306 To 89
        SetMemory(0x66F264, Add, -244),# images:Iscript ID  index:391    from 305 To 61
        SetMemory(0x66F334, Add, -197),# images:Iscript ID  index:443    from 286 To 89
        SetMemory(0x66F3B0, Add, -266),# images:Iscript ID  index:474    from 326 To 60
        SetMemory(0x66F434, Add, -168),# images:Iscript ID  index:507    from 257 To 89
        SetMemory(0x66F43C, Add, -171),# images:Iscript ID  index:509    from 260 To 89
        SetMemory(0x66F454, Add, -206),# images:Iscript ID  index:515    from 266 To 60
        SetMemory(0x66F468, Add, 25),# images:Iscript ID  index:520    from 230 To 255
        SetMemory(0x66F46C, Add, -143),# images:Iscript ID  index:521    from 232 To 89
        SetMemory(0x66F474, Add, -145),# images:Iscript ID  index:523    from 234 To 89
        SetMemory(0x66F478, Add, -146),# images:Iscript ID  index:524    from 235 To 89
        SetMemory(0x66F48C, Add, -158),# images:Iscript ID  index:529    from 240 To 82
        SetMemory(0x66F49C, Add, -157),# images:Iscript ID  index:533    from 246 To 89
        SetMemory(0x66F4A0, Add, -154),# images:Iscript ID  index:534    from 243 To 89
        SetMemory(0x66F4BC, Add, -158),# images:Iscript ID  index:541    from 247 To 89
        SetMemory(0x66F4D0, Add, -172),# images:Iscript ID  index:546    from 253 To 81
        SetMemory(0x66F4D8, Add, -179),# images:Iscript ID  index:548    from 268 To 89
        SetMemory(0x66F500, Add, -76),# images:Iscript ID  index:558    from 321 To 245
        SetMemory(0x655760, Add, -6553600),# upgrades:Mineral Cost Base  index:17    from 100 To 0
        SetMemory(0x655860, Add, -6553600),# upgrades:Vespene Cost Base  index:17    from 100 To 0
        SetMemory(0x655BA0, Add, -98304000),# upgrades:Research Time Base  index:17    from 1500 To 0
        SetMemory(0x656380, Add, -6553600),# techdata:Energy Required  index:1    from 100 To 0
    ])

