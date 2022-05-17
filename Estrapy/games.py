import json
from typing import List, Union, Optional
import requests
from io import BytesIO
from PIL import Image
from .http import get_api, BASE_URL
from .base import Base, ObjectConverter
import random as rd

__all__ = ("Games", "AniGames", "OsuClients", "Trivia")

Converter = ObjectConverter()


class Games:
    @staticmethod
    async def truth(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a Random Truth Challenge

        How to use truth function (Examples)
        ----------------------------

        ```
        async def truth():
            print(await Estrapy.Games.truth()) # Keep it as function or it will return function type
        ```

        :param generate
        :type formatter: Optional[int]
        """

        url = "games/truth"
        if generate:
            return await Base.produce(total=generate, full_url=url, type="text")

        return get_api(url)["text"]

    @staticmethod
    async def dare(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a Random Dare Challenge As Text

        How to use dare function (Examples)
        ----------------------------
        ```
        async def truth():
            print(await Estrapy.Games.truth()) # Keep it as function or it will return function type
        ```

        :param generate
        :type formatter: Optional[int]
        """

        url = "games/dare"
        if generate:
            return await Base.produce(total=generate, full_url=url, type="text")
        return get_api(url)["text"]

    @staticmethod
    async def shipper(
        player: Optional[str],
        player2: Optional[str],
        player_image: Union[str, bytes] = None,
        player2_image: Union[str, bytes] = None,
        background_image: Union[str, bytes] = None,
        background_size: Optional[tuple] = None,
    ):
        """
        Description
        --------------
        A Function That Will Return an Edited Image with customized Background and Player Image.
        Currently, for the customized image like player_image still using a url. And also, for the background image default size is `1920x1080`.
        There's 2 available size for custom background picture, `1920x1080` and `1280x720`.
        In case you don't want to add an custom background or a player image, you can add `None` to the parameter value.

        How to use shipper (image) function (Examples)
        ----------------------------

        ```
        async def shipper():
            test = await Estrapy.Games.shipper(player="Player1", player2="Player2", player_image="None", player2_image="None", background="None", background_size="None")
            test.show()
        ```

        :param player
        :type player: Optional[str]
        :param player2
        :type player2: Optional[str]
        :param player_image
        :type player_image: Union[str, bytes]
        :param player_image2
        :type player_image2: Union[str, bytes]
        :param background_image
        :type background_image: Union[str, bytes]
        :param background_size
        :type background_size: Optional[str]
        """
        url = f"{BASE_URL}/games/shipper/image/?player={player}&player2={player2}&player_image={player_image}&player2_image={player2_image}&background={background_image}"
        if background_size is None:
            req = requests.get(url)
        if background_size is not None:
            size = f"{background_size[0]}x{background_size[1]}"
            req = requests.get(f"{url}&background_size={size}")

        a = Image.open(BytesIO(req.content))
        return a


class AniGames:
    @staticmethod
    async def truth(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a Random Truth About Anime Challenge

        How to use truth [about anime] as function (Examples)
        ----------------------------

        ```
        async def truth():
            print(await Estrapy.AniGames.truth()) # Keep it as function or it will return function type
        ```

        :param generate
        :type formatter: Optional[int]
        """

        url = "anigames/truth"
        if generate:
            return await Base.produce(total=generate, full_url=url, type="text")
        return get_api(url)["text"]

    @staticmethod
    async def dare(generate: Optional[int] = None) -> None:
        """
        Description
        --------------
        A Function That Will Return a Random Dare Challenge As Text

        How to use dare [about anime] function (Examples)
        ----------------------------
        ```
        async def dare():
            print(await Estrapy.AniGames.dare()) # Keep it as function or it will return function type
        ```

        :param generate
        :type formatter: Optional[int]
        """

        url = "anigames/dare"
        if generate:
            return await Base.produce(total=generate, full_url=url, type="text")
        return get_api(url)["text"]

    @staticmethod
    async def waifu(formatter: bool = False):
        """
        Description
        --------------
        A Function That Will Return a Random Waifu Picture As PNG

        How to use waifu [about anime] function (Examples)
        ----------------------------
        ```
        async def waifu():
            print(await Estrapy.AniGames.waifu()) # Keep it as function or it will return function type
        ```

        :param formatter
        :type formatter: bool, default `False`
        """
        url = get_api("anigames/waifu")
        if formatter:
            return await Base.JSONFormatter(url)
        return url

    @staticmethod
    async def husbando(formatter: bool = False):
        """
        Description
        --------------
        A Function That Will Return a Random Husbando Picture As PNG

        How to use husbando [about anime] function (Examples)
        ----------------------------
        ```
        async def husbando():
            print(await Estrapy.AniGames.husbando()) # Keep it as function or it will return function type
        ```

        :param formatter
        :type formatter: bool, default `False`
        """

        url = get_api("anigames/husbando")
        if formatter:
            return await Base.JSONFormatter(url)
        return url

    @staticmethod
    async def shipper_waifu(player: str, formatter: bool = False):
        """
        Shipper_Waifu
        --------------
        Return Shipper Waifu JSON Data from EstraAPI

        Examples
        --------------
        ```
        async def shipper_waifu():
            print(await Estrapy.AniGames.shipper_waifu(player="Stawa"))
        ```

        :param player
        :type player: str
        :param formatter
        :type formatter: bool, default `False`
        """

        url = get_api(f"anigames/shipper/waifu/?player={player}")
        if formatter:
            return await Base.JSONFormatter(url)
        return url

    @staticmethod
    async def shipper_husbando(player: str, formatter: bool = False):
        """
        Shipper_Husbando
        --------------
        Return Shipper Husbando JSON Data from EstraAPI

        Examples
        --------------
        ```
        async def shipper_husbando():
            print(await Estrapy.AniGames.shipper_husbando(player="Stawa"))
        ```

        :param player
        :type player: str
        :param formatter
        :type formatter: bool, default `False`
        """

        url = get_api(f"anigames/shipper/husbando/?player={player}")
        if formatter:
            return await Base.JSONFormatter(url)
        return url


class OsuClients:
    def __init__(
        self,
        client_id: Union[int, str] = None,
        client_secret: str = None,
        output: str = "json",
    ) -> None:

        self.client_id = client_id
        self.client_secret = client_secret
        self.output = output
        self.output_list = ["json", "object"]

    async def osuprofile(
        self,
        username: Union[int, str] = None,
        formatter: bool = False,
    ):
        """
        Osuprofile
        --------------
        Return Osuprofile JSON Data

        Examples
        --------------
        ```
        async def osuprofile():
            print(await Estrapy.OsuClients.osuprofile(username="Stawa"))
        ```

        :param username
        :type username: int or str
        :param client_id
        :type client_id: int
        :param client_secret
        :type client_secret: str
        :param formatter: It will formatting JSON Data with EstraFormatter
        :type formatter: bool, default `False`
        """

        url = get_api(
            f"osu/?user={username}&client_id={self.client_id}&client_secret={self.client_secret}"
        )
        if self.output == self.output_list[1]:
            return Converter.convert_obj(json.dumps(url))

        if formatter:
            return await Base.JSONFormatter(url)
        return url

    async def osubeatmap(
        self,
        beatmap_id: int,
        formatter: bool = False,
    ):
        """
        Osubeatmap
        --------------
        Return Osubeatmap JSON Data

        Examples
        --------------
        ```
        async def osubeatmap():
            print(await Estrapy.OsuClients.osubeatmap(beatmap_id="2405223"))
        ```

        :param beatmap_id
        :type beatmap_id: int or str
        :param client_id
        :type client_id: int
        :param client_secret
        :type client_secret: str
        :param formatter: It will formatting JSON Data with EstraFormatter
        :type formatter: bool, default `False`
        """

        url = get_api(
            f"osubeatmap/?id={beatmap_id}&client_id={self.client_id}&client_secret={self.client_secret}"
        )
        if self.output == self.output_list[1]:
            return Converter.convert_obj(json.dumps(url))

        if formatter:
            return await Base.JSONFormatter(url)
        return url


class Trivia:
    def __init__(self):
        self.trivia = {"questions": {}}

    async def add(self, question: str, answer: str, options: dir = None) -> None:
        """
        Trivia Add
        --------------
        Adding Trivia Question to JSON File. You can add more than one question.
        You can add options to your question.
        If you don't want to add options, just leave it empty.

        ```
        from Estrapy import Trivia

        EstraTrivia = Trivia()

        async def create_question():
            options = {"A": "Stawa", "B": "RandomPerson", "C": "Phone"}

            question = await EstraTrivia.add(
                question="Who is the creator of this packages?",
                answer=list(options)[0],  # Or "A"
                options=options,
            )
            print(question)
        ```

        :param question
        :type str
        :param answer
        :type str
        :param option
        :type dir
        """

        num = 1
        i = 0

        with open("trivia.json", "r", encoding="utf-8") as f:
            try:
                trivia = json.load(f)
                num = max(map(int, trivia["questions"].keys())) + 1
            except:
                trivia = self.trivia

            try:
                for _ in trivia["questions"].items():
                    i += 1
                    if trivia["questions"][str(i)]["question"] == question:
                        return "Trivia: Question (#{}) is already exist on Question (#{})".format(
                            num, i
                        )
            except:
                pass

            try:
                existing = {int(key) for key in trivia["questions"]}
                missing = [i for i in range(1, max(existing)) if i not in existing]
                num = missing[0]
            except:
                pass

            trivia["questions"].update(
                ({num: {"question": question, "answer": answer, "options": options}})
            )

            with open("trivia.json", "w", encoding="utf-8") as f:
                json.dump(trivia, f, indent=4, ensure_ascii=False)
                return "Question (#{}) added".format(num)

    async def remove(self, num: int) -> None:
        """
        Trivia Remove
        --------------
        Removing Trivia Question from JSON File in Specific Number.
        It will remove at the specific number question from file.

        ```
        from Estrapy import Trivia

        EstraTrivia = Trivia()
        async def remove_question():
            print(await EstraTrivia.remove(1))  # Remove question number 1
        ```

        :param num
        :type int
        """

        with open("trivia.json", "r", encoding="utf-8") as f:
            try:
                trivia = json.load(f)
            except:
                return "Trivia: No Question Found"

        trivia["questions"].pop(str(num))
        with open("trivia.json", "w", encoding="utf-8") as f:
            json.dump(trivia, f, indent=4, ensure_ascii=False)
            return "Trivia: Question (#{}) Removed".format(num)

    async def run(self, num: Optional[int] = None, random_pick: bool = True) -> None:
        """
        Trivia Run
        --------------
        Running Trivia Question from JSON File. You can choose to random pick question or not.
        This function requires `Trivia.answer` function to run. Recommended to use `random_pick` parameter to True.
        #### Examples available in https://github.com/StawaDev/Estrapy-API/blob/main/Examples/Trivia.py

        :param random_pick
        :type bool, default `True`
        """

        if num and random_pick is not None:
            return "Please put None on unnecessary parameter or leave it empty"

        num = 0

        with open("trivia.json", "r") as f:
            File = json.load(f)
            Total = len(File["questions"])

        if random_pick:
            num = rd.randint(1, int(Total))

        while num <= int(Total):
            num = +1
            questions = File["questions"][str(num)]["question"]
            answers = File["questions"][str(num)]["answer"]
            options = File["questions"][str(num)]["options"]
            _options = []

            for i in options:
                _options.append("{}.{}".format(i, options[i]))

            return questions, num, answers, _options

    async def answer(self, run: any, guess: str = None):
        """
        Trivia Answer
        --------------
        Answer Trivia Question. You can guess answer or not.
        This function usually used for once. Recommend to use `random_pick` parameter on `Trivia.run` function.
        #### Examples available in https://github.com/StawaDev/Estrapy-API/blob/main/Examples/Trivia.py

        :param run
        :type any
        :param guess
        :type str
        """

        if str(guess).lower() == str(run[2]).lower():
            return True, run[2]
        return False, run[2]

    async def run_console(random_pick: bool = False) -> None:
        """
        Trivia Run Console
        --------------
        Run Trivia Through Console!
        This function requires Trivia.add to add the questions, answers also options.
        #### Examples available in https://github.com/StawaDev/Estrapy-API/blob/main/Examples/Trivia.py

        :param random_pick
        :type bool, default `False`
        """

        score = 0

        with open("trivia.json", "r") as f:
            File = json.load(f)
            Total = len(File["questions"])

        if random_pick:
            num = rd.randint(1, int(Total))

        for num in range(1, Total + 1):
            questions = File["questions"][str(num)]["question"]
            answers = File["questions"][str(num)]["answer"]
            options = File["questions"][str(num)]["options"]
            _options = []

            for i in options:
                _options.append("{}.{}".format(i, options[i]))

            print("Question (#{}) : {}".format(num, questions))
            print("Options: {}".format(", ".join(_options)))
            answer = input("Answer: ")

            if answer or str.lower(answer) == answers:
                score += 1

            print(
                "That's correct!"
                if answer or str.lower(answer) == answers
                else "That's incorrect!"
            )
        else:
            print(
                "Game over! no more questions! Score: {}%".format(
                    int(score / Total * 100)
                )
            )
