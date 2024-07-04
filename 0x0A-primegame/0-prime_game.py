def isWinner(x, nums):
 """Determine who the winner of the game is. Maria or Ben."""
 maria_wins = 0
 ben_wins = 0
 for num in nums:
  if num % 2 == 0:
    ben_wins += 1
  else:
    if num > 3:
      maria_wins += 1
    else:
      pass
  if maria_wins > ben_wins:
    return "Maria"
  elif ben_wins > maria_wins:
    return "Ben"
  else:
    return None
