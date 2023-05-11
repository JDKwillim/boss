import pandas as pd
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.globals import SymbolType, ThemeType


def data_clean():
    df = pd.read_csv('bossjob.csv')
    # print(df.head(5))
    print('数据行列为:',df.shape)
    df.info()
    df['job_education'].fillna('学历不限', inplace=True)
    df['job_experience'].fillna('学历不限', inplace=True)
    # df.info()
    print(df.duplicated())
    data=df.duplicated(keep='first').sum()
    print("数据重复值个为:",data)
    df['job_mean_salary'] = round((df['job_low_salary'] + df['job_high_salary']) / 2, 2)
    # print(df['job_mean_salary'])
    # df.to_csv('job_clean.csv')


df = pd.read_csv('job_clean.csv')


# print(df.head())
def bar():
    df_job_type = df.groupby(['job_type']).count()['job_title']
    df_job_type_x = df_job_type.index.tolist()
    df_job_type_y = df_job_type.values.tolist()
    # print(df_job_type_x)
    # print(df_job_type_y)
    c = (
        Bar()
        .add_xaxis(df_job_type_x)
        .add_yaxis("", df_job_type_y)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="各个岗位类型占比"),
            datazoom_opts=opts.DataZoomOpts(),
        )
        .render("可视化结果/各个岗位类型占比.html")
    )


def job_mean_bar():
    df_job = df.groupby(['job_type'])['job_mean_salary'].mean().astype(int)
    c = (
        Bar()
        .add_xaxis(df_job.index.tolist())
        .add_yaxis("", df_job.values.tolist())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="各个岗位类型占比"),
            datazoom_opts=opts.DataZoomOpts(),
        )
        .render("可视化结果/各个岗位平均价格.html")
    )


def job_education_pie():
    df_education = df.groupby(['job_education']).count()['job_title']
    c = (
        Pie()
        .add("", [list(z) for z in zip(df_education.index.tolist(), df_education.values.tolist())])
        .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
        .set_global_opts(title_opts=opts.TitleOpts(title="学历要求占比"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        .render("可视化结果/学历要求.html")
    )


def job_education_salary():
    df_education_max = df.groupby(['job_education'])['job_high_salary'].max()
    x = df_education_max.index.tolist()
    max_y = df_education_max.values.tolist()
    df_education_min = df.groupby(['job_education'])['job_low_salary'].min()
    min_y = df_education_min.values.tolist()
    df_education_mean = df.groupby(['job_education'])['job_mean_salary'].mean().astype(int)
    mean_y = df_education_mean.values.tolist()
    c = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("最大值", max_y, gap="0%")
        .add_yaxis("最小值", min_y, gap="0%")
        .add_yaxis("平均值", mean_y, gap="0%")
        .set_global_opts(title_opts=opts.TitleOpts(title="各个学历水平工资"))
        .render("可视化结果/各个学历水平工资.html")
    )


def company():
    list = ['京东', '美团', '腾讯', '百度', '字节跳动', '饿了么', '滴滴', '华为', '蚂蚁金服', '阿里']
    list2 = []
    for cam in list:
        data = df[df['job_company'].str.contains(cam)]['job_mean_salary'].mean().astype(int)
        list2.append(data)
    c = (
        Bar()
        .add_xaxis(list)
        .add_yaxis("平均工资", list2)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="大厂平均工资"),
            yaxis_opts=opts.AxisOpts(name="单位元"),
            xaxis_opts=opts.AxisOpts(name="公司名称"),
        )
        .render("可视化结果/大厂平均工资.html")
    )


def city():
    data = df.groupby(['company_city']).count()['job_mean_salary']
    c = (
        BMap()
        .add_schema(baidu_ak="FAKE_AK", center=[120.13066322374, 30.240018034923])
        .add(
            "map",
            [list(z) for z in zip(data.index.tolist(), data.values.tolist())],
            label_opts=opts.LabelOpts(formatter="{b}"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="主要城市招聘数量"))
        .render("可视化结果/主要城市招聘数量.html")
    )


def city_salary():
    min_salary=df.groupby(['company_city'])['job_low_salary'].min()
    max_salary=df.groupby(['company_city'])['job_high_salary'].max()
    print(min_salary)
    print(max_salary)
    x=max_salary.index.tolist()

    c = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("最大值", max_salary.values.tolist(), gap="0%")
        .add_yaxis("最小值", min_salary.values.tolist(), gap="0%")
        .set_global_opts(title_opts=opts.TitleOpts(title="各个城市工资"))
        .render("可视化结果/各个城市水平工资.html")
    )


if __name__ == '__main__':
    data_clean()
    # city_salary()
    # city()
