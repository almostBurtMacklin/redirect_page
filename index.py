import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.A("I've moved! I'm now using AWS Beanstalk. Click here to see my site!", href='http://baseballwebapp.us-east-2.elasticbeanstalk.com/home')
])

if __name__ == '__main__':
    app.run_server(debug=True)
