usd= 752
valor_producto= input("Ingrese el valor en dólares del producto: ")
valor_producto=float(valor_producto)
dcto=(valor_producto*0.35)
totaldcto = (valor_producto-dcto)
envio = totaldcto*0.04
totalenvio = envio+totaldcto
clp = totalenvio*usd
print("El valor a pagar en pesos chilenos corresponde a $",clp)