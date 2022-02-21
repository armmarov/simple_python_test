# Instruction on how to run the program
The program consists of 3 sections which answered different questions

## Pre-requisite
Make sure to pre-install python3.5 and above to run this application (python3.7 is preferred and tested). 

## Section 1, Question 1
```
cd section1_question1
./run.sh
648
```

## Section 2, Question 1

The data structure used for this case is dictionary type. The reason is we can map user's account number to their own account for easy search in future. Hence, we set the unique account number as the key, and their own Account object as the value. As long as we know the account number, we can retrieve and perform specific operation to that particular account. Normal array will cause the O(n) searching complexity to search that particular account, and will keep increasing the searching complexity linearly if we have hundred of thousands of data in one array. Therefore, the key/value dictionary structure is more straight forward and better solution to handle this use case.


```
cd section2_question1
./run.sh
```

## Section 2, Question 2
```
cd section2_question2
./run.sh
```
