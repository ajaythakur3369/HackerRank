'''
Task:- 
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:
A Student class constructor, which has 4 parameters:
 1. A string, firstName.
 2. A string, lastName.
 3. An integer, idNumber.
 4. An integer array (or vector) of test scores, scores.
A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:
Grading.

  Grading Scale 
Letter  Average (a) 
O       90 ≤ a ≤ 100 
E       80 ≤ a < 90
A       70 ≤ a < 80
P       55 ≤ a < 70 
D       40 ≤ a < 55
T       a < 40
'''

'''
Input Format:- 
The locked stub code in the editor reads the input and calls the Student class constructor with the necessary arguments. It also calls the calculate method which takes no arguments.

The first line contains firstName, lastName, and idNumber, separated by a space. The second line contains the number of test scores. The third line of space-separated integers describes scores.
'''

'''
Constraints:- 
 1 ≤ length of firstName, length of lastName ≤ 10
 length of idNumber ≡ 7 
 0 ≤ score ≤ 100 
'''

'''
Output Format:- 
Output is handled by the locked stub code. Your output will be correct if your Student class constructor and calculate() method are properly implemented.
'''

'''
Sample Input:-
Heraldo Memelli 8135627
2
100 80
'''

'''
Sample Output
 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O
'''

'''
Explanation:- 
This student had 2 scores to average: 100 and 80. The student's average grade is (100+80)/2 = 90. An average grade of 90 corresponds to the letter grade O, so the calculate() method should return the character'O'.
'''

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, testScores):
        super().__init__(firstName, lastName, idNumber)
        self.testScores = testScores

    def calculate(self):
        total = 0

        for testScore in self.testScores:
            total += testScore

        avg = total / len(self.testScores)

        if 90 <= avg <= 100:
            return 'O'
        if 80 <= avg < 90:
            return 'E'
        if 70 <= avg < 80:
            return 'A'
        if 55 <= avg < 70:
            return 'P'
        if 40 <= avg < 55:
            return 'D'
        return 'T'

'''       
Input (stdin):
Heraldo Memelli 8135627
2
100 80
'''

'''
Expected Output:- 
Name: Memelli, Heraldo
ID: 8135627
Grade: O
'''











