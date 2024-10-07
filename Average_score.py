grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades)
students = {'Aram','Boris','Kamala','Stars','Zorro'}
print(students)
average_score = ([(5+3+3+5+4)/5],[(2+2+2+3)/4],
[(4+5+5+2)/4],[(4+4+3)/3],[(5+5+5+4+5)/5])
print(average_score)
#numbers = ([5, 3, 3, 5, 4], [2,2,2,3], [4,5,5,2],[4,4,3],[5,5,5,4,5])
#average = sum(numbers) / len(numbers)
#print(average)
#import statistics
#numbers = [5, 3, 3, 5, 4]
#average = statistics.mean(numbers)
#print(average)
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Aram','Boris','Kamala','Stars','Zorro'}
students = sorted(students)
c = (sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]),
     sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]),
     sum(grades[4])/len(grades[4]))
klass = {students[0]: c[0], students[1]: c[1], students[2]: c[2], students[3]: c[3], students[4]: c[4]}
print(klass)
