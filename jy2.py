from pyamf.sol import *

# gamezly, gamelzy
source = decode(open("gamelzy.sol", "rb").read())
filename, s = source
sol = SOL(filename)


def SetLevel(v):
    s['LV'] = v
    s['JYZ'] = 0


def SetReputation(v):  # 声望
    s['S_W'] = v


def SetMoney(v):  # 银子
    s['Y_Z'] = v


def SetHealth(v):  # 生命
    s['S_M'] = s['S_M0'] = v


def SetCurHealthToOne():
    s['S_M0'] = 1


def SetEnergy(v):  # 内力
    s['N_L'] = s['N_L0'] = v


def SetStrength(v):  # 力道
    s['L_D'] = s['L_D0'] = v


def SetAgility(v):  # 身法
    s['S_F'] = v


def SetConstitution(v):  # 护体
    s['H_T'] = s['H_T0'] = v


def SetMedical(v):  # 医疗
    s['Y_L'] = v


def SetToxicology(v):  # 用毒
    s['Y_D'] = v


def SetDetoxification(v):  # 解毒
    s['J_D'] = v


def SetHandFighting(v):  # 拳掌
    s['Q_Z'] = v


def SetSwordmanship(v):  # 御剑
    s['Y_J'] = v


def SetHiddenWeapon(v):  # 暗器
    s['A_Q'] = v


def SetIntelligence(v):  # 悟性
    s['W_X'] = v


def SetLuckiness(v):  # 福源
    s['F_Y'] = v


def SetSkillPoint(v):  # 学习点
    s['XXD'] = v


def MaxLearnedSkills():  # 将所有已知功法熟练度提升到最大
    for i, v in s.items():
        if "lv_" in i and v != 0:
            skillName = i.split("lv_", 1)[1]
            s['exp_' + skillName] = 9999
            if "XF" in i or "xf" in i:
                s[i] = 5
            else:
                s[i] = 10


def MaxAllSkills():  # 将所有功法熟练度提升至最大
    for i, v in s.items():
        if "lv_" in i:
            if "XF" in i or "xf" in i:
                s[i] = 5
            else:
                s[i] = 10
        elif "exp_" in i:
            s[i] = 9999


def GetAllBooks():  # 获得所有书籍
    for i, v in s.items():
        if "no_" in i and ("XF" in i or "xf" in i):
            s[i] = 5


def DoubleAttack():  # 同时获得空明拳和左右互搏
    s['aaa'] = 1
    s['exp_kongming'] = 9999
    s['lv_kongming'] = 10


def CompareSOL(filepath):  # 对比两个存档文件的区别
    source2 = decode(open(filepath, "rb").read())
    for i, v in s.items():
        if v != source2[1][i]:
            print(i, source2[1][i], v)


def GetAllItems():
    s['no_jcy'] = 999  # 金疮药
    s['no_xhd'] = 999  # 小还丹
    s['no_yzs'] = 999  # 玉真散
    s['no_dhd'] = 999  # 大还丹
    s['no_jzxsw'] = 999  # 九转熊蛇丸
    s['no_jhylw'] = 999  # 九花玉露丸
    s['no_hydxg'] = 999  # 黑玉断续膏
    s['no_lbz'] = 999  # 腊八粥
    s['no_btyjw'] = 999  # 豹胎易筋丸
    s['no_pt'] = 999  # 大蟠桃
    s['no_qingwa'] = 999  # 莽牯朱蛤
    s['no_tsxl'] = 999  # 天山雪莲
    s['no_xbbhj'] = 999  # 玄冰碧火酒

    s['no_fb'] = 999  # 飞镖
    s['no_ssf'] = 999  # 生死符

    s['no_tj'] = 1  # 铁剑
    s['no_jsj'] = 1  # 金蛇剑
    s['no_zwj'] = 1  # 真武剑
    s['no_ytj'] = 1  # 倚天剑
    s['no_xtj'] = 1  # 玄铁剑

    s['no_by'] = 1  # 布衣
    s['no_tiejia'] = 1  # 铁甲
    s['no_jsj'] = 1  # 金丝甲
    s['no_wcy'] = 1  # 乌蚕衣

    s['no_gwbj'] = 1  # 关外白酒
    s['no_xjb'] = 1  # 犀角杯
    s['no_ptj'] = 1  # 葡萄酒
    s['no_ygb'] = 1  # 夜光杯


if __name__ == '__main__':
    SetHealth(9999)
    SetLevel(50)
    SetReputation(99999)

    SetMoney(99999)
    SetEnergy(9999)
    SetConstitution(1000)

    SetStrength(1000)
    SetAgility(1000)
    SetToxicology(1000)
    SetDetoxification(1000)
    SetMedical(1000)
    SetHiddenWeapon(1000)
    SetSwordmanship(1000)
    SetHandFighting(1000)
    SetLuckiness(1000)
    SetIntelligence(1000)

    SetSkillPoint(500)
    DoubleAttack()
    GetAllItems()

    MaxAllSkills()
    GetAllBooks()

    for i, v in s.items():
        sol[i] = v

    sol.save('out.sol')
