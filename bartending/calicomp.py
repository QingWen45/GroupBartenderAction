async def get_desc(inquiry: str) -> str:
    if inquiry == 'BadTouch':
        return """  BadTouch 是由2 Bronson Extract,2 Powdered Delta, 2 Flanergide和4 Karmotrine加冰,调制而成.
    "我们毕竟不过是群哺乳动物."
    酸味,时尚,复古."""
    elif inquiry == 'Beer':
        return """  Beer 是由1 Adelhyde,2 Bronson Extract,1 Powdered Delta, 2 Flanergide和4 Karmotrine调制而成.
    "以传统手法酿造的啤酒已经成为了奢侈品,但这种酒和真货的味道相当接近...."
    发泡,时尚,复古."""
    elif inquiry == 'BleedingJane':
        return """  BleedingJane 是由1 Bronson Extract,3 Powdered Delta,和3 Flanergide调和而成.
    "对着镜子重复三次这杯饮料的名字,就会让你看上去像个傻瓜."
    辛辣,经典,解酒"""
    elif inquiry == 'BloomLight':
        return """  BloomLight 是由4 Adelhyde,1 Bronson Extract, 2 Flanergide和3 Karmotrine陈化,加冰,调制而成.
    "这杯酒泛着完全多余的灰褐色...."
    辛辣,宣传,清淡.""" 
    elif inquiry == 'BlueFairy':
        return """  BlueFairy 是由4 Adelhyde,1 Flanergide和任选 Karmotrine陈化,调制而成.
    "只喝一口就能让你的牙齿变蓝.希望你喝完后能好好刷牙."
    甜味,女性化,温和."""
    
    elif inquiry == 'Brandtini':
        return """  Brandtini 是由6 Adelhyde,3 Powdered Delta和1 Karmotrine陈化,调制而成.
    "每10个自命不凡的混球里就会有8个推荐这种酒,但他们沉溺于自命不凡没空为人推荐什么."
    甜味,时尚,惬意."""
    elif inquiry == 'CobaltVelvet':
        return """  CobaltVelvet 是由2 Adelhyde,3 Flanergide和5 Karmotrine加冰,调制而成.
    "就如同把香槟倒在还剩一点可乐的杯子里."
    发泡,时尚,火辣."""
    elif inquiry == 'CreviceSpike':
        return """  CreviceSpike 是由2 Powdered Delta, 4 Flanergide和任选 Karmotrine调和而成.
    "它既能把你的醉意驱除,也能够把你的意识驱除."
    酸味,男性化,解酒."""
    elif inquiry == 'FluffyDream':
        return """  FluffyDream 是由3 Adelhyde,2 Powdered Delta和任选 Karmotrine陈化,调制而成.
    "一两口就足以取悦你的舌头,再多喝就可能会导致睡过头."
    酸味,女性化,温和."""
    elif inquiry == 'FringeWeaver':
        return """  FringeWeaver 是由1 Adelhyde和9 Karmotrine陈化,调制而成.
    "如同就着一勺糖喝下无水酒精."
    发泡,时尚,强烈."""
    elif inquiry == 'FrothyWater':
        return """  FrothyWater 是由1 Adelhyde,1 Bronson Extract,1 Powdered Delta和 1 Flanergide陈化,调制而成.
    "自2040年以来,家长指导级节目里最爱用的啤酒的代用品."
    发泡,经典,清淡."""
    elif inquiry == 'GrizzlyTemple':
        return """  GrizzlyTemple 是由3 Adelhyde,3 Bronson Extract,3 Powdered Delta和1 Karmotrine调和而成.
    "这种酒的味道几乎令人难以忍受.基本上只有它所宣传的那部电影的爱好者会点它."
    苦味,宣传,清淡."""
    elif inquiry == 'GutPunch':
        return """  GutPunch 是由5 Bronson Extract,1 Flanergide和任选Karmotrine陈化,调制而成.
    "这个名字的意思是'由内脏(Gut)制成的混合饮料(Punch)',但是同时也描述了饮用时的感受(重击腹部)."
    苦味,男性化,强烈."""
    elif inquiry == 'Marsblast':
        return """  Marsblast 是由6 Bronson Extract,1 Powdered Delta, 4 Flanergide和2 Karmotrine调和而成.
    "只要喝上一口就足以让你的脸像火星一样红."
    辛辣,男性化,强烈."""
    elif inquiry == 'Mercuryblast':
        return """  Mercuryblast 是由1 Adelhyde,1 Bronson Extract,3 Powdered Delta, 3 Flanergide和2 Karmotrine加冰,调和而成.
    "在这种酒的研发过程中,没有温度计遭到伤害."
    酸味,时尚,火辣."""
    elif inquiry == 'Moonblast':
        return """  Moonblast 是由6 Adelhyde,1 Powdered Delta, 1 Flanergide和2 Karmotrine加冰,调和而成.
    "与你每个月都有一周时间能看到的那座月球强子大炮没有任何关系."
    甜味,女性化,惬意."""
    elif inquiry == 'PianoMan':
        return """  PianoMan 是由2 Adelhyde,3 Bronson Extract,5 Powdered Delta, 5 Flanergide和3 Karmotrine加冰,调制而成.
    "该饮品不代表酒吧钢琴师协会及其相关组织的意见."
    酸味,宣传,强烈."""
    elif inquiry == 'PianoWoman':
        return """  PianoWoman 是由5 Adelhyde,5 Bronson Extract,2 Powdered Delta, 3 Flanergide和3 Karmotrine陈化,调制而成.
    "它的本名是Pretty Woman,但有很多人投诉说如果有种酒叫Piano Man(男钢琴师),就该有另一种被命名为Piano Woman(女钢琴师)."
    甜味,宣传,惬意."""
    elif inquiry == 'Piledriver':
        return """  Piledriver 是由3 Bronson Extract,3 Flanergide和4 Karmotrine调制而成.
    "你的舌头可能察觉不到它的火辣程度,但喝的时候请小心不要烧到嗓子."
    苦味,男性化,火辣."""
    elif inquiry == 'SparkleStar':
        return """  SparkleStar 是由2 Adelhyde,1 Powdered Delta和任选 Karmotrine陈化,调制而成.
    "这种饮料曾经真的能够迸出(Sparkle)杯子,但这导致过多顾客投诉皮肤问题,于是他们被迫重新设计了不会迸射出任何东西的版本."
    甜味,女性化,惬意."""
    elif inquiry == 'SugarRush':
        return """  SugarRush 是由2 Adelhyde,1 Powdered Delta和任选 Karmotrine调制而成.
    "甘甜,清淡,水果风味,不能更加女性化的饮品."
    甜味,女性化,惬意."""
    elif inquiry == 'Suplex':
        return """  Suplex 是由4 Bronson Extract,3 Flanergide和3 Karmotrine加冰,调制而成.
    "对Piledriver进行微妙调整之后,将火辣的感觉从喉咙转移到了舌头上."
    苦味,男性化,火辣."""
    elif inquiry == 'SunshineCloud':
        return """  SunshineCloud 是由2 Adelhyde,2 Bronson Extract和任选 Karmotrine加冰,调和而成.
    "味道就像昔日的巧克力牛奶,甚至还保留着那份香气.也有人说它有些焦糖的味道...."
    苦味,女性化,温和."""
    elif inquiry == 'ZenStar':
        return """  ZenStar 是由每种原料各加四份,加冰,调制而成.
    "你可能会认为如此均衡的配方能够令这杯酒变得美味...那你可就大错特错了."
    酸味,宣传,清淡."""

    elif inquiry == '帮助' or inquiry == 'help':
        return """名称 口味 种类 瓶装饮品
               |欢迎回来,
   B.T.C   |使用导航栏
调酒指南|浏览调酒配方"""

    elif inquiry == '名称':
        return """按名称搜索
C   G
S   Z
F   B
M   P"""
    elif inquiry =='C':
        return "CobaltVelvet\nCreviceSpike"
    elif inquiry =='G':
        return "GrizzlyTemple\nGutPunch"
    elif inquiry =='S':
        return """SparkleStar
SugarRush\nSunshineCloud\nSuplex"""
    elif inquiry =='Z':
        return "ZenStar"
    elif inquiry =='F':
        return "FluffyDream\nFringeWeaver\nFrothyWater"
    elif inquiry =='B':
        return """BadTouch
Beer\nBleedingJane\nBloomLight
BlueFairy\nBrandtini"""
    elif inquiry =='M':
        return "Marsblast\nMercuryblast\nMoonblast"
    elif inquiry =='P':
        return "PianoMan\nPianoWoman\nPiledriver"

    elif inquiry == '口味':
        return """按口味搜索
甜味饮品
苦味饮品
酸味饮品
辛辣饮品
发泡饮品"""
    elif inquiry == '甜味饮品':
        return """SugarRush
SparkleStar\nBlueFairy\nMoonblast
Brandtini\nPianoWoman"""
    elif inquiry == '苦味饮品':
        return """SunshineCloud
GutPunch\nPiledriver
Suplex\nGrizzlyTemple"""
    elif inquiry == '酸味饮品':
        return """FluffyDream
CreviceSpike\nBadTouch
Mercuryblast\nZenStar"""
    elif inquiry == '辛辣饮品':
        return """Marsblast
BleedingJane\nBloomLight"""
    elif inquiry == '发泡饮品':
        return """Beer
FrothyWater\nCobaltVelvet\nFringeWeaver"""

    elif inquiry == '种类':
        return """女性化饮品
男性化饮品
经典饮品
时尚饮品
宣传饮品"""
    elif inquiry == '女性化饮品':
        return """SugarRush
SparkleStar\nBlueFairy
FluffyDream\nSunshineCloud\nMoonblast"""
    elif inquiry == '男性化饮品':
        return """GutPunch\nPiledriver
Suplex\nMarsblast\nCreviceSpike"""
    elif inquiry == '经典饮品':
        return """Beer
BleedingJane\nFrothyWater"""
    elif inquiry == '时尚饮品':
        return """BadTouch
Brandtini\nCobaltVelvet\nFringeWeaver
Mercuryblast"""
    elif inquiry == '宣传饮品':
        return """GrizzlyTemple\nBloomLight\nZenStar
PianoMan\nPianoWoman"""

    elif inquiry == '瓶装饮品':
        return """MulanTea |AFedora
Absinthe |Rum
"这里每种饮料的定价都是$500" -Dana"""

    else:
        return "喂喂！错了！"
