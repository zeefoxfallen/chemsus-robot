from discord.ext import commands

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class  gpt2(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def gpt(self,ctx, lengthstr, *args ):
        if args == ():
            await ctx.channel.send("**[GPT-2]:** input required")
        else:
            try:
                length = int(lengthstr)
            except ValueError:
                await ctx.channel.send("first argument (output length) must be an integer value...")
                return
            inputstr = ""
            for arg in args:
                inputstr += str(arg)
                inputstr += " "
            inputstr = inputstr[:-1]

            await ctx.channel.send("got it, thinking... :brain:")

            # initialize tokenizer and model from pretrained GPT2 model
            tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
            model = GPT2LMHeadModel.from_pretrained('gpt2')

            inputs = tokenizer.encode(inputstr, return_tensors='pt')

            # we pass a maximum output length of 200 tokens
            outputs = model.generate(inputs, max_length=length, do_sample=True, temperature=1)

            text = tokenizer.decode(outputs[0], skip_special_tokens=True)

            if len(text) > 2000:
                await ctx.channel.send(f"The result was too long, so here's the first 1800 characters of it: \n>>> {text[:1800]}...")
            else:
                await ctx.channel.send("here's what I came up with: \n>>> " + text)