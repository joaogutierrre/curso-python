#Converta um número de segundos para horas, minutos e segundos.

segundos = input("Digite um número em segundo a ser convertido em horas, minutos e segundos:\n")
segundos_input = int(segundos)

segundosPorHora = 3600
segundosPorMinuto = 60

horasCalculado = segundos_input // segundosPorHora
horasResto = segundos_input % segundosPorHora

#print(horasResto)

if(horasResto < 60):
        minutosCalculado = int
        minutosCalculado = horasResto
        #print(minutosCalculado, "minutos")
else:
        minutosCalculado = horasResto // segundosPorMinuto
        #print(minutosCalculado, "minutos")
        
segundosCalculado = (horasResto % segundos_input) % segundosPorMinuto


    

        
print(horasCalculado,"horas", minutosCalculado, "minutos",segundosCalculado,"segundos")
        
     
