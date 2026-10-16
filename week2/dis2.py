def conv(C: float):
    return (C*9/5)+32

def main():
    print("your temperature in farenheight is :" , conv(float(input("input a temperature in Celcius: "))) , " degrees")

if __name__ == "__main__":
    main()
