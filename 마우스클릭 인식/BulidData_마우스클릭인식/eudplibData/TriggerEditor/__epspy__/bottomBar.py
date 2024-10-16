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
# (Line 3) import main as m;
import main as m
# (Line 5) const s = StringBuffer(1024);
s = _CGFW(lambda: [StringBuffer(1024)], 1)[0]
# (Line 7) const pcolor1	= PVariable();
pcolor1 = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 9) function bottomAction(cp);
# (Line 10) function bottomText(cp){
@EUDFunc
def f_bottomText(cp):
    # (Line 15) const mmX = sys.mouseUserX[cp]+320-sys.screenUserX[cp];
    mmX = sys.mouseUserX[cp] + 320 - sys.screenUserX[cp]
    # (Line 16) const mmY = sys.mouseUserY[cp];
    mmY = sys.mouseUserY[cp]
    # (Line 17) if(203 <= mmX && mmX <= 438 && 296 <= mmY && mmY <= 307){if(pcolor1[cp] == 0){pcolor1[cp] = 1;}}
    if EUDIf()(EUDSCAnd()(203 <= mmX)(mmX <= 438)(296 <= mmY)(mmY <= 307)()):
        if EUDIf()(pcolor1[cp] == 0):
            _ARRW(pcolor1, cp) << (1)
        EUDEndIf()
        # (Line 18) else{if(pcolor1[cp] == 1){pcolor1[cp] = 0;}}
    if EUDElse()():
        if EUDIf()(pcolor1[cp] == 1):
            _ARRW(pcolor1, cp) << (0)
        EUDEndIf()
        # (Line 19) eprintln("\x1E",ptr2s(sys.colorL[pcolor1[cp]]),"[ 여기를 누르면 다른 텍스트방식으로 토글되요. ]");
    EUDEndIf()
    f_eprintln("\x1E", ptr2s(sys.colorL[pcolor1[cp]]), "[ 여기를 누르면 다른 텍스트방식으로 토글되요. ]")
    # (Line 20) bottomAction(cp);
    f_bottomAction(cp)
    # (Line 21) }
    # (Line 23) function bottomAction(cp){

@EUDFunc
def f_bottomAction(cp):
    # (Line 24) if(sys.mouseClick[cp] == 1){ //왼클릭 했을 때
    if EUDIf()(sys.mouseClick[cp] == 1):
        # (Line 26) const mmX = sys.mouseUserX[cp]+320-sys.screenUserX[cp];
        mmX = sys.mouseUserX[cp] + 320 - sys.screenUserX[cp]
        # (Line 27) const mmY = sys.mouseUserY[cp];
        mmY = sys.mouseUserY[cp]
        # (Line 28) if(203 <= mmX && mmX <= 438 && 296 <= mmY && mmY <= 307){
        if EUDIf()(EUDSCAnd()(203 <= mmX)(mmX <= 438)(296 <= mmY)(mmY <= 307)()):
            # (Line 29) s.print("다른 방식으로 전환되요!");
            s.print("다른 방식으로 전환되요!")
            # (Line 30) if(m.selectText[cp] == 0){m.selectText[cp] = 1;}
            if EUDIf()(m.selectText[cp] == 0):
                _ARRW(m.selectText, cp) << (1)
                # (Line 31) else{m.selectText[cp] = 0;}
            if EUDElse()():
                _ARRW(m.selectText, cp) << (0)
                # (Line 32) sys.textUpdate[cp] = 1; //전환되면서 새로 텍스트를 그려야하니 갱신시켜주기.
            EUDEndIf()
            _ARRW(sys.textUpdate, cp) << (1)
            # (Line 33) }
            # (Line 34) }
        EUDEndIf()
        # (Line 35) }
    EUDEndIf()
