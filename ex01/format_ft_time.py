# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abaiao-r <abaiao-r@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/06/14 15:33:25 by abaiao-r          #+#    #+#              #
#    Updated: 2025/06/14 15:42:45 by abaiao-r         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from datetime import datetime 

# Get current timestamp
current_time = time.time()

# Print seconds since epoch in both float and scientific notation
print(f"Seconds since January 1, 1970: {current_time:,.4f} or {current_time:.2e} in scientific notation")
# {current_time:,.4f} formats the number with commas as thousands separators and 4 decimal places.
# {current_time:.2e} formats the number in scientific notation with 2 decimal places.

# Get current date and format as 'Mon DD YYYY'
now = datetime.now()
print(now.strftime("%b %d %Y"))
