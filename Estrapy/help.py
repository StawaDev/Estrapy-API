__all__ = ("SFW_LIST", "NSFW_LIST", "Help")


SFW_LIST = ["hug", "run", "smile", "headpat", "neko", "bite", "highfive", "poke", "slap"]
NSFW_LIST = ["yaoi", "yuri", "kill"]
GAMES_LIST = ["truth", "dare"]

class Help:
    @staticmethod
    def sfw():
        """
        Description
        --------------
        A Function That Will Return a List of Sfw Endpoints
        
        How to use sfw help function (Examples)
        ----------------------------
        
        ```
        Estrapy.Help.sfw() # Keep it as function or it will return function type
        ```
        """
        return SFW_LIST

    @staticmethod
    def nsfw():
        """
        Description
        --------------
        A Function That Will Return a List of Nsfw Endpoints
        
        How to use nsfw help function (Examples)
        ----------------------------
        
        ```
        Estrapy.Help.nsfw() # Keep it as function or it will return function type
        ```
        """
        return NSFW_LIST

    @staticmethod
    def games():
        """
        Description
        --------------
        A Function That Will Return a List of Games Endpoints
        
        How to use games help function (Examples)
        ----------------------------
        
        ```
        Estrapy.Help.games() # Keep it as function or it will return function type
        ```
        """
        return GAMES_LIST

    @staticmethod
    def all():
        """
        Description
        --------------
        A Function That Will Return a List of Sfw, Nsfw, Games Endpoints
        
        How to use all help function (Examples)
        ----------------------------
        
        ```
        Estrapy.Help.all() # Keep it as function or it will return function type
        ```
        """
        return SFW_LIST, NSFW_LIST, GAMES_LIST
