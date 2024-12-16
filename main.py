print ("A Loan Calculator")
#The initial loan amount
loan =float(1000.0)

#The rate applied per annum
apr = float(0.05)

#Calculate the total money due after 10 years and the interest amount
for year in range (10):
  loan = (loan*apr) + loan
  print("Year ",year+1,"payment is",round(loan,2))
  interest = loan - 1000

print("Your interest amount for 10 years is $",round(interest,2))