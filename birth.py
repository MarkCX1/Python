c_pop=312032486
sec_yr=365*24*60*60
no_birth=sec_yr//7
no_death=sec_yr//13
no_imm=sec_yr//45

new_pop=no_birth+no_imm-no_death
pop1=c_pop+new_pop
pop2=pop1+new_pop
pop3=pop2+new_pop
pop4=pop3+new_pop
pop5=pop4+new_pop

print('Year-1 Population.' ,pop1)
print('Year-2 Population.' ,pop2)
print('Year-3 Population.' ,pop3)
print('Year-4 Population.' ,pop4)
print('Year-5 Population.' ,pop5)