
import dash_mantine_components as dmc
from dash import Dash, html

app = Dash(__name__)

labels = ['isFemale', 'Class', 'Age', 'Fare', 'Embarked'] 
values = [0.33536932, 0.21223314, 0.19506383, 0.18866962 ,0.06866405]

def progres_bars (labels, values, barwidth = 300):
        bars_labes = []
        bars = []
        bars_text = []
        _max = max(values)
        for label, value in dict(zip(labels, values)).items():

            bar_label = str(round(value*100,2))+'%'
            percent_width =(value/_max)
            print(percent_width)

            bars_labes.append(dmc.Text(label, className='bar-labels'))
            bars.append(dmc.Progress(value = percent_width*100, style={'width':barwidth}, className='bars'))
            bars_text.append(dmc.Text(bar_label, className='bar-text', style={'marginLeft':-((barwidth+17)-(barwidth * percent_width))}))
           
        return html.Div(
            className='barChart',
            children=[
                dmc.Text('This is a Title', className='chart-title' ),
                dmc.Group(
                    className='bar-chart-group',
                    children=[
                        
                        html.Div(bars_labes,className='labels-div' ),
                        html.Div(bars, className='bars-div'),
                        html.Div(bars_text)
                    ]
                ) 
            ]
        )
       
bars = progres_bars (labels, values)  
app.layout = html.Div(
    
bars  )


if __name__ == '__main__':
	app.run_server(
      debug = True
    )
