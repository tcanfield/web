from models import Reading

for x in range(0, 364):
	f = open(str(x), "r")
	verses = f.getvalue()

	reading = Reading(day= x, verse= "verses")
	reading.save()
