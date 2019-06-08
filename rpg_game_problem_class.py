class rpg_game:
	def __init__(self,gn):#초기화
		self.gn=gn
	def Proportion(self):#비례
		rn=self.gn*0.1
		return int(rn)
	def Exp(self):#제곱
		re=self.gn*0.1
		exp=int(rn)*int(rn)
		return int(exp)
	def remain(self):#남은 골드
		re=1000-self.gn
		return re

		
rn=0
an=1
re=1
name=input("장비의 이름을 지어주세요\n")
print(name,"(+",rn,")")
print("공격력",an)
gold=input("투자할 골드를 입력하세요(최대 1,000):\n")
int_gold=int(gold)
rpg=rpg_game(int_gold)
rn=rpg.Proportion()
an=rpg.Exp()
re=rpg.remain()
if(int_gold<=1000):
	print(gold,"골드를 소모하여, 장비 강화 단계가 현재 +",rn,"강 입니다.")
	
	print(name,"(+",rn,")")
	print("공격력:",an)
	print("남은 골드: ",re)
else:
	print("골드가 부족합니다.")
	
	