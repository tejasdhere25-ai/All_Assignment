#percentage of subject

a=int(input("Enter a marks of OS"))
b=int(input("Enter a marks of DS"))
c=int(input("Enter a marks of DELD"))
d=int(input("Enter a marks of AI"))
e=int(input("Enter a marks of UHV"))

total=a+b+c+d+e
percentage=total/5
print("total marks:",total)
print("percentage:",percentage,"%")

if  percentage >= 90:
	print("Grade: 1st class")
elif percentage >=75:
	print("Grade: 2nd class")
elif percentage >=50:
	print("Grade: 3rd class")
else:
	print("Otherwise student is failed")