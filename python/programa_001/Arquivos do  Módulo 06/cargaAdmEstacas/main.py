from funcCapCargAoki import valoresK, propGeomEst



tipoEstaca = 'HCM'      # HCM, Escavada, Raiz
diametroEst = 0.30      # m
cargaAdmEsperada = 170  # kN
ListaNspt =     [0,   1,  1,  3,  6, 10, 11, 16,  30,  50,  50,  50, 50, 50, 50]
listaTipoSolo = [23, 23, 23, 23, 32, 32, 32, 32,  32,  12,  12,  12, 12, 12, 12] # usuário pode verificar no arquivo Convenções

# Execuções

print(valoresK(listaTipoSolo))
print(propGeomEst(diametroEst))
#print(valoresrp(listaTipoSolo, tipoEstaca))
