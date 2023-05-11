from collections import defaultdict

import numpy as np
import pandas as pd
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.globals import SymbolType, ThemeType
import pandas as pd
pd.set_option('display.max_columns', None)
data = pd.read_csv('jieguo.csv')
print(data.head(5))
result = np.vstack([data['experience'], data['job_mean_salary']]).T.tolist()
result.sort(key=lambda x: x[0])
groups = defaultdict(list)
colors = ['#5793F3', '#F44336', '#4CAF50', '#FFC107', '#9E9E9E', '#673AB7', '#FF4081', '#00BCD4']
for x, y in result:
    groups[x].append(y)
scatter = Scatter()
for index, (key, values) in enumerate(groups.items()):
    scatter.add_xaxis([key] * len(values))
    scatter.add_yaxis(str(key), values, label_opts=opts.LabelOpts(is_show=False), symbol_size=10, itemstyle_opts=opts.ItemStyleOpts(color=colors[index]))

scatter.set_global_opts(
    xaxis_opts=opts.AxisOpts(type_='value',name='工作经验',name_location='middle'),
    yaxis_opts=opts.AxisOpts(type_='value',name='平均工资',name_location='middle'),
    title_opts=opts.TitleOpts(title='聚类分布'),
)

scatter.render('可视化结果/聚类分布.html')







# data.info()
# data.describe()
# data_groupy = data.groupby(['类别']).count()['experience']
# c = (
#     Bar()
#     .add_xaxis(data_groupy.index.tolist())
#     .add_yaxis("", data_groupy.values.tolist())
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="各个类别数量"),
#         toolbox_opts=opts.ToolboxOpts(),
#         legend_opts=opts.LegendOpts(is_show=False),
#     )
#     .render("可视化结果/kmeans聚类数量.html")
# )


# def kmeans_0():
#     data0 = data.loc[data['类别'] == 0]
#     data0_d = data0.groupby(['job_type']).count()['experience']
#
#     c2 = (
#         Bar()
#         .add_xaxis(data0_d.index.tolist())
#         .add_yaxis("", data0_d.values.tolist())
#         .set_global_opts(
#             title_opts=opts.TitleOpts(title="0类各岗位数量"),
#             toolbox_opts=opts.ToolboxOpts(),
#             legend_opts=opts.LegendOpts(is_show=False),
#         )
#         .render("可视化结果/kmeans聚类0数量.html")
#     )
#
#
# def kmeans_1():
#     data0 = data.loc[data['类别'] == 1]
#     data0_d = data0.groupby(['job_type']).count()['experience']
#     print(data0.describe())
#     c2 = (
#         Bar()
#         .add_xaxis(data0_d.index.tolist())
#         .add_yaxis("", data0_d.values.tolist())
#         .set_global_opts(
#             title_opts=opts.TitleOpts(title="1类各岗位数量"),
#             toolbox_opts=opts.ToolboxOpts(),
#             legend_opts=opts.LegendOpts(is_show=False),
#         )
#         .render("可视化结果/kmeans聚类1数量.html")
#     )
#
#
# def kmeans_2():
#     data0 = data.loc[data['类别'] == 2]
#     data0_d = data0.groupby(['job_type']).count()['experience']
#     print(data0.describe())
#     c2 = (
#         Bar()
#         .add_xaxis(data0_d.index.tolist())
#         .add_yaxis("", data0_d.values.tolist())
#         .set_global_opts(
#             title_opts=opts.TitleOpts(title="2类各岗位数量"),
#             toolbox_opts=opts.ToolboxOpts(),
#             legend_opts=opts.LegendOpts(is_show=False),
#         )
#         .render("可视化结果/kmeans聚类2数量.html")
#     )
#
#
# def kmeans_3():
#     data0 = data.loc[data['类别'] == 3]
#     data0_d = data0.groupby(['job_type']).count()['experience']
#     print(data0.describe())
#     c2 = (
#         Bar()
#         .add_xaxis(data0_d.index.tolist())
#         .add_yaxis("", data0_d.values.tolist())
#         .set_global_opts(
#             title_opts=opts.TitleOpts(title="3类各岗位数量"),
#             toolbox_opts=opts.ToolboxOpts(),
#             legend_opts=opts.LegendOpts(is_show=False),
#         )
#         .render("可视化结果/kmeans聚类3数量.html")
#     )
# if __name__ == '__main__':
#     kmeans_0()
#     kmeans_1()
#     kmeans_2()
#     kmeans_3()