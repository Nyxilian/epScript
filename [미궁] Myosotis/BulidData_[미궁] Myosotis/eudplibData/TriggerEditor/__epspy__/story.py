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

# (Line 1) import Opening as op;
import Opening as op
# (Line 2) import functions as fx;
import functions as fx
# (Line 3) import mainStory as ms;
import mainStory as ms
# (Line 4) import Questions as qu;
import Questions as qu
# (Line 5) import Ending as ed;
import Ending as ed
# (Line 7) function Main() {
@EUDFunc
def Main():
    # (Line 8) switch(fx.current_Chapter()) {
    EUDSwitch(fx.f_current_Chapter())
    # (Line 9) case 0:
    _t1 = EUDSwitchCase()
    # (Line 10) op.intro();
    if _t1(0):
        op.f_intro()
        # (Line 11) break;
        EUDBreak()
        # (Line 12) case 10:
    _t2 = EUDSwitchCase()
    # (Line 13) op.opening();
    if _t2(10):
        op.f_opening()
        # (Line 14) break;
        EUDBreak()
        # (Line 15) case 1:
    _t3 = EUDSwitchCase()
    # (Line 16) ms.Chapter1();
    if _t3(1):
        ms.Chapter1()
        # (Line 17) break;
        EUDBreak()
        # (Line 18) case 11:
    _t4 = EUDSwitchCase()
    # (Line 19) qu.Question1();
    if _t4(11):
        qu.Question1()
        # (Line 20) break;
        EUDBreak()
        # (Line 21) case 2:
    _t5 = EUDSwitchCase()
    # (Line 22) ms.Chapter2();
    if _t5(2):
        ms.Chapter2()
        # (Line 23) break;
        EUDBreak()
        # (Line 24) case 12:
    _t6 = EUDSwitchCase()
    # (Line 25) qu.Question2();
    if _t6(12):
        qu.Question2()
        # (Line 26) break;
        EUDBreak()
        # (Line 27) case 3:
    _t7 = EUDSwitchCase()
    # (Line 28) ms.Chapter3();
    if _t7(3):
        ms.Chapter3()
        # (Line 29) break;
        EUDBreak()
        # (Line 30) case 13:
    _t8 = EUDSwitchCase()
    # (Line 31) qu.Question3();
    if _t8(13):
        qu.Question3()
        # (Line 32) break;
        EUDBreak()
        # (Line 33) case 4:
    _t9 = EUDSwitchCase()
    # (Line 34) ms.Chapter4();
    if _t9(4):
        ms.Chapter4()
        # (Line 35) break;
        EUDBreak()
        # (Line 36) case 14:
    _t10 = EUDSwitchCase()
    # (Line 37) qu.Question4();
    if _t10(14):
        qu.Question4()
        # (Line 38) break;
        EUDBreak()
        # (Line 39) case 5:
    _t11 = EUDSwitchCase()
    # (Line 40) ms.Chapter5();
    if _t11(5):
        ms.Chapter5()
        # (Line 41) break;
        EUDBreak()
        # (Line 42) case 15:
    _t12 = EUDSwitchCase()
    # (Line 43) qu.Question5();
    if _t12(15):
        qu.Question5()
        # (Line 44) break;
        EUDBreak()
        # (Line 45) case 6:
    _t13 = EUDSwitchCase()
    # (Line 46) ms.Chapter6();
    if _t13(6):
        ms.Chapter6()
        # (Line 47) break;
        EUDBreak()
        # (Line 48) case 16:
    _t14 = EUDSwitchCase()
    # (Line 49) qu.Question6();
    if _t14(16):
        qu.Question6()
        # (Line 50) break;
        EUDBreak()
        # (Line 51) case 7:
    _t15 = EUDSwitchCase()
    # (Line 52) ms.Chapter7();
    if _t15(7):
        ms.Chapter7()
        # (Line 53) break;
        EUDBreak()
        # (Line 54) case 17:
    _t16 = EUDSwitchCase()
    # (Line 55) qu.Question7();
    if _t16(17):
        qu.Question7()
        # (Line 56) break;
        EUDBreak()
        # (Line 57) case 8:
    _t17 = EUDSwitchCase()
    # (Line 58) ed.finale();
    if _t17(8):
        ed.f_finale()
        # (Line 59) break;
        EUDBreak()
        # (Line 60) case 9:
    _t18 = EUDSwitchCase()
    # (Line 61) ed.EndingCredit();
    if _t18(9):
        ed.EndingCredit()
        # (Line 62) default:
    # (Line 63) break;
    if EUDSwitchDefault()():
        EUDBreak()
        # (Line 64) }
    # (Line 65) }
    EUDEndSwitch()
