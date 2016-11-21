# fw = open('sample', 'w')
# fw.write("hello")
# fw.write("hello")
# fw.close()


# f = open("szovegfile", "w")
#  f.write("Ez az elso sor\n Ez a masodik sor\n")
#  f.write("Ez a harmadik sor\n Ez a negyedik sor\n")
#  f.close()

fr = open('sample', 'r')

text = fr.readline()

text2 = fr.readline(2)

text3 = fr.readlines(3)

print(text)
print(text2)
print(text3)

fr.close()




# 
# import requests
# req = requests.get('http://google.com')
# req.status_code


# class Diamond():
#     def __init__(self, depth):
#         self.depth = depth
#
#     def draw(self):
#         self.triangle(self.depth, 'up')
#         self.triangle(self.depth, 'down')
#
#     def triangle(self, depth, direction):
#         if direction == 'up':
#             buildRange = range(1,depth)
#         else:
#             buildRange = range(depth,0,-1)
#
#         for line in buildRange:
#             padding = depth - line
#             print( ' ' * padding + '*' * ( line * 2 - 1 ) )
#
#
# myDiamond = Diamond(11)
# myDiamond.draw()
