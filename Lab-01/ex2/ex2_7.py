print("nhập các dòng văn bản (nhập 'done' để kết thúc):")
line = []
while True:
    input_line = input()
    if input_line == 'done':
        break
    line.append(input_line)
#chuyên các dòng thành chữ in hoa và in ra màn hình
print("Các dòng văn bản in hoa:")
for l in line:
    print(l.upper())