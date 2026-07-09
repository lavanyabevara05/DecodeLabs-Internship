print("===== Recommendation System =====")

print("Choose your interest:")
print("1. Movies")
print("2. Music")
print("3. Books")
print("4. Sports")

choice = input("Enter your interest: ").lower()

if choice == "movies":
    print("\nRecommended Movies:")
    print("• Avengers")
    print("• Interstellar")
    print("• Bahubali")

elif choice == "music":
    print("\nRecommended Music:")
    print("• Imagine Dragons")
    print("• Arijit Singh")
    print("• A.R. Rahman")

elif choice == "books":
    print("\nRecommended Books:")
    print("• Atomic Habits")
    print("• Rich Dad Poor Dad")
    print("• The Alchemist")

elif choice == "sports":
    print("\nRecommended Sports:")
    print("• Cricket")
    print("• Football")
    print("• Badminton")

else:
    print("Sorry! No recommendations found.")
