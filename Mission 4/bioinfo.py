#Alexander Home
#Ibrahim Tounsi
#B13


def is_adn(text):
    for i in text:
        if i.lower() not in ("a","t","c","g"):
            return False
    return True

def positions(text,car):
    position_of_car=[]
    lencar=len(car)
    for i in range(len(text)):
        if car == text[i:(i+lencar)]:
            position_of_car.append(i)
    return position_of_car

def distance_h(text1,text2):
    distance=0
    if len(text1) != len(text2) :
        return None
    else:
        for i,j in zip(text1,text2):
            if i.lower() != j.lower():
                distance+=1
    return distance

def distances_matrice(l):
    matrix=[]
    for i in l:
        line = []
        for j in l:
            dis=distance_h(i,j)
            line.append(dis)
        matrix.append(line)
    return matrix
















