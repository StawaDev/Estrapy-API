import asyncio
from Estrapy.base import Base


async def save():
    a = await Base.save(
        target=("sfw", "hug"), total=2, filename="Hug"
    )  # Will save 2 of Hug GIFs
    print("File List: ", a[0], "\nURL List: ", a[1])


asyncio.run(save())
