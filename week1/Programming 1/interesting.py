# A program to compute the value of an investment
# carried 10 years into the future
def main():

    print("This program calculates the future value of a 10-year investment.")
    principal = float(input("Enter the initial investment/principal: "))
    apr = float(input("Enter the annual percentage rate (apr) interest rate (less than 1): "))
    installments = principal * float(input('Enter the half-yearly investment rate (less than 1): '))

    for i in range(1, 11, 1):
        # main formula
        principal = principal*(1+0.5*apr)**2 + installments*(2+0.5*apr)
        print(f"The balance after year {int(i)} is {principal}")

    print(f"The value after 10 years is: {principal}")

if __name__ == "__main__":
    main()
