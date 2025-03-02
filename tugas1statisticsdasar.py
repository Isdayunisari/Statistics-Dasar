"""
nama        :isda yunisari
nim         :D0424309
kelas       :sistem informasi
"""
import statistics

dataMean = [10,20,30,40]
mean = statistics.mean(dataMean)

dataMedian=[30,40,50,60]
median = statistics.median(dataMedian )

dataModus=[100,200,300,400]
modus = statistics.mode(dataModus)


print(f"data untuk mecari mean: {dataMean}")
print(f"mean: {mean}")

print(f"data untuk mecari median: {dataMedian}")
print(f"median: {median}")

print(f"data untuk mecari modus: {dataModus}")
print(f"modus: {modus}")
