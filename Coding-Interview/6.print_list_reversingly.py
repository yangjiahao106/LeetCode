#! python3
# __author__ = "YangJiaHao"
# date: 2018/12/25

# 从尾部到头打印链表， 使用递归实现栈结构,
# 链表过长会出现栈溢出
# sys.getrecursionlimit() 1000

def print_list_reversingly(root):
    if not root:
        return

    print_list_reversingly(root.next)

    print(root.val)
