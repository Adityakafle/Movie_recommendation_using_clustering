from decimal import Clamped
import pre_processing
from sklearn.cluster import KMeans

def clustered_final_df(df):
    df['cluster_id']=None

    Kmeans=KMeans(n_clusters=10)

    features=df[['P_Genre','S_Genre','T_Genre']]
    Kmeans.fit(features)
    df['cluster_id']=Kmeans.predict(features)
    return df

def cluster_everything(input_movie):
    df=pre_processing.pre_process_all()
    # print(df)
    df=clustered_final_df(df)
    # print(df)
    df.to_csv('Dataset_to_plot.csv')
    #Check if the movie is present or not:
    input_movie=input_movie.lower()
    try:
        movie_not_found=df.loc[~df['movie'].str.contains(input_movie)]
        if len(movie_not_found)==0:
            print('Movie not found')
            return 0

        get_cluster=df['cluster_id'].loc[df['movie'].str.contains(input_movie)].values[0]
        similar_movies_list=df['movie'].loc[df['cluster_id']==get_cluster].values
        return similar_movies_list
    except:
        print('Movie not found')
        return 0