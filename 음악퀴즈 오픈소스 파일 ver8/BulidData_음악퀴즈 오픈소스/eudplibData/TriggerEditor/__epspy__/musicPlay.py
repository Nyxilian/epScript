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
# (Line 2) import opening as op;
import opening as op
# (Line 3) import TriggerEditor.BGMPlayer as BGM;
from TriggerEditor import BGMPlayer as BGM
# (Line 4) import MusicSetting as ms;
import MusicSetting as ms
# (Line 5) import System as sys;
import System as sys
# (Line 6) import functions as fc;
import functions as fc
# (Line 8) const s = StringBuffer(1024);
s = _CGFW(lambda: [StringBuffer(1024)], 1)[0]
# (Line 9) const s2 = StringBuffer(1024);
s2 = _CGFW(lambda: [StringBuffer(1024)], 1)[0]
# (Line 10) var MusicStep			= 0;	//게임진행단계 1,오프닝->시작 2,음악세팅 3,음악재생중 4,음악재생종료후2초대기 5,종료세팅후 2로 보내기
MusicStep = EUDCreateVariables(1)
_IGVA([MusicStep], lambda: [0])
# (Line 11) var MusicTimer			= 0;
MusicTimer = EUDCreateVariables(1)
_IGVA([MusicTimer], lambda: [0])
# (Line 12) var MusicTemp			= 0;
MusicTemp = EUDCreateVariables(1)
_IGVA([MusicTemp], lambda: [0])
# (Line 13) var MusicDelay			= 0;
MusicDelay = EUDCreateVariables(1)
_IGVA([MusicDelay], lambda: [0])
# (Line 14) var MusicHintOpen1		= 0;
MusicHintOpen1 = EUDCreateVariables(1)
_IGVA([MusicHintOpen1], lambda: [0])
# (Line 15) var MusicHintOpen2		= 0;
MusicHintOpen2 = EUDCreateVariables(1)
_IGVA([MusicHintOpen2], lambda: [0])
# (Line 16) var MusicOpen			= 0;	//1이면 정답공개, 0이면 미공개
MusicOpen = EUDCreateVariables(1)
_IGVA([MusicOpen], lambda: [0])
# (Line 17) var MusicAnswerUser	= 0;	//정답을 맞힌 유저
MusicAnswerUser = EUDCreateVariables(1)
_IGVA([MusicAnswerUser], lambda: [0])
# (Line 18) var MusicRemain		= 0;
MusicRemain = EUDCreateVariables(1)
_IGVA([MusicRemain], lambda: [0])
# (Line 19) var CurrentMusic		= 0;
CurrentMusic = EUDCreateVariables(1)
_IGVA([CurrentMusic], lambda: [0])
# (Line 20) var EndingDelay			= 0;//MusicSetting의 EndingTimer*36 값 대입.
EndingDelay = EUDCreateVariables(1)
_IGVA([EndingDelay], lambda: [0])
# (Line 21) var VoteAll				= 0;
VoteAll = EUDCreateVariables(1)
_IGVA([VoteAll], lambda: [0])
# (Line 22) var MusicNumber2		= 0;//MusicNumber를 대신할 값.
MusicNumber2 = EUDCreateVariables(1)
_IGVA([MusicNumber2], lambda: [0])
# (Line 23) const MusicTextU		= PVariable();
MusicTextU = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 24) const CleanText			= PVariable();
CleanText = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 25) const UserAnswer		= PVariable();
UserAnswer = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 26) const VoteUser			= PVariable();
VoteUser = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 27) const Ending			= PVariable();
Ending = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 28) const TextMeassge		= PVariable();
TextMeassge = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 29) const TextType			= PVariable();
TextType = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 30) var MusicPlayFront		= 0; //순차재생부분 MusicNumber값에 도달하면 재순환, 재순환시 첫인덱스가 0이면 종료
MusicPlayFront = EUDCreateVariables(1)
_IGVA([MusicPlayFront], lambda: [0])
# (Line 31) var MusicPlayRear		= 0; //문제를 못맞췄을 때 채울 인덱스번호. 못맞출때마다 1씩 증가. 재순환시 0으로 초기화
MusicPlayRear = EUDCreateVariables(1)
_IGVA([MusicPlayRear], lambda: [0])
# (Line 34) const MusicIndex	= EUDArray(ms.MusicNumber);
MusicIndex = _CGFW(lambda: [EUDArray(ms.MusicNumber)], 1)[0]
# (Line 35) const MusicPlay		= EUDArray(ms.MusicNumber);
MusicPlay = _CGFW(lambda: [EUDArray(ms.MusicNumber)], 1)[0]
# (Line 39) function shuffle(arr, length) {
@EUDFunc
def f_shuffle(arr, length):
    # (Line 40) const arr_ = EUDArray.cast(arr);
    arr_ = EUDArray.cast(arr)
    # (Line 41) var temp;
    temp = EUDVariable()
    # (Line 42) var rand;
    rand = EUDVariable()
    # (Line 43) for(var i = 0; i < length-1; i++) {
    i = EUDVariable()
    i << (0)
    if EUDWhile()(i >= length - 1, neg=True):
        def _t2():
            i.__iadd__(1)
        # (Line 44) rand = dwrand() % (length - i) + i;
        rand << (f_dwrand() % (length - i) + i)
        # (Line 45) temp = arr_[i];
        temp << (arr_[i])
        # (Line 46) arr_[i] = arr_[rand];
        _ARRW(arr_, i) << (arr_[rand])
        # (Line 47) arr_[rand] = temp;
        _ARRW(arr_, rand) << (temp)
        # (Line 48) }
        # (Line 49) }
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    # (Line 50) function musicInit(){

@EUDFunc
def f_musicInit():
    # (Line 51) for(var i=0; i<ms.MusicNumber; i++){
    i = EUDVariable()
    i << (0)
    if EUDWhile()(i >= ms.MusicNumber, neg=True):
        def _t2():
            i.__iadd__(1)
        # (Line 52) MusicPlay[i] = i+1;
        _ARRW(MusicPlay, i) << (i + 1)
        # (Line 53) MusicIndex[i] = i+1;
        _ARRW(MusicIndex, i) << (i + 1)
        # (Line 54) }
        # (Line 55) EndingDelay = ms.EndingTimer*36;
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    EndingDelay << (ms.EndingTimer * 36)
    # (Line 56) if(ms.MusicSelect == 0){MusicNumber2 = ms.MusicNumber;}
    if EUDIf()(ms.MusicSelect == 0):
        MusicNumber2 << (ms.MusicNumber)
        # (Line 57) MusicRemain = MusicNumber2;
    EUDEndIf()
    MusicRemain << (MusicNumber2)
    # (Line 58) if(ms.MusicShuffle == 1){shuffle(MusicPlay, ms.MusicNumber);}
    if EUDIf()(ms.MusicShuffle == 1):
        f_shuffle(MusicPlay, ms.MusicNumber)
        # (Line 59) }
    EUDEndIf()
    # (Line 60) function musicSystem(){

@EUDFunc
def f_musicSystem():
    # (Line 61) if(MusicStep == 1){musicInit(); MusicStep = 2;}
    if EUDIf()(MusicStep == 1):
        f_musicInit()
        MusicStep << (2)
        # (Line 62) if(MusicStep == 2){
    EUDEndIf()
    if EUDIf()(MusicStep == 2):
        # (Line 63) MusicAnswerUser = 0;
        MusicAnswerUser << (0)
        # (Line 64) MusicDelay = 0;
        MusicDelay << (0)
        # (Line 65) MusicHintOpen1 = 0;
        MusicHintOpen1 << (0)
        # (Line 66) MusicHintOpen2 = 0;
        MusicHintOpen2 << (0)
        # (Line 67) MusicOpen = 0;
        MusicOpen << (0)
        # (Line 68) VoteAll = 0;
        VoteAll << (0)
        # (Line 69) MusicTemp = MusicPlay[MusicPlayFront];  //못맞춘 경우에 사용할 변수
        MusicTemp << (MusicPlay[MusicPlayFront])
        # (Line 70) CurrentMusic = MusicTemp;
        CurrentMusic << (MusicTemp)
        # (Line 71) if(ms.MusicShort == 1 && op.setting5 == 0){MusicTimer = ms.ShortTimer;} //짧게 듣기가 활성화된 경우, 설정된 길이만큼
        if EUDIf()(EUDSCAnd()(ms.MusicShort == 1)(op.setting5 == 0)()):
            MusicTimer << (ms.ShortTimer)
            # (Line 72) else{MusicTimer = ms.MusicLength[MusicTemp-1];} //짧게 듣기가 비활성화 된 경우, 음원 길이만큼
        if EUDElse()():
            MusicTimer << (ms.MusicLength[MusicTemp - 1])
            # (Line 74) MusicPlay[MusicPlayFront] = 0;
        EUDEndIf()
        _ARRW(MusicPlay, MusicPlayFront) << (0)
        # (Line 75) MusicPlayFront++;
        MusicPlayFront.__iadd__(1)
        # (Line 76) MusicStep = 3;
        MusicStep << (3)
        # (Line 77) foreach(p : EUDLoopPlayer('Human')){MusicTextU[p] = 1; CleanText[p] = 1; VoteUser[p] = 0;}
        for p in EUDLoopPlayer('Human'):
            _ARRW(MusicTextU, p) << (1)
            _ARRW(CleanText, p) << (1)
            _ARRW(VoteUser, p) << (0)
            # (Line 78) }

        # (Line 79) if(MusicStep == 3){
    EUDEndIf()
    if EUDIf()(MusicStep == 3):
        # (Line 80) if(MusicTimer > 0){
        if EUDIf()(MusicTimer <= 0, neg=True):
            # (Line 81) MusicDelay += 1;
            MusicDelay.__iadd__(1)
            # (Line 82) if(MusicDelay > 35){
            if EUDIf()(MusicDelay <= 35, neg=True):
                # (Line 83) MusicDelay = 0;
                MusicDelay << (0)
                # (Line 84) MusicTimer -= 1;
                MusicTimer.__isub__(1)
                # (Line 85) foreach(p : EUDLoopPlayer('Human')){MusicTextU[p] = 1;}
                for p in EUDLoopPlayer('Human'):
                    _ARRW(MusicTextU, p) << (1)
                    # (Line 86) }

                # (Line 87) if(MusicHintOpen1 == 0 && MusicAnswerUser == 0 && MusicTimer <= ms.MusicStart){
            EUDEndIf()
            if EUDIf()(EUDSCAnd()(MusicHintOpen1 == 0)(MusicAnswerUser == 0)(MusicTimer <= ms.MusicStart)()):
                # (Line 88) MusicHintOpen1 = 1; foreach(p : EUDLoopPlayer('Human')){MusicTextU[p] = 1;}
                MusicHintOpen1 << (1)
                for p in EUDLoopPlayer('Human'):
                    _ARRW(MusicTextU, p) << (1)
                    # (Line 89) }

                # (Line 90) if(MusicHintOpen2 == 0 && MusicAnswerUser == 0 && MusicTimer <= ms.MusicEnd){
            EUDEndIf()
            if EUDIf()(EUDSCAnd()(MusicHintOpen2 == 0)(MusicAnswerUser == 0)(MusicTimer <= ms.MusicEnd)()):
                # (Line 91) MusicHintOpen2 = 1; foreach(p : EUDLoopPlayer('Human')){MusicTextU[p] = 1;}
                MusicHintOpen2 << (1)
                for p in EUDLoopPlayer('Human'):
                    _ARRW(MusicTextU, p) << (1)
                    # (Line 92) }

                # (Line 93) }
            EUDEndIf()
            # (Line 94) if(MusicTimer == 0){
        EUDEndIf()
        if EUDIf()(MusicTimer == 0):
            # (Line 95) CurrentMusic = 0;
            CurrentMusic << (0)
            # (Line 96) MusicStep = 4;
            MusicStep << (4)
            # (Line 97) MusicDelay = 0;
            MusicDelay << (0)
            # (Line 98) if(op.setting1 == 0){   //정답공개설정
            if EUDIf()(op.setting1 == 0):
                # (Line 99) if(MusicAnswerUser == 0){
                if EUDIf()(MusicAnswerUser == 0):
                    # (Line 100) MusicOpen = 1;
                    MusicOpen << (1)
                    # (Line 101) MusicRemain--;
                    MusicRemain.__isub__(1)
                    # (Line 102) }
                    # (Line 103) }
                EUDEndIf()
                # (Line 104) else{
            if EUDElse()():
                # (Line 105) if(MusicAnswerUser == 0){
                if EUDIf()(MusicAnswerUser == 0):
                    # (Line 106) MusicPlay[MusicPlayRear] = MusicTemp;
                    _ARRW(MusicPlay, MusicPlayRear) << (MusicTemp)
                    # (Line 107) MusicPlayRear++;
                    MusicPlayRear.__iadd__(1)
                    # (Line 108) }
                    # (Line 109) }
                EUDEndIf()
                # (Line 110) }
            EUDEndIf()
            # (Line 111) const VoteN = sys.UserNumber;
        EUDEndIf()
        VoteN = sys.UserNumber
        # (Line 112) if(VoteAll >= ms.VoteNum[VoteN-1] || Deaths(fc.superUser, Exactly, 2, ms.KEY)){ //투표
        if EUDIf()(EUDSCOr()(VoteAll >= ms.VoteNum[VoteN - 1])(Deaths(fc.superUser, Exactly, 2, ms.KEY))()):
            # (Line 113) CurrentMusic = 0;
            CurrentMusic << (0)
            # (Line 114) MusicDelay = 0;
            MusicDelay << (0)
            # (Line 115) MusicStep = 4;
            MusicStep << (4)
            # (Line 116) if(MusicAnswerUser == 0){
            if EUDIf()(MusicAnswerUser == 0):
                # (Line 117) if(op.setting1 == 0){ //정답공개로 설정했을 때
                if EUDIf()(op.setting1 == 0):
                    # (Line 118) MusicOpen = 1;
                    MusicOpen << (1)
                    # (Line 119) MusicRemain--;
                    MusicRemain.__isub__(1)
                    # (Line 120) }
                    # (Line 121) else{				 //정답 비공개처리
                if EUDElse()():
                    # (Line 122) MusicPlay[MusicPlayRear] = MusicTemp;
                    _ARRW(MusicPlay, MusicPlayRear) << (MusicTemp)
                    # (Line 123) MusicPlayRear++;
                    MusicPlayRear.__iadd__(1)
                    # (Line 124) }
                    # (Line 125) }
                EUDEndIf()
                # (Line 127) if(VoteAll >= ms.VoteNum[VoteN-1]){
            EUDEndIf()
            if EUDIf()(VoteAll >= ms.VoteNum[VoteN - 1]):
                # (Line 128) foreach(p : EUDLoopPlayer('Human', None, None)){
                for p in EUDLoopPlayer('Human', None, None):
                    # (Line 129) setcurpl(p);
                    f_setcurpl(p)
                    # (Line 130) s2.print("\x1F■ \x04스킵투표로 현재곡을 스킵합니다.");
                    s2.print("\x1F■ \x04스킵투표로 현재곡을 스킵합니다.")
                    # (Line 131) MusicTextU[p] = 1;
                    _ARRW(MusicTextU, p) << (1)
                    # (Line 132) }
                    # (Line 133) }

                # (Line 134) else if(Deaths(fc.superUser, Exactly, 2, ms.KEY)){
            if EUDElseIf()(Deaths(fc.superUser, Exactly, 2, ms.KEY)):
                # (Line 135) foreach(p : EUDLoopPlayer('Human', None, None)){
                for p in EUDLoopPlayer('Human', None, None):
                    # (Line 136) setcurpl(p);
                    f_setcurpl(p)
                    # (Line 137) s2.print("\x1F■ \x04방장이 현재곡을 스킵했습니다.");
                    s2.print("\x1F■ \x04방장이 현재곡을 스킵했습니다.")
                    # (Line 138) MusicTextU[p] = 1;
                    _ARRW(MusicTextU, p) << (1)
                    # (Line 139) }
                    # (Line 140) }

                # (Line 141) SetDeaths(Force1, SetTo, 4, ms.EFFECT);
            EUDEndIf()
            # (Line 142) }
            DoActions(SetDeaths(Force1, SetTo, 4, ms.EFFECT))
            # (Line 143) }
        EUDEndIf()
        # (Line 144) if(MusicStep == 4){
    EUDEndIf()
    if EUDIf()(MusicStep == 4):
        # (Line 145) MusicDelay++;
        MusicDelay.__iadd__(1)
        # (Line 146) if(MusicDelay > 71){
        if EUDIf()(MusicDelay <= 71, neg=True):
            # (Line 147) MusicDelay = 0;
            MusicDelay << (0)
            # (Line 148) MusicStep = 5;
            MusicStep << (5)
            # (Line 149) }
            # (Line 150) }
        EUDEndIf()
        # (Line 151) if(MusicStep == 5){
    EUDEndIf()
    if EUDIf()(MusicStep == 5):
        # (Line 152) MusicStep = 2;
        MusicStep << (2)
        # (Line 153) if(MusicRemain > 0){
        if EUDIf()(MusicRemain <= 0, neg=True):
            # (Line 154) if(MusicPlayFront == MusicNumber2){
            if EUDIf()(MusicPlayFront == MusicNumber2):
                # (Line 155) shuffle(MusicPlay, MusicRemain);
                f_shuffle(MusicPlay, MusicRemain)
                # (Line 156) MusicPlayFront = 0;
                MusicPlayFront << (0)
                # (Line 157) MusicPlayRear = 0;
                MusicPlayRear << (0)
                # (Line 158) if(MusicPlay[MusicPlayFront] == 0){ //재순회했을 때, 0번인덱스가 0인 경우
                if EUDIf()(MusicPlay[MusicPlayFront] == 0):
                    # (Line 159) MusicStep = 20;
                    MusicStep << (20)
                    # (Line 160) CurrentMusic = ms.EndingMusic;
                    CurrentMusic << (ms.EndingMusic)
                    # (Line 161) }
                    # (Line 162) }
                EUDEndIf()
                # (Line 163) else{
            if EUDElse()():
                # (Line 164) if(MusicPlay[MusicPlayFront] == 0){ //순회 전에 값이 0인 경우
                if EUDIf()(MusicPlay[MusicPlayFront] == 0):
                    # (Line 165) MusicStep = 20;
                    MusicStep << (20)
                    # (Line 166) CurrentMusic = ms.EndingMusic;
                    CurrentMusic << (ms.EndingMusic)
                    # (Line 167) }
                    # (Line 168) }
                EUDEndIf()
                # (Line 169) }
            EUDEndIf()
            # (Line 170) else{
        if EUDElse()():
            # (Line 171) MusicStep = 20;
            MusicStep << (20)
            # (Line 172) CurrentMusic = ms.EndingMusic;
            CurrentMusic << (ms.EndingMusic)
            # (Line 173) }
            # (Line 174) }
        EUDEndIf()
        # (Line 175) }
    EUDEndIf()
    # (Line 176) function musicPlay(cp){ //플레이어 텍스트 및 정답관리

@EUDFunc
def f_musicPlay(cp):
    # (Line 177) if(MusicStep > 0){
    if EUDIf()(MusicStep <= 0, neg=True):
        # (Line 178) if(!Deaths(cp, Exactly, CurrentMusic, ms.MUSIC)){
        if EUDIf()(Deaths(cp, Exactly, CurrentMusic, ms.MUSIC), neg=True):
            # (Line 179) SetDeaths(cp, SetTo, CurrentMusic, ms.MUSIC);
            # (Line 180) BGM.SetBGM(CurrentMusic);
            DoActions(SetDeaths(cp, SetTo, CurrentMusic, ms.MUSIC))
            BGM.SetBGM(CurrentMusic)
            # (Line 181) }
            # (Line 182) if(MusicStep < 20){ //엔딩이 아닐 때
        EUDEndIf()
        if EUDIf()(MusicStep >= 20, neg=True):
            # (Line 183) if(MusicTextU[cp] == 1){
            if EUDIf()(MusicTextU[cp] == 1):
                # (Line 184) MusicTextU[cp] = 0;
                _ARRW(MusicTextU, cp) << (0)
                # (Line 185) if(IsUserCP()){
                if EUDIf()(IsUserCP()):
                    # (Line 186) s.insert(0);
                    s.insert(0)
                    # (Line 187) if(MusicStep <= 4){
                    if EUDIf()(MusicStep <= 4):
                        # (Line 188) s.append("\x13\x1E남은곡 ( ", MusicRemain, " / ", MusicNumber2, " )\n");
                        s.append("\x13\x1E남은곡 ( ", MusicRemain, " / ", MusicNumber2, " )\n")
                        # (Line 189) if(ms.MusicShort == 1 && op.setting5 == 0){ //짧게듣기가 활성화된 경우
                        if EUDIf()(EUDSCAnd()(ms.MusicShort == 1)(op.setting5 == 0)()):
                            # (Line 190) if(MusicAnswerUser == 0){s.append("\x13\x19음악\x04을 듣고 \x11답\x04을 입력하세요.\n");}
                            if EUDIf()(MusicAnswerUser == 0):
                                s.append("\x13\x19음악\x04을 듣고 \x11답\x04을 입력하세요.\n")
                                # (Line 191) else{s.append("\x13\x11정답 곡\x04을 재생하고 있습니다.\n");}
                            if EUDElse()():
                                s.append("\x13\x11정답 곡\x04을 재생하고 있습니다.\n")
                                # (Line 192) }
                            EUDEndIf()
                            # (Line 193) else{ //짧게듣기가 비활성화된 경우
                        if EUDElse()():
                            # (Line 194) s.append("\x13\x19음악\x04을 듣고 \x11답\x04을 입력하세요.\n");
                            s.append("\x13\x19음악\x04을 듣고 \x11답\x04을 입력하세요.\n")
                            # (Line 196) }
                            # (Line 197) s.append("\x13\x1F- \x1D", MusicTimer, "초 \x1F-\n");
                        EUDEndIf()
                        s.append("\x13\x1F- \x1D", MusicTimer, "초 \x1F-\n")
                        # (Line 198) if(op.setting3 == 0){if(MusicHintOpen1 == 1){s.append("\n\x13\x07",ptr2s(op.settingName3)," \x04: ", ptr2s(ms.MusicHint1[MusicTemp-1]), "");}}
                        if EUDIf()(op.setting3 == 0):
                            if EUDIf()(MusicHintOpen1 == 1):
                                s.append("\n\x13\x07", ptr2s(op.settingName3), " \x04: ", ptr2s(ms.MusicHint1[MusicTemp - 1]), "")
                            EUDEndIf()
                            # (Line 199) if(op.setting4 == 0){if(MusicHintOpen2 == 1){s.append("\n\x13\x07",ptr2s(op.settingName4)," \x04: ", ptr2s(ms.MusicHint2[MusicTemp-1]), "");}}
                        EUDEndIf()
                        if EUDIf()(op.setting4 == 0):
                            if EUDIf()(MusicHintOpen2 == 1):
                                s.append("\n\x13\x07", ptr2s(op.settingName4), " \x04: ", ptr2s(ms.MusicHint2[MusicTemp - 1]), "")
                            EUDEndIf()
                            # (Line 200) if(MusicOpen == 1){s.append("\n\x13\x1F정답 \x04: ", ptr2s(ms.MusicAnswer[MusicTemp-1]), "");}
                        EUDEndIf()
                        if EUDIf()(MusicOpen == 1):
                            s.append("\n\x13\x1F정답 \x04: ", ptr2s(ms.MusicAnswer[MusicTemp - 1]), "")
                            # (Line 201) }
                        EUDEndIf()
                        # (Line 202) }
                    EUDEndIf()
                    # (Line 203) }
                EUDEndIf()
                # (Line 204) if(IsUserCP()){s.DisplayAt(0);}
            EUDEndIf()
            if EUDIf()(IsUserCP()):
                s.DisplayAt(0)
                # (Line 205) if(op.setting2 == 0){
            EUDEndIf()
            if EUDIf()(op.setting2 == 0):
                # (Line 206) const VoteN = sys.UserNumber;
                VoteN = sys.UserNumber
                # (Line 207) if(VoteAll == 0){eprintln("\x1D( \x19\"K\"\x04키를 누르면, 곡을 넘깁니다. \x1D)");}
                if EUDIf()(VoteAll == 0):
                    f_eprintln("\x1D( \x19\"K\"\x04키를 누르면, 곡을 넘깁니다. \x1D)")
                    # (Line 208) else{eprintln("\x1D( \x19\"K\"\x04키를 누르면, 곡을 넘깁니다. \x1E투표인원 ", VoteAll, "/", ms.VoteNum[VoteN-1], " \x1D)");}
                if EUDElse()():
                    f_eprintln("\x1D( \x19\"K\"\x04키를 누르면, 곡을 넘깁니다. \x1E투표인원 ", VoteAll, "/", ms.VoteNum[VoteN - 1], " \x1D)")
                    # (Line 209) }
                EUDEndIf()
                # (Line 210) else{eprintln("\x1D( \x04스킵이 \x06비활성화\x04되어 있습니다. \x1D)");}
            if EUDElse()():
                f_eprintln("\x1D( \x04스킵이 \x06비활성화\x04되어 있습니다. \x1D)")
                # (Line 211) if(CleanText[cp] == 1){
            EUDEndIf()
            if EUDIf()(CleanText[cp] == 1):
                # (Line 212) CleanText[cp] = 0;
                _ARRW(CleanText, cp) << (0)
                # (Line 213) if(IsUserCP()){s2.printfAt(0, "\n\n\n\n\n\n\n\n");}
                if EUDIf()(IsUserCP()):
                    s2.printfAt(0, "\n\n\n\n\n\n\n\n")
                    # (Line 214) }
                EUDEndIf()
                # (Line 215) if(MusicStep == 3){
            EUDEndIf()
            if EUDIf()(MusicStep == 3):
                # (Line 216) if(Deaths(cp, Exactly, 1, ms.KEY)){
                if EUDIf()(Deaths(cp, Exactly, 1, ms.KEY)):
                    # (Line 217) if(op.setting2 == 0){
                    if EUDIf()(op.setting2 == 0):
                        # (Line 218) if(VoteUser[cp] == 0){
                        if EUDIf()(VoteUser[cp] == 0):
                            # (Line 219) VoteUser[cp] = 1;
                            _ARRW(VoteUser, cp) << (1)
                            # (Line 220) VoteAll += 1;
                            VoteAll.__iadd__(1)
                            # (Line 221) s2.print("\x08！\x04스킵에 투표하셨습니다.");
                            s2.print("\x08！\x04스킵에 투표하셨습니다.")
                            # (Line 222) SetDeaths(cp, SetTo, 2, ms.EFFECT);
                            # (Line 223) }
                            DoActions(SetDeaths(cp, SetTo, 2, ms.EFFECT))
                            # (Line 224) }
                        EUDEndIf()
                        # (Line 225) }
                    EUDEndIf()
                    # (Line 226) if(Deaths(cp, AtLeast, 1, ms.ANSWER)){ //정답처리
                EUDEndIf()
                if EUDIf()(Deaths(cp, AtLeast, 1, ms.ANSWER)):
                    # (Line 227) const key = fc.GetDeath(cp, ms.ANSWER);
                    key = fc.GetDeath(cp, ms.ANSWER)
                    # (Line 228) if(key-1 == MusicTemp){
                    if EUDIf()(key - 1 == MusicTemp):
                        # (Line 229) if(MusicOpen  == 0 && MusicAnswerUser == 0){
                        if EUDIf()(EUDSCAnd()(MusicOpen == 0)(MusicAnswerUser == 0)()):
                            # (Line 230) MusicAnswerUser = 1;
                            MusicAnswerUser << (1)
                            # (Line 231) MusicOpen = 1;
                            MusicOpen << (1)
                            # (Line 232) MusicRemain--;
                            MusicRemain.__isub__(1)
                            # (Line 233) if(ms.MusicShort == 1 && op.setting5 == 0){MusicTimer = ms.MusicLength[MusicTemp-1];}
                            if EUDIf()(EUDSCAnd()(ms.MusicShort == 1)(op.setting5 == 0)()):
                                MusicTimer << (ms.MusicLength[MusicTemp - 1])
                                # (Line 234) UserAnswer[cp] += 1;
                            EUDEndIf()
                            _ARRW(UserAnswer, cp).__iadd__(1)
                            # (Line 235) foreach(p : EUDLoopPlayer('Human', None, None)){
                            for p in EUDLoopPlayer('Human', None, None):
                                # (Line 236) setcurpl(p);
                                f_setcurpl(p)
                                # (Line 237) s2.print("\x1F■ ", PColor(cp), PName(cp), "\x04님께서 정답을 맞추셨습니다!");
                                s2.print("\x1F■ ", PColor(cp), PName(cp), "\x04님께서 정답을 맞추셨습니다!")
                                # (Line 238) MusicTextU[p] = 1;
                                _ARRW(MusicTextU, p) << (1)
                                # (Line 239) }
                                # (Line 240) setcurpl(cp);

                            f_setcurpl(cp)
                            # (Line 241) SetDeaths(Force1, SetTo, 5, ms.EFFECT);
                            # (Line 242) SetScore(cp, Add, 1, Custom);
                            DoActions(SetDeaths(Force1, SetTo, 5, ms.EFFECT))
                            # (Line 243) }
                            DoActions(SetScore(cp, Add, 1, Custom))
                            # (Line 244) }
                        EUDEndIf()
                        # (Line 245) }
                    EUDEndIf()
                    # (Line 246) }
                EUDEndIf()
                # (Line 247) }
            EUDEndIf()
            # (Line 248) if(MusicStep == 20){
        EUDEndIf()
        if EUDIf()(MusicStep == 20):
            # (Line 249) if(Ending[cp] == 0){
            if EUDIf()(Ending[cp] == 0):
                # (Line 250) s2.insert(0);
                s2.insert(0)
                # (Line 251) s2.append(ptr2s(ms.EndingText1), "\n");
                s2.append(ptr2s(ms.EndingText1), "\n")
                # (Line 252) s2.append(ptr2s(ms.EndingText2), "\n");
                s2.append(ptr2s(ms.EndingText2), "\n")
                # (Line 253) s2.append(ptr2s(ms.EndingText3), "\n");
                s2.append(ptr2s(ms.EndingText3), "\n")
                # (Line 254) s2.append(ptr2s(ms.EndingText4), "\n");
                s2.append(ptr2s(ms.EndingText4), "\n")
                # (Line 255) s2.append(ptr2s(ms.EndingText5), "\n");
                s2.append(ptr2s(ms.EndingText5), "\n")
                # (Line 256) s2.append(ptr2s(ms.EndingText6), "\n");
                s2.append(ptr2s(ms.EndingText6), "\n")
                # (Line 257) s2.append(ptr2s(ms.EndingText7));
                s2.append(ptr2s(ms.EndingText7))
                # (Line 258) }
                # (Line 259) if(IsUserCP()){s2.DisplayAt(0);}
            EUDEndIf()
            if EUDIf()(IsUserCP()):
                s2.DisplayAt(0)
                # (Line 260) if(Ending[cp] > EndingDelay){Victory();}
            EUDEndIf()
            if EUDIf()(Ending[cp] <= EndingDelay, neg=True):
                DoActions(Victory())
                # (Line 261) Ending[cp] += 1;
            EUDEndIf()
            _ARRW(Ending, cp).__iadd__(1)
            # (Line 262) }
            # (Line 263) else{
        if EUDElse()():
            # (Line 264) if(TextMeassge[cp] < 4320){TextMeassge[cp] += 1;}
            if EUDIf()(TextMeassge[cp] >= 4320, neg=True):
                _ARRW(TextMeassge, cp).__iadd__(1)
                # (Line 265) else{
            if EUDElse()():
                # (Line 266) TextMeassge[cp] = 0;
                _ARRW(TextMeassge, cp) << (0)
                # (Line 267) if(TextType[cp] == 0){
                if EUDIf()(TextType[cp] == 0):
                    # (Line 268) TextType[cp] = 1;
                    _ARRW(TextType, cp) << (1)
                    # (Line 269) s2.print("\x1F■ \x04방장은 다른 유저를 \x08강퇴\x04할 수 있는 권한을 가지고 있습니다.\n   \x1E\"!강퇴\"+\"플레이어숫자\"를 채팅으로 치면 강퇴됩니다. Ex. !강퇴1");
                    s2.print("\x1F■ \x04방장은 다른 유저를 \x08강퇴\x04할 수 있는 권한을 가지고 있습니다.\n   \x1E\"!강퇴\"+\"플레이어숫자\"를 채팅으로 치면 강퇴됩니다. Ex. !강퇴1")
                    # (Line 270) }
                    # (Line 271) else if(TextType[cp] == 1){
                if EUDElseIf()(TextType[cp] == 1):
                    # (Line 272) TextType[cp] = 0;
                    _ARRW(TextType, cp) << (0)
                    # (Line 273) s2.print("\x1F■ \x04방장은 \x02P키\x04를 눌러서 곡을 \x06강제로 스킵\x04할 수 있습니다.");
                    s2.print("\x1F■ \x04방장은 \x02P키\x04를 눌러서 곡을 \x06강제로 스킵\x04할 수 있습니다.")
                    # (Line 274) }
                    # (Line 275) }
                EUDEndIf()
                # (Line 276) }
            EUDEndIf()
            # (Line 277) }
        EUDEndIf()
        # (Line 278) }
    EUDEndIf()
