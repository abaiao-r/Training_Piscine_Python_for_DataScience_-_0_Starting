# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abaiao-r <abaiao-r@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/06/14 16:29:14 by abaiao-r          #+#    #+#              #
#    Updated: 2025/06/14 16:30:32 by abaiao-r         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 1:
    # No argument, do nothing
    pass
elif len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
else:
    arg = sys.argv[1]
    # Check if argument is an integer
    try:
        num = int(arg)
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")

