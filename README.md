# Coffee Machine Project

This project simulates a simple coffee machine that manages resources (water, milk, coffee, and money) to make different types of coffee: Espresso, Latte, and Cappuccino. It tracks the available resources, checks if enough resources are present to fulfill a coffee request, handles payments, and restocks resources as needed.

## Features

- **Coffee Selection**: Choose between Espresso, Latte, and Cappuccino.
- **Resource Management**: The machine keeps track of the available water, milk, coffee, and money.
- **Restocking**: If resources run out, the machine will automatically restock to predefined levels.
- **Payment System**: Accepts quarters, dimes, nickels, and pennies as payment for coffee.
- **Resource Deduction**: When a coffee is purchased, the appropriate amount of resources is deducted.
- **Cost Calculation**: Displays the cost of each drink and provides change after purchase.

## Global Variables

- `machine_resources`: Stores the current levels of water, milk, coffee, and money in the machine.

```python
machine_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
