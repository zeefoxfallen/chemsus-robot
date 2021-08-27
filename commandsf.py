import botcore

class botcommands:
    def __init__(self,bot):
        @bot.command()
        async def echo(ctx, *args):
            print(args)
            if args == ():
                await ctx.channel.send(":zipper_mouth:")
            else:
                output = ""
                for arg in args:
                    output += str(arg)
                    output += " "
                await ctx.channel.send(output)
