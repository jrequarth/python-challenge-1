# python-challenge-1

This program allows for a customer to numerically submit an order.

A dictionary with multiple items is provided by the company.
The keys are "Snacks", "Meals", "Drinks", and Desserts"

The first step is to create a new dictionary that has numerical keys.
In this new dictionary, "tea, green" and tea, whatever" are given individual keys.

A while loop is created to enable the customer to order multiple items.
The customer is asked for an item number and that is matched to a string that contains the item name and price.
Price is converted into a float variable.

The customer is asked how many of these items (by name) are wanted. 

A list of dictionaries is created called: customer_order_list [].
That list contains the string(item_name), a float(price), and the number of items in integer form.
East time a new item is selected, the customer_order_list is appended.

In a nested While loop, the customer is asked if they want to order more
If so, another the program returns to where the customer is asked what category of items they want, so they can select another item.
When the customer wants to stop ordering, the nested loop sets a variable to False so that when the program returns to the top, it doesn't enter the outer While loop.

The order is printed out with a total cost of the order.
