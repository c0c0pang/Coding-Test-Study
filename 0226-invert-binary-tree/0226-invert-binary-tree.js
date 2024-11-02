/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function(root) {
    if(!root) return root;
    const left_val = root.left;
    const right_val = root.right;
    const root_val = root.val;
    let temp = root.left;
    root.left = root.right;
    invertTree(root.left)
    root.right = temp;
    invertTree(root.right)

    return root
};

//이진 트리 구현
//부모 노드를 기준으로 왼쪽 노드는 더 큰 값, 오른쪽 노드는 더 작은 값으로 변환해야한다.
//재귀로 풀이