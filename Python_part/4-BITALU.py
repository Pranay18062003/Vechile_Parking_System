# ---------------- VEHICLE PARKING SYSTEM ----------------

# Total parking slots
total_slots = 5
occupied = 0

while True:
    print("\n🚗 Vehicle Parking System 🚗")
    print(f"Total Slots: {total_slots}")
    print(f"Occupied Slots: {occupied}")
    print(f"Available Slots: {total_slots - occupied}")
    print("\n1. Park a Vehicle")
    print("2. Remove a Vehicle")
    print("3. Exit")

    choice = input("\nEnter your choice (1/2/3): ")

    if choice == "1":
        if occupied < total_slots:
            occupied += 1
            print("✅ Vehicle Parked Successfully!")
        else:
            print("❌ Parking Full! No Slots Available.")
    
    elif choice == "2":
        if occupied > 0:
            occupied -= 1
            print("🚙 Vehicle Removed Successfully!")
        else:
            print("❌ No Vehicle to Remove.")
    
    elif choice == "3":
        print("👋 Exiting... Have a good day!")
        break

    else:
        print("⚠️ Invalid choice! Please try again.")
