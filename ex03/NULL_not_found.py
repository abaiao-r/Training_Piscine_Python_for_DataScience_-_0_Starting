# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abaiao-r <abaiao-r@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/06/14 16:13:25 by abaiao-r          #+#    #+#              #
#    Updated: 2025/06/14 16:21:05 by abaiao-r         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def NULL_not_found(object: any) -> int:
    # None check
    if object is None:
        print("Nothing: None <class 'NoneType'>")
        return 0
    # NaN check (NaN != NaN)
    elif type(object) is float and object != object:
        print("Cheese: nan <class 'float'>")
        return 0
    # Zero check
    elif type(object) is int and object == 0:
        print("Zero: 0 <class 'int'>")
        return 0
    # Empty string check
    elif type(object) is str and object == "":
        print("Empty: <class 'str'>")
        return 0
    # False check
    elif type(object) is bool and object is False:
        print("Fake: False <class 'bool'>")
        return 0
    else:
        print("Type not Found")
        return 1



