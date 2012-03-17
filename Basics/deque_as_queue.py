#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-

################################################################################
## Summary: simple Python program demonstrating using a deque as a stack.
################################################################################

from collections import deque

queue = deque([3, 4, 5])
print(queue)

queue.append(6)
print(queue)

queue.append(7)
print(queue)

out1=queue.popleft()
print(queue)
print(out1)

out2=queue.popleft()
print(queue)
print(out2)

queue.append(8)
print(queue)

out3=queue.popleft()
print(queue)
print(out3)

## END
