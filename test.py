from uagents import Agent,Context

alice = Agent(name = "Samridhi", seed = "YOUR NEW PHRASE")
count = 0
@alice.on_interval(period=2.0)
async def say_hello(ctx: Context):
    ctx.logger.info(f'hello, my name is {alice.name}')
# Run the agent
if __name__ == "__main__":
    alice.run()