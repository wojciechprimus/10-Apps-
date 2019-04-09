from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.models.annotations import Title, ColumnDataSource
from bokeh.embed import components
from bokeh.resources import CDN

start=datetime.datetime(2016,3,1)
end=datetime.datetime(2016,3,25)
df=data.DataReader(name="GOOG", data_source="yahoo", start=start, end=end)

def inc_dec(c,o):
    if c > o:
        value="Increase"
    elif c < o:
        value="Decrease"
    else:
        value="Equal"
    return value

df["Status"]=[inc_dec(c,o) for c, o in zip(df.Close, df.Open)]
df["Middle"]=(df.Open + df.Close)/2
df["Height"]=abs(df.Open - df.Close)

p=figure(x_axis_type='datetime', width=1000, height=300)
hours_12=12*60*60*1000
t=Title()
t.text ="Candlestick Chart"
p.title=t
p.grid.grid_line_alpha=1
p.segment(df.index, df.High, df.index, df.Low, color="Black")
p.rect(df.index[df.Status=="Increase"], df.Middle[df.Status=="Increase"],
       hours_12, df.Height[df.Status=="Increase"], fill_color="green",line_color="black")
p.rect(df.index[df.Status=="Decrease"], df.Middle[df.Status=="Decrease"],
       hours_12, df.Height[df.Status=="Decrease"], fill_color="Red",line_color="black")

script1, div1 = components(p)
cdn_js=CDN.js_files[0]
cdn_css=CDN.css_files[0]
return render_template("plot.html",
script1=script1,
div1=div1,
cdn_js=cdn_js,
cdn_css=cdn_css)
