my_menu = {
    "sushi": {"price": 19.25, "best_served": "cold"},
    "paella": {"price": 15, "best_served": "hot"},
    "samosa": {"price": 14, "best_served": "hot"},
    "gazpacho": {"price": 8, "best_served": "cold"},
}

# Iterate the items of the menu and print
# whether the dish must be served hot or cold
for dish, values in my_menu.items():
    print(f"{dish.title()} is best served {values['best_served']}.")
