#Programmming terms using dictionary


Dict ={"Algorithm":"An algorithm is a set of instructions or rules designed to solve a definite problem. The problem can be simple like adding two numbers or a complex one, such as converting a video file from one format to another.",
       " Program":"A computer program is termed as an organized collection of instructions, which when executed perform a specific task or function. A program is processed by the central processing unit (CPU) of the computer before it is executed. An example of a program is Microsoft Word, which is a word processing application that enables users to create and edit documents. The browsers that we use are also programs created to help us browse the internet.",
       " API":"Application Programming Interface (API) is a set of rules, routines, and protocols to build software applications. APIs help in communication with third party programs or services, which can be used to build different software. Companies such as Facebook and Twitter actively use APIs to help developers gain easier access to their services.",
       "Argument":"Argument or arg is a value that is passed into a command or a function. For example, if SQR is a routine or function that returns the square of a number, then SQR(4) will return 16. Here, the value 4 is the argument. Similarly, if the edit is a function that edits a file, then in edit myfile.txt, ‘myfile.txt’ is the argument"}
print("Enter the word")
Data1=input()
print(Data1,"means",Dict[Data1])