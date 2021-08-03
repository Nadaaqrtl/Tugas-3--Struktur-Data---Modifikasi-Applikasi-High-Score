class GameEntry :
    sum_player = 0
    def __init__(self, name, score, timeg):
        self.name = name
        self.score = score
        self.timeg = timeg

        GameEntry.sum_player =+ 0

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def set_time(self, timeg):
        self.timeg = timeg

    def get_time(self):
        return self.timeg

    def get_sum(self):
        return GameEntry.sum_player

class ScoreBoard :
    def __init__(self, capacity):
        self.capacity = capacity
        self.board = [None] * self.capacity
        self.n = 0

    def add(self, game_entry):
        score = game_entry.get_score()

        good = len(self.board) > self.n or score > self.board[self.capacity - 1].get_score()
        if good :
            if self.n < self.capacity :
                self.n = self.n + 1

            j= self.n - 1
            while j > 0 and self.board[j-1].get_score < score :
                self.board[j] = self.board[j-1]
                j -= 1
            self.board[j] = game_entry
            print ("Entry ditambahkan")

    def list_entries(self):
        for i in range(0, self.n):
                print(i + 1, ". ", score_board.board[i].get_name(), "||", score_board.board[i].get_score(), "||", score_board.board[i].get_time())




# capacity
score_board = ScoreBoard(10)

# MENU
active = True
while active :
    print ('\n Menu  \n 1. Add Score \n 2. View Score \n 3. Exit \n')
    menu = int (input("Enter your choice : "))

    if menu == 1 :
        add_name = str (input("Enter your name : "))
        add_score = int (input("Enter your score : "))
        add_timeg = int (input("Enter your time : "))

        add = GameEntry(add_name, add_score, add_timeg)
        set_board = score_board.add(add)

    elif menu == 2 :
        score_board.list_entries()

    else :
        break







