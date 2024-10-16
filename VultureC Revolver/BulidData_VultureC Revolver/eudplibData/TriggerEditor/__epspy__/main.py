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

# (Line 1) import PluginVariables as msqcvar;
import PluginVariables as msqcvar
# (Line 2) import functions as fx;
import functions as fx
# (Line 4) const s = StringBuffer(1024);
s = _CGFW(lambda: [StringBuffer(1024)], 1)[0]
# (Line 6) function onPluginStart() {
@EUDFunc
def onPluginStart():
    # (Line 8) SetMemory(0x5124F0, SetTo, 21); //2배속
    # (Line 9) fx.playerRev();
    DoActions(SetMemory(0x5124F0, SetTo, 21))
    fx.f_playerRev()
    # (Line 10) fx.variableInit();
    fx.f_variableInit()
    # (Line 11) foreach(cp : EUDLoopPlayer("Computer")) {
    for cp in EUDLoopPlayer("Computer"):
        # (Line 12) setcurpl(cp);
        f_setcurpl(cp)
        # (Line 13) SetAllianceStatus(Force1, Enemy);
        # (Line 14) }
        DoActions(SetAllianceStatus(Force1, Enemy))
        # (Line 15) foreach(cp : EUDLoopPlayer("Human")) {

    for cp in EUDLoopPlayer("Human"):
        # (Line 16) setcurpl(cp);
        f_setcurpl(cp)
        # (Line 17) RunAIScript("+Vi7");
        # (Line 18) }
        DoActions(RunAIScript("+Vi7"))
        # (Line 19) }

    # (Line 21) function beforeTriggerExec() {

@EUDFunc
def beforeTriggerExec():
    # (Line 23) }
    # (Line 25) function afterTriggerExec() {
    pass

@EUDFunc
def afterTriggerExec():
    # (Line 27) fx.detectHold();
    fx.f_detectHold()
    # (Line 28) SetMemory(0x6509A0, SetTo, 0); //EUD터보
    # (Line 29) }
    DoActions(SetMemory(0x6509A0, SetTo, 0))
