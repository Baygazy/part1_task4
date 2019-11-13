#Make sure to un-comment the function line below when you are
#done.
#Remember to name your function correctly.
# WRITE YOUR CODE HERE...
def last_letter(bgz): return bgz[-1]   #СЛАЙС, СРЕЗ последний элемент в строке
#DO NOT remove lines below here,
#this is designed to test your code.
def test_last_letter():
 assert last_letter('hello!') == '!'
 assert last_letter('banana') == 'a'
 assert last_letter('8') == '8'
 assert last_letter('funnyguys') == 's'
 assert last_letter('101') == '1'
 print("YOUR CODE IS CORRECT!")
#test your code by un-commenting the line(s) below
test_last_letter()