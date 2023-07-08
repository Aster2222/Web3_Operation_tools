# What is it used for
to get transfer history list from zksync blockexplorer.

# How to use

python ./get_transfer_list.py [target address] [max page number]
exp：python ./get_transfer_list.py 0x0000000000000000000000000000000000000000 15

you can check max page number from below.
https://explorer.zksync.io/address/[target address]#transfers

# output format

from,to,timestamp,amount
