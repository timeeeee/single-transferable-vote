"""
stv:
compute quota
while some seats don't have winners
  count votes by first preference
  if a candidate has at least the quota:
    elect them
    redistribute their excess votes
  otherwise:
    eliminate candidate with least votes
    redistribute their votes
"""


def droop_quota(votes_cast, seats_to_fill):
    """Return number of votes needed to win.

    This is an extension of 50% + 1 majority in single winner elections- with
    3 candidates elected, each can get 25% + 1 of the vote, with 9 each can get
    10% + 1, etc.
    """
    return int(float(votes_cast) / (seats_to_fill + 1)) + 1


class Ballot(object):
    def __init__(self, candidate_list):
        self.order = candidate_list
        self.value = 1.0

    def eliminate(self, candidate):
        if candidate in self.order:
            self.order.remove(candidate)

    def favorite(self):
        return self.order[0]


def tally_votes(ballots):
    votes = dict()
    for ballot in ballots:
        favorite = ballot.favorite()
        if favorite not in votes:
            votes[favorite] = 0
        votes[favorite] += ballot.value
    return votes
        

def eliminate_winner(ballots, quota, votes):
    # Eliminate winner from ballots, reducing the voting power of the ballots
    # who listed that candidate as first choice. Surplus voting power should be
    # divided among unexhausted ballots.
    surplus = votes - quota


def eliminate_loser


def elect(ballots, seats, candidates):
    """Elect a number of candidates using single transferable vote method"""
    quota = droop_quota(len(ballots), seats)
    elected = []
    # elect or remove candidates until no more seats to fill
    while seats > 1:
        vote_count = tally_votes(ballots)
        winner, winner_votes = max(vote_count, key=lambda x: x[1])
        if winner_votes > quota:
            # We have a winner. Excess votes redistributed.
            eliminate_winner(ballots, quota, winner_votes)
            
            


if __name__ == "__main__":
    print tally_votes([Ballot([1, 2, 3, 4]),
                       Ballot([1, 3, 4, 5]),
                       Ballot([2, 1, 3, 4]),
                       Ballot([5, 2, 1, 3])])


"""
how to represent candidates and ballots? Candidate class with name and id?
string is hashable so if all names will be unique simpler to just use those.
ballots just need to indicate an order of candidates: just a list of names?
operations on ballot: get first vote, remove candidate.

In the case of exhausted ballots, does the full voting power of excess get
redistributed among the unexhausted ballots? This seems to increase voting
power at somewhat arbitrary times. The ideal would be to start the whole
process over, as if the exhausted ballots and candidates had never been part of
the process. edit: turns out this is the wright system!

Ideally, the election results should be the most common result if all
exhausted ballots had their votes for the rest of the candidates assigned at
random. Maybe have one ballot able to split their votes?

Define process functionally, recursively before taking shortcuts.

Ok to count exhausted ballots with no votes as abstentions because not
ranking candidates equivalent to saying they don't care about the rest- if
their ranked candidates had not run they would have abstained.

Voting power is subtracted when someone is elected because otherwise a majority
with similar preferences could have all of their preferences elected, with no
input from others.
"""

"""
For an election in general, the ideal is getting some input from each voter,
and using it to find which of all possible election results "best represents"
the group. Maybe this means, the average order? Is it possible to create a
measure of "fitness" for a particular result, representing how well it
represents the stv results for a particular election?
"""
