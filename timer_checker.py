import asyncio
import files
import time

filepath = 'UserData'

async def main_loop(client):
    while not client.is_closed():
        await asyncio.sleep(1)
        data = files.load_users()

        current_timers = []

        for userid, userdata in data.items():
            for timer in userdata['timers']:
                if timer['time'] < time.time() + 60:
                    timer['user_id'] = int(userid.replace('.json',''))
                    current_timers.append(timer)
                    userdata['timers'].remove(timer)
            files.save_user(userid.replace('.json',''), userdata)

        print(current_timers)

        for sec in range(59):
            await asyncio.sleep(1)
            for timer in current_timers:
                if timer['time'] < time.time():
                    user = client.get_user(timer['user_id'])
                    message = timer['message']
                    link = f'''<https://discordapp.com/channels/{timer['guild_id']}/{timer['channel_id']}/{timer['message_id']}>'''
                    await user.send(f'⏰ Timer: ``{message}``\n\n{link}')
                    current_timers.remove(timer)


