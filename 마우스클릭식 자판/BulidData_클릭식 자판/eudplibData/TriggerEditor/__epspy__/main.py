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
# (Line 2) import System as sys;
import System as sys
# (Line 3) import keyboardFunctions as kf;
import keyboardFunctions as kf
# (Line 4) import keyboardController as kc;
import keyboardController as kc
# (Line 6) const s = StringBuffer(1024);
s = _CGFW(lambda: [StringBuffer(1024)], 1)[0]
# (Line 8) const saveMX	= PVariable();
saveMX = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 9) const saveMY	= PVariable();
saveMY = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 10) const saveSX	= PVariable();
saveSX = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 12) function onPluginStart(){
@EUDFunc
def onPluginStart():
    # (Line 14) randomize();
    f_randomize()
    # (Line 15) sys.variableInit();
    sys.f_variableInit()
    # (Line 16) foreach(cp : EUDLoopPlayer("Human")){
    for cp in EUDLoopPlayer("Human"):
        # (Line 17) setcurpl(cp);
        f_setcurpl(cp)
        # (Line 18) sys.textUpdate[cp] = 1; //최초 화면갱신
        _ARRW(sys.textUpdate, cp) << (1)
        # (Line 19) kc.keySwitch[cp] = 1;
        _ARRW(kc.keySwitch, cp) << (1)
        # (Line 20) }
        # (Line 21) }

    # (Line 23) function beforeTriggerExec(){

@EUDFunc
def beforeTriggerExec():
    # (Line 26) SetMemory(0x6509A0, SetTo, 0); //EUD터보
    # (Line 27) foreach(cp : EUDLoopPlayer("Human")){
    DoActions(SetMemory(0x6509A0, SetTo, 0))
    for cp in EUDLoopPlayer("Human"):
        # (Line 28) setcurpl(cp);
        f_setcurpl(cp)
        # (Line 29) sys.checkScreenMouse(); //비공유 좌표 및 크기 산출
        sys.f_checkScreenMouse()
        # (Line 30) if(sys.mouseClick[cp] == 1){
        if EUDIf()(sys.mouseClick[cp] == 1):
            # (Line 31) saveMX[cp] = sys.mouseUserX[cp];
            _ARRW(saveMX, cp) << (sys.mouseUserX[cp])
            # (Line 32) saveMY[cp] = sys.mouseUserY[cp];
            _ARRW(saveMY, cp) << (sys.mouseUserY[cp])
            # (Line 33) saveSX[cp] = sys.screenUserX[cp];
            _ARRW(saveSX, cp) << (sys.screenUserX[cp])
            # (Line 34) }
            # (Line 35) s.printAt(0, "\x13mouseX : ", saveMX[cp], "  mouseY : ", saveMY[cp], "  screenSizeX : ", saveSX[cp], "  screenX : ", saveMX[cp]+320-saveSX[cp], "  screenY : ", saveMY[cp]);
        EUDEndIf()
        s.printAt(0, "\x13mouseX : ", saveMX[cp], "  mouseY : ", saveMY[cp], "  screenSizeX : ", saveSX[cp], "  screenX : ", saveMX[cp] + 320 - saveSX[cp], "  screenY : ", saveMY[cp])
        # (Line 36) }
        # (Line 37) }

    # (Line 39) function afterTriggerExec(){

@EUDFunc
def afterTriggerExec():
    # (Line 42) foreach(cp : EUDLoopPlayer("Human")){
    for cp in EUDLoopPlayer("Human"):
        # (Line 43) setcurpl(cp);
        f_setcurpl(cp)
        # (Line 44) kc.controllerText(cp);
        kc.f_controllerText(cp)
        # (Line 45) kf.keyboardScreen(cp);
        kf.f_keyboardScreen(cp)
        # (Line 46) }
        # (Line 47) }
