jsh = 120

class sjw:
    def __init__(self, a, b):
        self.a = a 
        self.b = b
    def sjw1(self, a, b):
        if a > b:
            return False
        else:
            return True 

print("정상훈 키우기")
while jsh:
    if jsh >= 140:
        print("The. End")
        break

    chip = int(input("정상훈이 먹은 쿠키 개수 (0을 누르면 종료): "))

    if chip == 0:
        print("프로그램을 종료합니다.")
        break

    y = True

    print("정상훈이 %s개 먹었습니다." % chip)

    while y:

        p = jsh
        jsh += 10 * chip 
        o = jsh
        x = sjw(p, o)
        y = x.sjw1(o, p)

        print("정상훈은 현재 %s kg 입니다." % jsh)
        if jsh < 130:
            print("비만입니다 주의하세요.")
        elif jsh < 140 and jsh >= 130:
            print("고도 비만입니다 주의하세요")
        elif jsh < 150 and jsh >= 140:
            print("정상훈이 초고도 비만으로 사망에 이르렀습니다.")


            


    
