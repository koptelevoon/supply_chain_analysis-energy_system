import matplotlib.pyplot as plt

def createLineChart(x, y, labelx, labely, title):
    plt.figure(figsize=(10, 6), dpi=100)
    plt.plot(x, y)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(title)
    plt.fill_between(x, y)
    plt.gcf().autofmt_xdate()
    plt.show()

def createlineChart1500(x, y, labelx, labely, title):
    plt.figure(figsize=(10, 6), dpi=100)
    plt.plot(x, y)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(title)
    plt.fill_between(x, y)
    plt.gcf().autofmt_xdate()
    ax = plt.gca()
    ax.set_ylim([0, 1500])
    plt.show()

def createlineChart3000(x, y, labelx, labely, title):
    plt.figure(figsize=(10, 6), dpi=100)
    plt.plot(x, y)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(title)
    plt.fill_between(x, y)
    plt.gcf().autofmt_xdate()
    ax = plt.gca()
    ax.set_ylim([0, 3000])
    plt.show()

def createlineChart5000(x, y, labelx, labely, title):
    plt.figure(figsize=(10, 6), dpi=100)
    plt.plot(x, y)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(title)
    plt.fill_between(x, y)
    plt.gcf().autofmt_xdate()
    ax = plt.gca()
    ax.set_ylim([0, 5000])
    plt.show()

def createlineChart13000(x, y, labelx, labely, title):
    plt.figure(figsize=(10, 6), dpi=100)
    plt.plot(x, y)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(title)
    plt.fill_between(x, y)
    plt.gcf().autofmt_xdate()
    ax = plt.gca()
    ax.set_ylim([0, 13000])
    plt.show()

def createlineChart50000(x, y, labelx, labely, title):
    plt.figure(figsize=(10, 6), dpi=100)
    plt.plot(x, y)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(title)
    plt.fill_between(x, y)
    plt.gcf().autofmt_xdate()
    ax = plt.gca()
    ax.set_ylim([0, 50000])
    plt.show()

def createLineChartInjection(x, a, b, c, labelx, labely, title):
    plt.figure(figsize=(10, 6), dpi=100)
    plt.plot(x, a, label="3% injection")
    plt.plot(x, b, label="10% injection")
    plt.plot(x, c, label="20% injection")
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(title)
    plt.fill_between(x, a)
    plt.fill_between(a, b)
    plt.fill_between(b, c)
    plt.gcf().autofmt_xdate()
    plt.show()

def createLineChart70(x, y, labelx, labely, title):
    plt.figure(figsize=(10, 6), dpi=100)
    plt.plot(x, y)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(title)
    plt.fill_between(x, y)
    plt.gcf().autofmt_xdate()
    ax = plt.gca()
    ax.set_ylim([0, 70])
    plt.show()

def createLineChart160(x, y, labelx, labely, title):
    plt.figure(figsize=(10, 6), dpi=100)
    plt.plot(x, y)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(title)
    plt.fill_between(x, y)
    plt.gcf().autofmt_xdate()
    ax = plt.gca()
    ax.set_ylim([0, 160])
    plt.show()

def createLineChart900(x, y, labelx, labely, title):
    plt.figure(figsize=(10, 6), dpi=100)
    plt.plot(x, y, color="green")
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(title)
    plt.fill_between(x, y, color="green")
    plt.gcf().autofmt_xdate()
    ax = plt.gca()
    ax.set_ylim([0, 900])
    plt.show()

def createLineChart1200(x, y, labelx, labely, title):
    plt.figure(figsize=(10, 6), dpi=100)
    plt.plot(x, y)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(title)
    plt.fill_between(x, y)
    plt.gcf().autofmt_xdate()
    ax = plt.gca()
    ax.set_ylim([0, 1200])
    plt.show()

def createLineChart5000(x, y, labelx, labely, title):
    plt.figure(figsize=(10, 6), dpi=100)
    plt.plot(x, y)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(title)
    plt.fill_between(x, y)
    plt.gcf().autofmt_xdate()
    ax = plt.gca()
    ax.set_ylim([0, 5000])
    plt.show()

def createBarChart(dates, dir_inj, legend1):
    fig, ax = plt.subplots()

    ax.bar(dates, dir_inj, label=legend1)

    ax.set_ylabel("Amount injected (kg)")
    ax.set_title("Amount injected over time (kg)")
    ax.legend()

    plt.gcf().autofmt_xdate()

    plt.show()

def createBarChart70(dates, dir_inj, legend1):
    fig, ax = plt.subplots()

    ax.bar(dates, dir_inj, label=legend1)

    ax.set_ylabel("Amount injected (kg)")
    ax.set_title("Amount injected over time (kg)")
    ax.legend()

    plt.gcf().autofmt_xdate()

    ax = plt.gca()
    ax.set_ylim([0, 70])

    plt.show()

def createStackedBarChart(dates, dir_inj, ind_inj, legend1, legend2):
    fig, ax = plt.subplots()

    ax.bar(dates, dir_inj, label = legend1)
    ax.bar(dates, ind_inj, bottom=dir_inj, label=legend2)

    ax.set_ylabel("Amount injected (kg)")
    ax.set_title("Amount injected over time (kg)")
    ax.legend()

    plt.show()

