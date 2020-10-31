import discord
import asyncio
import botToken
import utils
import helpMessage


""" Server """
ukus = None

""" Channels """
rolesChannel = None

""" Admins """
slava = None

""" Roles with privileges """
zamkom = None
voenkom = None

""" Public role """
publicRole = None

""" Discord client object """
client = discord.Client()

@client.event
async def on_ready():
    
    """ Global variables """
    global ukus
    global rolesChannel
    global slava
    global zamkom
    global voenkom
    global publicRole


    """ Information about bot """
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------')
    

    """ Information about server """
    ukus = client.get_guild(344190396043100170)
    print('Server: ' + ukus.name)
    print(ukus.id)
    print('-----------')


    """ Set 'test_bot_channel' channel """
    rolesChannel = client.get_channel(717471224321540206)
    
    """ Set server admins """
    slava = client.get_user(225667885240942592)

    """ Set roles with privileges """
    zamkom = ukus.get_role(631212978926125113)
    voenkom = ukus.get_role(631213266231754801)

    """ Set public role """
    publicRole = ukus.get_role(638862708309229579)


@client.event
async def on_message(message):

    """ Global variables """
    global ukus
    global rolesChannel
    global slava
    global zamkom
    global voenkom
    global publicRole

    """ If sender == bot -> do nothing """
    if message.author == client.user:
        return

    if message.channel == rolesChannel:
        if message.content.startswith('.доступ'):
            print('Starts with .доступ')
            if message.author.roles.count(zamkom) == 1 or message.author.roles.count(voenkom) == 1:
                if len(message.content.split()) == 2:
                    try:
                        await utils.set_role_by_owner(message.channel, message.content, message.author, publicRole, ukus)
                    except:
                        error = utils.set_error_embed("Проблема с выдачей доступа. За информацией обратитесь к " + slava.mention)
                        await rolesChannel.send(embed=error)
                        print('Can not set role\n\n')
                        return
                else:
                    error = utils.set_error_embed("Неверный формат ввода. Используйте:\n\n```.доступ @Пользователь```")
                    await rolesChannel.send(embed=error)
                    print('Wrong input format\n\n')
                    return
            else:
                error = utils.set_error_embed("У вас нет прав на использование этой команды")
                await rolesChannel.send(embed=error)
                print('User do not have permissions to use this format\n\n')
                return
    

        if message.content.startswith('.удалить_доступ'):
            print('Starts with .удалить_доступ')
            if message.author.roles.count(zamkom) == 1 or message.author.roles.count(voenkom) == 1:
                if len(message.content.split()) == 2:
                    try:
                        await utils.delete_role_by_owner(message.channel, message.content, message.author, publicRole, ukus)
                    except:
                        error = utils.set_error_embed("Проблема с удалением доступа. За информацией обратитесь к " + slava.mention)
                        await rolesChannel.send(embed=error)
                        print('Can not delete role\n\n')
                        return
                else:
                    error = utils.set_error_embed("Неверный формат ввода. Используйте:\n\n```.удалить_доступ @Пользователь```")
                    await rolesChannel.send(embed=error)
                    print('Wrong input format\n\n')
                    return
            else:
                error = utils.set_error_embed("У вас нет прав на использование этой команды")
                await rolesChannel.send(embed=error)
                print('User do not have permissions to use this format\n\n')
                return

        if message.content.startswith('.имя'):
            print('Starts with .имя')
            if message.author.roles.count(zamkom) == 1 or message.author.roles.count(voenkom) == 1:
                if len(message.content.split()) > 2:
                    try:
                        await utils.change_nickname(message.channel, message.content, message.author, ukus)
                    except:
                        error = utils.set_error_embed("Проблема с изменением имени. За информацией обратитесь к " + slava.mention)
                        await rolesChannel.send(embed=error)
                        print('Can not change nickname\n\n')
                        return
                else:
                    error = utils.set_error_embed("Неверный формат ввода. Используйте:\n\n```.имя @Пользователь <Новый никнейм>```")
                    await rolesChannel.send(embed=error)
                    print('Wrong input format\n\n')
                    return
            else:
                error = utils.set_error_embed("У вас нет прав на использование этой команды")
                await rolesChannel.send(embed=error)
                print('User do not have permissions to use this format\n\n')
                return
        
        if message.content.startswith('.help') or message.content.startswith('.info') or message.content.startswith('<@!771802616841240617>'):
            information = utils.set_information_embed(helpMessage.helpMessage)
            await rolesChannel.send(embed=information)
            return


""" BOT TOKEN """
client.run(botToken.DISCORD_BOT_TOKEN)