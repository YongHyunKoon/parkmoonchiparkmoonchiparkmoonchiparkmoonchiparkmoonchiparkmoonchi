import os


info ={}
die = os.getcwd()
f = open(die+"/info.txt",'w')

def setting():
	studentid = input('학번을 입력하세요. : ')
	print('학번 :'+studentid+'')
	info['studentid'] = studentid
	f.write(info['studentid']+'\n')
	name = input('이름을 입력하세요. : ')
	print('이름 :'+name+'')
	info['name'] = name
	f.write(info['name']+'\n')
	

def makedir():

	for x in range(2,4):
		# print(x)
		info[str(x)] = str(x)
		if info[str(x)] == '2':
			info[str(x)] = input('input 폴더 명을 입력하세요 . :')
			try:
				if not(os.path.isdir(die+'/'+info[str(x)])):
					os.makedirs(os.path.join(die+'/'+info[str(x)]))
					f.write(die+'/'+info[str(x)]+'\n')
					print(die+'/'+info[str(x)]+' 설정완료')
			except OSError as e:
				if e.errno != errno.EEXIST:
					print("디렉토리 설정 실패")
				else:
					print('같은 이름의 폴더가 존재하는 것 같으므로, 뒤에(1)을 붙이겠습니다.')
					info[str(x)] = info[str(x)]+'(1)'
					os.makedirs(os.path.join(die+'/'+info[str(x)]))
					f.write(die+'/'+info[str(x)]+'\n')
					print(die+'/'+info[str(x)]+' 설정완료')
		else:
			info[str(x)] = input('output 폴더 명을 입력하세요 . :')
			try:
				if not(os.path.isdir(die+'/'+info[str(x)])):
					os.makedirs(os.path.join(die+'/'+info[str(x)]))
					f.write(die+'/'+info[str(x)])
					print(die+'/'+info[str(x)]+' 설정완료')
				else:
					print('같은 이름의 폴더가 존재하는 것 같으므로, 뒤에(1)을 붙이겠습니다.')
					info[str(x)] = info[str(x)]+'(1)'
					os.makedirs(os.path.join(die+'/'+info[str(x)]))
					f.write(die+'/'+info[str(x)])
					print(die+'/'+info[str(x)]+' 설정완료')
			except OSError as e:
				if e.errno != errno.EEXIST:
					print("디렉토리 설정 실패")
	print('사용법 : input폴더에 과제를 넣어주고 run.py를 실행해 주세요.')

def remove():
	ans = input('초기화를 원하시면 1, 그렇지 않으면 2를 누르십시오.')
	if ans == 1:
		os.remove(die+'/info.txt')
	else:
		print('ㅄ')
setting()
makedir()
print(die)
print(info)
f.close()

