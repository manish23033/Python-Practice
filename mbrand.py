from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def get_brand_by_number(mobile_number):
    # Simulated number-brand mapping
    number_to_brand = {
        "9876543210": "Apple iPhone 13",
        "9812345678": "Samsung Galaxy S21",
        "9823456789": "Xiaomi Redmi Note 12",
        "9834567890": "OnePlus Nord CE",
        "9845678901": "Realme Narzo 50",
        "9856789012": "Vivo Y75",
        "9867890123": "Oppo Reno 8"
    }

    return number_to_brand.get(mobile_number, None)

def is_valid_number(number):
    return number.isdigit() and len(number) == 10

def main():
    print(Fore.CYAN + "📱 Mobile Brand Tracker")
    print(Fore.LIGHTBLACK_EX + "Type 'exit' to quit.\n")

    while True:
        mobile_number = input(Fore.YELLOW + "Enter a 10-digit mobile number: ").strip()
        
        if mobile_number.lower() == "exit":
            print(Fore.GREEN + "Exiting... Have a great day!")
            break

        if not is_valid_number(mobile_number):
            print(Fore.RED + "❌ Invalid input! Please enter a 10-digit number.\n")
            continue

        brand = get_brand_by_number(mobile_number)
        if brand:
            print(Fore.GREEN + f"✅ Brand: {brand}\n")
        else:
            print(Fore.RED + "❓ No brand info found for this number.\n")

if __name__ == "__main__":
    main()
