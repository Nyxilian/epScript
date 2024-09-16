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
# (Line 2) import StageSwitch as ss;
import StageSwitch as ss
# (Line 3) import functions as fx;
import functions as fx
# (Line 4) import bgm as bgm;
import bgm as bgm
# (Line 6) const s = StringBuffer(1024);
s = _CGFW(lambda: [StringBuffer(1024)], 1)[0]
# (Line 8) function onPluginStart() {
@EUDFunc
def onPluginStart():
    # (Line 10) SetMemory(0x657A9C, SetTo, 0);
    # (Line 11) fx.SingleBan();
    DoActions(SetMemory(0x657A9C, SetTo, 0))
    fx.SingleBan()
    # (Line 12) fx.SpeedBan();
    fx.SpeedBan()
    # (Line 13) fx.playerCheck();
    fx.f_playerCheck()
    # (Line 14) fx.set_vulHP();
    fx.f_set_vulHP()
    # (Line 15) bgm.play_init();
    bgm.f_play_init()
    # (Line 16) foreach(cp : EUDLoopPlayer("Computer")) {
    for cp in EUDLoopPlayer("Computer"):
        # (Line 17) setcurpl(cp);
        f_setcurpl(cp)
        # (Line 18) SetAllianceStatus(Force1, Enemy);
        # (Line 19) }
        DoActions(SetAllianceStatus(Force1, Enemy))
        # (Line 20) foreach(cp : EUDLoopPlayer("Human")) {

    for cp in EUDLoopPlayer("Human"):
        # (Line 21) setcurpl(cp);
        f_setcurpl(cp)
        # (Line 22) RunAIScript("+Vi6");
        # (Line 23) }
        DoActions(RunAIScript("+Vi6"))
        # (Line 24) SetMemory(0x5124F0, SetTo, 21); //2배속

    # (Line 26) fx.bossHP_init();
    DoActions(SetMemory(0x5124F0, SetTo, 21))
    fx.f_bossHP_init()
    # (Line 27) }
    # (Line 29) function beforeTriggerExec() {

@EUDFunc
def beforeTriggerExec():
    # (Line 31) fx.timeFlow();
    fx.f_timeFlow()
    # (Line 32) fx.moveLoc();
    fx.f_moveLoc()
    # (Line 33) fx.dontLeave();
    fx.f_dontLeave()
    # (Line 34) if(fx.stage != 5) {
    if EUDIf()(fx.stage == 5, neg=True):
        # (Line 35) fx.bulletRemover();
        fx.f_bulletRemover()
        # (Line 36) }
        # (Line 37) fx.playerLimiter();
    EUDEndIf()
    fx.f_playerLimiter()
    # (Line 38) fx.playerBlockade();
    fx.f_playerBlockade()
    # (Line 39) bgm.play();
    bgm.f_play()
    # (Line 40) }
    # (Line 42) function afterTriggerExec() {

@EUDFunc
def afterTriggerExec():
    # (Line 44) ss.stage();
    ss.f_stage()
    # (Line 45) fx.actionLoc();
    fx.f_actionLoc()
    # (Line 46) fx.defeatCheck();
    fx.f_defeatCheck()
    # (Line 47) fx.Invulnerability();
    fx.Invulnerability()
    # (Line 48) foreach(cp : EUDLoopPlayer("Human")) {
    for cp in EUDLoopPlayer("Human"):
        # (Line 49) setcurpl(cp);
        f_setcurpl(cp)
        # (Line 50) if(fx.off_bgm(cp)) {
        if EUDIf()(fx.f_off_bgm(cp)):
            # (Line 51) s.printAt(0, "\n\n\n\n\n\n\n\n\n");
            s.printAt(0, "\n\n\n\n\n\n\n\n\n")
            # (Line 52) s.printfAt(5, "\x13\x1F[  \x04알    림  \x1F]\n\n\x13\x07Ctrl + SS\x04를 눌러 \x03브금\x04을 꺼주세요\n\x13\x1FInsert \x04키를 눌러 다시 킬 수 있습니다");
            s.printfAt(5, "\x13\x1F[  \x04알    림  \x1F]\n\n\x13\x07Ctrl + SS\x04를 눌러 \x03브금\x04을 꺼주세요\n\x13\x1FInsert \x04키를 눌러 다시 킬 수 있습니다")
            # (Line 53) }
            # (Line 54) if(fx.on_bgm(cp)) {
        EUDEndIf()
        if EUDIf()(fx.f_on_bgm(cp)):
            # (Line 55) s.printAt(0, "\n\n\n\n\n\n\n\n\n");
            s.printAt(0, "\n\n\n\n\n\n\n\n\n")
            # (Line 56) s.printAt(5, "\x13\x1F[  \x04알    림  \x1F]\n\n\x13\x03브금\x04을 켰습니다");
            s.printAt(5, "\x13\x1F[  \x04알    림  \x1F]\n\n\x13\x03브금\x04을 켰습니다")
            # (Line 57) }
            # (Line 58) }
        EUDEndIf()
        # (Line 59) SetMemory(0x6509A0, SetTo, 0); //EUD터보

    # (Line 60) }
    DoActions(SetMemory(0x6509A0, SetTo, 0))