from nonebot import on_command, CommandSession
from .calicomp import get_desc
from .bartending import get_drink
import random

__plugin_name__ = '调酒'
__plugin_usage__ = r"""试着调一杯酒
命令1: calicomp %参数%
输入help打开主面板,输入选项名打开该选项.
命令2: 调酒 %0/0/0/0/0/000%
每个0分别代表了Adelhyde, Bronson Ext, Pwd Delta, Flannergide, Karmotrine,加冰,陈化和是否调和.
你不会真的输入%吧?"""

@on_command('calicomp', aliases=('调酒指南'), only_to_me=False)
async def calicomp(session: CommandSession):

    t = random.randrange(6)
    if t == 0:
        op = '调制生活,改变饮料.'
    else:
        op = '调制饮料,改变生活.'

    inquiry = session.get('inquiry', prompt=op)
    desc = await get_desc(inquiry)
    await session.send(desc)

@calicomp.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['inquiry'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('无结果.')

    session.state[session.current_key] = stripped_arg

@on_command('bartending', aliases=('调酒'), only_to_me=False)
async def bartending(session: CommandSession):
    formula = session.get('formula', prompt='请输入配方.')
    desc = await get_drink(formula)
    await session.send(desc)

@bartending.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['formula'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('这就是你的“我根本不知道自己在干嘛，所以就用这个将就一下”对策吗？')

    session.state[session.current_key] = stripped_arg