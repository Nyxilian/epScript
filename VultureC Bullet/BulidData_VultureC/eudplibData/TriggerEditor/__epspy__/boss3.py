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
# (Line 4) var boss3EPD;
boss3EPD = EUDVariable()
# (Line 5) var boss3Face;
boss3Face = EUDVariable()
# (Line 6) var boss3AttkCycle;
boss3AttkCycle = EUDVariable()
# (Line 8) const s = StringBuffer(1024);
s = _CGFW(lambda: [StringBuffer(1024)], 1)[0]
# (Line 10) function stage3() {
@EUDFunc
def f_stage3():
    # (Line 11) boss3Face = bread_epd(boss3EPD + 0x21/4, 1);
    boss3Face << (f_bread_epd(boss3EPD + 0x21 // 4, 1))
    # (Line 12) boss3AttkCycle = bread_epd(boss3EPD + 0x55/4, 1);
    boss3AttkCycle << (f_bread_epd(boss3EPD + 0x55 // 4, 1))
    # (Line 14) once {
    if EUDExecuteOnce()():
        # (Line 15) fx.setBulletDam(4, 20);
        fx.f_setBulletDam(4, 20)
        # (Line 16) }
        # (Line 18) if(fx.cur_bSwitch() == 0) { //보스 소환
    EUDEndExecuteOnce()
    if EUDIf()(fx.f_cur_bSwitch() == 0):
        # (Line 19) boss3EPD = fx.SetNextUnitEPD();
        boss3EPD << (fx.SetNextUnitEPD())
        # (Line 20) CreateUnit(1, 48, bossLoc, 6);
        # (Line 21) fx.set_bSwitch(1);
        DoActions(CreateUnit(1, 48, bossLoc, 6))
        fx.f_set_bSwitch(1)
        # (Line 22) foreach(cp : EUDLoopPlayer("Human")) {
        for cp in EUDLoopPlayer("Human"):
            # (Line 23) setcurpl(cp);
            f_setcurpl(cp)
            # (Line 24) s.printAt(0, "\n\n\n\n\n\n\n\n\n");
            s.printAt(0, "\n\n\n\n\n\n\n\n\n")
            # (Line 25) s.printAt(2, "\x13\x1E━━━\x02━━━\x04━━ \x1F[ \x08위   험 \x1F]\x04 ━━\x02━━━\x1E━━━\n\n\x13\x07[\x04 Stage \x033 \x07]\n\n\x13\x04폭풍의 \x03궤멸충\n\n\x13\x1E━━━\x02━━━━\x04━━━━━━━\x02━━━━\x1E━━━━");
            s.printAt(2, "\x13\x1E━━━\x02━━━\x04━━ \x1F[ \x08위   험 \x1F]\x04 ━━\x02━━━\x1E━━━\n\n\x13\x07[\x04 Stage \x033 \x07]\n\n\x13\x04폭풍의 \x03궤멸충\n\n\x13\x1E━━━\x02━━━━\x04━━━━━━━\x02━━━━\x1E━━━━")
            # (Line 26) }
            # (Line 27) }

        # (Line 29) fx.playerRevive(); //플레이어 소환
    EUDEndIf()
    fx.f_playerRevive()
    # (Line 31) fx.printBossHP(boss3EPD);
    fx.f_printBossHP(boss3EPD)
    # (Line 33) if(fx.bulletTimer(40) == True) { //중앙 미사일
    if EUDIf()(fx.f_bulletTimer(40) == True):
        # (Line 34) CreateUnit(8, 195, bossLoc, 7);
        # (Line 35) setcurpl(7);
        DoActions(CreateUnit(8, 195, bossLoc, 7))
        f_setcurpl(7)
        # (Line 36) RunAIScriptAt("JYDg", bossLoc);
        # (Line 37) }
        DoActions(RunAIScriptAt("JYDg", bossLoc))
        # (Line 39) if(boss3AttkCycle % 12 == 0 && boss3AttkCycle > 59) { //보스 기본 공격
    EUDEndIf()
    if EUDIf()(EUDSCAnd()(boss3AttkCycle % 12 == 0)(boss3AttkCycle <= 59, neg=True)()):
        # (Line 40) var currentMissile;
        currentMissile = EUDVariable()
        # (Line 41) for(var i = 0; i < 8; i++) {
        i = EUDVariable()
        i << (0)
        if EUDWhile()(i >= 8, neg=True):
            def _t5():
                i.__iadd__(1)
            # (Line 42) currentMissile = fx.SetNextUnitEPD();
            currentMissile << (fx.SetNextUnitEPD())
            # (Line 43) CreateUnit(1, 198, bossLoc, 6);
            # (Line 44) fx.SetMissileDir(currentMissile, (boss3Face + 32*i) % 256);
            DoActions(CreateUnit(1, 198, bossLoc, 6))
            fx.SetMissileDir(currentMissile, (boss3Face + 32 * i) % 256)
            # (Line 45) }
            # (Line 46) Order(198, 6, "Anywhere", Move, "PlayerRevive");
            EUDSetContinuePoint()
            _t5()
        EUDEndWhile()
        # (Line 47) }
        DoActions(Order(198, 6, "Anywhere", Move, "PlayerRevive"))
        # (Line 49) if(Deaths(6, Exactly, 1, 48)) {
    EUDEndIf()
    if EUDIf()(Deaths(6, Exactly, 1, 48)):
        # (Line 50) KillUnit(19, Force1);
        # (Line 51) fx.set_bSwitch(0);
        DoActions(KillUnit(19, Force1))
        fx.f_set_bSwitch(0)
        # (Line 52) fx.set_pSwitch(0);
        fx.f_set_pSwitch(0)
        # (Line 53) fx.set_Stage(4);
        fx.f_set_Stage(4)
        # (Line 54) fx.bulletInit();
        fx.f_bulletInit()
        # (Line 55) fx.playerBlockInit();
        fx.f_playerBlockInit()
        # (Line 56) foreach(cp : EUDLoopPlayer("Human")) {
        for cp in EUDLoopPlayer("Human"):
            # (Line 57) setcurpl(cp);
            f_setcurpl(cp)
            # (Line 58) CenterView("PlayerRevive");
            # (Line 59) }
            DoActions(CenterView("PlayerRevive"))
            # (Line 60) }

        # (Line 61) }
    EUDEndIf()