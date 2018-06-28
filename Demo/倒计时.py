import time,subprocess

timeLeft=5

resourcePath="C:\\Users\\ca_nc\\Music\\虾米音乐\\Glen Hansard-When Your Mind's Made Up.mp3"
# resourcePath="D:\\Workspaces\\Python\\Demo\\myProgramLog.txt"

playerPath="D:\Program Files (x86)\Tencent\QQPlayer\QQPlayer.exe"

while timeLeft>0:
	print(timeLeft)
	time.sleep(1)
	timeLeft=timeLeft-1

# subprocess.Popen(['start',resourcePath],shell=True)
subprocess.Popen([playerPath,resourcePath])