class Player:

    def __init__(self, name):
        self.name = name
        self.is_goal = False
        self.points = 0

    def output(self):
        print(self.name)

    def point(self):
        self.points += 1

    def nil(self):
        self.is_goal = False
        self.points = 0


class HitsMatch:

    def __init__(self, count_of_holes, players):
        self.count_of_holes = count_of_holes
        self.players = players
        self.finished = False
        self.now_hole = 0
        self.now_player = 0
        self.results_of_hole = []
        self.first_player = self.players[0].name
        self.results = {}
        for player in self.players:
            self.results[player.name] = list(None for _ in range(count_of_holes))

    def hit(self, success=False):
        try:
            if self.now_hole == self.count_of_holes:
                self.finished = True
                self.hit()
            elif self.now_player == len(self.players):
                for player in self.players:
                    if not player.is_goal:
                        break
                if player.is_goal:
                    for p in self.players:
                        p.nil()
                    self.players.append(self.players.pop(0))
                    self.now_hole += 1
                self.now_player = 0
                self.hit(success)
            else:
                if self.players[self.now_player].is_goal:
                    self.now_player += 1
                    self.hit(success)
                else:
                    self.players[self.now_player].point()
                    if self.players[self.now_player].points == 10:
                        self.players[self.now_player].is_goal = True
                    else:
                        self.players[self.now_player].is_goal = success
                    if self.players[self.now_player].is_goal:
                        self.results[self.players[self.now_player].name][self.now_hole] = self.players[
                            self.now_player].points
                    self.now_player += 1
        except:
            raise RuntimeError

    def get_winners(self):
        try:
            winners = []
            results = {}
            for result in self.results:
                results[result] = sum(self.results[result])
            for result in results:
                if results[result] == results[min(results, key=results.get)]:
                    winners.append(result)
            return winners
        except:
            raise RuntimeError

    def get_table(self):
        players1 = []
        for p in self.players:
            players1.append(p)
        while self.players[0].name != self.first_player:
            self.players.append(self.players.pop(0))
        list_of_results = [tuple(p.name for p in self.players)]
        for i in range(self.count_of_holes):
            list_of_results.append(tuple(self.results[p.name][i] for p in self.players))
        self.players = players1
        return list_of_results


class HolesMatch:

    def __init__(self, count_of_holes, players):
        self.count_of_holes = count_of_holes
        self.players = players
        self.finished = False
        self.now_player = 0
        self.now_hole = 0
        self.now_round = 0
        self.results = []
        self.results.append(list(player.name for player in self.players))
        for i in range(count_of_holes):
            self.results.append(list(None for _ in self.players))

    def hit(self, success=False):
        try:
            if self.now_hole == self.count_of_holes:
                self.finished = True
                self.hit()
            elif self.now_round == 10:
                self.now_hole += 1
                self.now_player = 0
                for player in self.players:
                    player.nil()
                self.hit(success)
            elif self.now_player == len(self.players):
                for player in self.players:
                    if player.is_goal:
                        self.now_hole += 1
                        self.now_round = -1
                        break

                if self.now_round == -1:
                    for player in self.players:
                        player.nil()

                self.now_round += 1
                self.now_player = 0
                self.hit(success)
            else:
                self.players[self.now_player].is_goal = success
                if success:
                    self.players[self.now_player].points = 1
                self.results[self.now_hole + 1][self.now_player] = self.players[self.now_player].points
                self.now_player += 1
        except:
            raise RuntimeError

    def get_winners(self):
        try:
            winners = []
            results = {}
            for i in range(len(self.results[0])):
                results[self.results[0][i]] = 0
            for i in range(1, len(self.results)):
                for j in range(len(self.results[i])):
                    results[self.results[0][j]] += self.results[i][j]
            for result in results:
                if results[result] == results[max(results, key=results.get)]:
                    winners.append(result)
            return winners
        except:
            raise RuntimeError

    def get_table(self):
        list_of_results = []
        for i in range(0, len(self.results)):
            list_of_results.append(tuple(self.results[i]))
        return list_of_results
