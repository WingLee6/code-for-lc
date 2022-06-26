# -*- coding: utf-8 -*-
# @Time    : 2022/3/5 
# @Author  : li
# @FileName: BasicOperationsListNode.py
# @Desc    : 链表相关基础操作


from typing import List, Type


# 定义单链表
class ListNode(object):
    def __init__(self, val=0, next=None):
        """
        单链表
        :param val:
        :param next:
        """
        self.val = val
        self.next = next


# 定义双链表
class DListNode(object):
    def __init__(self, val=0, prior=None, next=None):
        """
        双链表
        :param val:
        :param prior:
        :param next:
        """
        self.val = val
        self.prior = prior
        self.next = next


# 创建单链表（不带头结点）
class LinkList(object):
    def __init__(self):
        """
        初始化头节点，默认None
        """
        self.head = None

    def initHeadInsert(self, data: List[int]) -> ListNode:
        """
        初始化单链表头插法
        :param data: 列表类型
        :return:
        """
        self.head = ListNode(data[0])

        for i in data[1:]:
            node = ListNode(i)
            node.next = self.head
            self.head = node

        return self.head

    def initTailInsert(self, data: List[int]) -> ListNode:
        """
        初始化单链表尾插法
        :param data:
        :return:
        """
        self.head = ListNode(data[0])
        # 初始化p指向头节点
        p = self.head
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next

        return self.head

    def headInsert(self, data: int) -> ListNode:
        """
        单链表头插法
        :param data: 列表类型
        :return:
        """
        node = ListNode(data)
        node.next = self.head
        self.head = node

        return self.head

    def tailInsert(self, data: int) -> ListNode:
        """
        单链表尾插法
        :param data:
        :return:
        """
        node = ListNode(data)
        p = self.head
        while p.next:
            p = p.next
        p.next = node
        node.next = None

        return self.head

    def getElem(self, l: ListNode, i: int) -> Type[ListNode]:
        """
        获取第i个结点（如果有）
        :param i:
        :return:
        """
        p = l
        j = 1
        if i == 1:
            return l
        if i < 1:
            return ListNode
        while p and j < i:
            p = p.next
            j += 1

        return p



    def travelList(self, l: ListNode):
        """
        遍历链表
        :return:
        """
        # if self.isEmpty():
        #     exit(0)
        p = l
        while p:
            print(p.val)
            p = p.next




# 测试内容
# testDataList = [7, 2, 3]
# l1 = LinkList()
# l1.init_head_insert(data=testDataList)
# l1.tail_insert(data=88)
# # l1.init_tail_insert(data=testDataList)
#
# if l1.get_elem(5) != None:
#     print(l1.get_elem(4).val)
# else:
#     print("out of Linklist")
#
# l1.travel_list()
