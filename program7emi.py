def emi_calculate(amount,rate_year,tenuare_month):
    interest=(amount*(tenuare_month/12)*rate_year)/100
    total_amount=amount+interest
    emi_amount=int(total_amount/tenuare_month)
    emis=[]
    for i in range(1,tenuare_month):
        emis.append(emi_amount)
    if total_amount% emi_amount>0:
        emis.append(emi_amount+(total_amount%emi_amount))
    else:
        emis.append(emi_amount)
    return emis
amount= float(input("enter principle amount:"))
rate=float(input("enter amount rate of interest:"))
tenuare=int(input("enter tenuare in month:"))
emi=emi_calculate(amount,rate,tenuare)
index=1
for emi in emi:
    print("EMI for months",index,"is:",emi)
    index+=1


# emi calculte interest decrise principle amount
def emi_calculate(amount,rate_year,tenuare_months):
    emis=[]
    monthly_installment= amount/tenuare_months
    for i in range(0,tenuare_months):
        pending_amount=amount-(monthly_installment*i)
        interest=((pending_amount*(tenuare_months/12)*rate_year)/100)/tenuare_months
        emi_amount=monthly_installment+interest
        emis.append(emi_amount)
    return emis    
amount=100000
rate=12
tenuare=12
emis=emi_calculate(amount,rate,tenuare)
total=0
Index=1
for emi in emis:
    print("EMI for months",index,"is:",emi)
    total+=emi
    index+=1
