from pyamf.sol import *
from pyamf import MixedArray

fr = open("JY1.sol", "rb")
s = decode(fr.read())
sol = SOL(s[0])


def change_skill(_k, array, st="", sn=0, en=0):
    if _k == st:
        d_ = dict(array)
        index = -1
        for skill in range(sn, en + 1):
            index += 1
            d_[index] = skill
        item[st] = MixedArray(d_)


for item in s:
    if type(item) == dict:
        for key, value in item.items():
            # 個人屬性
            if key == "m":
                m_d = dict(value)
                m_d[1] = "風"
                m_d[2] = "嘯天"
                m_d[50] = "風雲決"
                for i in range(15, 38):
                    m_d[i] = 100
                for i in range(52, 56):
                    m_d[i] = 209
                for i in [5, 44, 45, 46, 47, 110, 197, 198]:
                    m_d[i] = 99999
                m_d[128] = 225  # 跳转事件
                # sol["m"] = m_d
                item["m"] = MixedArray(m_d)
            # 武功等級
            if key == "v":
                v_d = dict(value)
                for i, v in v_d.items():
                    if type(v) == int:
                        if i in range(2, 183) or i in range(187, 191):
                            v_d[i] = 999
                item["v"] = MixedArray(v_d)
            # 内功/轻功等级
            if key == "x":
                x_d = dict(value)
                for i, v in x_d.items():
                    if v == -1 and 131 <= i < 182:
                        x_d[i] = 50
                item["x"] = MixedArray(x_d)
            # 穴道
            if key == "n":
                n_d = dict(item["n"])
                for i in n_d:
                    n_d[i] = 1
                item["n"] = MixedArray(n_d)
            # 物品栏位：物品编号
            if key == "f":
                f_d = dict(item["f"])
                index = -1
                for i in range(2, 92):
                    index += 1
                    f_d[index] = i
                item["f"] = MixedArray(f_d)
            # 物品编号：物品数量
            if key == "g":
                g_d = dict(item["g"])
                # 武器
                for i in range(2, 63):
                    g_d[i] = 1
                # 暗器
                for i in range(63, 73):
                    g_d[i] = 1000
                # 防具
                for i in range(73, 92):
                    g_d[i] = 1
                item["g"] = MixedArray(g_d)
            change_skill(key, value, "t", 2, 9)  # 暗器
            change_skill(key, value, "r", 10, 22)  # 刀法
            change_skill(key, value, "s", 23, 32)  # 棍法
            change_skill(key, value, "q", 33, 65)  # 劍法
            change_skill(key, value, "o", 66, 113)  # 拳掌
            change_skill(key, value, "p", 114, 130)  # 指法
            change_skill(key, value, "u", 131, 169)  # 内功
            change_skill(key, value, "v_1", 170, 182)  # 輕功
            change_skill(key, value, "w", 187, 190)  # 其他
            # sol[key] = value

for i, v in s[1].items():
    sol[i] = v

sol.save("tst.sol")
