import random
class genarate_sudoko:
    def find_num1(self,number,x):
        if x // 9 in [0,3,6]:
            return number
        elif x // 9 in [1,4,7]:
            return number - 1
        elif x //9 in [2,5,8]:
            return number - 2   
    def get_prob1(self,array):
        numbers=[i for i in range(1,10)]
        get_probablity=[[]for i in range(81)]  
        for x in range(81):
            prob=[]
            asign_prob=[]
            if array[x] > 0:
                continue
            else:
                for num1 in range(3):
                    for num2 in range(3):
                        prob.append(array[
                            ((x // 3 ) * 3 ) + ( self.find_num1(num1,x) * 9 ) +num2])
                for line in range(9):
                    prob.append(array[((x // 9 ) * 9 ) + line])
                    prob.append(array[(x % 9 ) + ( 9 * line )])
                prob=list(set(prob))
                prob.remove(0)
                for i in range(len(numbers)):
                    if numbers[i] not in prob:
                        asign_prob.append(numbers[i])
                    
                get_probablity[x]=asign_prob
        return get_probablity
    def search_places(self,get_prob,place_value):
        places=[]
        for number in range(81):
            if len(get_prob[number]) == place_value:
                places.append(number)
        return places
    def least_placeholder(self,get_prob):
        least_place=7
        for num in range(len(get_prob)):
            if len(get_prob[num]) < least_place and len(get_prob[num]) != 0 :
                least_place=len(get_prob[num])
        return least_place
    def solve(self,array,get_prob):
        for i in range(54):
            lp=self.least_placeholder(get_prob)
            pl=self.search_places(get_prob,lp)
            if lp == 1:
                x=pl[0]
                num=get_prob[pl[0]][0]
                for num1 in range(3):
                    for num2 in range(3):
                        place=((x // 3 ) * 3 ) + ( self.find_num1(num1,x) * 9 ) +num2
                        if num in get_prob[place]:
                            get_prob[place].remove(num)
                for line in range(9):
                    place1=((x // 9 ) * 9 ) + line
                    if num in get_prob[place1]:
                        get_prob[place1].remove(num)
                    place2=(x % 9 ) + ( 9 * line )
                    if num in get_prob[place2]:
                        get_prob[place2].remove(num)
                get_prob[x]=[]
                array[x]=num
            else:
                random_num=random.choice(get_prob[pl[0]])
                x=pl[0]
                for num1 in range(3):
                    for num2 in range(3):
                        place=((x // 3 ) * 3 ) + ( self.find_num1(num1,x) * 9 ) +num2
                        if random_num in get_prob[place]:
                            get_prob[place].remove(random_num)
                for line in range(9):
                    place1=((x // 9 ) * 9 ) + line
                    if random_num in get_prob[place1]:
                        get_prob[place1].remove(random_num)
                    place2=(x % 9 ) + ( 9 * line )
                    if random_num in get_prob[place2]:
                        get_prob[place2].remove(random_num)
                get_prob[x]=[]
                array[x]=random_num 
        return array
    def __init__(self,diffculty):
        if diffculty > 80:
            raise("diffculty should less than 80")
        while True:
            try:
                self.array=[0 for i in range(81)]
                self.dif=diffculty
                for box in range(3):
                    numbers=[i for i in range(1,10)]
                    for num in range(9):
                        random_number=random.choice(numbers)
                        self.array[box*27+box*3+num//3*9+num%3] = random_number
                        numbers.remove(random_number)
                self.get_probablity=self.get_prob1(self.array)
                self.array=self.solve(self.array,self.get_probablity)
                break
            except:
                continue
        for_random=[i for i in range(81)]
        self.solved_array=self.array.copy()
        for numbers in range(self.dif):
            rnum=random.choice(for_random)
            self.array[rnum]=0
            for_random.remove(rnum)