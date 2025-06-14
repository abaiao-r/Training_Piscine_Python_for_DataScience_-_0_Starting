# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abaiao-r <abaiao-r@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/06/14 15:46:35 by abaiao-r          #+#    #+#              #
#    Updated: 2025/06/14 15:58:48 by abaiao-r         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:
    # Check for list
    if object.__class__.__name__ == "list":
        print("List : <class 'list'>")
    # Check for tuple
    elif object.__class__.__name__ == "tuple":
        print("Tuple : <class 'tuple'>")
    # Check for set
    elif object.__class__.__name__ == "set":
        print("Set : <class 'set'>")
    # Check for dict
    elif object.__class__.__name__ == "dict":
        print("Dict : <class 'dict'>")
    # Check for string
    elif object.__class__.__name__ == "str":
        print("Brian is in the kitchen : <class 'str'>")
    else:
        print("Type not found")
    
    return 42

