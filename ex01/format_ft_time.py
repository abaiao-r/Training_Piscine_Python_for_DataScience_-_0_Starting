# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abaiao-r <abaiao-r@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/06/14 15:33:25 by abaiao-r          #+#    #+#              #
#    Updated: 2025/06/14 15:44:32 by abaiao-r         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from datetime import datetime 

# Get current timestamp
current_time = time.time()

# Print seconds since epoch in both float and scientific notation
print(f"Seconds since January 1, 1970: {current_time:,.4f} or {current_time:.2e} in scientific notation")

# Get current date and format as 'Mon DD YYYY'
now = datetime.now()
print(now.strftime("%b %d %Y"))
