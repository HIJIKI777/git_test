# -*- coding: utf-8 -*-
#↑これを入力することで日本語でのコメントアウトが可能になる

# 何かを出力する時は print()
print('Hello, world!')
print(1 + 2)

# 入力と条件分岐は以下のように
a_str = input('Enter a value ')
b_str = input('Enter b value ')

a = int(a_str)
b = int(b_str)

if a > b:
    print('a is larger than b')
elif a < b:
    print('a is smaller than b')
else:
    print('a = b')

# 繰り返し処理を行う時は以下のように

c = int(input('Enter the count number '))

for i in range(0,c):
    print "i = ", i

i = 0
while i < 5:
    print "i = ", i
    i = i + 1

# リストという配列みたいな奴は以下のように利用できる(これ便利すぎだろ・・・)

list_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# insert() : インデックスを指定して挿入
list_x.insert(2,10)
print "list_x.insert(2,10) : ", list_x
# remove() : リスト中に指定した引数の値があったら削除
list_x.remove(3)
print "list_x.remove(3) : ", list_x
# pop() : リストの末尾を削除。引数を指定すると、そのインデックスの要素が削除される。
list_x.pop()
print "list_x.pop() : ", list_x
# index() : 引数で指定した値のインデックスを取得
print "list_x.index(10) : ", list_x.index(10)
# インデックスを指定しての値の変更
list_x[1] = 100
print "list_x[1] = 100 : ", list_x
# len() リストのd長さを取得
print "list_x length : ", len(list_x)
# append() : 配列へ追加したい要素を引数として指定する

#自作関数は以下のようにして利用できる

# 引数なしの関数
def print_hello():
    print "hello"
# 引数ありの関数
# 戻り値はreturnで返す
def add( d, e ):
    return d + e

print_hello()
print add(100,300)
