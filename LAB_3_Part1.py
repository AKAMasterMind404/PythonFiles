from DataStructures import BST_Hackerrank as bst

with open('numbers.txt','r') as nums:
    values=[int(i.strip()) for i in nums]
    #values=[4,1,7,5,9,11,10]
    print("values are:",values)

    bt=bst.BinarySearchTree()
    for i in values:
        bt.insert(i)

    while True:
        print("Enter 1 for printing the tree and its height:")#Question 2
        print("Enter 2 for printing In order traversal:")# Question 1
        print("Enter 3 to run the lowest common ancestor function:")#Question 3
        print()
        command=int(input("Your choice here:"))
        print('####################')
        if command==1:
            bt.treeHeight(True)
        elif command==2:
            print("In order traversal:")
            bst.inorderTraversal(bt.root)
        elif command==3:
            n1=int(input("Enter Value for node 1:"))
            n2=int(input("Enter Value for node 2:"))

            ans=bt.lowestCommonAncestor(n1,n2)
            print("Lowest common ancestor for",n1,"and",n2,"is",ans.info)
        else:print("Please enter a valid command!")
        print('\n######################')