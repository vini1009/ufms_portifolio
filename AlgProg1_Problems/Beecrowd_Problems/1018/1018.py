
amount_input = int(input())

ballots = [100, 50, 20, 10, 5, 2, 1]

def getBallotCounted (amount_rest, ballot):
    return amount_rest // ballot # Obter valor inteiro na divisão 

amount_rest = amount_input

print(f"{amount_input}")

for ballot in ballots:
    ballotCount = getBallotCounted(amount_rest, ballot)
    if(ballotCount < 0 ):
        ballotCount = 0
    amount_rest -= ballot * ballotCount
    print(f"{ballotCount} nota(s) de R$ {ballot},00")