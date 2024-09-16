## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY
from eudplib import *

def _IGVA(vList, exprListGen):
    def _():
        exprList = exprListGen()
        SetVariables(vList, exprList)
    EUDOnStart(_)

def _CGFW(exprf, retn):
    rets = [ExprProxy(None) for _ in range(retn)]
    def _():
        vals = exprf()
        for ret, val in zip(rets, vals):
            ret._value = val
    EUDOnStart(_)
    return rets

def _ARR(items):
    k = EUDArray(len(items))
    for i, item in enumerate(items):
        k[i] = item
    return k

def _VARR(items):
    k = EUDVArray(len(items))()
    for i, item in enumerate(items):
        k[i] = item
    return k

def _SRET(v, klist):
    return List2Assignable([v[k] for k in klist])

def _SV(dL, sL):
    [d << s for d, s in zip(FlattenList(dL), FlattenList(sL))]

class _ATTW:
    def __init__(self, obj, attrName):
        self.obj = obj
        self.attrName = attrName

    def __lshift__(self, r):
        setattr(self.obj, self.attrName, r)

    def __iadd__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov + v)

    def __isub__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov - v)

    def __imul__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov * v)

    def __ifloordiv__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov // v)

    def __iand__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov & v)

    def __ior__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov | v)

    def __ixor__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov ^ v)

class _ARRW:
    def __init__(self, obj, index):
        self.obj = obj
        self.index = index

    def __lshift__(self, r):
        self.obj[self.index] = r

    def __iadd__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov + v

    def __isub__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov - v

    def __imul__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov * v

    def __ifloordiv__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov // v

    def __iand__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov & v

    def __ior__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov | v

    def __ixor__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov ^ v

def _L2V(l):
    ret = EUDVariable()
    if EUDIf()(l):
        ret << 1
    if EUDElse()():
        ret << 0
    EUDEndIf()
    return ret

def _MVAR(vs):
    return List2Assignable([
        v.makeL() if IsEUDVariable(v) else EUDVariable() << v
        for v in FlattenList(vs)])

def _LSH(l, r):
    if IsEUDVariable(l):  return f_bitlshift(l, r)
    else: return l << r

## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY

# (Line 1) import functions as fx;
import functions as fx
# (Line 3) var bossLoc = $L("Boss");
bossLoc = EUDCreateVariables(1)
_IGVA([bossLoc], lambda: [GetLocationIndex("Boss")])
# (Line 4) var boss5EPD;
boss5EPD = EUDVariable()
# (Line 5) var boss5Face;
boss5Face = EUDVariable()
# (Line 6) var boss5AttkCycle;
boss5AttkCycle = EUDVariable()
# (Line 7) var boss5TargetEPD;
boss5TargetEPD = EUDVariable()
# (Line 8) var boss5TargetPlayer;
boss5TargetPlayer = EUDVariable()
# (Line 9) var bulletHead = 0;
bulletHead = EUDCreateVariables(1)
_IGVA([bulletHead], lambda: [0])
# (Line 10) var bulletSwitch = 0;
bulletSwitch = EUDCreateVariables(1)
_IGVA([bulletSwitch], lambda: [0])
# (Line 12) const s = StringBuffer(1024);
s = _CGFW(lambda: [StringBuffer(1024)], 1)[0]
# (Line 14) function stage5() {
@EUDFunc
def f_stage5():
    # (Line 15) boss5Face = bread_epd(boss5EPD + 0x21/4, 1);
    boss5Face << (f_bread_epd(boss5EPD + 0x21 // 4, 1))
    # (Line 16) boss5AttkCycle = bread_epd(boss5EPD + 0x55/4, 1);
    boss5AttkCycle << (f_bread_epd(boss5EPD + 0x55 // 4, 1))
    # (Line 18) once {
    if EUDExecuteOnce()():
        # (Line 19) wwrite(0x6C9858 + 2752 + 163 * 2, 195); //비행정보 163 탄환 스프라이트스카웃 변형
        f_wwrite(0x6C9858 + 2752 + 163 * 2, 195)
        # (Line 20) dwwrite(0x6C9858 + 1696 + 163 * 4, 1400); //비행정보 163 최고 속도 변환
        f_dwwrite(0x6C9858 + 1696 + 163 * 4, 1400)
        # (Line 21) wwrite(0x665AC0 + 1696 + 195 * 2, 365); //스프라이트 195 이미지 365으로 변환
        f_wwrite(0x665AC0 + 1696 + 195 * 2, 365)
        # (Line 22) fx.setBulletDam(1, 15);
        fx.f_setBulletDam(1, 15)
        # (Line 23) }
        # (Line 25) if(fx.cur_bSwitch() == 0) {
    EUDEndExecuteOnce()
    if EUDIf()(fx.f_cur_bSwitch() == 0):
        # (Line 26) boss5EPD = fx.SetNextUnitEPD();
        boss5EPD << (fx.SetNextUnitEPD())
        # (Line 27) CreateUnit(1, 68, bossLoc, 6);
        # (Line 28) fx.set_bSwitch(1);
        DoActions(CreateUnit(1, 68, bossLoc, 6))
        fx.f_set_bSwitch(1)
        # (Line 29) foreach(cp : EUDLoopPlayer("Human")) {
        for cp in EUDLoopPlayer("Human"):
            # (Line 30) setcurpl(cp);
            f_setcurpl(cp)
            # (Line 31) s.printAt(0, "\n\n\n\n\n\n\n\n\n");
            s.printAt(0, "\n\n\n\n\n\n\n\n\n")
            # (Line 32) s.printAt(2, "\x13\x1E━━━\x02━━━\x04━━ \x1F[ \x08위   험 \x1F]\x04 ━━\x02━━━\x1E━━━\n\n\x13\x07[\x04 Stage \x115 \x07]\n\n\x13\x1E혹한의 \x03거인\n\n\x13\x1E━━━\x02━━━━\x04━━━━━━━\x02━━━━\x1E━━━━");
            s.printAt(2, "\x13\x1E━━━\x02━━━\x04━━ \x1F[ \x08위   험 \x1F]\x04 ━━\x02━━━\x1E━━━\n\n\x13\x07[\x04 Stage \x115 \x07]\n\n\x13\x1E혹한의 \x03거인\n\n\x13\x1E━━━\x02━━━━\x04━━━━━━━\x02━━━━\x1E━━━━")
            # (Line 33) }
            # (Line 34) }

        # (Line 35) fx.playerRevive();
    EUDEndIf()
    fx.f_playerRevive()
    # (Line 37) fx.printBossHP(boss5EPD);
    fx.f_printBossHP(boss5EPD)
    # (Line 39) fx.bulletReflector();//중앙 탄막
    fx.f_bulletReflector()
    # (Line 41) if(fx.bulletTimer(72) == True) {
    if EUDIf()(fx.f_bulletTimer(72) == True):
        # (Line 42) CreateUnit(10, 195, bossLoc, 7);
        # (Line 43) setcurpl(7);
        DoActions(CreateUnit(10, 195, bossLoc, 7))
        f_setcurpl(7)
        # (Line 44) RunAIScriptAt("JYDg", bossLoc);
        # (Line 45) }
        DoActions(RunAIScriptAt("JYDg", bossLoc))
        # (Line 48) if(boss5AttkCycle == 191) { //보스 평타 발사
    EUDEndIf()
    if EUDIf()(boss5AttkCycle == 191):
        # (Line 49) boss5TargetEPD = EPD(dwread_epd(boss5EPD + 0x5C/4));
        boss5TargetEPD << (EPD(f_dwread_epd(boss5EPD + 0x5C // 4)))
        # (Line 50) boss5TargetPlayer = bread_epd(boss5TargetEPD + 0x4C/4, 0);
        boss5TargetPlayer << (f_bread_epd(boss5TargetEPD + 0x4C // 4, 0))
        # (Line 51) MoveLocation("BossTargetSmall", 19, boss5TargetPlayer, fx.loc[boss5TargetPlayer]);
        # (Line 52) MoveLocation("BossTarget", 19, boss5TargetPlayer, fx.loc[boss5TargetPlayer]);
        DoActions(MoveLocation("BossTargetSmall", 19, boss5TargetPlayer, fx.loc[boss5TargetPlayer]))
        # (Line 53) CreateUnit(1, 196, bossLoc, 6);
        DoActions(MoveLocation("BossTarget", 19, boss5TargetPlayer, fx.loc[boss5TargetPlayer]))
        # (Line 54) Order(196, 6, bossLoc, Move, "BossTarget");
        DoActions(CreateUnit(1, 196, bossLoc, 6))
        # (Line 55) }
        DoActions(Order(196, 6, bossLoc, Move, "BossTarget"))
        # (Line 57) if(Bring(6, Exactly, 1, 196, "BossTargetSmall")) { //평타 도달 조건문
    EUDEndIf()
    if EUDIf()(Bring(6, Exactly, 1, 196, "BossTargetSmall")):
        # (Line 58) RemoveUnitAt(1, 196, "BossTargetSmall", 6);
        # (Line 59) bulletSwitch = 1;
        DoActions(RemoveUnitAt(1, 196, "BossTargetSmall", 6))
        bulletSwitch << (1)
        # (Line 60) }
        # (Line 62) if(fx.bulletTimer(3) == True && bulletSwitch == 1) {//도달시 산탄 생성
    EUDEndIf()
    if EUDIf()(EUDSCAnd()(fx.f_bulletTimer(3) == True)(bulletSwitch == 1)()):
        # (Line 63) MoveLocation("B5", 104, 7, "BossTargetSmall");
        # (Line 64) fx.PolarLocation("B5", 64, 20 * (bulletHead % 18));
        DoActions(MoveLocation("B5", 104, 7, "BossTargetSmall"))
        fx.PolarLocation("B5", 64, 20 * (bulletHead % 18))
        # (Line 65) CreateUnit(1, 199, "B5", 7);
        # (Line 66) bulletHead++;
        DoActions(CreateUnit(1, 199, "B5", 7))
        bulletHead.__iadd__(1)
        # (Line 67) }
        # (Line 69) if(bulletHead % 18 == 17) {//산탄 중앙이동
    EUDEndIf()
    if EUDIf()(bulletHead % 18 == 17):
        # (Line 70) bulletSwitch = 0;
        bulletSwitch << (0)
        # (Line 71) Order(199, 7, "Anywhere", Move, "BossTargetSmall");
        # (Line 72) }
        DoActions(Order(199, 7, "Anywhere", Move, "BossTargetSmall"))
        # (Line 74) if(Bring(7, AtLeast, 1, 199, "BossTargetSmall")) {//정야독
    EUDEndIf()
    if EUDIf()(Bring(7, AtLeast, 1, 199, "BossTargetSmall")):
        # (Line 75) GiveUnits(All, 199, 7, "BossTargetSmall", 6);
        # (Line 76) setcurpl(6);
        DoActions(GiveUnits(All, 199, 7, "BossTargetSmall", 6))
        f_setcurpl(6)
        # (Line 77) RunAIScriptAt("JYDg", "BossTargetSmall");
        # (Line 78) bulletHead = 0;
        DoActions(RunAIScriptAt("JYDg", "BossTargetSmall"))
        bulletHead << (0)
        # (Line 79) }
        # (Line 81) if(Deaths(6, Exactly, 1, 68)) {
    EUDEndIf()
    if EUDIf()(Deaths(6, Exactly, 1, 68)):
        # (Line 82) KillUnit(19, Force1);
        # (Line 83) fx.set_bSwitch(0);
        DoActions(KillUnit(19, Force1))
        fx.f_set_bSwitch(0)
        # (Line 84) fx.set_pSwitch(0);
        fx.f_set_pSwitch(0)
        # (Line 85) fx.set_Stage(6);
        fx.f_set_Stage(6)
        # (Line 86) fx.bulletInit();
        fx.f_bulletInit()
        # (Line 87) fx.playerBlockInit();
        fx.f_playerBlockInit()
        # (Line 88) foreach(cp : EUDLoopPlayer("Human")) {
        for cp in EUDLoopPlayer("Human"):
            # (Line 89) setcurpl(cp);
            f_setcurpl(cp)
            # (Line 90) CenterView("PlayerRevive");
            # (Line 91) }
            DoActions(CenterView("PlayerRevive"))
            # (Line 92) }

        # (Line 93) }
    EUDEndIf()
