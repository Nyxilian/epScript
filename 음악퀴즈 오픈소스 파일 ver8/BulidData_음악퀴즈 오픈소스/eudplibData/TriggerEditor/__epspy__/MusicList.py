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

# (Line 1) import MusicSetting as ms;
import MusicSetting as ms
# (Line 2) import functions as fc;
import functions as fc
# (Line 4) var flagEPD = 0;
flagEPD = EUDCreateVariables(1)
_IGVA([flagEPD], lambda: [0])
# (Line 6) function CreateList(){
@EUDFunc
def CreateList():
    # (Line 7) if(ms.MusicList == 1){
    if EUDIf()(ms.MusicList == 1):
        # (Line 8) const listLoc = fc.etcLoc;
        listLoc = fc.etcLoc
        # (Line 9) const maxValue = ms.MusicNumber;
        maxValue = ms.MusicNumber
        # (Line 10) const RowNum = ms.ListRow;
        RowNum = ms.ListRow
        # (Line 11) fc.SetLocation(listLoc, 32*ms.ListPosX+16, 32*ms.ListPosY+16, 8);
        fc.SetLocation(listLoc, 32 * ms.ListPosX + 16, 32 * ms.ListPosY + 16, 8)
        # (Line 12) for(var i=1; i<maxValue+1; i++){
        i = EUDVariable()
        i << (1)
        if EUDWhile()(i >= maxValue + 1, neg=True):
            def _t3():
                i.__iadd__(1)
            # (Line 13) flagEPD = epdread_epd(EPD(0x628438));
            flagEPD << (f_epdread_epd(EPD(0x628438)))
            # (Line 14) CreateUnit(1, 215, listLoc, P8);
            # (Line 15) SetMemoryXEPD(flagEPD + 9, SetTo, i*65536, 0xFF0000);
            DoActions(CreateUnit(1, 215, listLoc, P8))
            # (Line 16) if(i % RowNum == 0){fc.EUDMoveLocation(listLoc, -32*(RowNum-1), -32);}
            DoActions(SetMemoryXEPD(flagEPD + 9, SetTo, i * 65536, 0xFF0000))
            if EUDIf()(i % RowNum == 0):
                fc.EUDMoveLocation(listLoc, -32 * (RowNum - 1), -32)
                # (Line 17) else{fc.EUDMoveLocation(listLoc, 32, 0);}
            if EUDElse()():
                fc.EUDMoveLocation(listLoc, 32, 0)
                # (Line 18) }
            EUDEndIf()
            # (Line 19) }
            EUDSetContinuePoint()
            _t3()
        EUDEndWhile()
        # (Line 20) }
    EUDEndIf()
