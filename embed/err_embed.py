from discord import Embed


def general_err_embed(reason):
    embed = Embed(color=0xFFA46E)
    embed.title = '[Failed]'
    embed.description = f'Command execution failed. Reason:\n```{reason}```'

    return embed


def missing_param_embed(param_name):
    reason = f'Missing parameter. <{param_name}> is required, please make sure you entered the <{param_name}> parameter when you use the command.'
    embed = Embed(color=0xFFA46E)
    embed.title = '[Failed]'
    embed.description = f'Command execution failed. Reason:\n```{reason}```'

    return embed
