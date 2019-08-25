import files
import timing
import time
import command_me
import asyncio
from discord.utils import find

async def load_commands(msg, cha, par, client):
    files.user_exists(msg.author)
    user_data = files.load_user(msg.author.id)

    if par[1] == 'me':
        try:
            distance = timing.string_into_seconds(par[2])
            await command_me.set_timer(msg, cha, par, time.time() + distance, user_data)
        except:
            try:
                target = timing.time_to_seconds(par[2])
                await command_me.set_timer(msg, cha, par, target, user_data)
            except Exception as e:
                await cha.send(f'Error occured: ```{e}``` \n Be sure to use this format: ``rem me <time> <comment>``')

    if par[1] == 'friend':
        print('friend')
        try:
            try:
                guild = cha.guild
                DM = False
            except:
                DM = True

            print(DM)

            if DM:
                def filtering(m):
                    if m.name == par[2]:
                        return True
                    if str(m.id) == par[2]:
                        return True
                    if m.mention == par[2]:
                        return True

                member = find(filtering, client.users)
                files.user_exists(member)
                user_data2 = files.load_user(member.id)

                if member.id in user_data['friends'] or msg.author.id in user_data2['friends']:
                    await cha.send('You are already friends!')

                await cha.send(f'Invite sent to {str(member)}')
                friend_msg = await member.send(f'{msg.author} wants to add you to their friendlist so that you can send each other alarms. React with ✅ to accept.')
                await friend_msg.add_reaction('✅')

                def check(r, user):
                    if r.message.id == friend_msg.id and user == member and str(r.emoji) == '✅':
                        return True
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=60*60*24, check=check)
                except asyncio.TimeoutError:
                    await member.send('Timed out friend request')
                    return
                else:
                    await member.send(f'Accepted friend request, you and {str(msg.author)} are now friends')


                files.user_exists(member)

                user_data['friends'].append(member.id)
                user_data2 = files.load_user(member.id)
                user_data2['friends'].append(msg.author.id)

                files.save_user(msg.author.id, user_data)
                files.save_user(member.id, user_data2)
            else:
                def filter2(m):
                    if m.name == par[2]:
                        return True
                    if str(m.id) == par[2]:
                        return True
                    if m.mention == par[2]:
                        return True

                member = find(filter2, guild.members)
                files.user_exists(member)
                user_data2 = files.load_user(member.id)

                if member.id in user_data['friends'] or msg.author.id in user_data2['friends']:
                    await cha.send('You are already friends!')

                await cha.send(f'Invite sent to {str(member)}')
                friend_msg = await cha.send(f'{member.mention}, {msg.author} wants to add you to their friendlist so that you can send each other alarms. React with ✅ to accept.')
                await friend_msg.add_reaction('✅')

                def check(r, user):
                    if r.message.id == friend_msg.id and user == member and str(r.emoji) == '✅':
                        return True

                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=60 * 60 * 24, check=check)
                except asyncio.TimeoutError:
                    await cha.send('Timed out friend request')
                    return
                else:
                    await cha.send(f'Accepted friend request, {str(member)} and {str(msg.author)} are now friends')

                files.user_exists(member)

                user_data = files.load_user(msg.author.id)
                user_data['friends'].append(member.id)
                user_data2 = files.load_user(member.id)
                user_data2['friends'].append(msg.author.id)

                files.save_user(msg.author.id, user_data)
                files.save_user(member.id, user_data2)
        except Exception as e:
            await cha.send(f'Error occured: ```{e}``` \n Be sure to use this format: ``rem friend <user>``')
            raise e

    if par[1] == 'them':

        def filtering(m):
            if m.name == par[2]:
                return True
            if str(m.id) == par[2]:
                return True
            if m.mention == par[2]:
                return True
        member = find(filtering, client.users)

        if member is None:
            await cha.send(f'Member {par[2]} not found')

        if member.id not in user_data['friends']:
            await cha.send(f'Member {str(member)} not in your friendlist, use ``rem friend <user>``')

        user_data = files.load_user(member.id)

        try:
            distance = timing.string_into_seconds(par[3])
            await command_me.set_timer_for_friend(msg, cha, par, time.time() + distance, user_data, member)
        except:
            try:
                target = timing.time_to_seconds(par[2])
                await command_me.set_timer_for_friend(msg, cha, par, target, user_data)
            except Exception as e:
                await cha.send(f'Error occured: ```{e}``` \n Be sure to use this format: ``rem them <user> <time> <comment>``')
                raise e







