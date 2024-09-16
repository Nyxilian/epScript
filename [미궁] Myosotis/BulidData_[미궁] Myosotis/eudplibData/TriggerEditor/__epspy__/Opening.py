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
# (Line 3) const s = StringBuffer(1024);
s = _CGFW(lambda: [StringBuffer(1024)], 1)[0]
# (Line 5) function intro() {
@EUDFunc
def f_intro():
    # (Line 6) fx.set_BG(0);
    fx.f_set_BG(0)
    # (Line 7) foreach (cp : EUDLoopPlayer("Human")) {
    for cp in EUDLoopPlayer("Human"):
        # (Line 8) setcurpl(cp);
        f_setcurpl(cp)
        # (Line 9) CenterView("Story");
        # (Line 11) if(fx.off_bgm(cp)) {
        DoActions(CenterView("Story"))
        if EUDIf()(fx.f_off_bgm(cp)):
            # (Line 12) s.printAt(10, "\x13\x07Ctrl + SS\x02를 눌러 브금을 꺼주세요. \x1DInsert\x02키로 다시 킬 수 있습니다.");
            s.printAt(10, "\x13\x07Ctrl + SS\x02를 눌러 브금을 꺼주세요. \x1DInsert\x02키로 다시 킬 수 있습니다.")
            # (Line 13) }
            # (Line 15) if(fx.on_bgm(cp)) {
        EUDEndIf()
        if EUDIf()(fx.f_on_bgm(cp)):
            # (Line 16) s.printAt(10, "\x13브금을 켰습니다.");
            s.printAt(10, "\x13브금을 켰습니다.")
            # (Line 17) }
            # (Line 19) if(fx.timer(0,144)) {
        EUDEndIf()
        if EUDIf()(fx.f_timer(0, 144)):
            # (Line 20) s.printAt(0,"\n\n\n\n\n\n\n\n\n");
            s.printAt(0, "\n\n\n\n\n\n\n\n\n")
            # (Line 21) s.fadeIn("\x08\x13\"나의 유일한 \x0F희망\x08\"", wait=8, line=9);
            s.fadeIn("\x08\x13\"나의 유일한 \x0F희망\x08\"", wait=8, line=9)
            # (Line 22) }
            # (Line 24) if(fx.timer(144, 288)) {
        EUDEndIf()
        if EUDIf()(fx.f_timer(144, 288)):
            # (Line 25) s.printAt(0,"\n\n\n\n\n\n\n\n\n");
            s.printAt(0, "\n\n\n\n\n\n\n\n\n")
            # (Line 26) s.fadeIn("\x08\x13\"나의 유일한 도피처마저 \x03망가지고 \x08말았어...\"", wait=4, line=9);
            s.fadeIn("\x08\x13\"나의 유일한 도피처마저 \x03망가지고 \x08말았어...\"", wait=4, line=9)
            # (Line 27) }
            # (Line 29) if(fx.timer(288, 360)) {
        EUDEndIf()
        if EUDIf()(fx.f_timer(288, 360)):
            # (Line 30) s.printAt(0, "\n\n\n\n\n\n\n\n\n");
            s.printAt(0, "\n\n\n\n\n\n\n\n\n")
            # (Line 31) }
            # (Line 33) if(fx.timer(360, 432)) {
        EUDEndIf()
        if EUDIf()(fx.f_timer(360, 432)):
            # (Line 34) s.printAt(0,"\n\n\n\n\n\n\n\n\n");
            s.printAt(0, "\n\n\n\n\n\n\n\n\n")
            # (Line 35) s.fadeIn("\x04\x13헉...", wait=8, line=9);
            s.fadeIn("\x04\x13헉...", wait=8, line=9)
            # (Line 36) }
            # (Line 38) if(fx.timer(432, 528)) {
        EUDEndIf()
        if EUDIf()(fx.f_timer(432, 528)):
            # (Line 39) s.printAt(0,"\n\n\n\n\n\n\n\n\n");
            s.printAt(0, "\n\n\n\n\n\n\n\n\n")
            # (Line 40) s.printAt(9, "\x04\x13이 익숙한 목소리는... 설마...?");
            s.printAt(9, "\x04\x13이 익숙한 목소리는... 설마...?")
            # (Line 41) }
            # (Line 43) if(fx.timer(528,600)) {
        EUDEndIf()
        if EUDIf()(fx.f_timer(528, 600)):
            # (Line 44) fx.time_reset();
            fx.f_time_reset()
            # (Line 45) fx.Chapter_change(10);
            fx.Chapter_change(10)
            # (Line 46) }
            # (Line 47) }
        EUDEndIf()
        # (Line 48) }

    # (Line 50) function opening() {

@EUDFunc
def f_opening():
    # (Line 51) foreach (cp: EUDLoopPlayer("Human")) {
    for cp in EUDLoopPlayer("Human"):
        # (Line 52) setcurpl(cp);
        f_setcurpl(cp)
        # (Line 53) CenterView("Story");
        # (Line 55) if(fx.off_bgm(cp)) {
        DoActions(CenterView("Story"))
        if EUDIf()(fx.f_off_bgm(cp)):
            # (Line 56) s.printAt(10, "\x13\x07Ctrl + SS\x02를 눌러 브금을 꺼주세요. \x1DInsert\x02키로 다시 킬 수 있습니다.");
            s.printAt(10, "\x13\x07Ctrl + SS\x02를 눌러 브금을 꺼주세요. \x1DInsert\x02키로 다시 킬 수 있습니다.")
            # (Line 57) }
            # (Line 59) if(fx.on_bgm(cp)) {
        EUDEndIf()
        if EUDIf()(fx.f_on_bgm(cp)):
            # (Line 60) s.printAt(10, "\x13브금을 켰습니다.");
            s.printAt(10, "\x13브금을 켰습니다.")
            # (Line 61) }
            # (Line 63) if(fx.timer(0, 144)) {
        EUDEndIf()
        if EUDIf()(fx.f_timer(0, 144)):
            # (Line 64) s.printAt(0,"\n\n\n\n");
            s.printAt(0, "\n\n\n\n")
            # (Line 65) s.fadeIn("\x05\x13[ 미 궁 ] M y o s o t i s", wait=4, line=4);
            s.fadeIn("\x05\x13[ 미 궁 ] M y o s o t i s", wait=4, line=4)
            # (Line 66) s.printAt(5, "\n\n\n\n\n");
            s.printAt(5, "\n\n\n\n\n")
            # (Line 67) }
            # (Line 68) if(fx.timer(144,148)) {
        EUDEndIf()
        if EUDIf()(fx.f_timer(144, 148)):
            # (Line 69) s.printAt(0,"\n\n\n\n");
            s.printAt(0, "\n\n\n\n")
            # (Line 70) s.printAt(4, "\x05\x13[ 미 궁 ] M yo s o t i s");
            s.printAt(4, "\x05\x13[ 미 궁 ] M yo s o t i s")
            # (Line 71) s.printAt(5, "\n\n\n\n\n");
            s.printAt(5, "\n\n\n\n\n")
            # (Line 72) }
            # (Line 73) if(fx.timer(148,152)) {
        EUDEndIf()
        if EUDIf()(fx.f_timer(148, 152)):
            # (Line 74) s.printAt(0,"\n\n\n\n");
            s.printAt(0, "\n\n\n\n")
            # (Line 75) s.printAt(4, "\x05\x13[ 미 궁 ] Myos o t i s");
            s.printAt(4, "\x05\x13[ 미 궁 ] Myos o t i s")
            # (Line 76) s.printAt(5, "\n\n\n\n\n");
            s.printAt(5, "\n\n\n\n\n")
            # (Line 77) }
            # (Line 78) if(fx.timer(152,156)) {
        EUDEndIf()
        if EUDIf()(fx.f_timer(152, 156)):
            # (Line 79) s.printAt(0,"\n\n\n\n");
            s.printAt(0, "\n\n\n\n")
            # (Line 80) s.printAt(4, "\x05\x13[ 미 궁 ] Myoso t i s");
            s.printAt(4, "\x05\x13[ 미 궁 ] Myoso t i s")
            # (Line 81) s.printAt(5, "\n\n\n\n\n");
            s.printAt(5, "\n\n\n\n\n")
            # (Line 82) }
            # (Line 83) if(fx.timer(156,160)) {
        EUDEndIf()
        if EUDIf()(fx.f_timer(156, 160)):
            # (Line 84) s.printAt(0,"\n\n\n\n");
            s.printAt(0, "\n\n\n\n")
            # (Line 85) s.printAt(4, "\x05\x13[ 미 궁] Myosot i s");
            s.printAt(4, "\x05\x13[ 미 궁] Myosot i s")
            # (Line 86) s.printAt(5, "\n\n\n\n\n");
            s.printAt(5, "\n\n\n\n\n")
            # (Line 87) }
            # (Line 88) if(fx.timer(160,164)) {
        EUDEndIf()
        if EUDIf()(fx.f_timer(160, 164)):
            # (Line 89) s.printAt(0,"\n\n\n\n");
            s.printAt(0, "\n\n\n\n")
            # (Line 90) s.printAt(4, "\x05\x13[ 미궁] Myosoti s");
            s.printAt(4, "\x05\x13[ 미궁] Myosoti s")
            # (Line 91) s.printAt(5, "\n\n\n\n\n");
            s.printAt(5, "\n\n\n\n\n")
            # (Line 92) }
            # (Line 93) if(fx.timer(164,168)) {
        EUDEndIf()
        if EUDIf()(fx.f_timer(164, 168)):
            # (Line 94) s.printAt(0,"\n\n\n\n");
            s.printAt(0, "\n\n\n\n")
            # (Line 95) s.printAt(4, "\x05\x13[미궁] Myosotis");
            s.printAt(4, "\x05\x13[미궁] Myosotis")
            # (Line 96) s.printAt(5, "\n\n\n\n\n");
            s.printAt(5, "\n\n\n\n\n")
            # (Line 97) }
            # (Line 98) if(fx.timer(168,172)) {
        EUDEndIf()
        if EUDIf()(fx.f_timer(168, 172)):
            # (Line 99) s.printAt(0,"\n\n\n\n");
            s.printAt(0, "\n\n\n\n")
            # (Line 100) s.printAt(4, "\x03\x13[미궁] Myosotis");
            s.printAt(4, "\x03\x13[미궁] Myosotis")
            # (Line 101) s.printAt(5, "\n\n\n\n\n");
            s.printAt(5, "\n\n\n\n\n")
            # (Line 102) }
            # (Line 103) if(fx.timer(172,176)) {
        EUDEndIf()
        if EUDIf()(fx.f_timer(172, 176)):
            # (Line 104) s.printAt(0,"\n\n\n\n");
            s.printAt(0, "\n\n\n\n")
            # (Line 105) s.printAt(4, "\x04\x13[미궁] Myosotis");
            s.printAt(4, "\x04\x13[미궁] Myosotis")
            # (Line 106) s.printAt(5, "\n\n\n\n\n");
            s.printAt(5, "\n\n\n\n\n")
            # (Line 107) }
            # (Line 108) if(fx.timer(176,240)) {
        EUDEndIf()
        if EUDIf()(fx.f_timer(176, 240)):
            # (Line 109) s.printAt(0,"\n\n\n\n");
            s.printAt(0, "\n\n\n\n")
            # (Line 110) s.printAt(4, "\x04\x13[미궁] \x1DMyosotis");
            s.printAt(4, "\x04\x13[미궁] \x1DMyosotis")
            # (Line 111) s.printAt(5, "\n\n\n\n\n");
            s.printAt(5, "\n\n\n\n\n")
            # (Line 112) }
            # (Line 113) if(fx.timer(240,260)) {
        EUDEndIf()
        if EUDIf()(fx.f_timer(240, 260)):
            # (Line 114) fx.time_reset();
            fx.f_time_reset()
            # (Line 115) fx.Chapter_change(1);
            fx.Chapter_change(1)
            # (Line 116) }
            # (Line 117) }
        EUDEndIf()
        # (Line 118) }
