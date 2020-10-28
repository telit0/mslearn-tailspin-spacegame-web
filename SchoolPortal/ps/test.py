import subprocess;
process=subprocess.Popen(["powershell","C:\\ps\\test.ps1"],stdout=subprocess.PIPE)
result=process.communicate()[0]
print (result)