principle = 1000
Rate = 0.05

for i in range(10):
  principle+=(principle*Rate)
  print("Year",i+1,"is",round(principle,2))

