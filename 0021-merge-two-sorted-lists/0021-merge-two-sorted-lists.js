/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    if(!list1) return list2
    if(!list2) return list1
    if(list1.val<=list2.val){
        list1.next = mergeTwoLists(list1.next,list2)
        console.log(list1,list2)
        return list1
    }
    else{
        list2.next = mergeTwoLists(list1,list2.next)
        console.log(list1,list2)
        return list2
    }
};

//재귀를 통해 list를 변경한다.
//val의 값을 비교하여 작은 list에 큰 리스트로 옮긴다.