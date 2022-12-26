"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    
    return {item : items.count(item) for item in items}
# print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    temp_inventory = inventory.copy()
    for item in items:
        inventory[item] = items.count(item) + temp_inventory[item] if item in temp_inventory else items.count(item)
        # inventory[item] = inventory.get(item, 0) + 1
    return inventory
# print(add_items({"wood":5}, ["wood", "iron", "coal", "wood"]))


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    # for item in items:
        # inventory[item] = max(inventory[item]-1, 0)

    for item in inventory:
        inventory[item] = inventory[item] - items.count(item) if items.count(item) <= inventory[item] else 0
    return inventory
# print(decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"]))


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    if item in inventory:
        inventory.pop(item)
    return inventory
# print(remove_item({"coal":2, "wood":1, "diamond":2}, "coal"))


def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [(item, value) for item, value in inventory.items() if value > 0]
# print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))
