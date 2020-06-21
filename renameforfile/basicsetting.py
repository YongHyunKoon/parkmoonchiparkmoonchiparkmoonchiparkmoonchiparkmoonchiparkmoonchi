import os


studentid = input('학번을 입력하세요. : ')
print('학번 :'+studentid+'')

name = input('이름을 입력하세요. : ')
print('이름 :'+name+'')

full = studentid+'-'+name
print(full)
die = os.getcwd()
# print(die)
put = ['/input','/output']

for x in range(0,2):
	# print(x)
	print(die+put[x]+' 설정완료')
	try:
	    if not(os.path.isdir(die+put[x])):
	    	os.makedirs(os.path.join(die+put[x]))
	except OSError as e:
	    if e.errno != errno.EEXIST:
	        print("디렉토리 설정 실패")
	        raise
	pass

print('사용법 : input폴더에 과제를 넣어주고 run.py를 실행해 주세요.')

