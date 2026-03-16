"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Precision PC Builder System
Developer: Predrag Komljenovic
"""

PARTS_FILE = "Mid-Project/parts.txt"
BUILD_HISTORY_FILE = "Mid-Project/build_history.txt"

builds = []


def get_customer_info():
    """Collect customer name and build purpose."""

    name = input("Enter Customer Name: ").strip()
    purpose = input("Build Purpose (Gaming / Office / Streaming): ").strip()

    return name, purpose


def select_components():
    """Collect PC component selections."""

    print("\nSelect PC Components")

    cpu = input("CPU: ").strip()
    gpu = input("GPU: ").strip()
    ram = input("RAM: ").strip()
    storage = input("Storage: ").strip()
    case = input("Case: ").strip()

    return {
        "cpu": cpu,
        "gpu": gpu,
        "ram": ram,
        "storage": storage,
        "case": case
    }


def calculate_total(build_data):
    """Calculate total cost using parts.txt"""

    total = 0

    try:
        with open(PARTS_FILE, "r") as file:

            for line in file:

                if line.strip() == "":
                    continue

                category, part, price = line.strip().split(",")

                part = part.strip()
                price = float(price.strip())

                if build_data["cpu"] == part:
                    total += price

                if build_data["gpu"] == part:
                    total += price

                if build_data["ram"] == part:
                    total += price

                if build_data["storage"] == part:
                    total += price

                if build_data["case"] == part:
                    total += price

    except FileNotFoundError:
        print("Error: parts.txt file not found.")

    return total


def review_build(build_record):
    """Display build summary and ask for confirmation."""

    print("\nPRECISION PC BUILDER SUMMARY")
    print("--------------------------------")

    print(f"CUSTOMER: {build_record['customer']}")
    print(f"PURPOSE: {build_record['purpose']}")

    print(f"\nCPU: {build_record['cpu']}")
    print(f"GPU: {build_record['gpu']}")
    print(f"RAM: {build_record['ram']}")
    print(f"STORAGE: {build_record['storage']}")
    print(f"CASE: {build_record['case']}")

    print(f"\nTOTAL BUILD COST: ${build_record['total']:.2f}")

    decision = input("\n(C) Confirm Build | (E) Edit Build: ").strip().upper()

    return decision


def save_build(build_record):
    """Save build information to build_history.txt"""

    try:
        with open(BUILD_HISTORY_FILE, "a") as file:

            file.write("\n-----------------------------\n")
            file.write(f"Customer: {build_record['customer']}\n")
            file.write(f"Purpose: {build_record['purpose']}\n")
            file.write(f"CPU: {build_record['cpu']}\n")
            file.write(f"GPU: {build_record['gpu']}\n")
            file.write(f"RAM: {build_record['ram']}\n")
            file.write(f"Storage: {build_record['storage']}\n")
            file.write(f"Case: {build_record['case']}\n")
            file.write(f"Total: ${build_record['total']:.2f}\n")

    except:
        print("Error saving build.")


def main():
    """Main program controller"""

    print("PRECISION PC BUILDER SYSTEM v1.0\n")

    name, purpose = get_customer_info()

    components = select_components()

    build_record = {
        "customer": name,
        "purpose": purpose,
        "cpu": components["cpu"],
        "gpu": components["gpu"],
        "ram": components["ram"],
        "storage": components["storage"],
        "case": components["case"]
    }

    total_price = calculate_total(build_record)
    build_record["total"] = total_price

    decision = review_build(build_record)

    if decision == "C":
        builds.append(build_record)
        save_build(build_record)
        print("\nBuild saved successfully.")

    else:
        print("\nBuild cancelled.")


main()
