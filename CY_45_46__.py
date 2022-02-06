import winsound
f=500
duration=100
#winsound.Beep(f,duration)
for i in range(0,5):
    winsound.Beep(f,duration)
    f+=100
    duration+=50
# print("Playing the file 'abc.wav'")
# winsound.PlaySound('abc.wav',winsound.SND_FILENAME)
# winsound.PlaySound("SystemQuestion",winsound.SND_ALIAS)
