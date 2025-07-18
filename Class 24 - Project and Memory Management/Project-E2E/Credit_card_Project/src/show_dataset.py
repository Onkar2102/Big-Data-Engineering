def show_data(df):
    if(config['env']=='local'):
        print df.show()
        