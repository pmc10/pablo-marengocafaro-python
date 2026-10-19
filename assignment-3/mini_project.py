# Miniproyecto: Planificador diario automatizado con 9 combinaciones
day = input("What day is it? ").strip().lower()
time = input("What time of day? ").strip().lower()

# Validación de entradas correctas
valid_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
valid_times = ["morning", "afternoon", "evening"]

if day not in valid_days or time not in valid_times:
    print("Suggestion: Enjoy your day! Please enter a valid day and time next time.")
else:
    # Lógica de decisiones por días y horas específicas
    if day == "monday":
        if time == "morning":
            print("Suggestion: Set your goals for the week and grab a coffee.")
        elif time == "afternoon":
            print("Suggestion: Team synchronization and deep work session.")
        elif time == "evening":
            print("Suggestion: Rest early to power through the rest of the week.")
            
    elif day == "tuesday":
        if time == "morning":
            print("Suggestion: Morning Python class - great time to focus!")
        elif time == "afternoon":
            print("Suggestion: Review coding exercises and debug your scripts.")
        elif time == "evening":
            print("Suggestion: Go for a relaxing walk or workout.")
            
    elif day == "saturday":
        if time == "morning":
            print("Suggestion: Enjoy a hearty breakfast and read a book.")
        elif time == "afternoon":
            print("Suggestion: Outdoor activities or visiting friends.")
        elif time == "evening":
            print("Suggestion: Perfect night for a movie or trying a new recipe.")
            
    else:
        # Respuesta genérica para el resto de días válidos
        if time == "morning":
            print("Suggestion: Keep up the good momentum with your daily routine.")
        elif time == "afternoon":
            print("Suggestion: Finish your pending tasks before the day ends.")
        elif time == "evening":
            print("Suggestion: Unwind and prepare for tomorrow.")
