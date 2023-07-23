```Java
package org.example;

import lombok.NoArgsConstructor;
import lombok.ToString;

import java.io.BufferedReader;
import java.io.CharArrayReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;


@ToString
class Node {
  int value;
  Node left;
  Node right;

  public Node(int val) {
    this.value = val;
  }
}

@NoArgsConstructor
class MyTreeNode {

  Node node;

  public Node append(int val) {
    if (this.node == null) {
      this.node = new Node(val);
      return this.node;
    }
    return append(this.node, val);
  }

  private Node append(Node node, int val) {
    if (node == null)
      return new Node(val);
    if (val <= node.value) {
      node.left = append(node.left, val);
    } else {
      node.right = append(node.right, val);
    }
    return node;
  }

  String printLevelOrder() {
    Queue<Node> queue = new LinkedList<>();
    Node root = this.node;
    queue.add(root);

    StringBuilder result = new StringBuilder();

    while (!queue.isEmpty()) {
      Node node = queue.poll();
      result.append(node.value).append(" ");

      if (node.left != null) {
        queue.offer(node.left);
      }
      if (node.right != null) {
        queue.offer(node.right);
      }
    }

    return result.toString();
  }
}


public class BinaryTreeWalking {

  //  Обход дерева в порядке level-order
  public static void test(String input, String assertOutput) {
    try (BufferedReader in = new BufferedReader(new CharArrayReader((input).toCharArray()))) {

      Integer n = Integer.parseInt(in.readLine());

      MyTreeNode tree = new MyTreeNode();

      while (n-- > 0) {
        int nodeVal = Integer.parseInt(in.readLine());
        tree.append(nodeVal);
      }

      String res = tree.printLevelOrder();
      assert res.equals(assertOutput);

    } catch (IOException e) {
      throw new RuntimeException(e);
    }
  }


  public static void main(String[] args) {
    test("10\n" +
      "10\n" +
      "5\n" +
      "4\n" +
      "7\n" +
      "9\n" +
      "8\n" +
      "6\n" +
      "3\n" +
      "2\n" +
      "1\n", "10 5 4 7 3 6 9 2 8 1");

    test("10\n" +
      "9\n" +
      "8\n" +
      "6\n" +
      "10\n" +
      "4\n" +
      "3\n" +
      "2\n" +
      "5\n" +
      "1\n" +
      "7\n", "9 8 10 6 4 7 3 5 2 1");

  }
}
```
