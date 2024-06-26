'''
Task:- 
Write a single generic function named printArray; this function must take an array of generic elements as a parameter (the exception to this is C++, which takes a vector). The locked Solution class in your editor tests your function.
'''

'''
Input Format:- 
The locked Solution class in your editor will pass different types of arrays to your printArray function.
'''

'''
Constraints:- 
 You must have exactly 1 function named printArray.
'''

'''
Output Format:- 
Your printArray function should print each element of its generic array parameter on a new line.
'''

using namespace std;

'''
Name: printArray
Print each element of the generic vector on a new line. Do not return anything.
@param A generic vector
Write your code here
'''

template<typename Element>

void printArray(vector<Element> arr) {
    for (int i = 0; i < arr.size(); i++)
        cout << arr[i] << endl;
}

int main() {
	int n;
	
	cin >> n;
	vector<int> int_vector(n);
	for (int i = 0; i < n; i++) {
		int value;
		cin >> value;
		int_vector[i] = value;
	}
	
	cin >> n;
	vector<string> string_vector(n);
	for (int i = 0; i < n; i++) {
		string value;
		cin >> value;
		string_vector[i] = value;
	}

	printArray<int>(int_vector);
	printArray<string>(string_vector);

	return 0;
}

'''
Input (stdin):- 
3
1
2
3
2
Hello
World
'''

'''
Expected Output:- 
1
2
3
Hello
World
'''
