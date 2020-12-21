


# Let's rename the columns so that they make sense. We can use rename() method by passing in a dictionary of old and new names as follows:
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.columns

# We will also add a 'Total' column that sums up the total immigrants by country over the entire period 1980 - 2013, as follows:
df_can['Total'] = df_can.sum(axis=1)



'''

There are two ways to filter on a column name:

Method 1: Quick and easy, but only works if the column name does NOT have spaces or special characters.

    df.column_name 
        (returns series)
Method 2: More robust, and can filter on multiple columns.

    df['column']  
        (returns series)
    df[['column 1', 'column 2']] 
        (returns dataframe)
'''

'''
There are main 3 ways to select rows:

    df.loc[label]        
        #filters by the labels of the index/column
    df.iloc[index]       
        #filters by the positions of the index/column
'''
df_can.set_index('Country', inplace=True)
# tip: The opposite of set is reset. So to reset the index, we can use df_can.reset_index()



# 1. the full row data (all columns)
print(df_can.loc['Japan'])

# alternate methods
print(df_can.iloc[87])
print(df_can[df_can.index == 'Japan'].T.squeeze())

# 2. for year 2013
print(df_can.loc['Japan', 2013])

# alternate method
print(df_can.iloc[87, 36]) # year 2013 is the last column, with a positional index of 36

# 3. for years 1980 to 1985
print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]])
print(df_can.iloc[87, [3, 4, 5, 6, 7, 8]])



# 1. create the condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)
# 2. pass this condition into the dataFrame
df_can[condition]
# we can pass mutliple criteria in the same line. 
# let's filter for AreaNAme = Asia and RegName = Southern Asia

df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]

# note: When using 'and' and 'or' operators, pandas requires we use '&' and '|' instead of 'and' and 'or'
# don't forget to enclose the two conditions in parentheses









# Visualiazation


import matplotlib.pyplot as plt

# plotting at position(5, 5), o
plt.plot(5, 5, 'o')
plt.show()

#matplotlib notebook for editing existing figure 

# plotting using padas 
india_chine_df.plot(kind="line")
india_chine_df['India'].plot(kind='hist')

df_can.head()

years=list(map(str, range(1980, 2014)))
df_canada.loc['Haiti', years].plot(kind='line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()


# to change the style
print(plt.style.available)
mpl.style.use(['ggplot']) # optional: for ggplot-like style


haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
haiti.head()
haiti.plot()


# alternate
haiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show() # need this line to show the updates made to the figure




# We can clearly notice how number of immigrants from Haiti spiked up from 2010 as 
# Canada stepped up its efforts to accept refugees from Haiti. Let's annotate this spike in the plot by using the plt.text() method.
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

# annotate the 2010 Earthquake. 
# syntax: plt.text(x, y, label)
plt.text(2000, 6000, '2010 Earthquake') # see note below

plt.show() 


### type your answer here
df_can.sort_values(by='Total', ascending='False', axis=0, inplace=True)

df_top5 = df_can.head(5)
df_top5 = df_top5[years].transpose()

# print(df_top5)

df_top5.index = df_top5.index.map(int)
df_top5.plot(kind='line', figsize=(10,5))
plt.title("Immigration of top 5 countries")
plt.ylabel('Number of Immigrants')
plt.xlabel("years")
plt.show()










# Area Chart
df_top5.plot(kind='area')

# alternate
# The unstacked plot has a default transparency (alpha value) at 0.5. We can modify this value by passing in the alpha parameter.	
df_top5.plot(kind='area', 
             alpha=0.25, # 0-1, default value a= 0.5
             stacked=False,
             figsize=(20, 10),
            )

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()




# Histogram
df_canada['2013'].plot(kind='hist')
plt.show()

# to align bins correctly
import numpy as np
count, bin_edges = np.histogram(df_canada['2013'])

df_canada['2013'].plot(kind='hist', xticks=bin_edges)
plt.show()




count, bin_edges = np.histogram(df_can['2013'])

# let's get the x-tick values
count, bin_edges = np.histogram(df_t, 15)

# un-stacked histogram
df_t.plot(kind ='hist', 
          figsize=(10, 6),
          bins=15,
          alpha=0.6,
          xticks=bin_edges,
          color=['coral', 'darkslateblue', 'mediumseagreen']
         )

plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')

plt.show()

# BAR CHART 
years = list(map(str, range(1980, 2014)))
df_iceland = df_canada.loc['Iceland', years]
df_iceland.plot(kind='bar')
