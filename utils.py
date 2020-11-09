import discord


""" Create success embed """
def set_success_embed(embedDescription):
    success = discord.Embed()
    success.color = 65280
    success.set_author(name = "УСПЕХ", icon_url="https://cdn.discordapp.com/emojis/530403526573162509.png")
    success.description = embedDescription
    return success


""" Create error embed """
def set_error_embed(embedDescription):
    error = discord.Embed()
    error.color = 16711680
    error.set_author(name="ОШИБКА", icon_url="https://cdn.discordapp.com/emojis/530401936063594498.png")
    error.description = embedDescription
    return error


""" Create information embed """
def set_information_embed(embedDescription):
    information = discord.Embed()
    information.color = 49151
    information.set_author(name="ИНФОРМАЦИЯ", icon_url="https://cdn.discordapp.com/emojis/530405208405311488.png")
    information.description = embedDescription
    return information


""" Create notification embed """
def set_notification_embed(embedDescription):
    notification = discord.Embed()
    notification.color = 16753920
    notification.set_author(name="УВЕДОМЛЕНИЕ", icon_url="https://cdn.discordapp.com/emojis/530401936533356544.png")
    notification.description = embedDescription
    return notification


""" Set role by request on role's owner """
async def set_role_by_owner(channel, message, author, authorsRole, server):
    print('Requested by ' + author.name)
    user_id = int(message.split()[1].replace('<', '').replace('>', '').replace('!', '').replace('@', ''))
    print('mes[1] == ' + message.split()[1])
    print('id == ' + str(user_id))
    try:
        user = await server.fetch_member(user_id)       #try to use get_member(user_id) instead (not coroutine)
        print('user == ' + user.name)
        if user.roles.count(authorsRole) == 1:
            error = set_error_embed("У данного пользователя уже есть доступ")
            await channel.send(embed=error)
            print('User already has access\n\n')
            return
        if user.roles.count(authorsRole) == 0:
            try:
                await user.add_roles(authorsRole)
                success = set_success_embed("Пользователю " + user.mention + " был выдан доступ")
                await channel.send(embed=success)
                print('Access successfully added \n\n')
                return
            except:
                error = set_error_embed("По каким-то непонятным причинам не удалось дать доступ. Пожалуйста, обратитесь к <@!225667885240942592>")
                await channel.send(embed=error)
                print('CAN NOT ADD ACCESS. ERROR IS HERE\n\n')
                return
    except:
        error = set_error_embed("Пользователь не найден")
        await channel.send(embed=error)
        print('User did not found\n\n')
        return


""" Delete role by request on role's owner """
async def delete_role_by_owner(channel, message, author, authorsRole, server):
    print('Requested by ' + author.name)
    user_id = message.split()[1].replace('<', '').replace('>', '').replace('!', '').replace('@', '')
    print('mes[1] == ' + message.split()[1])
    try:
        user = await server.fetch_member(user_id)       #try to use get_member(user_id) instead (not coroutine)
        print('user == ' + user.name)
        if user.roles.count(authorsRole) == 0:
            error = set_error_embed("У данного пользователя нет доступа")
            await channel.send(embed=error)
            print('User do not has access\n\n')
            return
        if user.roles.count(authorsRole) == 1:
            try:
                await user.remove_roles(authorsRole)
                success = set_success_embed("У пользователя " + user.mention + " был удален доступ")
                await channel.send(embed=success)
                print('Successfully removed\n\n')
                return
            except:
                error = set_error_embed("По каким-то непонятным причинам не удалось удалить доступ. Пожалуйста, обратитесь к <@!225667885240942592>")
                await channel.send(embed=error)
                print('CAN NOT REMOVE ACCESS. ERROR IS HERE\n\n')
                return
    except:
        error = set_error_embed("Пользователь не найден")
        await channel.send(embed=error)
        print('User did not found\n\n')
        return


""" Change users nickname """
async def change_nickname(channel, message, author, server):
    print('Requested by ' + author.name)
    user_id = message.split()[1].replace('<', '').replace('>', '').replace('!', '').replace('@', '')
    print('mes[1] == ' + message.split()[1])
    print('userId == ' + str(user_id))
    newNick = ''
    counter = 0
    for i in message.split():
        if counter > 1:
            newNick = newNick + i + ' '
        counter = counter + 1
    print('new nickname == ' + newNick)
    user = await server.fetch_member(user_id)       #try to use get_member(user_id) instead (not coroutine)
    print('user == ' + user.name)
    try:
        if newNick != '':
            try:
                await user.edit(nick=newNick)
                success = set_success_embed("Пользователю  " + user.mention + " было успешно изменено имя")
                await channel.send(embed=success)
                print('Nickname successfully changed')
                return
            except:
                error = set_error_embed("По каким-то непонятным причинам не удалось изменить имя. Пожалуйста, обратитесь к <@!225667885240942592>")
                await channel.send(embed=error)
                print('Can not change nickname')
                return
        else:
            error = set_error_embed("Судя по всему новое имя не введено или введено некорректно")
            await channel.send(embed=error)
            print('newNick == empty\n\n')
            return
    except:
        error = set_error_embed("Пользователь не найден")
        await channel.send(embed=error)
        print('User did not found\n\n')
        return
