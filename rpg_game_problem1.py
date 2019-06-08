rn=0
an=1
name=input("장비의 이름을 지어주세요\n")
print(name,"(+",rn,")")
print("공격력",an)
gold=input("투자할 골드를 입력하세요(최대 1000):\n")
int_gold=int(gold)
if(int_gold<=1000):
	rn=int_gold*0.1
	int_rn=int(rn)
	print(gold,"골드를 소모하여, 장비 강화 단계가 현재 +",int_rn,"강 입니다.")
	exp_rn=int_rn*int_rn
	print(name,"(+",int_rn,")")
	print("공격력:",exp_rn)
	print("남은 골드: ",1000-int_gold)
else:
	print("골드가 부족합니다.")
	
	
	
	