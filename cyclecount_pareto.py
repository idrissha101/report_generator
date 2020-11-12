import pandas as pd 
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import os

def pareto(filename):
	today = date.today()

	x = []

	df = pd.read_csv(filename)
	df = df.sort_values(by=['fixtureId', 'timeStamp'], ascending=False)
	df = df.drop_duplicates(subset=['fixtureId'], keep='first')
	df.drop(columns=['timeStamp', 'fixtureId'])
	df = df.sort_values(by='cycleCount', ascending=False)
	df["cumpercentage"] = 100 * df["cycleCount"].cumsum() / df["cycleCount"].sum()

	if len(df) > 10:
		df = df.head(10)

	fig, ax = plt.subplots()
	ax.bar(df["fixtureName"], df["cycleCount"], color="C0")
	ax.set_xlabel('Fixture Name')
	ax.set_ylabel('Probe Cycle Count')
	ax2 = ax.twinx()
	ax2.plot(df["fixtureName"], df["cumpercentage"], color="C1", marker="D", ms=7)
	ax2.set_ylim(0, 100)
	ax2.yaxis.set_major_formatter(PercentFormatter())
	ax2.set_ylabel('% Pareto')

	ax.tick_params(axis="y", colors="C0")
	ax2.tick_params(axis="y", colors="C1")

	x = [20000] * len(df)
	ax.plot(df["fixtureName"], x, color="r")
	x = [40000] * len(df)
	ax.plot(df["fixtureName"], x, color="k")
	ax.legend(['20k cycle count - Purchase new probes', '40k cycle count - Reprobing'])

	plt.title("Pareto Plot of Probe Cycle Count")
	
	if not os.path.exists('pareto'):
		os.makedirs('pareto')

	fig = plt.gcf()

	fig.set_size_inches(12.8, 8)

	plt.savefig("pareto\\" + str(today) + ".pdf", dpi=300)

	while True:
		plt.show(block=False)
		i = input("\n\nEnter text or Enter to quit... ")
		if not i:
			break

	