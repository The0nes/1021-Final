class Game:

    def __init__(self):
        self.name = ""
        self.age = 0
        self.stage = "start"

    def start(self):
        print("Welcome to 'Life with the Xbox'!")
        self.name = input("Enter your name: ")
        self.stage = "home"
        self.home()

    def home(self):
        print(f"{self.name}, you are 7 years old.")
        print("Living down the street from Brown International Academy.")
        print(
            "Your earliest memory is playing on your father's Xbox in the living room."
        )
        choice = input("Do you want to play a game on the Xbox? (yes/no): ")
        if choice.lower() == "yes":
            self.living_room()
        else:
            self.basement()

    def living_room(self):
        print(
            "You start playing a game on the Xbox. It could be Halo or Gears of War."
        )
        choice = input("Which game do you want to play? (Halo/Gears of war): ")
        if choice.lower() == "Halo":
            print("You play Halo and have a great time.")
            print(
                "You enjoy you time fighting against the covenant as master chief"
            )
        else:
            print("You play Gears of War and have a great time.")
            print("You enjoy you time fighting against the locust as marcus")
            print("" + self.name + ", you are now ready to go to school.")

        self.elementary_school()

    def basement(self):
        print("You decide not to play a game on the Xbox.")
        print("You end up going downstairs")
        print("You look around but you find nothing interesting to do.")
        print("You decide to play Xbox in your living room.")
        self.living_room()

    def elementary_school(self):
        print(
            "You and your friends bond over games and remain close throughout school."
        )
        print(
            "You talk about these games at school and make friends with three kids."
        )
        choice = input("Do you want to talk to you friends? (yes/no): ")
        if choice.lower() == "yes":
            print("")
        print("However, you move across the city into a new school district.")
        self.middle_school()

    def middle_school(self):
        print(f"{self.name}, you are now 11 years old.")
        print("In middle school, you attend three schools.")
        print("never stay longer than a year in each.")
        print(
            "You rely more on the internet and your console for entertainment."
        )
        print("Discovering Twitch and your favorite streamer, Myth.")
        print("You decide that it's time for a big change.")
        choice = input("Do you want to take a break from gaming? (yes/no): ")
        if choice.lower() == "yes":
            self.solitude()
        else:
            self.gaming()

    def solitude(self):
        print(
            "You take a break from gaming and find yourself in a space of loneliness."
        )
        print("You regret not connecting with your friends")
        print("The plus side is that you can now focus on your studies.")
        self.seighth_grade()

    def gaming(self):
        print("You dive deeper into gaming, finding solace and entertainment.")
        print("You continue to watch Myth and making virtual connections.")
        print("You become a dedicated gamer and enjoy your time with friends.")
        print(
            "your grade suffer as a result of your lack of focus on school work."
        )
        self.eighth_grade()

    def seighth_grade(self):
        print(f"{self.name}, you are now 13 years old.")
        print("You are now in 8 grade.")
        print("You are now in the top 10% of your class.")
        print("You try making friends but you can't socialize with anyone.")
        print("You find no use in trying to make friends.")

    def eighth_grade(self):
        print("In eighth grade, you attend Denver Discovery School.")
        print("You make some long-term friends")
        print("Then out of the blue a pandemic moves everything online.")
        print("You reflect on your experiences with gaming and friendships.")
        print(
            "You realize that gaming bring you joy in life and it helps you relax."
        )
        self.high_school()

    def high_school(self):
        print(
            "You reconnet with on of your elementary friends during the summer."
        )
        print(
            "You have a great time with them and you become closer with them.")
        print("You are now in high school")
        print(" you learn you elementary is going to the same school.")
        print("you make a female friend that plays video games.")
        print("You start playing video games more along side your friends.")
        print("You realize the impact gaming has had on your life.")
        print("you realize gaming has a huge effect that reflects on your grades.")
        print("But it can also bring people together.")
        self.end()

    def end(self):
        print("Thank you for playing 'Life with the Xbox'.")
        print("Your journey through childhood and adolescence.")
        print("Gaming has shown the power of connection.")
        print("Gaming has been a source of joy and fulfillment.")
        print("But gaming can also have negative effects.")
        print("You learn from your experiences and make informed decisions.")
        print("The End.")


if __name__ == "__main__":
    game = Game()
    game.start()
