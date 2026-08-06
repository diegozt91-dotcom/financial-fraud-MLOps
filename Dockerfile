FROM jupyter/pyspark-notebook:latest
USER root
RUN mamba remove -y numexpr bottleneck && \
    mamba clean --all -f -y
RUN pip install --no-cache-dir \
    datashader holoviews bokeh plotly yellowbrick scikit-learn xgboost \
    pandas numexpr>=2.10.2 bottleneck>=1.4.2 \
    geopy pgeocode geonamescache sweetviz \
#     streamlit dash
    polars
USER jovyan
