# 3- Conversor de Temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C/F/K): ").upper()
destino = input("Converter para (C/F/K): ").upper()

def converter(temp, origem, destino):
    if origem == destino:
        return temp
    if origem == "C":
        return temp + 273.15 if destino == "K" else (temp * 9/5) + 32
    if origem == "F":
        return (temp - 32) * 5/9 if destino == "C" else ((temp - 32) * 5/9) + 273.15
    if origem == "K":
        return temp - 273.15 if destino == "C" else ((temp - 273.15) * 9/5) + 32

resultado = converter(temp, origem, destino)
print(f"{temp}°{origem} = {resultado:.2f}°{destino}")
