import turtle

# Flag to track turtle status
turtle_active = True

# Setup turtle window
def setup_turtle():
    global turtle_active
    try:
        turtle.title("AI Health Status Result")
        turtle.speed(0)
        turtle.hideturtle()
        turtle.penup()
        turtle.tracer(0)
    except turtle.Terminator:
        turtle_active = False

# Display result on screen
def show_screen(bg_color, message, food_list):
    global turtle_active
    if not turtle_active:
        print("⚠️ Turtle window is closed. Skipping display.")
        return

    try:
        turtle.clear()
        turtle.bgcolor(bg_color)
        turtle.color("white")
        turtle.goto(0, 40)
        turtle.write(message, align="center", font=("Arial", 24, "bold"))
        turtle.goto(0, -20)
        turtle.write("Recommended Food: " + food_list, align="center", font=("Arial", 18, "italic"))
        turtle.goto(0, -60)
        turtle.write("Stay healthy and take care!", align="center", font=("Arial", 14, "normal"))
        turtle.update()
    except turtle.Terminator:
        turtle_active = False
        print("⚠️ Turtle window was closed.")

# Analyze user health and recommend food
def health_analysis(sleep, water, exercise):
    if sleep >= 7 and water >= 8 and exercise == "yes":
        message = "✅ You are Healthy!"
        food = "🥗 Fruit Salad + 🥜 Nuts + 🥒 Cucumber Slices"
        show_screen("green", message, food)

    elif sleep >= 5 and water >= 5:
        message = "⚠️ Needs Improvement! Focus on good habits."
        food = "🥥 Coconut Water + 🍌 Banana + 🥘 Paneer"
        show_screen("orange", message, food)

    else:
        message = "❌ Unhealthy! Get more rest and hydrate!"
        food = "🍠 Sweet Potato + 🥣 Oats + 🥦 Steamed Vegetables"
        show_screen("red", message, food)

# Main program loop
def main():
    global turtle_active
    setup_turtle()

    while True:
        print("\n🌟 Welcome to the AI Health Checker 🌟")

        try:
            sleep = int(input("🛏️  How many hours did you sleep last night? "))
            water = int(input("💧 How many glasses of water did you drink today? "))
            exercise = input("🏃 Did you exercise today? (yes/no): ").strip().lower()

            if exercise not in ["yes", "no"]:
                print("❌ Please enter 'yes' or 'no' for exercise.")
                continue

        except ValueError:
            print("❌ Invalid input. Please enter numeric values for sleep and water.")
            continue

        if turtle_active:
            health_analysis(sleep, water, exercise)

        again = input("\n🔁 Do you want to check again? (yes/no): ").strip().lower()
        if again != "yes":
            print("👋 Thank you for using the AI Health Checker! Stay healthy!")
            break

    if turtle_active:
        try:
            turtle.bye()
        except turtle.Terminator:
            pass

# Run the app
main()

