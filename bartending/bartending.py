async def get_drink(formula: str) -> str:
    if formula == '0/2/2/2/4/100':
        return "咸猪手(Bad Touch),这么蠢的名字."
    elif formula == '1/2/1/2/4/000':
        return "P—I—J—I—U：啤酒（Beer）。"
    elif formula == '2/4/2/4/8/000':
        return "好，这杯啤酒不错。非常棒。干得好。"
    elif formula == '0/1/3/3/0/001':
        return "好吧，又到了这个月的这个时候，一杯Bleeding Jane."
    elif formula == '4/0/1/2/3/110':
        return "这是什么……Bloom Light？"
    elif formula[:7] == '4/0/0/1' and formula[-3:] == '010':
        return "一杯尽善尽美的蓝精灵（Blue Fairy）."
    elif formula == '6/0/3/0/1/010':
        return "你对于Brandtini可是相当执着。"
    elif formula == '2/0/0/3/5/100':
        return "哦！一杯Cobalt Velvet。我已经很久没有喝过这种酒了。"
    elif formula[:7] == '0/0/2/4' and formula[-3:] == '001':
        return "Crevice Spike,几乎从来没人点过这种酒."
    elif formula[:7] == '3/0/3/0' and formula[-3:] == '010':
        return "Fluffy Dream？我喜欢这个名字的发音。"
    elif formula == '1/0/0/0/9/010':
        return "嗯……来尝尝Fringe Weaver吧。"
    elif formula == '1/1/1/1/0/010':
        return "啊，没错，Frothy Water,正是我要的那种虚假。"
    elif formula == '3/3/3/1/0/001':
        return "一杯Grizzly Temple，对吧？马上就好。"
    elif formula[:7] == '0/5/0/1' and formula[-3:] == '010':
        return "不管你怎么理解这个名字，那杯酒都不会一拳打向你的肚子（Gut Punch）。"
    elif formula == '0/6/1/4/2/001':
        return "Marsblast不是红色的。我也不明白为什么。"
    elif formula == '1/1/3/3/2/101':
        return "这不是从某颗星球上发生的爆破（Mercury Blast），只是一杯酒而已。"
    elif formula == '6/0/1/1/2/101':
        return "Moonblast, 你知道月亮在塔罗牌里代表什么吗?"
    elif formula == '2/3/5/5/3/100':
        return "PianoMan, 酒也有决定性别的权力吗?"
    elif formula == '5/5/2/3/3/010':
        return "无论是打算庆祝，还是感到失落的时候，都想来一杯Piano Woman."
    elif formula == '0/3/0/3/4/000':
        return "这只是一杯普通的Piledriver。"
    elif formula[:7] == '2/0/1/0' and formula[-3:] == '010':
        return "S—P—A—R R……kle Star。"
    elif formula[:7] == '2/0/1/0' and formula[-3:] == '000':
        return "从最基本的开始。一杯Sugar Rush。"
    elif formula == '0/4/0/3/3100':
        return "菜单里有种酒是在这里创造出来的，Suplex."
    elif formula[:7] == '2/2/0/0' and formula[-3:] == '101':
        return "SunshineCloud.嗯,SunshineCloud."
    elif formula == '4/4/4/4/4/100':
        return "Zen Star,这杯饮料丝毫没有沾染人类的原罪。它不会有意识地造成伤害。"
    else:
        return "如果我没记错的话，你是有调酒指南的。不妨看一眼？"