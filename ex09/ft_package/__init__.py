def count_in_list(lst, item):
    """
    Count how many times `item` appears in `lst`.

    Parameters:
    - lst (list): The list to search in.
    - item: The item to count.

    Returns:
    int: Number of occurrences of item in the list.
    """
    if not isinstance(lst, list):
        raise TypeError("First argument must be a list.")
    return lst.count(item)
