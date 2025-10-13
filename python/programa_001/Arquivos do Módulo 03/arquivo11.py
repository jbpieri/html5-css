import math
from os import W_OK

# Função seno
y = math.sin(math.pi / 2)

print(y)

# Função coseno
w = math.cos(math.pi / 6)
print(w)

# Função tangente
tan =  math.tan(math.pi / 4)
print(tan)

# Trabalhando com graus
angulo = math.radians(30)
sen30 = math.sin(angulo)
print(sen30)


def senGraus(anguloGraus):
    anguloRadianos = math.radians(anguloGraus)
    seno = math.sin(anguloRadianos)
    
    return seno

print(senGraus(90))

# Funçoes inversas

y = math.asin(0.9)
print(y)