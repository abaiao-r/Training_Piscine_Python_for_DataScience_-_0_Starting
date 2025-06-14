# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abaiao-r <abaiao-r@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/06/14 15:11:47 by abaiao-r          #+#    #+#              #
#    Updated: 2025/06/14 15:26:33 by abaiao-r         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Update list
ft_list[1] = "World!"

# Create a new tuple (tuples are immutable)
ft_tuple = (ft_tuple[0], "Portugal!")

# Update set without functions (re-create the set)
ft_set = {"Hello", "Lisbon!"}

# Update dictionary value
ft_dict["Hello"] = "42Lisbon!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# Output:
# ['Hello', 'World!']
# ('Hello', 'Portugal!')
# {'Hello', 'Lisbon!'}
# {'Hello': '42Lisbon!'}

# +---------+---------+---------+----------------+-------------------+
# | Python  | Ordered | Mutable | Unique Elements| C++98 Equivalent  |
# +---------+---------+---------+----------------+-------------------+
# | list    |  Yes    |  Yes    |      No        | std::vector/list  |
# | tuple   |  Yes    |   No    |      No        | std::pair         |
# | set     |   No    |  Yes    |     Yes        | std::set          |
# | dict    |   No    |  Yes    |  Keys: Yes     | std::map          |
# +---------+---------+---------+----------------+-------------------