import pandas as pd
from turtle import RawTurtle
FILE_PATH = "assets/36_States.csv"


class Quiz:
    def __init__(self, t: RawTurtle):
        self.turtle = t
        self.turtle.hideturtle()
        self.turtle.penup()
        data = pd.read_csv(FILE_PATH)
        self.all_state = data.to_dict(orient="records")
        self.answer = ""
        self.score = 0
        self.known_states = []

    def set_answer(self, answer):
        self.answer = answer

    def display_position(self):
        states = [state['state'].lower() for state in self.all_state]
        if self.answer in states:
            self.write_on_map(self.answer)

    def write_on_map(self, answer):
        for state in self.all_state:
            if answer == state['state'].lower():
                self.turtle.goto(x=int(state['x']), y=int(state['y']))
                self.turtle.write(answer)
                self.score += 1
                self.known_states.append(answer)

    def get_score(self):
        score = f"0{self.score}" if self.score < 10 else self.score
        total = f"0{len(self.all_state)}" if len(self.all_state) < 10 else len(self.all_state)
        return f"{score}/{total}"

    def quiz_summary(self, time):
        summary = f"Time Left: {time}\n\n" \
                  f"Number of states you know: {self.score}\n\n"

        for index in range(len(self.known_states)):
            state = self.known_states[index].title()
            if index % 3 == 0:
                summary += f"{state} State\n"
            else:
                summary += f"{state} State\t"
        self.full_map()
        return summary

    def full_map(self):
        states = [state['state'].lower() for state in self.all_state]
        unknown_state = [s for s in states if s not in self.known_states]

        for state in unknown_state:
            self.write_on_map(state)
