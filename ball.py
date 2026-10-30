goals = 58                             # number of goals scored
matches = 40                           # number of matches played
goals_per_match = goals / matches      # now i created a varaible called goals_per_match its value is dividing the total goals of 58 into 40 matches the outcome becomes the value
print(goals_per_match)                 # my guess is 1.45
whole_goals = (goals // matches)       # whole goals per match: 58 // 40 drops the decimal parthes played to get total goal
print(whole_goals)                     #  my guess: is 1
leftover = (goals % 5)                 # this is me sharing goals(58) into 5 what i need is the remainder
print(leftover)                        # my guess: is 3
is_high = goals > 50                   # my guess is True
print(is_high)
both = goals > 50 and matches < 30     # my guess is False
print(both)
goals += 3                             # my guess is 61 
print(goals)