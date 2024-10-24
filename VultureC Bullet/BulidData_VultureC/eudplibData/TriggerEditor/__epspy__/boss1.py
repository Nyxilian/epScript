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
# (Line 4) var boss1EPD;
boss1EPD = EUDVariable()
# (Line 5) var boss1Face;
boss1Face = EUDVariable()
# (Line 7) const s = StringBuffer(1024);
s = _CGFW(lambda: [StringBuffer(1024)], 1)[0]
# (Line 9) function stage1() {
@EUDFunc
def f_stage1():
    # (Line 10) boss1Face = bread_epd(boss1EPD + 0x21/4, 1);
    boss1Face << (f_bread_epd(boss1EPD + 0x21 // 4, 1))
    # (Line 12) if(fx.cur_bSwitch() == 0) {
    if EUDIf()(fx.f_cur_bSwitch() == 0):
        # (Line 13) SetMemory(0x657A9C, SetTo, 31);
        # (Line 14) boss1EPD = fx.SetNextUnitEPD();
        DoActions(SetMemory(0x657A9C, SetTo, 31))
        boss1EPD << (fx.SetNextUnitEPD())
        # (Line 15) CreateUnit(1, 15, bossLoc, 6);
        # (Line 16) fx.set_bSwitch(1);
        DoActions(CreateUnit(1, 15, bossLoc, 6))
        fx.f_set_bSwitch(1)
        # (Line 17) foreach(cp : EUDLoopPlayer("Human")) {
        for cp in EUDLoopPlayer("Human"):
            # (Line 18) setcurpl(cp);
            f_setcurpl(cp)
            # (Line 19) s.printAt(0, "\n\n\n\n\n\n\n\n\n");
            s.printAt(0, "\n\n\n\n\n\n\n\n\n")
            # (Line 20) s.printAt(2, "\x13\x1E━━━\x02━━━\x04━━ \x1F[ \x08위   험 \x1F]\x04 ━━\x02━━━\x1E━━━\n\n\x13\x07[\x04 Stage \x0F1 \x07]\n\n\x13\x04평범한 \x03시민\n\n\x13\x1E━━━\x02━━━━\x04━━━━━━━\x02━━━━\x1E━━━━");
            s.printAt(2, "\x13\x1E━━━\x02━━━\x04━━ \x1F[ \x08위   험 \x1F]\x04 ━━\x02━━━\x1E━━━\n\n\x13\x07[\x04 Stage \x0F1 \x07]\n\n\x13\x04평범한 \x03시민\n\n\x13\x1E━━━\x02━━━━\x04━━━━━━━\x02━━━━\x1E━━━━")
            # (Line 21) CenterView("PlayerRevive");
            # (Line 22) }
            DoActions(CenterView("PlayerRevive"))
            # (Line 23) }

        # (Line 24) fx.playerRevive();
    EUDEndIf()
    fx.f_playerRevive()
    # (Line 26) fx.printBossHP(boss1EPD);
    fx.f_printBossHP(boss1EPD)
    # (Line 28) if(fx.bulletTimer(72) == True) {
    if EUDIf()(fx.f_bulletTimer(72) == True):
        # (Line 29) CreateUnit(5, 194, bossLoc, 7);
        # (Line 30) setcurpl(7);
        DoActions(CreateUnit(5, 194, bossLoc, 7))
        f_setcurpl(7)
        # (Line 31) RunAIScriptAt("JYDg", bossLoc);
        # (Line 32) }
        DoActions(RunAIScriptAt("JYDg", bossLoc))
        # (Line 34) if(Deaths(6, Exactly, 1, 15)) {
    EUDEndIf()
    if EUDIf()(Deaths(6, Exactly, 1, 15)):
        # (Line 35) KillUnit(19, Force1);
        # (Line 36) fx.set_bSwitch(0);
        DoActions(KillUnit(19, Force1))
        fx.f_set_bSwitch(0)
        # (Line 37) fx.set_pSwitch(0);
        fx.f_set_pSwitch(0)
        # (Line 38) fx.set_Stage(2);
        fx.f_set_Stage(2)
        # (Line 39) fx.bulletInit();
        fx.f_bulletInit()
        # (Line 40) fx.playerBlockInit();
        fx.f_playerBlockInit()
        # (Line 41) foreach(cp : EUDLoopPlayer("Human")) {
        for cp in EUDLoopPlayer("Human"):
            # (Line 42) setcurpl(cp);
            f_setcurpl(cp)
            # (Line 43) CenterView("PlayerRevive");
            # (Line 44) }
            DoActions(CenterView("PlayerRevive"))
            # (Line 45) }

        # (Line 46) }
    EUDEndIf()
