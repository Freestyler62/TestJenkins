print("Running test code for job2")
f = open("TestResult.txt", "w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
f.close() 
