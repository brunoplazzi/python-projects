#programa para encontrar o mdc de dois numeros inteiros utilizando o algoritmo de euclides.

def f_mdc(num1,num2):

    mdc = int(0)
    dividendo = num1
    divisor = num2

    while(divisor != 0):
        resto = dividendo % divisor
        dividendo = divisor
        divisor = resto

    mdc = dividendo

    return mdc


def main():
    print("*** CALCULADORA MDC ***")
    print("*** Para terminar a execução, insira os dois numeros = 0 ***")
    mdc = int(0)

    num1 = int(input("1° Numero: "))
    num2 = int(input("2° Numero: "))

    while(num1 !=0 or num2 !=0):

        mdc = f_mdc(num1,num2)

        print(mdc)

        num1 = int(input("1° Numero: "))
        num2 = int(input("2° Numero: "))

    print("***FIM***")

if __name__=="__main__":
    main()