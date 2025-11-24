def gradingStudents(g):
    # Write your code here
    l=[]
    for i in g:
        m1=i
        r= ((((i//5)+1)*5))-i
        if((5-r)>=3):
            i=i+r
            if(i>=40):
                l.append(i)
            else:
                l.append(m1)
        else:
            l.append(i)
    return l
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
