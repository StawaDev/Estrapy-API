from .http import get_api

__all__ = ("Games",)

class Games:
    @staticmethod
    def truth():
        """
        Description
        --------------
        A Function That Will Return a Random Truth Challenge 
        
        How to use truth function (Examples)
        ----------------------------
        
        ```
        Estrapy.Games.truth() # Keep it as function or it will return function type
        ```
        """
        return get_api("games/truth")["text"]

    @staticmethod
    def dare():
        """
        Description
        --------------
        A Function That Will Return a Random Dare Challenge As Text
        
        How to use dare function (Examples)
        ----------------------------
        ```
        Estrapy.Games.dare() # Keep it as function or it will return function type
        ```
        """

        return get_api("games/dare")["text"]
