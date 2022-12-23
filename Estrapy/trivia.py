from typing import Union
from pathlib import Path
import random as rd
import time
import json
import os

__all__ = ("Trivia",)


class Trivia:
    def __init__(self, path: str = "EstraTrivia/trivia.json"):
        self.path = path
        self.trivia = {"questions": {}}

    def check_path(self) -> None:
        """Determining whether or not a path exists, It will create it if it does not already exist.

        .. versionadded:: 0.2.8
        """

        if not os.path.exists(self.path):
            os.makedirs(self.path.split("/")[-1 + 1])
        open(self.path, "a")

    async def add(self, question: str, answer: str, options: dict, **kwargs) -> str:
        """This function will add a new question with followed by the given parameters to a JSON file.
        The options argument requires a directory, ex. `{'A': 'Answer_1', 'B': 'Answer_2'}`.

        Parameters
        -----------
        question: str
            The question to add
        answer: str
            The answer of the question
        options: dict
            The options of the question
        category: Optional[str]
            The category of the question
        difficulty: Optional[str]
            The difficulty of the question

        Returns
        --------
        str
            This will let you know if the question was added or existed.
        """

        num = 1
        i = 0

        self.check_path()
        with open(self.path, "r", encoding="utf-8") as f:
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
                (
                    {
                        num: {
                            "question": question,
                            "answer": answer,
                            "options": options,
                            "difficulty": kwargs.get("difficulty"),
                            "category": kwargs.get("category"),
                        }
                    }
                )
            )

            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(trivia, f, indent=4, ensure_ascii=False)
                return "Question (#{}) added".format(num)

    async def remove(self, num: Union[int, str]) -> str:
        """There's nothing special about this function but it does can remove specific question you want to remove from the JSON file.

        Parameters
        -----------
        num: Union[int, str]
            The number of question to remove

        Returns
        --------
        str
            This will let you know if the question is removed or not.
        """

        self.check_path()
        with open(self.path, "r", encoding="utf-8") as f:
            try:
                trivia = json.load(f)
            except:
                return "Trivia: No Question Found"

        trivia["questions"].pop(str(num))
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(trivia, f, indent=4, ensure_ascii=False)
            return "Trivia: Question (#{}) Removed".format(num)

    async def run(self, num: Union[int, str] = None, random_pick: bool = True) -> tuple:
        """Play Estra Trivia using functions, recommended using this function for Discord Bot.

        Parameters
        -----------
        num: Union[int, str]
            Number of the question to pick
        random_pick: bool = True
            Randomize to pick available questions

        Returns
        --------
        tuple
            This will return `num`, `question`, `answer`, `options`, `difficulty`, `category`
        """

        self.check_path()
        if num and random_pick is not None:
            return "Please put None on unnecessary parameter or leave it empty"

        num = 0

        with open(self.path, "r") as f:
            _file = json.load(f)["questions"]
            total = len(_file)

        if random_pick:
            num = rd.randint(1, total)

        while num <= int(total):
            _options = []
            questions = _file[str(num)]["question"]
            answer = _file[str(num)]["answer"]
            options = _file[str(num)]["options"]
            difficulty = _file[str(num)]["difficulty"]
            category = _file[str(num)]["category"]

            for i in options:
                _options.append("{}.{}".format(i, options[i]))

            return num, questions, answer, _options, difficulty, category

    async def answer(self, run, guess: str = None) -> tuple:
        """Answer the question using function, this is function will be checking if the answer is correct or not.
        Recommended using `:class:~Estrapy.Trivia.run` method.

        Parameters
        -----------
        run: any
            Requires argument from `Estrapy.Trivia.run`
        guess: str
            Player's guess
        """

        if str.lower(guess) == str.lower(run[2]):
            return True, run[2]
        return False, run[2]

    async def run_console(self, random_pick: bool = False) -> None:
        """Play Estra Trivia only using console, easy to access and interact!

        Parameters
        -----------
        random_pick: bool = True
            Randomize to pick available questions
        """

        score = 0
        _options = []

        self.check_path()
        with open(self.path, "r") as f:
            File = json.load(f)
            Total = len(File["questions"])

        if random_pick:
            num = rd.randint(1, Total)

        for num in range(1, Total + 1):
            questions = File["questions"][str(num)]["question"]
            answers = File["questions"][str(num)]["answer"]
            options = File["questions"][str(num)]["options"]
            difficulty = File["questions"][str(num)]["difficulty"]
            category = File["questions"][str(num)]["category"]

            for i in options:
                _options.append("{}.{}".format(i, options[i]))

            print("Question (#{}) : {}".format(num, questions))
            print("Options: {}".format(", ".join(_options)))
            print("Difficulty: {}".format(difficulty))
            print("Category: {}".format(category))
            answer = input("Answer: ")

            if str.lower(answer) == str.lower(answers):
                score += 1

            print(
                "That's correct!"
                if str.lower(answer) == str.lower(answers)
                else "That's incorrect!"
            )
            time.sleep(2)
            for x in options:
                _options.remove("{}.{}".format(x, options[x]))
        else:
            print(
                "Game over! no more questions! Score: {}%".format(
                    int(score / Total * 100)
                )
            )
