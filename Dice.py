import random
import plotly.express as px 
import plotly.figure_factory as ff 
import statistics
import plotly.graph_objects as go 
diceresult = []
count = []
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceresult.append(dice1+dice2)
    count.append(i)
#print(count)
#fig = px.bar(x = diceresult , y = count)
mean = statistics.mean(diceresult)
median = statistics.median(diceresult)
mode = statistics.mode(diceresult)
standarddeviation = statistics.stdev(diceresult)
print(mean,median,mode,standarddeviation)
fsds,fsde = mean-standarddeviation , mean+standarddeviation
ssds,ssde  = mean-(2*standarddeviation) , mean+(2*standarddeviation)
tsds,tsde = mean-(3*standarddeviation) , mean+(3*standarddeviation)
fig = ff.create_distplot([diceresult],['result'],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = 'lines',name = 'mean'))
fig.add_trace(go.Scatter(x = [fsds,fsds],y = [0,0.17],mode = 'lines',name = 'standarddeviation1'))
fig.add_trace(go.Scatter(x = [fsde,fsde],y = [0,0.17],mode = 'lines',name = 'standarddeviation1'))
fig.add_trace(go.Scatter(x = [ssds,ssds],y = [0,0.17],mode = 'lines',name = 'standarddeviatoion2'))
fig.add_trace(go.Scatter(x = [ssde,ssde],y = [0,0.17],mode = 'lines',name = 'standarddeviatio2'))
fig.add_trace(go.Scatter(x = [tsds,tsds],y = [0,0.17],mode = 'lines',name = 'standarddeviation3'))
fig.add_trace(go.Scatter(x = [tsde,tsde],y = [0,0.17],mode = 'lines',name = 'standarddeviation3'))
fig.show()
listofdatawithinstandarddeviation1 = [result for result in diceresult if result>fsds and  result<fsde]
listofdatawithinstandarddeviation2 = [result for result in diceresult if result>ssds and  result<ssde]
listofdatawithinstandarddeviation3 = [result for result in diceresult if result>tsds and  result<tsde]
print((len(listofdatawithinstandarddeviation1)*100/len(diceresult)))
print((len(listofdatawithinstandarddeviation2)*100/len(diceresult)))
print((len(listofdatawithinstandarddeviation3)*100/len(diceresult)))

