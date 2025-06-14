def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    items = list(iterable)
    if function is None:
        return (item for item in items if item)
    else:
        return (item for item in items if function(item))
