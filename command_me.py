import time
import files
import timing

async def set_timer(msg, cha, par, target, user_data):
    end = target
    timestring = time.ctime(end)
    if len(par) < 4:
        par.append('Timer')

    print(type(cha))
    try:
        guildid = cha.guild.id
    except:
        guildid = '@me'

    user_data['timers'].append({'id': len(user_data['timers']),
                                'time': end,
                                'message': ' '.join(par[3:]),
                                'set': time.time(),
                                'message_id': msg.id,
                                'channel_id': cha.id,
                                'guild_id': guildid,
                                'repeat': 0})

    files.save_user(msg.author.id, user_data)
    await cha.send(f'Timer set for us ``{timestring}`` which is in ``{timing.seconds_to_string(end - time.time())}``')


async def set_timer_for_friend(msg, cha, par, target, user_data, friend):
    end = target
    timestring = time.ctime(end)
    if len(par) < 5:
        par.append('Timer')

    print(type(cha))
    try:
        guildid = cha.guild.id
    except:
        guildid = '@me'

    user_data['timers'].append({'id': len(user_data['timers']),
                                'time': end,
                                'message': ' '.join(par[4:]),
                                'set': time.time(),
                                'message_id': msg.id,
                                'channel_id': cha.id,
                                'guild_id': guildid,
                                'repeat': 0})

    files.save_user(friend.id, user_data)
    await cha.send(f'Timer set for user ``{str(friend)}`` for ```{timestring}`` which is in ``{timing.seconds_to_string(end - time.time())}``')




