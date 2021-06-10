
'''
Problem 1:Password Validation

Create a program that checks whether given strings are valid passwords or not.

Input Format:

The first line contains a natural number n. The next n lines contain the strings.

Output Format:

For each input print 'Valid' if the given string is a valid password. If not, then print 'Invalid' to the console.

A valid password:

1)Must have a length between 8 to 20 characters
2)Must begin with a lowercase alphabet.
3)Must not contain any spaces.
4)Must contain atleast one number and one uppercase character.

Sample Input 1:
4
abcd@ABCD
ganesh_S1
slapStick_090
my Password

Sample Output 1:
Invalid
Valid
Valid
Invalid

Explanation:
Input 1 is invalid because it does not contain atleast one number
Input 4 is invalid because it contains a space
'''

'''
Problem 2: Rishil's Gift

Rishil has received the grades for multiple course examinations recently. It's his birthday
next week, and his father has promised him to buy him a gift. However, here is the catch.
The gift that Rishil will receive will depend upon his result.

Input Format:
The first line contains a number n which signifies the number of courses Rishil has appeared in.
The next n lines follow a series of inputs for each course. For each ith input 0<i<=n 

The first line contains two numbers j,k separated by space indicating the number of subjects in the given 
course and the number of subjects Rishil has flunked in that course respectively. The next line 
contains j space separated numbers indicating individual marks of each subject in the given course.

Output Format:

Rishil has performed well in a course if:

The number of subjects cleared by him > The number of subjects he flunked in

and,

The average of all subjects is greater than 55.

For each course if Rishil has performed well, print "Good" to the console.
Or else, print "Not Good"

In the end if the number of "Good" results are greater than the number of "Bad" results,
Rishil gets a "Car" as a gift. If not he gets a "Cycle".

Hence print the gift that Rishil will get for his birthday.

Sample Input 1:
4
6 2
64 71 83 64 39 33 59.0
5 0
77 83 91 92 51
6 3
89 95 96 39 38 39
2 0
77 75

Sample Output 1:
Good
Good
Not Good
Good
Car

Explanation:
Outputs 1,2,4 are "Good" as the number of subjects Rishil cleared is greater than the number
of subjects he flunked in, and the average marks of subjects in each of the courses 1,2,4 is 
greater than 55.

Output 3 is "Not Good" because the number of subjects Rishil failed in is 3 which is not greater
the number of subjects he passed(6-3=3).

Rishil gets a "Car", as he performed well in 3 subjects and poorly in 1 subject. (3>1)
'''
'''
Problem 3: Christmas Gift

Santa Clause wishes to donate a certain amount of money to a group of orphanages based on how
many donations they have received in the past years.

Input Format:
THe first line contains a number n indicating the number of orphanages he will be visiting this year.
The next n lines follow. For each ith input , 0<i<=n, 

the first line will consist of two numbers separated by space indicating the number of 
active years of the orphanage and the "Target Number" of that orphanage
respectively. The next line contains the number of children residing in that orphanage.

Output Format:

For each orphanage, print the amount of gifts Santa will be gifting to the orphanage.

The number of money worth of gifts is given by this formula:

M = (Target Number * Number of children)/Number of Active Years 

Print the number of gifts(floor of integer) ie M/010 for each Orphanage

Sample Input 1:

3
6 1000
500
3 20000
600
8 100000
550

Sample Output 1
83
4000
6875
'''

'''
Problem 4:Coronavirus Conques
'''