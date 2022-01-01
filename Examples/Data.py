import Estrapy

# Print Only Examples
print(Estrapy.Data.totalSfw("run"))
print(Estrapy.Data.totalAniGames("truth"))

# Function Examples
def function():
    print(f"Total Games Truth: {Estrapy.Data.totalGames('truth')}")
    print(f"Total AniGames Dare: {Estrapy.Data.totalAniGames('dare')}")
    print(f"Total Sfw Poke: {Estrapy.Data.totalSfw('poke')}")
    print(f"Total Nsfw Kill: {Estrapy.Data.totalNsfw('kill')}")


function()
